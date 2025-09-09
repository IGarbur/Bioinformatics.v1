def match(bracket):
    brackets = {"[":"]","{":"}","(":")"}
    return brackets[bracket]
def valid(s):
    stack = []
    if s[0] in "]})":
        return False
    for i in range(len(s)):
        if s[i] in "[{(":
            stack.append(s[i])
        else:
            if match(stack.pop())==s[i]:
                continue
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False
def main():
    s = "([])"
    x = valid(s)
    print(x)
main()