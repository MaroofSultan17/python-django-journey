# Assessment Task 1: Student Scholarship Evaluation System
# Topic: Conditional Statements (if, elif, else), Comparison and Logical Operators

# Problem Statement:
# An educational institution wants to automate its scholarship evaluation process.
# A student must meet academic, attendance, and family income criteria to qualify.
#
# Requirements:
# 1. Collect student's name, academic marks, attendance percentage, and monthly family income.
# 2. Validate all inputs using simple if-else statements inside loops (no try-except).
# 3. Apply the following eligibility criteria:
#    - Academic marks must be at least 80%.
#    - Attendance must be at least 85%.
#    - Monthly family income must be Rs. 50,000 or less.
# 4. If eligible, award scholarship tier:
#    - Marks 90% or above: Full Scholarship
#    - Marks between 80% and 89%: Partial Scholarship
# 5. If not eligible, show the exact reason(s) why the student did not qualify.
# 6. Display a complete scholarship evaluation report.

print("--- Student Scholarship System ---")

# ----------------------------------------------------
# Step 1: Collect and validate student information
# ----------------------------------------------------

# Validate Student Name (cannot be empty)
while True:
    student_name = input("Enter student name: ").strip()
    if student_name == "":
        print("Name cannot be empty! Please try again.")
    else:
        break

# Validate Academic Marks
# Note: Maximum marks is assumed to be 100, so marks is already the percentage.
# We do not need an extra formula like (marks / 100) * 100.
while True:
    academic_marks = float(input("Enter academic marks (0-100): "))
    if academic_marks < 0 or academic_marks > 100:
        print("Invalid marks! Marks must be between 0 and 100.")
    else:
        break

# Validate Attendance Percentage (must be between 0 and 100)
while True:
    attendance_percentage = float(input("Enter attendance percentage (0-100): "))
    if attendance_percentage < 0 or attendance_percentage > 100:
        print("Invalid attendance! Attendance must be between 0 and 100.")
    else:
        break

# Validate Monthly Family Income (must be 0 or positive)
while True:
    monthly_income = float(input("Enter monthly family income (Rs.): "))
    if monthly_income < 0:
        print("Invalid income! Income cannot be negative.")
    else:
        break

# ----------------------------------------------------
# Step 2: Check eligibility criteria & track reasons
# ----------------------------------------------------

# We create an empty list to store reasons if any condition is not met
ineligibility_reasons = []

# Criterion 1: Academic marks must be at least 80%
if academic_marks < 80:
    ineligibility_reasons.append(f"Academic marks ({academic_marks}%) are below the required 80%.")

# Criterion 2: Attendance must be at least 85%
if attendance_percentage < 85:
    ineligibility_reasons.append(f"Attendance ({attendance_percentage}%) is below the required 85%.")

# Criterion 3: Monthly family income must be Rs. 50,000 or less
if monthly_income > 50000:
    ineligibility_reasons.append(f"Monthly income (Rs. {monthly_income}) exceeds Rs. 50,000.")

# ----------------------------------------------------
# Step 3: Determine scholarship award tier
# ----------------------------------------------------

# If list is empty, it means the student passed all 3 criteria
if len(ineligibility_reasons) == 0:
    is_eligible = True
    # Marks of 90% or above get Full Scholarship, otherwise Partial Scholarship
    if academic_marks >= 90:
        scholarship_type = "Full Scholarship"
    else:
        scholarship_type = "Partial Scholarship"
else:
    is_eligible = False
    scholarship_type = "Not Eligible"

# ----------------------------------------------------
# Step 4: Display complete evaluation report
# ----------------------------------------------------

print("\n--- Scholarship Evaluation Report ---")
print(f"Student Name: {student_name}")
print(f"Academic Marks: {academic_marks}%")
print(f"Attendance: {attendance_percentage}%")
print(f"Monthly Income: Rs. {monthly_income}")
print(f"Eligibility Status: {scholarship_type}")

# Display congratulatory message or failure reasons
if is_eligible:
    print(f"\nResult: Congratulations {student_name}! You are awarded a {scholarship_type}.")
else:
    print(f"\nResult: Sorry {student_name}, you are not eligible for a scholarship.")
    print("Reasons for Ineligibility:")
    for reason in ineligibility_reasons:
        print(f"- {reason}")
