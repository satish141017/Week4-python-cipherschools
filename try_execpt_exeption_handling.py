while True:
    try:
        age=int(input("Enter your age : "))
        break
    except ValueError:
        print("youy are puting a wrong valuetype")
    except:
        print(" I dont know this type of error pease check the code")


# notes  except wala block tab chalta hai agr try maii error aye or woo kewal ek bar chalta hai


if age<15:
    print("you can watch")
else:
    print("You can't watch")