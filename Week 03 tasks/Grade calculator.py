# Grade Calculator for 3 Subjects

try:
    Subject1 = float(input("Enter marks for Subject 1: "))
    Subject2 = float(input("Enter marks for Subject 2: "))
    Subject3 = float(input("Enter marks for Subject 3: "))

    TotalObtainedMarks = Subject1 + Subject2 + Subject3
    Percentage = (TotalObtainedMarks / 300) * 100 

    if Percentage >= 85:
        Grade = "A"
    elif Percentage >= 70:
        Grade = "B"
    elif Percentage >= 50:
        Grade = "C"
    else:
        Grade = "Fail"

    # Output the results
    print("Total Marks:", TotalObtainedMarks)
    print("Percentage:", Percentage)
    print("Grade:", Grade)

except ValueError:
    print("Error: Please enter valid numeric marks.")
