""" with open('names.txt' , 'r') as names_db: #best practice , using with clause
    all_names = names_db.read()
    print(all_names) """


    #without using 'with' clause

""" names_db = open('names.txt' , 'r') 
all_names = names_db.read()
print(all_names)
names_db.close() """

with open('names.txt' , 'r') as names_db: #best practice , using with clause
    all_names = names_db.read()
    print(all_names)