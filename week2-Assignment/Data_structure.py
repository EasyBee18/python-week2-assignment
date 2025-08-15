# to create an empty list 
my_list = [];

# to append items to the list
my_list.append(10);
my_list.append(20);
my_list.append(30);
my_list.append(40);

# to insert a value in a list
my_list.insert(1,15);

# to extend the list
my_list.extend([50, 60, 70]);

# to remove the last item from the list
my_list.pop();

# to sort the list in ascending order
my_list.sort()

# to find the index of an item in the list and print the value
Index_of_nthList = my_list.index(30);
print("Index of 30 in the list:", Index_of_nthList);
