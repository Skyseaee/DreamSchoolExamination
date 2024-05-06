def match_blanket(target: str) -> str:
    stack = []
    ans = [' '] * len(target)
    for i, ch in enumerate(target):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if len(stack) > 0:
                stack = stack[:len(stack) - 1]
            else:
                ans[i] = '?'

    for s in stack:
        ans[s] = 'x'
    
    return ''.join(ans)


if __name__ == '__main__':
    target = input()
    ans = match_blanket(target)
    # print(target)
    print(ans)