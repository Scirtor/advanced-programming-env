import json
import os

def run():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "students.json")
        with open(file_path, "r", encoding="utf-8") as file:
            students = json.load(file)


        for student in students:
            grades = student.get("grades", [])
            avg = sum(grades) / len(grades) if grades else 0
            student["average"] = round(avg, 2)

        with open("students_with_average.json", "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

        print("New file created: students_with_average.json")


    except FileNotFoundError:
        print("students.json not found!")