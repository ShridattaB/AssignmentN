# Question9: Create a dictionary representing a shopping cart with items and their prices. Calculate the total cost of the items.

# Sample Input:
# Shopping Cart: {'item1': 10.0, 'item2': 20.0, 'item3': 15.0}

# Expected Output:
# Total cost: 45.0

# Explanation: Calculate the total cost by summing the prices of the items in the shopping cart.
shopping_Cart={'item1': 10.0, 'item2': 20.0, 'item3': 15.0}
values= shopping_Cart.values()
sum=0
for i in values:
    sum=sum+i
print(sum)

