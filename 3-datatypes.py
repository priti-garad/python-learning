# learning Data Types in Python
# 7 Data types

# # 1.Text Data Type1
#String
customer_name="Rohit"
print("customer_name is :",customer_name)
print("customer Datatype is :",type(customer_name))

# #2.Numeric Data Type
#2.1-Integer-complete number
rating = 4
order_quantity =3
print("Rating data type",type(rating))
print("order_Quantity data type :",type(order_quantity))

#2.2-Float-Decimal number
order_amount = 8599.50
print("order_amount data type :",type(order_amount))

# #2.3-Complex Number
a=3+4j
print(type(a))

# #3.Boolean-True/False
is_paid = True
print(is_paid,type(is_paid))

# 4.sequence
#4.1-List
cities=["Mumbai","Delhi","Pune","Chennai"]
print(cities)
print(type(cities))

#4.2-Tuple
dimension=(1928,1080)
print(dimension)
print(type(dimension))

#4.3-Range
num = range(5)
print(list(num))#[0,1,2,3]
print(type(num))

#5.Dictionary(dict)
student = {
   "name":"Anvi",
    "age":5,
    "city":"Mumbai"
}
print(student)
print(type(student))

#6.Set
numbers = {1,2,2,3,4}
print(numbers) #output{1,2,3,4}
print(type(numbers))

# 7,NoneType-No value
remarks=None
print(remarks,type(remarks))