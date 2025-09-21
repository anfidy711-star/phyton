class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


def main():

    student_name = input("Вкажіть своє ім'я: ")


    student = Student(student_name)

    for i in range(2):
        while True:
            try:
                grade = float(input(f"Вкажіть оцінку {i + 1}: "))
                student.add_grade(grade)
                break
            except ValueError:
                print("Не число. Будь ласка, вкажіть оцінку.")


    average_grade = student.calculate_average()

    print("\n--- Електронний щоденник ---")
    print(f"Ім'я учня: {student.name}")
    print(f"Оцінки: {student.grades}")
    print(f"Середній бал: {average_grade:.2f}")


if __name__ == "__main__":
    main()