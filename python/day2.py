"""
						ARRAY
						-----

#  array to store multiple values at one place but all values should of same tyep

# arr = [1, 2, 3, 4]

# print(f"length of array named arr: {len(arr)}")
# print(f"index 0 of arr: {arr[0]}")

# # update array arr

# arr[0] = 100


# print(f"updated array: {arr[0]}")

					 __              __
					|	one D array	   |								
					|__              __|

####################################################################################
						STACK (LIFO) 	
						------------
	   |        |
	   |--------|
	   |	5	|
	   |--------|
	   |	4	|   <----- Stack
	   |--------|
	   |	2	|
	   |________|

	
			time complexity <--- O(n)



			STACK operation
				

				1) push()  			<-- push on top  
				2) pop()   			<-- pop from top
				3) peek() / top() 	<-- peek at top of the stack
				4) isEmpty()  		<-- return True or False 
				5) isFull()			<-- return True if full and false if not full


####################################################################################
						Queue ( first in first out)
						---------------------------


				time complexity <-- O(1)

													opertions which we can perform																									
		 _________														
		|         |	Front 							1) Enqueue() <-- add element at the end			
		|    1    |										  and rear is updated		
		|_________|									2) Dequeue() <-- remove the front element
		|         |    <--- line or Queue				   and the Front is updated
		|    2    |									3) Peek() <-- used to check the top or front
		|_________|											of queue
		|         |									4) isFull() <-- gives True or False
		|     3   |									5) isEmpty() <-- gives True or False
		|_________|
		|         |
		|      4  |	Rear
		|_________|

	types of Queue:
	---------------

	a) Simple Queue

		(front) -----elements--------- (rear)
	
	b) Circular Queue
		
		(rear){E}------{D}-----{C}
				^		    	|
				|			    |
				|			    |
		 (front) {A}------------{B}

	c) Priority Queue
		
		priority

		1  {call}
		2  {game} {app} {movie}
		3  {download the updates}

	d) DOuble Ended Queue

	   add and remove elements from both front and rear

	   (front)----------elements-----(rear)

	   operations:
	   
	   1) popfront()
	   2) poprear()
	   3) pushrear()
	   4) pushfront()
####################################################################################
						

####################################################################################
####################################################################################
####################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################

"""