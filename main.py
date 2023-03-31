# Modules for use
import csv
import sys

FILENAME = "employee.csv"
# This is used to read the file
def read_employees():
    try:
        employees = []
        with open(FILENAME,newline= "") as file: 
            reader = csv.reader(file)
            for row in reader:
                employees.append(row)
        return employees
    except FileNotFoundError as error:
      print(f"{error}")
      exit_program()
    except Exception as e:
      print(type(e),e)
      exit_program()
      
# This is used to update the file
def write_employees(employees):
  try:
    with open(FILENAME,"w",newline="") as file:
      writer = csv.writer(file)
      writer.writerows(employees)
  except Exception as e:
    print(type(e),e)
    exit_program()

def exit_program():
  print("Terminating Program.")
  sys.exit()

#This is used to add the employee to the file
def add_employee(employees):
  empid = input("Enter in the Employee ID.").replace(" ",'')
  empsal = input("Enter in the Employee salary.").replace(" ",'')
  employee = [empid,empsal]
  employees.append(employee)
  write_employees(employees)
  print(f"Employee: {empid} with salary {empsal} was added.")
  
# This lists all of the data from the employee file
def list_employees(employeesdata):
  for i, employee in enumerate(employeesdata,start = 1):
    print(f"{i}. Employee ID: {employee[0]} Employee Salary: ${employee[1]}")
    
# This let's the user set a range to filter for employee salary
def sal_range(employeedata):
  startsal = input("Enter in the starting salary.").replace(",","")
  endsal = input("Enter in the ending salary.").replace(",","")
  count = 0
  for i,employee in enumerate(employeedata, start = 1):
    convertedval = employee[1].replace(",","")
    if(int(convertedval) >= int(startsal) and int(convertedval) <= int(endsal)):
      count += 1
      print(f"{count}. Employee ID: {employee[0]} Employee Salary: ${employee[1]}")
  if(count < 1):
      print("There are no employees within that salary range. Check input.")
      
  # This let's the user set a range to filter for employee id
def id_range(employeedata):
  startid = input("Enter in the starting ID.").replace(",","")
  endid = input("Enter in the ending ID.").replace(",","")
  count = 0
  for i,employee in enumerate(employeedata, start = 0):
    convertedval = employee[0].replace(",","")
    if(int(convertedval) >= int(startid) and int(convertedval) <= int(endid)):
      count += 1
      print(f"{count}. Employee ID: {employee[0]} Employee Salary: ${employee[1]}")
  if(count < 1):
      print("There are no employees within that ID range. Check input.")
      
  # This deletes existing employees
def delete_employees(employeedata):
  located = False
  id = input("Enter in the Employee ID you are looking for.")
  for i, employee in enumerate(employeedata,start = 0):
    if(employee[0] == id):
      located = True
      print(f"Employee: {employee[0]}, was successfully deleted.")
      employeedata.pop(i)
      
  if (located == False):
    print("Employee not found")
  else:
    write_employees(employeedata)
    
# This updates the employees salary
def give_raise(employeesdata):
  located = False
  empid = input("Enter in the Employee ID.").replace(" ",'')
  for i, employee in enumerate(employeesdata,start = 0):
    if(employee[0] == empid):
      located = True
      print(f"Employee: {employee[0]} was located.")
      empsalary = input("Enter in new salary.")
      employee[1] = empsalary
  if(located == False):
    print(f"Employee: {empid} was not found. Check input")
  else:
    write_employees(employeesdata)
    
# This updates the employee id
def update_employee_id(employeedata):
  located = False
  empid = input("Enter in the Employee ID.")
  for i, employee in enumerate(employeedata,start = 0):
    if(employee[0] == empid):
      located = True
      print(f"Employee: {employee[0]} was found.")
      newempid = input("Enter in the new Employee ID.")
      employee[0] = newempid
      print(f"Employee: {empid} ID was updated to {newempid}")
    if(located == False):
      print(f"Employee: {empid} was not found.")
    else:
      write_employees(employeedata)
      
# Display Menu that lists the list of commands
def display_menu():
  print("The Employee Salary Program")
  print()
  print("Select from a list of the commands below")
  print("list - List all employees.")
  print("add - Add an employee.")
  print("del - Delete an employee.")
  print("raise - Updates the employees salary.")
  print("empid - Updates the employees ID.")
  print("filtersal - Filter between a range of salaries.")
  print("filterid - Filter between a range of ID's.")
  print("exit - Exit Program.")
  print()

# Here are the function calls to display the menu and initially ready the employee file
display_menu()
employees = read_employees()

# Loop that waits for user to input the next command
while True:
  command = input("Command: ")
  if command.lower() == "list":
    list_employees(employees)
  elif command.lower() == "add":
      add_employee(employees)
  elif command.lower() == "del":
      delete_employees(employees)
  elif command.lower() == "raise":
      give_raise(employees)
  elif command.lower() == "empid":
      update_employee_id(employees)
  elif command.lower() == "filtersal":
      sal_range(employees)
  elif command.lower() == "filterid":
      id_range(employees)
  elif command.lower() == "exit":
      break
  else:
        print("Not a valid command. Please try again.\n")
print("Ending Salary Program")







