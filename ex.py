import os
import csv
# Task 1

# def show_data_list():
#     lst = os.listdir('src/data/initial')
#     lst.sort(reverse=True)
#     for i in lst:
#         print(i)
    
# show_data_list()



#Task 2


ROOT = os.path.abspath(os.getcwd())
DATA_ROOT = ROOT + os.path.abspath('/src/data/initial')

# print(f'{ROOT}\n{DATA_ROOT}')




#Task 3


def create_data_directories(lst):
    
    for i in lst:
        # try:
        os.makedirs(DATA_ROOT+'/'+i, exist_ok=False)
    
        # except OSError as error:
        #     print(f"Error creating directory '{DATA_ROOT}/{i}': {error}")
            
        
dirs = ["personal", "work"]


#Task 4

def classify(dictionary):
    for key in dictionary:
        lst = dictionary.get(key)
        for i in lst:
            os.rename(DATA_ROOT +'/'+i, DATA_ROOT +'/'+key+'/'+i)
            


categories = {
            "personal": ["todos.txt", "bookmarks.txt"],
            "work": ["customers.csv", "jobs.csv"]
            }
# classify(categories)



#Task 5

os.makedirs(DATA_ROOT+'/work/reports', exist_ok=True)


customers_dict = {}
with open('src/data/initial/work/customers.csv', 'r') as customers:
    csv_reader = csv.reader(customers)
    next(csv_reader)
    for row in csv_reader:
        customer_id, name, _ = row
        customers_dict[customer_id] = name


pending_jobs = [] 
with open('src/data/initial/work/jobs.csv', 'r') as jobs:   
    csv_reader = csv.reader(jobs)
    next(csv_reader)
    for row in csv_reader:
        id, client_id, description, status = row
        if status != 'done':
            client_name = customers_dict[client_id]
            pending_jobs.append([id, description, client_name])


with open('src/data/initial/work/reports/pending_jobs.csv', 'w', newline='') as report:
    csv_writer = csv.writer(report)
    csv_writer.writerow(['id', 'description', 'client'])
    csv_writer.writerows(pending_jobs)
