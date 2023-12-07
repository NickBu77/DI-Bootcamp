import json


with open(r'C:\Users\97258\Documents\DI-Bootcamp\week_3\day_4\course_notes\file.json','r') as family_obj:
    my_family = json.load(family_obj)





print(my_family['children'])
my_family['favorite_color'] = ['red','blue']

print(my_family)



with open(r'C:\Users\97258\Documents\DI-Bootcamp\week_3\day_4\course_notes\file.json','w') as family_obj:
    json.dump(my_family, family_obj)

with open(r'C:\Users\97258\Documents\DI-Bootcamp\week_3\day_4\course_notes\file.json','r') as obj:
    mys_family = json.load(obj)

print(mys_family)  

