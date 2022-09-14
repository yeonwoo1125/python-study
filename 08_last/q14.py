s = input()

res = ''
for i in range(len(s)):
    cnt = 1

    for j in range(i + 1, len(s) - 1):
        if s[i] == s[j]:
            cnt += 1
    res += s[i]
    res += str(cnt)
    i += cnt

print(res)
