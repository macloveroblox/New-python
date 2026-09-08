performance_data = {
    "Sales": {
        "Alice": [80, 85, 88, 90],
        "Bob": [70, 75, 78, 80],
        "Charlie": [60, 65, 70, 72]
    },
    "Engineering": {
        "David": [90, 92, 94, 95],
        "Eve": [85, 88, 87, 90],
        "Frank": [88, 87, 86, 86]
    },
    "HR": {
        "Grace": [70, 72, 74, 76],
        "Heidi": [65, 68, 70, 73],
        "Ivan": [60, 62, 64, 66]
    }
}


def calculate_average(scores):
    return sum(scores) / len(scores)


employee_averages = {
    department: {
        employee: calculate_average(scores)
        for employee, scores in employees.items()
    }
    for department, employees in performance_data.items()
}

department_top_performers = {
    department: max(averages, key=averages.get)
    for department, averages in employee_averages.items()
}

department_averages = {
    department: sum(averages.values()) / len(averages)
    for department, averages in employee_averages.items()
}

highest_average_department = max(department_averages, key=department_averages.get)

continuously_improving = [
    employee
    for employees in performance_data.values()
    for employee, scores in employees.items()
    if all(current > previous for previous, current in zip(scores, scores[1:]))
]


print("Performance Summary Report")
print("=" * 28)

print("\nAverage performance score for each employee:")
for department, averages in employee_averages.items():
    print(f"{department}:")
    for employee, average in averages.items():
        print(f"  {employee}: {average:.2f}")

print("\nTop performer in each department:")
for department, employee in department_top_performers.items():
    print(f"  {department}: {employee} ({employee_averages[department][employee]:.2f})")

print("\nDepartment with the highest average performance score:")
print(
    f"  {highest_average_department} "
    f"({department_averages[highest_average_department]:.2f})"
)

print("\nEmployees showing continuous improvement:")
for employee in continuously_improving:
    print(f"  {employee}")