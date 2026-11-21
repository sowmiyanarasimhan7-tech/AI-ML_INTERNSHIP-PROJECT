"""
Module 02 - Student Grade Calculator
A beginner-friendly Python mini project.
"""

SUBJECTS = ["Python", "Mathematics", "Computer Science", "English", "Data Science"]


def get_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Please enter a mark between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"


def main():
    print("=" * 45)
    print("             STUDENT GRADE CALCULATOR")
    print("=" * 45)

    name = input("Enter student name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    marks = {}
    for subject in SUBJECTS:
        marks[subject] = get_mark(subject)

    total = sum(marks.values())
    average = total / len(SUBJECTS)
    grade = calculate_grade(average)
    status = "Pass" if average >= 60 else "Needs improvement"

    print("\n" + "=" * 45)
    print("                    RESULT")
    print("=" * 45)
    print(f"Student Name : {name}")
    for subject, mark in marks.items():
        print(f"{subject:<20}: {mark:g}")
    print("-" * 45)
    print(f"Total Marks  : {total:g} / {len(SUBJECTS) * 100}")
    print(f"Average      : {average:.2f}%")
    print(f"Grade        : {grade}")
    print(f"Status       : {status}")
    print("=" * 45)


if __name__ == "__main__":
    main()
