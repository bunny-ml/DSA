a: int = 12
b: str = "hello"
c: bool = True



if c == b == c:
	print("True")
else:
	print("False")

# or i can also do it like below 

result: bool = a == b == c
print(result)


if 4 > 2 > 1> 0 :
	print("this is not good way to write code")

l: list[int] = [ 1 , 3, 3]
l.append(l)

print(l)


infinity : float = float("inf")
neg_infinity: float = float("-inf")


print(infinity)
print(neg_infinity)
print(0 > infinity)
print(0 < infinity)
print(0 > neg_infinity)
print(0 < neg_infinity)
print(infinity/ neg_infinity)


text: str = "A" "B" "C" # not a good way to write a code 
print(text)

# same as 

text1: str = "A" + "B" + "C"
print(text1)


