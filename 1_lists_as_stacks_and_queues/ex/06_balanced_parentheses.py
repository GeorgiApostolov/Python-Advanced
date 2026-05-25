expression = input()

parentheses = {
    "(": ")",
    "{": "}",
    "[": "]"
}
stack = []

for ch in expression:
    if ch in parentheses:
        stack.append(ch)
    elif ch in parentheses.values():
        if not stack:
            print("NO")
            break
        last_opening = stack.pop()
        if parentheses[last_opening] != ch:
            print("NO")
            break
else:
    if stack:
        print("NO")
    else:
        print("YES")