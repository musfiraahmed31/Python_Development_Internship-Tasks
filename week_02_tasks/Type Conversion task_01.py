# Marks Percentage Calculator

print("Enter marks for 5 subjects:")

sub1 = int(input("Subject 1: "))
sub2 = int(input("Subject 2: "))
sub3 = int(input("Subject 3: "))
sub4 = int(input("Subject 4: "))
sub5 = int(input("Subject 5: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks / 500) * 100 

print(f"\nTotal Marks: {total_marks} / 500")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 90:
    print("Grade: A")

elif percentage >= 80:
    print("Grade: B")

elif percentage >= 70:
    print("Grade: C")

else:
    print("Grade: Fail")
