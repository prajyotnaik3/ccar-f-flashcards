#!/usr/bin/env bash
# Local setup for CCAR-F flashcard builds (macOS/Linux)
set -euo pipefail
cd "$(dirname "$0")/.."

if [[ ! -d .venv ]]; then
  python3 -m venv .venv
fi

.venv/bin/pip install -q -r requirements.txt
.venv/bin/python scripts/build_all.py

echo ""
echo "Done. Import dist/anki/ccar-f.apkg into Anki."
echo "Web viewer: cd web && python3 -m http.server 8080"
