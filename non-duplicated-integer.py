# QUESTION:
# This is an interview question asked by Google.
# Given an array of integers where every integer occurs three times except for one integer, 
# which only occurs once, find and return the non-duplicated integer.
# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19. 

# 1:
def check_array(my_array):
    sant_array = set(my_array)
    return (i for i in sant_array if (my_array.count(i) == 1))

# 2:
a = [6, 1, 3, 3, 3, 6, 6, 1, 5, 55, 6, 5]
for i in range(len(a)):
	if a[i] not in a[i+1:] and a[i] not in a[:i]:
		print(a[i])
		break

# 3:
for i in x:
    if x.count(i) == 1:
        print(i)