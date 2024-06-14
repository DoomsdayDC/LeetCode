from threading import stack_size
import sys

line = input()
stack = []

for char in line:
    if stack and char == stack[-1]:
        stack.pop()
    else:
        stack.append(char)
if stack:  # 这里检查 stack 是否为空
    print("".join(stack))
else:
    print(0)
