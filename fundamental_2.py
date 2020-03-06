#page 43-63, subject involving: FOR, RANGE, DIMENSION, TAKING PART OF THE LIST, DIMENSIONS
#these are all side notes, all the way pushed to the lefthand wall
    #these are sub-excise topics
        #these are categorical topics to keep me focused. W/o further due, I shall begin 

        #6. for 
weapons=['epee','sabre','foil']
for weapon in weapons:
    print(weapon.title()+"!")
    print("-the best weapon")


        #7. range
for value in range(13,23):
    print(value)

    #horizontal list: x=list(range(a,b))
numbers=list(range(1,6))
print(numbers)

    #even number list 
even_numbers=list(range(12,24,2))
print(even_numbers)
#13 is the starting number, add 2, until reaching 23 

    #ood number list 
odd_numbers=list(range(13,25,2))
print(odd_numbers)

    #squares
squares=[]
for value in range(13,23):
        square=value**2
        squares.append(square)
print(squares)
#alternative, cleaner version 
squares=[]
for value in range(13,23):
    squares.append(value**2)
print(squares)
#alternaitve, cleanest version 
squares=[value**2 for value in range(13,23)]
print(squares)

    #triple 
triplpe=[value*3 for value in range(1,13)]
print(triplpe)

        #8. part of the list 
    #take a part of the list: [a:b]
fav_cities=['shanghai','florence','new york','oxford']
print(fav_cities[0:2])

    #take the begining to a certain spot: [:b]
print(fav_cities[:3])
print(fav_cities[3:])

    #take last few: [-a:]
print(fav_cities[-3:])

    #take part of the list and loop it 
print("These are my top 3 favourite cities:")
for city in fav_cities[0:3]: 
    print("\t"+city.title())

    #copy list: [:]
my_fav_cities=['shanghai','florence','new york','oxford']
friend_fav_cities=my_fav_cities[:]

print("My favourite cities are:")
print(my_fav_cities)

print("My friend's favourite cities are:")
print(friend_fav_cities)

    #add to the copied list: x.append('a')
friend_fav_cities.append('suzhou')
print(friend_fav_cities)
#delete one element, use del
del friend_fav_cities[4]
print(friend_fav_cities)
friend_fav_cities.remove('oxford')
friend_fav_cities.pop()
print(friend_fav_cities)

        #9. dimension 
dimensions=(0,23)
print(dimensions[0])
print(dimensions[1])
#[0]refer to the first input number 

# cannot change qualitie but can redefine 
dimensions=(0,23)
print("Here is the origional dimensions:")
for dimension in dimensions: 
    print(dimensions)

dimensions=(23,0)
print("Here is the modified dimensions:")
for dimension in dimensions: 
    print(dimension)

