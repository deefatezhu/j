#page 16-43, subject involing: MESSAGE, LIST, SORT 
#these are all side notes, all the way pushed to the lefthand wall
    #these are sub-excise topics
        #these are categorical topics to keep me focused. W/o further due, I shall begin 

        #1. get some message out there 
print("This is Judy, and I am struggling with Python.")
#another way of displaying words
message="Actually my 2nd time practicing the basics, \n the 1st time was accidentally deleted, \n what a pain."
print(message)
#headsup when using lower case i and upper case O, can be mistaken as 1 & 0

name='satoshi nakamoto'
print(name.title())
print(name.upper())
print(name.lower())

first_name='satoshi'
last_name='nakamoto'
full_name=first_name.title()+" "+last_name.title()
print(full_name)

        #2. str(#)
age=23
message="Hey, old man"+" you are already"+str(age)+" year old."
print(message)

        #3. list:x=['a','b','c']
fav_authors=['xiaobuo','tolstoy','bronte']
print(fav_authors[0].title())
print(fav_authors[-1].title())
message="Recently I have been really interested in the following authors:"+"\n\t"+fav_authors[0].title()+"\n\t"+fav_authors[-2].title()
print(message)

        #4. changing qualities in a list 
    #changing one fav authors: x[1]='new'
message=fav_authors[1].title()+"'s words can be too delicate and so it is off my recent fav."
print(message)
fav_authors[1]='shaofeng han'
print(fav_authors) 

    #adding: x.append.('y')
fav_authors.append('camus')
print(fav_authors)

    #adding to an emptly list x=[], x.append('y')
fav_artists=[]
fav_artists.append('caravagio')
fav_artists.append('duchamp')
fav_artists.append('coubert')

    #adding at a chosen place: insert(place, 'y')
fav_artists.insert(0,'Michelangelo')
print(fav_artists)

    #deleting a chosen element: del x[where]
del fav_artists[0]
print(fav_artists)

    #deleting the last element using pop(): 
fav_artists.append('Michelangelo')
pop_artist=fav_artists.pop()
print(fav_artists)
print(pop_artist)
#use pop if the deleted MAY come back for good, if for certain, use del

#deleting an element you know but dk where: x.remove('y')
fav_artists.append('Michelangelo')
fav_artists.remove('Michelangelo')
print(fav_artists)

fav_artists.append('Michelangelo')
too_cliche='Michelangelo'
fav_artists.remove(too_cliche)
print(fav_artists)
print("I'm not particularly a"+" "+too_cliche.title()+" fan b/c I forgot to wear glasses when I was visting the Sistine Chapel.")

        #5. sort: x.sort() or reverse it x.sort(reverse=True)
fav_authors.sort()
print(fav_authors)
fav_authors.sort(reverse=True)
print(fav_authors)

    #present a pretty sorted list: print(sorted(x))
print("This is the origional list:")
print(fav_authors)

print("This is the sorted list:")
print(sorted(fav_authors))
print(fav_authors)

    #reverse the list once and for all: x.reverse()
fav_authors.reverse()
print(fav_authors)

#Uploading to github, do the following: 
# git add .&& git commit -m"updates" && git push
# when in doubt: git --help 