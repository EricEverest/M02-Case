# Eric Troutman
# M02Case
# Enter information about students to see if they have qualified for honors

print("Welcome to the Dean's List and Honor Roll Checker!")
print("Enter 'ZZZ' for the last name to quit.\n")

while True:
    last_name = input("Enter student's last name: ")
    if last_name == 'ZZZ':
        print("Quitting...")
        break
        
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print("{first_name} {last_name} made the Dean's List!")
    elif gpa >= 3.25:
         print("{first_name} {last_name} made the Honor Roll!")
    else:
        print("Sorry, {first_name} {last_name} did not qualify for any honors.")
