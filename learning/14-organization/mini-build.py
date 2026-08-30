products = [
    {"name" : "laptop" ,"price" : "3000"} , 
    {"name" : "mouse" , "price" : "1000"} , 
    {"name" : "Keyboard" , "price" : "200"}
]

product_name = []

for item in products:
    product_name.append(item["name"])

print(product_name)