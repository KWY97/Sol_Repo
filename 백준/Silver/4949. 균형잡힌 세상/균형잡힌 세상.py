while True:
    sentence = input()

    if sentence == ".":
        break

    stack = []
    balanced = True

    for char in sentence:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")" and stack and stack[-1] == "(":  
            stack.pop()
        elif char == "]" and stack and stack[-1] == "[": 
            stack.pop()
        elif char == ")" or char == "]":
            balanced = False
            break

    if balanced and not stack:
        print("yes")
    else:
        print("no")
