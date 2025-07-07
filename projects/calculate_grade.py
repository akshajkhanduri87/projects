# 7/7/25

grade_percent = int(input("Please enter the grade you received in percentage: "))

def calculate_grade(percent):
    if percent <= 100 and percent >= 90:
        print("You received an A")
    elif percent < 90 and percent >= 80:
        print("You received a B")
    elif percent < 80 and percent >= 70:
        print("You received a C")
    elif percent < 70 and percent >= 60:
        print("You received a D")
    elif percent < 60:
        print("You received an F")
    else:
        print("Please enter a valid number")


calculate_grade(grade_percent)