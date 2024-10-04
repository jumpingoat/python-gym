
while ValueError or ZeroDivisionError:
    try:
        total = float(input("What was the total bill? "))
        tip = float(input("How much tip you'd like to give? "))
        people = int(input("How many people to split the bill? "))
        amount = (total + (total * tip) / 100) / people
        print(f"{amount:.2f}")
        break
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("You can't divide by zero")
