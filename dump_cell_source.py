import json
nb = json.load(open('knowledge_representation.ipynb','r',encoding='utf-8'))
src = nb['cells'][0]['source']
print('LINES:', len(src))
for i, l in enumerate(src, 1):
    print(i, repr(l))
