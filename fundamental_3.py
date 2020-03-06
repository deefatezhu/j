#page 65-80, subject involving: IF-ELIF-ELSE, RAMEN ORDERING EXAMPLE
#these are all side notes, all the way pushed to the lefthand wall
    #these are sub-excise topics
        #these are categorical topics to keep me focused. W/o further due, I shall begin 

        #10. if: if x=='y': ###doing something 
todo_things=['python','painting','lyrics','polishing songs','updating cv','writing book']
if todo_things=='python':
    print("This the most urgent thing this month")
else: 
    print("Wait until you finish learning python")

    #banned friend example (doesn't run here)
banned_friends=['dahei','colin','carmen']
friend='dahei'

if friend not in banned_friends:
    print("hi, "+friend.title())

    #if-elif-else 
age=23 
if age<20:
    print("you are too young to be friends with me")
elif age<35:
    print("heyy, whatsup")
else:
    print('hello')

    #if-elif-elif-else
age=28 
if age<18:
    print("you are too young to be friends with me")
elif age<25:
    print("heyy, whatsup")
elif age<30:
    print("hey")
else:
    print('hello')
#elif is just an extra if, can put as many 

    #if-elif-elif-elif
age=35 
if age<18:
    print("you are too young to be friends with me")
elif age<25:
    print("heyy, whatsup")
elif age<30:
    print("hey")
elif age>30:
    print('hello')
#elif is great for multiple conditions passing but not for the following case 

    #if-if-if: if 'a' in x: 
ramen_toppings=['tofu','extra noodle','chashu']
if 'tofu' in ramen_toppings:
    print("adding tofu")
if 'extra noodle' in ramen_toppings:
    print("adding extra noodle")
if 'chashu' in ramen_toppings:
    print("adding chashu")
print("Your bowl is coming up")
#arg, why did i do the above, this is so much simpler
for ramen_topping in ramen_toppings: 
    print("addding "+ramen_topping)

    #ramen if-else example: tofu ran out
ramen_toppings=['tofu','extra noodle','chashu']
if 'tofu' in ramen_toppings: 
    print("Sorry, we ran out of tofu")
else: 
    print("Adding"+ramen_topping)
print("Your bowl is coming up")

    #fill in an empty list 
requested_toppings=[]
if requested_toppings: 
    for requested_topping in requested_toppings:
        print("adding"+requested_topping)
else: 
    print("Are you sure of no topping?")

    #final ramen example, requested vs available, I'm not having ramen for a while 
available_toppings=['extra noodle','tofu','chashu']
customer_toppings=['extra cheese','extra noodle']
for customer_topping in customer_toppings:
    if customer_topping in available_toppings:
        print("Adding "+customer_topping)
    else: 
        print("Sorry, we ran out of "+customer_topping)
print("Your bowl is coming up!")
