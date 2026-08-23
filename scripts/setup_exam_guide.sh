#!/usr/bin/env bash
# Copy official CCAR-F Exam Guide PDF into docs/exam-guide/ (gitignored local copy)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST_DIR="$ROOT/docs/exam-guide"
DEST="$DEST_DIR/CCAR-F-Exam-Guide.pdf"

mkdir -p "$DEST_DIR"

if [[ -f "$DEST" ]]; then
  echo "Already exists: $DEST"
  exit 0
fi

# Common download locations (macOS)
CANDIDATES=(
  "$HOME/Downloads/Claude+Certified+Architect+–+Foundations+Exam+Guide.pdf"
  "$HOME/Downloads/Claude Certified Architect – Foundations Exam Guide.pdf"
  "$HOME/Downloads/CCAR-F-Exam-Guide.pdf"
)

for src in "$CANDIDATES"; do
  if [[ -f "$src" ]]; then
    cp "$src" "$DEST"
    echo "Copied to $DEST"
    exit 0
  fi
done

echo "Exam Guide PDF not found in Downloads."
echo "Download from Partner Academy, then either:"
echo "  cp /path/to/guide.pdf $DEST"
echo "Or re-run this script after downloading to ~/Downloads/"
exit 1
