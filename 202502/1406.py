from collections import deque
import sys

char = list(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

stack_left = deque(char)
stack_right = deque()

for _ in range(M):
    order = sys.stdin.readline().rstrip().split()
    if order[0] == 'P':
        stack_left.append(order[1])
    elif order[0] == 'B':
        if stack_left:
            stack_left.pop()
    elif order[0] == 'L':
        if stack_left:
            stack_right.appendleft(stack_left.pop())
    elif order[0] == 'D':
        if stack_right:
            stack_left.append(stack_right.popleft())

print("".join(stack_left) + "".join(stack_right))
