x = int(input())
y = int(input())

a = 0
if x > y:
    x, y = y, x
    
    
for j in range(x + 1,y):
    if j % 2 != 0:
        a = a + j

print(a)
