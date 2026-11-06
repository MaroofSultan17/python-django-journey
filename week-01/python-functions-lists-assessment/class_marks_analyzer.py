# Assessment: Functions, Strings and Lists - Task 2
# Class Marks Analyzer
# Topic: Lists (create, append(), loop over, len(), sum(), max(), min(), sorted())


def get_student_count():
    # Asks for total number of students and validates using isdigit without try-except
    while True:
        user_input = input("Enter total number of students in the class: ").strip()
        if user_input.isdigit():
            count = int(user_input)
            if count > 0:
                return count
            else:
                print("  Number of students must be at least 1.")
        else:
            print("  Please enter a valid whole number.")


def get_valid_mark(student_name):
    # Asks for a student's mark and validates 0-100 without try-except
    while True:
        user_input = input(f"Enter marks for {student_name} (0-100): ").strip()
        if user_input.isdigit():
            mark = int(user_input)
            if 0 <= mark <= 100:
                return mark
            else:
                print("  Marks must be between 0 and 100.")
        else:
            print("  Invalid mark! Please enter a whole number between 0 and 100.")


def calculate_class_average(marks):
    # Calculates class average using sum() divided by len()
    if len(marks) == 0:
        return 0.0
    return sum(marks) / len(marks)


def find_performers_by_mark(names, marks, target_mark):
    # Finds all student names who scored a specific mark
    performers = []
    for i in range(len(marks)):
        if marks[i] == target_mark:
            performers.append(names[i])
    return performers


def get_students_above_average(names, marks, class_average):
    # Finds all students who scored strictly higher than class average
    above_average_list = []
    for i in range(len(names)):
        if marks[i] > class_average:
            above_average_list.append((names[i], marks[i]))
    return above_average_list


def display_analysis_report(names, marks):
    # Calculates class statistics and prints a clear report
    total_students = len(marks)
    class_average = calculate_class_average(marks)
    highest_mark = max(marks)
    lowest_mark = min(marks)

    highest_scorers = find_performers_by_mark(names, marks, highest_mark)
    lowest_scorers = find_performers_by_mark(names, marks, lowest_mark)

    passed_count = 0
    failed_count = 0
    for m in marks:
        if m >= 50:
            passed_count += 1
        else:
            failed_count += 1

    above_average_students = get_students_above_average(names, marks, class_average)
    sorted_marks = sorted(marks, reverse=True)

    print("\n" + "=" * 65)
    print("                    CLASS MARKS ANALYSIS REPORT                  ")
    print("=" * 65)
    print(f" Total Students Evaluated : {total_students}")
    print(f" Class Average Mark       : {class_average:.2f} / 100")
    print(f" Highest Mark Achieved    : {highest_mark} (Scored by: {', '.join(highest_scorers)})")
    print(f" Lowest Mark Achieved     : {lowest_mark} (Scored by: {', '.join(lowest_scorers)})")
    print("-" * 65)
    print(f" Students Passed (>= 50)  : {passed_count}")
    print(f" Students Failed (< 50)   : {failed_count}")
    print("-" * 65)

    print(" Students Scoring Above Class Average:")
    if len(above_average_students) > 0:
        for index, (s_name, s_mark) in enumerate(above_average_students, start=1):
            difference = s_mark - class_average
            print(f"   {index}. {s_name:<25} - {s_mark} marks (+{difference:.2f} above average)")
    else:
        print("   None (all students scored the same mark).")

    print("-" * 65)
    print(" Marks Ranked from Highest to Lowest:")
    ranked_string = ", ".join(str(m) for m in sorted_marks)
    print(f"   [ {ranked_string} ]")
    print("=" * 65 + "\n")


# ----------------------------------------------------
# Main Program Execution
# ----------------------------------------------------

print("=" * 65)
print("             ACADEMIC CLASS MARKS ANALYZER               ")
print("=" * 65)

student_count = get_student_count()

student_names = []
student_marks = []

print(f"\nEntering records for {student_count} student(s):")
for i in range(1, student_count + 1):
    print(f"\n--- Student #{i} ---")
    while True:
        raw_name = input(f"Enter name of Student #{i}: ").strip()
        if raw_name == "":
            print("  Name cannot be empty. Please enter a valid name.")
        else:
            clean_name = raw_name.title()
            break

    valid_mark = get_valid_mark(clean_name)
    student_names.append(clean_name)
    student_marks.append(valid_mark)

# Display final analytical summary
display_analysis_report(student_names, student_marks)
