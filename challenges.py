# STACK CHALLENG

def reverse_with_stack(s):
    stack = []                  # 1) create empty stack (list used as stack)
    for ch in s:                # 2) push each character of the string
        stack.append(ch)        #    append() is the push operation for list-based stack
    reversed_chars = []         # 3) container to collect popped chars (reversed order)
    while stack:                # 4) while stack not empty
        reversed_chars.append(stack.pop())  #    pop from stack (LIFO) and append to result
    return ''.join(reversed_chars)  # 5) join characters into a single string

# Example run
print(reverse_with_stack("RWANDAFIFO"))  # expected output: "OFIFADNAWR"

# QUEUE CHALLENG

from collections import deque                 # deque supports efficient O(1) append/popleft -> ideal for FIFO queues. 
queue = deque()                               # Step 1: create empty FIFO queue

# Step 2: on arrival
queue.append({"token": token, "arrival": timestamp})  # enqueue at tail

# Step 4: to serve
person = queue.popleft()                      # dequeue from head -> person to serve
give_goods(person)                            # hand out goods and record the transaction

# Step 5: loop until goods exhausted or queue empty
while goods_left and queue:
    person = queue.popleft()
    give_goods(person)
