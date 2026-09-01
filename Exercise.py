with open('employees.txt', 'r') as emp_file:
    line = emp_file.readline()
    while line != '':
        name = line.strip()
        id_num = emp_file.readline().strip()
        dept = emp_file.readline().strip()
        print(f'Name: {name}')
        print(f'ID: {id_num}')
        print(f'Department: {dept}')
        line = emp_file.readline()