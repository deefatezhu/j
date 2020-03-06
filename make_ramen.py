def make_ramen(size, *toppings):
    print("\nMaking a "+str(size)+" size ramen with the following topping:")
    for topping in toppings: 
        print(topping)
        #make sure this place says topping instead of toppings which then would display the toppings twice
make_ramen(16,'chashu')
make_ramen(13,'extra noodle','extra fatty chashu')

