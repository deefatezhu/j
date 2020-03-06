#page 133-186, subject involing: IMPORT, AS, CLASS(skipped), READ DOC
#these are all side notes, all the way pushed to the lefthand wall
    #these are sub-excise topics
        #these are categorical topics to keep me focused. W/o further due, I shall begin 

        #19. import: import filename .... filename.variable(commend to display)
import make_ramen
make_ramen.make_ramen(3,'extra cheese')
make_ramen.make_ramen(4,'chashu','extra noodle')

    #import a particular varibale 
#from py_doc_name import function_name
from make_ramen import make_ramen
make_ramen(12,"cheese")

    #import multiple variables 
#from module_name import function_name1, function_2, function_3

        #20. shorten the process up with AS
from make_ramen import make_ramen as mr
mr(13,"vinegar")

        #21. shorten it up further 
import make_ramen as mr
mr.make_ramen(23,"garbage")
#import py_doc as initial and initial.function(a,"b")

        #22. file reader
with open('pi_digits.txt')as file_object:
    contents=file_object.read()
    print(contents)

    #or 
filename='pi_digits.txt'
with open(filename)as file_object: 
    for line in file_object:
#to get rid of the empty line in between, take: .rstrip()
        print(line.rstrip())


        #23. path 
    #supposingly we need find a find_me.txt under a folder called text_files which is under python_work  
#with open('text_files/find_me.txt')as file_object: 

#or: 
#file_path='/home/ehmatthes/other_files/text_files/filename.txt'
#following line: with open (file_path) as file_object

        #24. creating a doc 
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write('I fucking hate programming, can I go to sleep\n')
#now the programming.txt has been created with the 'message' in it
    file_object.write('\tyo I think I had too much tea....')
#save and run the code for the txt to appear 

        #25. saving with JSON 
#but honestly I think now py is common enough
#step 1, import JSON 
import json
#step 2, content of the to be saved thing in json 
numbers=[3,3,4,5,5,4,3,2,1,1,2,3,3,2,2]
#step 3, choose a name of the file 
filename='numbers.json'
#step 4, create the file and save the content in that file 
with open(filename,'w')as file_object:
    json.dump(numbers,file_object)

        #26. loading with JSON
#step 1, import JSON
import json
#step 2, locate the file in JSON format and you need to open
filename='numbers.json'
#step 3, open it 
with open(filename) as file_object: 
    numbers=json.load(file_object)
#check
print(numbers)

