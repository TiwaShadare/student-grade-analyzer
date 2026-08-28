import csv


def calculate_average(exam1, exam2, project):
    """Calculate the average of three grades."""
    return (exam1 + exam2 + project) / 3


def assign_letter_grade(average):
    """Assign a letter grade based on the average."""

    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def analyze_students():

    students = []

    with open("students.csv", "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            exam1 = float(row["Exam1"])
            exam2 = float(row["Exam2"])
            project = float(row["Project"])

            average = calculate_average(
                exam1,
                exam2,
                project
            )

            letter_grade = assign_letter_grade(average)

            student = {
                "name": row["Name"],
                "average": average,
                "grade": letter_grade
            }

            students.append(student)

    return students


def display_results(students):

    print("\nSTUDENT GRADE REPORT")
    print("-" * 40)

    for student in students:

        print(
            f"{student['name']}: "
            f"{student['average']:.2f} "
            f"({student['grade']})"
        )


def class_statistics(students):

    averages = []

    for student in students:
        averages.append(student["average"])

    class_average = sum(averages) / len(averages)

    highest_student = max(
        students,
        key=lambda student: student["average"]
    )

    lowest_student = min(
        students,
        key=lambda student: student["average"]
    )

    print("\nCLASS STATISTICS")
    print("-" * 40)

    print(f"Class Average: {class_average:.2f}")

    print(
        f"Highest Average: "
        f"{highest_student['name']} "
        f"({highest_student['average']:.2f})"
    )

    print(
        f"Lowest Average: "
        f"{lowest_student['name']} "
        f"({lowest_student['average']:.2f})"
    )


students = analyze_students()

display_results(students)

class_statistics(students)
