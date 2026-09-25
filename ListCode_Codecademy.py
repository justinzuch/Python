# Your code below: 
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]

preferred_size.append("Medium")
#preferred_size = [["Ainsley", "Small"], ["Ben", "Large"], ["Chani", "Medium"]]

print(preferred_size)

customer_data = [
["Ainsley", "Small", True],
["Ben", "Large", False],
["Chani", "Medium", True],
["Depak", "Medium", False]
]
new_customers = [
["Amit", "Large", True],
["Karim", "X-Large", False]
]

customer_data[2][2] = False
customer_data[1].remove(False)

print(customer_data)

customer_data_final = customer_data + new_customers
print(customer_data_final)
