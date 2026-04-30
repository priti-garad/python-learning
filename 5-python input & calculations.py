#Inpuit and Typecastng

name=input("Enter your name :")
print("Welcome",name)

age =int(input ("Enter your age:"))
print(type(age))
age=age+5
print("Your age is :",age)

temprature=float(input ("Enter today's temprature:"))
print(type(temprature))

#convert number to string
sales=50000
text="Total sales:"+str(sales)
print(text)

#Total Sales calculator
product=input("product name:")
quantity=int(input("Enter quantity sold:"))
price_per_unit=float(input("Enter price per unit:"))
total_sales = quantity * price_per_unit
print("Product:",product)
print("Total Sales Amount=",total_sales)

name = input("Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))
bonus = float(input("Enter Bonus Amount: "))
tax_percentage = float(input("Enter Tax %: "))

gross_salary = basic_salary + bonus
tax_amount = gross_salary * (tax_percentage / 100)
net_salary = gross_salary - tax_amount

print("\n--- Salary Slip ---")
print("Employee:", name)
print("Gross Salary:", gross_salary)
print("Tax:", tax_amount)
print("Net Salary:", net_salary)

