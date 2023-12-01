list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# Create a new list with odd numbers from list1 and even numbers from list2
new_list = [x for x in list1 if x % 2 != 0] + [x for x in list2 if x % 2 == 0]

print("New List:", new_list)
