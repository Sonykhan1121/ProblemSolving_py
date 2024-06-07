subjects,students  = map(int,input().split())
a = []
for i in range(students):
    a.append(list(map(float,input().split())))
# print(a)
for j in range(subjects):
    sum =0
    for i in range(students):
        sum+=a[i][j]
    print(f"{sum/students:.1f}")
