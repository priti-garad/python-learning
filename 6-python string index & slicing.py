#string Indexing
name="Priit"
print(name)
print(name[0])

#string slicing
product="laptop pro 2024"
print(product[0:5])

text="DataAnalytics"
# # extracting first 4 characters
print("first 4 letters:",text[0:4])      #Data

# # extracting characters from middle
print("middle slice:",text[4:12])        #Analysis

# # extract till end
print("Till end:",text[4:])              #Analysis

# # extract from beginning
print("From start:",text[:4])            #Data

# # extract last 5 characters
print("Last 5 letters:",text[-5:])       #Analysis

# # skip text
print("skip Text:",text[0:12:2])
print("Reverse:",text[::-1])