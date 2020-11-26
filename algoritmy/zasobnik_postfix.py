from queue import LifoQueue


stack = LifoQueue()
postfix = ["2", "3", "4", "*", "+", "5", "-"]

for i in postfix:
    if i.isdigit():
        stack.put(int(i))
    else:
        a = stack.get()
        b = stack.get()
        if i == "*":
            stack.put(a * b)
        elif i == "/":
            stack.put(b / a)
        elif i == "+":
            stack.put(a + b)
        elif i == "-":
            stack.put(b - a)

print(stack.get())


# reseni z Engeto
postfix2 = [2, 3, 4, '*', '+', 5, '-']

def reduction(postfix):
    stack = LifoQueue(maxsize=len(postfix))
    for item in postfix:
        if item == '+':
            stack.put(stack.get() + stack.get())
        elif item == '-':
            stack.put(-stack.get() + stack.get())
        elif item == '*':
            stack.put(stack.get() * stack.get())
        elif item == '/':
            op2 = stack.get()
            op1 = stack.get()
            stack.put(op1 // op2)
        else:
            stack.put(int(item))
    return stack.get()

print(reduction(postfix2))

