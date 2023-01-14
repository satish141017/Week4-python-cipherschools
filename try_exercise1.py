def divide(num1,num2):
    try:
        k= num1 / num2
        return k
    except ZeroDivisionError as err:# ye err use karte hai jo by default error hai wo print karane ke liye
        # print("dont divide by zero please !")
        # agar by default o massage print hota hai wo print karana ho to
        print(err)
    except TypeError as err:
        print("type galat dale ho string nahi integer dalo")
    except:
        print("unecepted errro !!!!!!")
    
print(divide(5,"0"))
