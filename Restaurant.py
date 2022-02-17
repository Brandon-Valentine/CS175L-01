#BrandonValentine
#CS175L_01
#Restaurant
keep_going='yes'
while keep_going=='yes':
    vegan=False
    vegetarian=False
    gluten_free=False
    response1=input('Is anyone in your party Vegetarian?')
    while response1=='yes':
        vegetarian=True

    response2=input('Is anyone in you party vegan?')
    while response2=='yes':
        vegan=True

    response3=input('Is anyone in your party gluten free?')
    while response3=='yes':
        gluten_free=True
    print('Here are your restaurant choices.')
    keep_going='yes'
    print('Corner Cafe')
    print('The Chef\'s Kitchen')
        
    while vegetarian==False and vegan==False and gluten_free==False and keep_going=='yes':
          print('Joe\'s Gourmet Burgers')
          keep_going='n'

    while vegetarian==False and vegan==False and gluten_free==False and keep_going=='yes':
        print('Joe\'s Gourmet Burgers')
        keep_going='n'
    while vegetarian==True and vegan==False and gluten_free==True and keep_going=='yes':
         print('Main Street Pizza Company')
         keep_going='n'
    while vegetarian==True and vegan==False and gluten_free==False and keep_going=='yes':
        print('Mama\'s Fine Italian')
        keep_going='n'

    keep_going=input('Would you like to search again?enter yes to continue: ')

