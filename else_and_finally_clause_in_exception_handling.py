while True:
    try:
        age=int(input("Enter your age : "))
        
    except ValueError:
        print("youy are puting a wrong valuetype")
    except:
        print(" I dont know this type of error pease check the code")
    else:
        print(f"blah blah blah blah {age}")
        break
    finally:
        # finally block tab chalta hai chahe error aye ya na aye
        print("mai finally block mai likha gya hoon achha thik hai chalte hai hum")




    # try agar sucessful ho to exept wala block nahi chalta hai
    # humelse mai bacha hua code likhte hai try ke safal hone par