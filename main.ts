// gta6-meme-x-01-v5 — "My AI agent played GTA 6 for me" (Node 22, stdlib only).
//
// The entry is the X post itself: the house reads the meme picture and the
// caption straight from X and hands them to the AI judge. This program has
// one job — carry POST.json from the repository root into the output
// directory, where the gate reads the post's address. Nothing it writes is
// judged.
//
// Local run:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(outDir, { recursive: true });

let post: string;
try {
  post = readFileSync(join(botDir, 'POST.json'), 'utf8');
} catch (err) {
  console.error(`cannot read POST.json from ${botDir}: ${(err as Error).message}`);
  process.exit(1);
}

const parsed: unknown = JSON.parse(post); // fail loudly on a malformed post file
if (typeof parsed !== 'object' || parsed === null || typeof (parsed as { url?: unknown }).url !== 'string') {
  console.error('POST.json must be a JSON object with a string url field');
  process.exit(1);
}
writeFileSync(join(outDir, 'POST.json'), post);
console.log('POST.json copied to', join(outDir, 'POST.json'));
