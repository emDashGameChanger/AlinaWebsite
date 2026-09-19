#!/usr/bin/env bash
# Build the allowlisted copy of the site that gets deployed to Namecheap.
#
# Rule: only web content goes on the public host -- HTML, CSS, and page
# resources (images, video, fonts, JS, data files, PDFs). Anything else
# (markdown, plain text, notes, scripts, config) stays in the repo only.
# biolab/ (docking tooling, notes, run data) is never deployed.
#
# Usage: stage-site.sh [output-dir]   (default: _site)
set -euo pipefail

out="${1:-_site}"
rm -rf "$out"
mkdir -p "$out"

find . -type f \
  -not -path './biolab/*' \
  -not -path './.git/*' \
  -not -path './.github/*' \
  -not -path "./${out#./}/*" \
  -regextype posix-extended \
  -iregex '.*\.(html?|css|js|json|csv|xml|png|jpe?g|gif|svg|webp|avif|ico|mp4|webm|woff2?|ttf|otf|pdf)' \
  -print0 | rsync -a --from0 --files-from=- ./ "$out/"

# Guard: a broken stage must never reach the server (the deploy deletes
# anything on the server that is missing from the staged folder).
for required in index.html styles.css; do
  if [ ! -f "$out/$required" ]; then
    echo "ERROR: $required missing from staged site; refusing to deploy." >&2
    exit 1
  fi
done

echo "Staged $(find "$out" -type f | wc -l) files into $out/"
