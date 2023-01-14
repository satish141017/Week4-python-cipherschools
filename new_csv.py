# CSV - means comma seperated values
# use to store tabular data
# values also can be seperated with "*" ,",","|"
# for working with csv files we have to import a reader function or Dictwriter fro csv module
from csv import reader
with open("new_file.csv","r") as f:
    csv_reader=reader(f)
    # csv_reader is iterator
    print(csv_reader)
    print(type(csv_reader))
    for row in csv_reader:
        print(row)

