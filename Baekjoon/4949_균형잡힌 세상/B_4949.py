while True:
    words = input()
    if words == '.':
        break
    else:
        stack = []
        flag = False
        for word in words:
            if word == "[" or word == "(":
                stack.append(word)
            else:
                if word == "]" or word == ")":
                    if not len(stack):
                        print("no")
                        flag = True
                        break
                    else:
                        if word == "]":
                            if stack[-1] == "[":
                                stack.pop()
                            else:
                                print("no")
                                flag = True
                                break
                        elif word == ")":
                            if stack[-1] == "(":
                                stack.pop()
                            else:
                                print("no")
                                flag = True
                                break

        if not flag:
            if not len(stack):
                print("yes")
            else:
                print("no")
