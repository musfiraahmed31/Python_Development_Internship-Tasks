# Task: Check Promotion Eligibility

try:

    Attendance = float(input("Enter your attendance percentage %: "))
    FinalMarks = float(input("Enter your final marks: "))

    if Attendance >= 75 and FinalMarks >= 50:
        print("Promote")

    else:
        print("Not promoted")

except ValueError:
    print("Error: Please enter valid numeric values.")
