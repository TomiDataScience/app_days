print("Welcome to the tip calculator!")
bill=input("What was the total bill?")
people=input("How many people split the bill?")
percent = input("What was the tip percentage 10, 12, 15?")
x=(float(bill) * float(percent) / float(people))/100
print("Each person should pay:", int(x), "zł")
