
import json 
patients = [{'id' :1, 'name' : 'rahul'}, {'id': 2 , 'name': 'modiji'}]
with open('question2_data.json' , 'w') as apteints_db:
    json.dump(patients, patients_db) #dump - writing to file
print('Dictonary written to JSON file.')
