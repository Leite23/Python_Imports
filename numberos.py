#f = ['fizz' for i in range(1,21) if i%3 == 0]
f = ['fizz' if i%3==0 else i for i in range(1,21) if i%2!=0]

print(f)