n = int(input())

in_ = 0
out_ = 0
for i in range(n):
    k = int(input())
    if 10 <= k <= 20:
        in_ += 1
    else:
        out_ += 1
print(f"{in_} in")
print(f"{out_} out")