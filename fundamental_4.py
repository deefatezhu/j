#page 80-132, subject involing: DICTIONARY, DEF 
#these are all side notes, all the way pushed to the lefthand wall
    #these are sub-excise topics
        #these are categorical topics to keep me focused. W/o further due, I shall begin 

        #11. dictionary: x={'a':'b','c':'d',etc}
book_0={'color':'green','font size':'13'}
print(book_0['color'])
font_size=book_0['font size']
print("font size = "+str(font_size))

    #adding qualities: x['a']=b
book_0['page']=250

    #starting from an empty dictionary
book_1={}
book_1['color']='black'
#make sure to put'non-string'
book_1['page']=275
book_1['font size']=13

    #modifying qualities
book_1['color']='yellow'
print("now, book 1's color is "+book_1['color'])

    #removing qualities: del
del book_1['color']

fav_languages={'judy':'mandarin','aj':'english'}
print("Judy's favourite language to speak is: "+" "+fav_languages['judy'].title())
for name, language in fav_languages.items():
    print(name.title()+"'s favourite language to speak is"+language.title())
#name, language here seperates the 'a','b' to be found in x
#items() makes it callable, actually dk what that does 

    #key & value 
#if just capture the 'a','a1' in dict {'a:'b','a1:'b1'}, use key: x.keys()
for name in fav_languages.keys():
    print(name.title())

#if capturing the 'b', 'b1' in dict
for language in fav_languages.values():
    print(language.title())

        #12. automating the dictionary
book_0={'color':'green','font size':'13'}
book_1={'color':'black','font size':'13'}
book_2={'color':'yellow','font size':'13'}

books=[book_0,book_1,book_2]
for book in books: 
    print(book)

for book_number in range(23): 
    nbook={'color':'green','font size':'13'}
    books.append(nbook)

for book in books: 
    print(book)

print("the total number of books are "+str(len(book)))

        #13. complicate it up {'a':'b','a1':['b1','b11']}
ramen={'thickness':'thick', 'toppings':['chashu','extra cheese']}
print("you have ordered "+ramen['thickness']+" noodle with the follwing topping:")
for topping in ramen['toppings']:
    print("\t"+topping)

    #another example 
fav_languages={'judy':['mandarin','english','shanghainese'],'erin':['mandarin','english','taiwanness'],'aj':['english'],}
#tricky: make sure put comma, 
for name,languages in fav_languages.items():
    print(name.title()+" speaks:")
    for language in languages: 
        print("\t"+language.title())
#attention here, previously, I put x=lanaguges
# at the line of for language in languages:, it got mixed up
       
        #14. I am skipping a subchapter on WHILE 

        #15. def
def greet_user(username):
    print("hello "+username.title())
greet_user('judy')

def describe_tofu(tofu_thickness, tofu_name):
    print("I bought "+tofu_name+","+tofu_thickness+".")
describe_tofu('thick','aged tofu')
describe_tofu(tofu_name='tofu skin',tofu_thickness='thin')
#specified or not, both can work
#but if you mess around the orders, just make sure you specifiy x='a', y='b'

    #def with one fixed quality
def describe_tofu(tofu_thickness,tofu_name='tofu curb'):
    print("I bought "+tofu_name+","+tofu_thickness+".")
describe_tofu(tofu_thickness='thin')

        #16. def return 
def get_formatted_name(first_name,last_name):
    full_name=first_name+" "+last_name
    return full_name.title()

artist_0=get_formatted_name('marcel','duchamp')
print(artist_0.title())
#from my understanding, return mingles the full name part, and now get_formatted_name got formulated as full name

    #if-else middle name example 
def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=first_name+" "+middle_name+" "+last_name
    else: 
        full_name=first_name+" "+last_name
    return full_name.title()

artist=get_formatted_name('marcel','duchamp')
print(artist)

def build_person(first_name, last_name, age=''):
    if age: 
        person=first_name+" "+last_name+": "+age+" year-old"
    else: 
        person=first_name+" "+last_name
    return person

person=build_person('judy','zhu','23')
print(person.title())

    #multiple 
def greet_user(names):
    for name in names: 
        msg='Hello, '+name.title() +"!"
        print(msg)

usernames=['judy','erin','ue']
greet_user(usernames)


        #17. while-things to do example 
things_todos=['learn python','submit naybr','read a book','draft another song']
completed_todos=[]

while things_todos:
    current_todo=things_todos.pop()

    print("I am working on: "+current_todo)
    completed_todos.append(current_todo)

print("The following to do has been completed: ")
for completed_todo in completed_todos:
    print(completed_todo)

        #18. ramen example with def 
def make_ramen(*toppings):
    print("\n Making ramen with the following toppings:")
    for topping in toppings: 
        print("-"+topping)

make_ramen('extra noodle')
make_ramen('chashu','cheese')

def make_ramen(size, *toppings):
    print("\nMaking a "+str(size)+" size ramen with the following topping:")
    for topping in toppings: 
        print(toppings)
make_ramen(12,'chashu')

