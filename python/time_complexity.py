print("DSA in python")

import time 
# start = time.time()


# for i in range(10):
#     print(i* '*')
# end = time.time() - start
# print(" time taken ",end)

start1 = time.time()

j = 0

while j<= 10:
    print( j * '*')
    j += 1

print(' time taken ' , time.time() - start1)