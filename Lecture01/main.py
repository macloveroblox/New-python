import random
import sys


def print_title():
    print("= " * 20)
    print("โปรแกรมจัดการข้อมูลนักเรียน (Basic Python)")
    print("= " * 20)


def get_integer(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("กรุณาใส่จำนวนเต็มเท่านั้น")
            continue

        if min_value is not None and value < min_value:
            print(f"ค่าต้องไม่ต่ำกว่า {min_value}")
            continue
        if max_value is not None and value > max_value:
            print(f"ค่าต้องไม่เกิน {max_value}")
            continue
        return value


def show_students(students):
    if not students:
        print("ยังไม่มีข้อมูลนักเรียน")
        return

    print("\nรายการนักเรียนทั้งหมด:")
    for idx, student in enumerate(students, start=1):
        name = student['name']
        scores = student['scores']
        average = sum(scores) / len(scores)
        print(f"{idx}. {name}: คะแนน {scores}, เฉลี่ย {average:.2f}")


def add_student(students):
    name = input("ใส่ชื่อนักเรียน: ").strip()
    if not name:
        print("ชื่อต้องไม่ว่าง")
        return

    scores = []
    for subject in ["คณิตศาสตร์", "ภาษาอังกฤษ", "วิทยาศาสตร์"]:
        score = get_integer(f"คะแนน{subject} (0-100): ", 0, 100)
        scores.append(score)

    students.append({
        'name': name,
        'scores': scores,
    })
    print(f"เพิ่มนักเรียน {name} แล้ว")


def find_student(students, keyword):
    keyword = keyword.lower()
    return [student for student in students if keyword in student['name'].lower()]


def search_student(students):
    keyword = input("ค้นหาชื่อนักเรียน: ").strip()
    if not keyword:
        print("กรุณาใส่คำค้นหา")
        return

    found = find_student(students, keyword)
    if not found:
        print("ไม่พบชื่อนักเรียนที่ต้องการ")
        return

    print("ผลการค้นหา:")
    show_students(found)


def remove_student(students):
    if not students:
        print("ไม่มีนักเรียนให้ลบ")
        return

    show_students(students)
    index = get_integer("เลือกหมายเลขนักเรียนที่ต้องการลบ: ", 1, len(students))
    removed = students.pop(index - 1)
    print(f"ลบนักเรียน {removed['name']} ออกเรียบร้อย")


def random_student(students):
    if not students:
        print("ยังไม่มีนักเรียนในระบบ")
        return
    student = random.choice(students)
    average = sum(student['scores']) / len(student['scores'])
    print(f"สุ่มนักเรียน: {student['name']} (คะแนนเฉลี่ย {average:.2f})")


def calculate_grade(average):
    if average >= 80:
        return 'A'
    if average >= 70:
        return 'B'
    if average >= 60:
        return 'C'
    if average >= 50:
        return 'D'
    return 'F'


def show_report(students):
    if not students:
        print("ยังไม่มีข้อมูลสำหรับแสดงรายงาน")
        return

    report = []
    for student in students:
        average = sum(student['scores']) / len(student['scores'])
        grade = calculate_grade(average)
        report.append((student['name'], average, grade))

    report.sort(key=lambda item: item[1], reverse=True)
    print("\nรายงานผลคะแนนเฉลี่ย (เรียงจากมากไปน้อย):")
    for idx, (name, average, grade) in enumerate(report, start=1):
        print(f"{idx}. {name}: เฉลี่ย {average:.2f}, เกรด {grade}")


def main():
    students = []

    actions = {
        1: ("แสดงนักเรียนทั้งหมด", show_students),
        2: ("เพิ่มนักเรียน", add_student),
        3: ("ค้นหานักเรียน", search_student),
        4: ("ลบข้อมูลนักเรียน", remove_student),
        5: ("สุ่มนักเรียน", random_student),
        6: ("แสดงรายงานเกรด", show_report),
        0: ("ออกจากโปรแกรม", None),
    }

    while True:
        print_title()
        for key, (label, _) in actions.items():
            print(f"{key}. {label}")

        choice = get_integer("เลือกเมนู: ", 0, max(actions.keys()))
        if choice == 0:
            print("ขอบคุณที่ใช้โปรแกรม! บ๊ายบาย")
            sys.exit(0)

        _, action = actions[choice]
        action(students)
        input("กด Enter เพื่อกลับสู่เมนูหลัก...")
        print()  # ช่องว่างระหว่างรอบ


if __name__ == '__main__':
    main()