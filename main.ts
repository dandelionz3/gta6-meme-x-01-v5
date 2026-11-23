// gta6-meme-x-01-v5 — "Pre-order receipt" (Node 22, stdlib only).
// Revision: the meme is now a Vice City pre-order receipt — ordered
// Sep 17, 2013, delivered Nov 19, 2026, $2,574 after 13 years of
// waiting fees, hype storage and an 847 GB download. Same entry shape:
// the X post itself is the entry; this program only carries POST.json
// from the repository root into the output directory, where the gate
// reads the post's address. Nothing it writes is judged.
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
const url = (parsed as { url: string }).url.trim();
if (url.length === 0) {
  console.error('POST.json url must not be empty');
  process.exit(1);
}
if (post.length > 16384) {
  // the gate's post_file cap: POST.json may be at most 16384 bytes
  console.error(`POST.json is ${post.length} bytes, over the 16384-byte cap`);
  process.exit(1);
}
writeFileSync(join(outDir, 'POST.json'), post);
console.log('POST.json copied to', join(outDir, 'POST.json'));
