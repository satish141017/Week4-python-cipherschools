from csv import DictWriter
with open("new_file.csv","w",newline="") as f:
    csv_writer=DictWriter(f,fieldnames=["Firstname","lastname","age"])
    # csv_writer.writerow({
    #     "Firstname":"Satish",
    #     "lastname":"Kumar",
    #     "age":50
    # })
    # csv_writer.writerow({
    #     "Firstname":"Hersshit",
    #     "lastname":"Kumar",
    #     "age":500
    # })
    # writerows[dict1,dict2,dict3]
    csv_writer.writerows([{
        "Firstname":"Hersshit","lastname":"Kumar","age":500},
        {"Firstname":"SAtish","lastname":"Kumar","age":200},
        {"Firstname":"sandeep","lastname":"singh","age":45}
        ])