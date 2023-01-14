# reader , DictReader
# writer , DictWriter
from csv import DictReader , DictWriter
with open("new_file3.csv","r") as rf:
    with open("new_file4.csv","w",newline="") as wf:
        csv_raeder=DictReader(rf)
        csv_writer=DictWriter(wf,fieldnames=["name","age"])
        csv_writer.writeheader()
        for row in csv_raeder:
            naam,ages=row["name"],row["age"]
            csv_writer.writerow({
                "name":naam.upper(),
                "age":ages
            }
            )












