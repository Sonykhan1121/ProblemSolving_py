import re
s = input()
ans = re.findall(r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[aeiouAEIOU]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])",s)
# print(ans)
for i in ans:
    print(i)
if len(ans)==0:
    print(-1)