try:
    n=int(input("enter numerator:"))
    d=int(input("enter denominator:"))
    r=n/d
    print(f"result:{r}")
except ZeroDivisionError:
    print("Error:cannot divided by zero.")
except ValueError:
    print("Error:please enter valid integers")    
