
a = [10, 5, 10]
n = len(a)
second_min=min = 1000000
second_max = max = -1000000
for i in range(n):
    if max < a[i]:
        second_max = max
        max = a[i]
    elif second_max < a[i] and a[i]<max:
        second_max = a[i]
    if min > a[i]:
        second_min = min
        min = a[i]
    elif second_min > a[i] and a[i]>min:
        second_min = a[i]

print(second_min)
print(min)
print(second_max,max)
