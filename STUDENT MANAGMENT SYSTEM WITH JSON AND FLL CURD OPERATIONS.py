import json
import os

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return {}

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print("\n[!] Student ID already exists!")
        else:
            self.students[student_id] = {"name": name, "age": age, "grade": grade}
            self.save_data()
            print("\n[+] Student added successfully!")

    def search_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(f"\nFound -> ID: {student_id} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']}")
        else:
            print("\n[!] Student not found.")

    def update_student(self, student_id, name, age, grade):
        if student_id in self.students:
            self.students[student_id] = {"name": name, "age": age, "grade": grade}
            self.save_data()
            print("\n[+] Student updated successfully!")
        else:
            print("\n[!] Student ID not found.")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            self.save_data()
            print("\n[+] Student deleted successfully!")
        else:
            print("\n[!] Student ID not found.")

    def show_all(self):
        if not self.students:
            print("\n[!] No student records found.")
        else:
            print("\n--- All Student Records ---")
            for sid, info in self.students.items():
                print(f"ID: {sid} | Name: {info['name']} | Age: {info['age']} | Grade: {info['grade']}")


def main():
    manager = StudentManager()

    while True:
        print("\n=== Student Record System Menu ===")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Show All Records")
        print("6. Exit")

        choice = input("\nChoose an option (1-6): ").strip()

        if choice == "1":
            sid = input("Enter Student ID: ").strip()
            name = input("Enter Name: ").strip()
            age = input("Enter Age: ").strip()
            grade = input("Enter Grade: ").strip()
            manager.add_student(sid, name, age, grade)

        elif choice == "2":
            sid = input("Enter Student ID to search: ").strip()
            manager.search_student(sid)

        elif choice == "3":
            sid = input("Enter Student ID to update: ").strip()
            name = input("Enter New Name: ").strip()
            age = input("Enter New Age: ").strip()
            grade = input("Enter New Grade: ").strip()
            manager.update_student(sid, name, age, grade)

        elif choice == "4":
            sid = input("Enter Student ID to delete: ").strip()
            manager.delete_student(sid)

        elif choice == "5":
            manager.show_all()

        elif choice == "6":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()