import employee_crud_mysql as emp

class Employee:
    def __init__(self):
        print("Welcome to the Employee Crud")

    def menu(self, chioce):
        match(chioce):
            case 1 : emp.create_db()
            case 2 : emp.create_table()
            case 3 : emp.desc_table()
            case 4 : emp.add_row_by_user()
            case 5 : emp.update_row_by_user()
            case 6 : emp.delete_row_by_user()
            case 7 : emp.read_all_employees()
            case 8 : emp.search_employee()
            case 9 : pass
            case _ : print("Invaild chioce")

    def database_start(self):
        while True:
            print("Enter your chioce : ")
            print("1. Create Database \n2. Create table \n3 .Desc Table \n4 .Add Row \n5. Update row \n6. Delete row \n7. Read all employees details \n8. Search employee\n9. Exit")
            chioce = int(input("Enter chioce : "))
            if chioce == 9:
                break
            self.menu(chioce)
        print("Application closed")


employee = Employee()
employee.database_start()