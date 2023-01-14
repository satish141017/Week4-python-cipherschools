#write #DictWriter
from csv import writer
with open("new_file3.csv","w",newline="") as f:
    csv_write=writer(f)
    # 2 methods ---- writerow , writerows
    csv_write.writerow(["name","country"])
    csv_write.writerow(["Satish","kumar"])
    csv_write.writerow(["Rajupunjabi","pta nahi"])


    # writerows will take lists
    csv_write.writerows([["name","country"],["Satish","kumar"],["Rajupunjabi","pta nahi"]])
    
