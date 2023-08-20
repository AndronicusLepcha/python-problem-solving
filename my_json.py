
#serilzation of an object
import json
employee={'name':'Andronicus',
        'city':'Namchi',
        'isEmployee':'True'}


j_string=json.dumps(employee)
print(j_string)
with open('emp.json','w') as f:
    json.dump(employee,f,indent=4)