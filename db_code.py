import sqlite3
import pandas as pd 

# Connect to the database
conn = sqlite3.connect('STAFF.db')

# --- Creating and loading the first table (INSTRUCTOR) ---
table_name = 'INSTRUCTOR'
attribute_list = ['ID','FNAME','LNAME','CITY','CCODE']
file_path = '/home/project/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)
df.to_sql(table_name,conn,if_exists = 'replace',index = False)
print("Table is ready")

# --- Queries for the INSTRUCTOR table ---
#Function for querys

def execute_query(query):
    query_output = pd.read_sql(query,conn)
    print(query)
    print(query_output)


#Viewing all the data in the table 
execute_query = f"SELECT * FROM {table_name}"

#Viewing only FNAME
execute_query = f"SELECT FNAME FROM {table_name}"

#Viewing total of entrys
execute_query = f"SELECT COUNT(*) FROM {table_name}"

# --- Adding data to the INSTRUCTOR table ---

data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)
data_append.to_sql(table_name,conn,if_exists = 'append', index = False)
print('Data append successfully')

#Viewing total of entrys after insertion
execute_query = f"SELECT COUNT(*) FROM {table_name}"


# --- Creating and loading the second table (Departments) ---
table_name1 = "Deparments"
attribute_list1 = ['DEPT_ID','DEP_NAME','MANAGER_ID','LOC_ID']
file_path1 = '/home/project/Departments.csv'
df1 = pd.read_csv(file_path1, names = attribute_list1)
df1.to_sql(table_name1,conn,if_exists = 'replace',index = False)
print("Table 2 is ready")

#Viewing all the data in the table 
execute_query = f"SELECT * FROM {table_name1}"

#Appending data to table 2(departments)

data_dict1 = {'DEPT_ID': [9],
              'DEP_NAME': ['Quality Assurance'],
              'MANAGER_ID': [30010],
              'LOC_ID': ['L0010']}
data_append1 = pd.DataFrame(data_dict1)
data_append1.to_sql(table_name1,conn, if_exists = 'append', index = False)
print('Data append successfully')

#Viewing all the data in the table after insertion
execute_query = f"SELECT * FROM {table_name1}"

# Close connection
conn.close()