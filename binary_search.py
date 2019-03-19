def search(sorted_array, value):
	length = len(sorted_array)
	half_length = int(length/2)
	middle = sorted_array[half_length]
	if len(sorted_array) == 1 and sorted_array[0] != value:
		return False
	elif (middle == value):
		return True
	elif (middle > value):
		return search(sorted_array[0:half_length], value)
	else:
		return search(sorted_array[half_length:length], value)

my_list = [1,2,3,4,5,6]
print(search(my_list, 4))
