with open("salary.txt","r") as read_file:
    with open("salary2.txt","a") as write_file:
        for i in read_file.readlines():
            k=i.split(",")
            l=f"{k[0]} salary is {k[1]}"
            write_file.write(l)

            
