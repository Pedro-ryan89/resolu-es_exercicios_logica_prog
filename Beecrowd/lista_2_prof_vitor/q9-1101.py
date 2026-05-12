n, m = map(int, input().split())

while n > 0 and m > 0: 
    a = 0
    if n < m:
        m ,n= n,m      
    for i in range(m,n + 1):
        print(i, end=" ")
        a = a + i
    print(f"Sum={a}")
    
    n, m = map(int, input().split())

  

