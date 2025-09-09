#tokens = ["2","1","+","3","*"]
tokens = ["4","13","5","/","+"]
stack = []
for i in range(len(tokens)):
    if tokens[i] not in "+-*/":
        stack.append(tokens[i])
    else:
        second = int(stack.pop())
        first = int(stack.pop())
        if tokens[i] == "+":
            result = first + second
        elif tokens[i] == "-":
            result = first - second
        elif tokens[i] == "*":
            result = first * second
        elif tokens[i] == "/":
            result = int(first / second) 
        stack.append(result)
print(stack)