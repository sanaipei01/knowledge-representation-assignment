import json
import sys
from pathlib import Path

nb_path = Path('knowledge_representation.ipynb')
if not nb_path.exists():
    print('Notebook not found:', nb_path)
    sys.exit(1)

with nb_path.open('r', encoding='utf-8') as f:
    nb = json.load(f)

globals_ = {}
for idx, cell in enumerate(nb.get('cells', []), start=1):
    if cell.get('cell_type') == 'code':
        source = ''.join(cell.get('source', []))
        if not source.strip():
            continue
        print(f'--- Executing cell {idx} ---')
        print('SOURCE REPR:', repr(source))
        try:
            exec(source, globals_)
        except Exception:
            import traceback
            traceback.print_exc()
            sys.exit(1)

print('\nAll code cells executed.')
