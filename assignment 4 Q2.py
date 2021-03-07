test_list1 = [int(item) for item in input("Enter the list items : ").split()]
test_list2 = [int(item) for item in input("Enter the list items : ").split()]

size_1 = len(test_list1) 
size_2 = len(test_list2) 

res = [] 
i, j = 0, 0

while i < size_1 and j < size_2: 
	if test_list1[i] < test_list2[j]: 
	    res.append(test_list1[i]) 
	    i += 1
	else: 
	    res.append(test_list2[j]) 
	    j += 1
for x in range(i, size_1):
    res.append(test_list1[x])
for x in range(j, size_2):
    res.append(test_list2[x])
print ("The combined sorted list is : " + str(res)) 
