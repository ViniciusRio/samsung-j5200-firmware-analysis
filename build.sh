#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir -p build/NAO_INSTALAVEL
cp src/prototype/index.html src/prototype/style.css src/prototype/app.js build/NAO_INSTALAVEL/
python3 -m unittest discover -s tests -v
node tests/test_prototype.js
python3 src/analyze_firmware.py --output analysis/inventory.json
printf '%s\n' 'Protótipo local em build/NAO_INSTALAVEL/ (não é pacote para TV).'
