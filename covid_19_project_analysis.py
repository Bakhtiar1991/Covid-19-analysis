class DataTable:

    def __init__(self):
        self.data = ''
        self.row = ''
        self.column = ''

    def read_csv(self, path):
        row_number = 0
        column_number = 0
        list_for_data = []
        with open(path, 'r') as file:
            first_line = file.readline().strip().split(",")
            # taking first line of the data(meta data of the file) and split function making it a list
            for i in first_line:
                column_number += 1

            for line in file:
                k = line.strip().split(",")  # made another list with rest of the data
                dic_of_data = dict(zip(first_line, k))  # using zip and dict function to create dictionary
                list_for_data.append(dic_of_data)
                row_number += 1
            self.data = list_for_data
            self.row = row_number + 1
            self.column = column_number - 1
            #print(f"This dataset has {row_number + 1} rows including heading line and {column_number - 1} columns without the index column")

    def locate_column(self, column_name):
        list_for_column = []  # this method is going to return the data of the corrusponding column
        for info in self.data:
            a = info[column_name]
            list_for_column.append(a)

        print(list_for_column)

    def locate_index(self, index_name):
        for index_line in self.data:
            if index_line["index"] == index_name:  # this method will only print the index number we entered
                print(index_line)
                break

    def filter_value(self, column_name, value):
        for ind in self.data:
            if ind[column_name] == value:  # this method will print the rows of the value given.
                print(ind)
    def value_count(self, column_name):
        list_value_count = []
        for column in self.data:
            a = column[column_name]
            list_value_count.append(a)

        list_for_occurance = []
        for value_in_list in list_value_count:
            occurance = list_value_count.count(value_in_list)
            list_for_occurance.append(occurance)
        dictionary_of_value_count = dict(zip(list_value_count, list_for_occurance))
        print(dictionary_of_value_count)

    def recover(self, column_name, name_of_the_country):
        sum_of_recover = 0
        list_of_country = []
        list_for_recover = []
        for ind in self.data:
            if ind[column_name] == name_of_the_country:
                list_of_country.append(ind)
        for rec in list_of_country:
            a = rec["recovered"]
            list_for_recover.append(a)
        for adding in list_for_recover:
            sum_of_recover += float(adding)

        print(f"{name_of_the_country} {sum_of_recover} people have recovered")

    def death_value1(self, value):

        list_0 = []


        a = 0
        for ind in self.data:
            if ind["country"] == value:
                list_0.append(ind)

        for ind1 in list_0:
            a = a + float(ind1["deaths"])
        return a

    def confirmed_cases(self, column_name, value):
        list_0= []
        a = 0
        for row in self.data:
            if row[column_name] == value:
                list_0.append(row)
        print(list_0)

        for con in list_0:
            a += float(con["deaths"])
            if a >= 1000:
                print(f"row = {con}")
                print(f"The Date is {con['date']}")
                break

        if a >= 1000:
         print(f"The number of the death on this county till {con['date']} is {a}")
        elif a < 1000:
            print("Country did not reach 1000 deaths yet.")





# From this portion I will start calling the objects.

datatable = DataTable()
datatable.read_csv("/home/bakhtiar/Documents/Covid_19_project/Covid-19-analysis/covid-19_data.csv")
print(datatable.data)
print(f"This data set has {datatable.row} including heading line and {datatable.column} columns without index column")

# this code is for coulmn list
list_of_col =[]
i = int(input("Enter the number of column you want to see (it needs to be an integer value) : "))
for column_value in range (i):
    name_of_the_column = input("Enter the name of the column : ")
    list_of_col.append(name_of_the_column)
for calling_column in list_of_col:
    datatable.locate_column(calling_column)

#this cod is for lokking into index
list_of_index =[]
i = int(input("Enteer the number of index you want to see (it needs to be an integer value) : "))
for index_value in range(i):
    index_number = input("please iner the index number to see that line : ")
    list_of_index.append(index_number)
for calling_index in list_of_index:
    datatable.locate_index(calling_index)
#retunrs the rows of the value from the columns.
print("ENTERING THE COLUMN NAME AND THE VALUE OF THE COLUMN NAME YOU WILL SEE THE ROWS THAT VALUE IS PRESENT")
col_name_for_filter_value = input("Please enter the columne name :")
value_for_filter_value = input("Please enter the value for the column name you just gave :")
datatable.filter_value(col_name_for_filter_value, value_for_filter_value)

#it gives the occurance of each value
column_for_value_count = input("Please enter the name of the column and you will get to see the occurance of each value : ")
datatable.value_count(column_for_value_count)

#it gives the number of recoverd people.
country_name = input("Enter the name of the country to see the number of recovered people : ")
datatable.recover("country",country_name)
option = input("Enter y to see the highest death or n to skip : ")
if option == 'y':

    list_a = []
    list_b = []
    with open('/home/bakhtiar/Documents/Covid_19_project/Covid-19-analysis/covid-19_data.csv', 'r') as f:
        first_line = f.readline().strip().split(",")
        # taking first line of the data(meta data of the file) and split function making it a list
        for line in f:
            k = line.strip().split(",")  # made another list with rest of the data
            d = dict(zip(first_line, k))  # using zip and dict function to create dictionary
            list_a.append(d)
        list_for_column = []  # this method is going to return the data of the corrusponding column
        for info in list_a:
            a = info["country"]
            list_for_column.append(a)
            set_create = set(list_for_column)
            list_of_set = list(set_create)
        for countries in list_of_set:
            ap = datatable.death_value1(countries)
            list_b.append(ap)
        dictionary_with_deathValue = dict(zip(list_of_set,list_b))
        max_key = max(dictionary_with_deathValue, key = dictionary_with_deathValue.get)
        max_value = max(dictionary_with_deathValue.values())
        print(f"{max_key} has the highest deaths and it is {max_value}")
elif option == "n":
    pass

#this code will give the date when the country reached 1000 deaths.
country_name_for_death_count = input("Enter the name of the country to know which country reached death to 1000 and when : ")
datatable.confirmed_cases("country", country_name_for_death_count)