#1. Update values in dictionaries and lists
#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#Change the last_name of the first student from 'Jordan' to 'Bryant'
#In the sports_directory, change 'Messi' to 'Andres'
#Change the value 20 in z to 30

x=[[5,2,3],[10,8,9]]
students=[
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"}
]
sports_directory={
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"]
}
z=[{"x": 10, "y": 20}]
x[1][0]=15
print(x)
students[0]["last_name"]="Bryant"
print(students)
sports_directory["soccer"][0]="Andres"
print(sports_directory)
z[0]["y"]=30
print(z)

#2. Iterate through a list of dictionaries
#Creat a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students=[
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"}
]
def iterate_dictionary(list):
    for x in range(0,len(list),1):
        print(f"first_name- {list[x]['first_name']},last_name- {list[x]['last_name']}")

iterate_dictionary(students)

#3. Get Values From a List of Dictionaries
#Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
def iterate_dictionary2(key_name,some_list):
    for x in range(len(some_list)):
        print(some_list[x][key_name])
iterate_dictionary2("last_name",students)

#4. Iterate Through a Dictionary with List Values
#Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
dojo={
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": ["Michael", "Amy", "Eduardo", "Josh", "Graham", "Patrick", "Minh", "Devon"]
}
def print_info(list):
    for k in list:
        num=len(list[k])
        print(num,k.upper())
        for i in range(len(list[k])):
            print(list[k][i])
print_info(dojo)


        