marks = int(input("Enter Your Mark :"))

if marks > 80:
    print("Letter Grade : A+", "Grade Point : 4.00")
elif marks > 75:
    print("Letter Grade : A", "Grade Point : 3.75")
elif marks > 70:
    print("Letter Grade : A-", "Grade Point : 3.50")
elif marks > 65:
    print("Letter Grade : B+", "Grade Point : 3.25")
elif marks > 60:
    print("Letter Grade : B", "Grade Point : 3.00")
elif marks > 55:
    print("Letter Grade : B-", "Grade Point : 2.75")
elif marks > 50:
    print("Letter Grade : C+", "Grade Point : 2.50")
elif marks > 45:
    print("Letter Grade : C", "Grade Point : 2.25")
elif marks > 40:
    print("Letter Grade : D", "Grade Point : 2.00")
else:
    print("Letter Grade : F", "Grade Point : 0.00")
