def num(num1,num2):


    try:
        res=num1+num2
    except NameError:
        return "check varible"
    except TypeError as e:
        return "invalid num"
    else:
        return (f"safe excute{res}")
    finally:
        print("excution completed")


print(num(1,2))
print(num(1,"d"))
print(num(1,9))