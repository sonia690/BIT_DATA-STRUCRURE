# STACK QUESTIONS

# Practical 1 — MoMo undo
stack = []
stack.append("Dial")
stack.append("PIN")
stack.append("Confirm")

# Undo one operation
undone = stack.pop()

print("Popped (undone):", undone)
print("Stack after undo (bottom → top):", stack)
top = stack[-1] if stack else None
print("Top (what remains):", top)
    


    # Practical 2 — UR labs
stack = []
stack.append("LabX")
stack.append("LabY")
stack.append("LabZ")

# Pop twice
pop1 = stack.pop()
pop2 = stack.pop()

print("Popped:", pop1, pop2)
print("Stack after two pops (bottom → top):", stack)
top = stack[-1] if stack else None
print("Top (what remains):", top)


# QUEUE QUESTIONS
from collections import deque

# CHUK: 8 patients labeled P1..P8 (front -> rear)
q = deque(['P1','P2','P3','P4','P5','P6','P7','P8'])

# serve 4 patients (dequeue 4)
served = [q.popleft() for _ in range(4)]

# state after serving
print("Served (in order):", served)
print("Queue now (front -> rear):", list(q))
print("Front now:", q[0] if q else None)


from collections import deque

# RRA: 6 clients labeled C1..C6 (front -> rear)
q = deque(['C1','C2','C3','C4','C5','C6'])

# serve three to determine who is served third
served_first_three = [q.popleft() for _ in range(3)]

print("First three served (in order):", served_first_three)
print("Third served:", served_first_three[-1])
print("Queue remaining (front -> rear):", list(q))
