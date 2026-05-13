bal=1000

try:
    withdra=int(input("enter withdraw amount :"))

    if withdra > bal:
        raise ValueError("Insufficint balance")
    bal -= withdra

    print("transaction successfull")
    print(f"remaining balance : {bal}")

except ValueError as e:
    print(e)

