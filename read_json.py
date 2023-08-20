import json
with open('emp.json','r') as f:
    e=json.load(f)

print(e.name)