"""
	find the minimum value 
"""

# l = [ 1, 2, 5, 6, 7, 9, 10 , 11, 0 , 22, 33, 11]

# lenth = len(l)
# value = l[0]

# for i in range(lenth):
# 	if value > l[i]:
# 		value = l[i]

# print(value)



"""
	find the max value in list 
"""

# l = [ 1, 1, 2, 11, 44, 66, 10, 69]

# value = l[0]
# for i in l:
# 	if value < i:
# 		value = i
# print(value)


"""
	stack 
"""
stack = [ '1', 'a', 'b']
print(f"stack {stack}")

# push
stack.append('x')
print(f"stack push {stack}")

# pop 
stack.remove('a')
print(f"stack pop {stack}")

# isEmpty
if bool(stack) == True:
	print(f"stack isEmpty")
else:
	print(f"stack is not Empty")
# size 
print(f"size of stack is {len(stack)}")

