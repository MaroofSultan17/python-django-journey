# Assessment: Functions, Strings and Lists - Task 1
# Student Result Card Generator (Pakistani Board BISE Format)
# Topic: Functions, String Methods, and Input Validation

subjects = ["English", "Mathematics", "Science", "Urdu", "Computer Studies"]
max_marks_per_subject = 100
passing_marks_per_subject = 40


def format_name(name):
    # Cleans spaces from both sides and converts name to title case
    return name.strip().title()


def get_valid_marks(subject):
    # Asks for subject marks and validates without try-except using isdigit and if-else
    while True:
        user_input = input(f"Enter marks obtained in {subject} (0-100): ").strip()
        if user_input.isdigit():
            marks = int(user_input)
            if 0 <= marks <= 100:
                return marks
            else:
                print("  Marks must be between 0 and 100. Please try again.")
        else:
            print("  Invalid input! Please enter a valid whole number (0-100).")


def calculate_percentage(total, max_total):
    # Calculates percentage from total obtained marks and maximum marks
    if max_total <= 0:
        return 0.0
    return (total / max_total) * 100.0


def get_grade(percentage):
    # Returns letter grade based on percentage score
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


def get_valid_roll_number():
    # Asks for roll number and checks that it only contains digits
    while True:
        roll_number = input("Enter student roll number (digits only): ").strip()
        if roll_number.isdigit():
            return roll_number
        else:
            print("  Roll number must be numbers only. Please try again.")


def print_result_card(name, roll_number, subject_marks, failed_subjects, total_marks, max_total, percentage, grade, is_pass):
    # Prints a clean result card following Pakistani Board (BISE) rules
    print("\n" + "=" * 60)
    print("           BOARD OF INTERMEDIATE & SECONDARY EDUCATION      ")
    print("                     ANNUAL RESULT STATEMENT               ")
    print("=" * 60)
    print(f" Student Name : {name:<25} Roll Number : {roll_number}")
    print("-" * 60)
    print(f" {'No.':<4} | {'Subject Name':<28} | {'Max Marks':<10} | {'Obtained':<8}")
    print("-" * 60)

    for index, (sub, marks) in enumerate(subject_marks.items(), start=1):
        status_tag = " (F)" if marks < passing_marks_per_subject else ""
        marks_display = f"{marks}{status_tag}"
        print(f" {index:<4} | {sub:<28} | {max_marks_per_subject:<10} | {marks_display:<8}")

    print("-" * 60)

    # Pakistani Board (BISE) Examination Policy:
    # If a student fails (in any subject or overall), percentage and grade are withheld.
    # Result status shows RE-APPEAR with the list of subjects to reappear in.
    if is_pass:
        print(f" Total Marks Obtained : {total_marks} / {max_total}")
        print(f" Overall Percentage   : {percentage:.2f}%")
        print(f" Grade Awarded        : {grade}")
        print(" Final Result Status  : PASS")
        print("-" * 60)
        print(" Congratulations! The student has successfully passed the examination.")
    else:
        print(f" Total Marks Obtained : {total_marks} / {max_total}")
        print(" Overall Percentage   : --- (Not awarded on Re-appear)")
        print(" Grade Awarded        : ---")
        print(" Final Result Status  : RE-APPEAR")
        print("-" * 60)
        if len(failed_subjects) > 0:
            failed_list = ", ".join(failed_subjects)
            print(f" Notice: Candidate must RE-APPEAR in: {failed_list}")
        else:
            print(" Notice: Candidate must RE-APPEAR (Overall percentage below passing criteria).")
        print(" Eligible to appear in the upcoming supplementary examination.")

    print("=" * 60 + "\n")


# ----------------------------------------------------
# Main Program Execution
# ----------------------------------------------------

print("=" * 60)
print("             STUDENT RESULT CARD GENERATOR             ")
print("=" * 60)

# Step 1: Collect student name with validation
while True:
    raw_name = input("Enter student full name: ").strip()
    if raw_name == "":
        print("  Name cannot be empty. Please enter student name.")
    else:
        student_name = format_name(raw_name)
        break

# Step 2: Collect student roll number
student_roll_number = get_valid_roll_number()

# Step 3: Collect marks for each subject
print("\n--- Enter Marks for 5 Subjects ---")
subject_marks = {}
failed_subjects = []

for sub in subjects:
    marks = get_valid_marks(sub)
    subject_marks[sub] = marks
    if marks < passing_marks_per_subject:
        failed_subjects.append(sub)

# Step 4: Calculate total and percentage
total_marks = sum(subject_marks.values())
max_total = len(subjects) * max_marks_per_subject
percentage = calculate_percentage(total_marks, max_total)
grade = get_grade(percentage)

# Step 5: Check passing condition
# Student passes only if NO subject is below 40 AND percentage is at least 50
if len(failed_subjects) == 0 and percentage >= 50:
    is_pass = True
else:
    is_pass = False

# Step 6: Print result card
print_result_card(
    student_name,
    student_roll_number,
    subject_marks,
    failed_subjects,
    total_marks,
    max_total,
    percentage,
    grade,
    is_pass
)
