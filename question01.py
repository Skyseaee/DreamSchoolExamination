import sys

def generate_strings(source: str, target: str) -> int:
    m, n = len(source), len(target)
    dicts = {}
    for i, s in enumerate(source):
        if s in dicts:
            dicts[s].append(i)
        else:
            dicts[s] = [i]

    for t in target:
        if t not in dicts:
            return -1

    ans = sys.maxsize
    def dfs(i, j, res):
        nonlocal ans
        if j == n:
            ans = min(res, ans)
        
        if res > ans:
            return
        
        if i == m:
            res = dfs(0, j, res + 1)
        else:
            for k in range(i, m):
                if source[k] == target[j]:
                    dfs(k + 1, j + 1, res)
                
                dfs(k + 1, j, res)
        
    dfs(0, 0, 1)
    return ans

if __name__ == '__main__':
    ans = generate_strings('abc', 'abcbc')
    print(ans)