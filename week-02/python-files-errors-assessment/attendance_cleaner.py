# Student Attendance Cleaner
# Topic: File Handling (TXT & CSV), Sets, List Comprehensions, and Exception Handling

import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "attendance.txt")
OUTPUT_FILE = os.path.join(BASE_DIR, "attendance_clean.csv")


def read_attendance():
    # Reads student attendance lines from attendance.txt
    # Catches FileNotFoundError if the file does not exist
    try:
        with open(INPUT_FILE, mode="r", encoding="utf-8") as file:
            raw_lines = file.readlines()
        return raw_lines
    except FileNotFoundError:
        print(f"Error: '{os.path.basename(INPUT_FILE)}' was not found.")
        print(f"Please ensure '{os.path.basename(INPUT_FILE)}' is in the program directory.")
        return None


def clean_attendance_records(raw_lines):
    # Cleans student names using strip() and title() inside a list comprehension
    cleaned_names = [line.strip().title() for line in raw_lines if line.strip() != ""]
    return cleaned_names


def save_cleaned_attendance(cleaned_list):
    # Saves cleaned and sorted student names to attendance_clean.csv
    try:
        with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["student_name"])
            for student in cleaned_list:
                writer.writerow([student])
        print(f"Successfully saved {len(cleaned_list)} unique students to '{os.path.basename(OUTPUT_FILE)}'.")
    except IOError as error:
        print(f"File writing error: {error}")


def display_attendance_summary(original_count, sorted_students):
    # Displays original count, unique count, and cleaned alphabetical list
    unique_count = len(sorted_students)
    duplicates_removed = original_count - unique_count

    print("\n" + "=" * 50)
    print("      STUDENT ATTENDANCE CLEANER REPORT           ")
    print("=" * 50)
    print(f" Total Raw Records Read  : {original_count}")
    print(f" Unique Students Found   : {unique_count}")
    print(f" Duplicate Names Removed : {duplicates_removed}")
    print("-" * 50)
    print(" Cleaned Attendance List (Alphabetical Order):")
    print("-" * 50)
    for idx, student in enumerate(sorted_students, 1):
        print(f"  {idx:<3} {student}")
    print("=" * 50 + "\n")


# ----------------------------------------------------
# Main Program Execution
# ----------------------------------------------------

print("\n========================================")
print("     STUDENT ATTENDANCE CLEANER         ")
print("========================================")

raw_records = read_attendance()

if raw_records is not None:
    # 1. Clean names with strip() and title() using a list comprehension
    cleaned_records = clean_attendance_records(raw_records)
    original_records_count = len(cleaned_records)

    # 2. Use a set to identify unique students and calculate unique count
    unique_students_set = set(cleaned_records)

    # 3. Sort cleaned student names alphabetically
    sorted_unique_students = sorted(unique_students_set)

    # 4. Save the final cleaned list to attendance_clean.csv
    save_cleaned_attendance(sorted_unique_students)

    # 5. Display summary metrics and formatted list
    display_attendance_summary(original_records_count, sorted_unique_students)
