#BrandonValentine
#CS175L_01
#Restaurant
vegan=False
vegetarian=False
gluten_free=False
response1=input('Is anyone in your party Vegetarian?')
if response1=='yes':
    vegetarian=True

response2=input('Is anyone in you party vegan?')
if response2=='yes':
    vegan=True

response3=input('Is anyone in your party gluten free?')
if response3=='yes':
    gluten_free=True
print('Here are your restaurant choices:')
if not vegetarian and not vegan and not gluten_free:
    print('Joe\'s Gourmet Burgers')
if not vegan and  not gluten_free:
    print('Mama\'s Fine Italian')
if not vegan:
    print('Main Street Pizza')
print('Corner Cafe')
print('Chef\'s Kitchen')
