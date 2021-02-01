
n = float(input())
sum = 1;fact = 1;
i = 1
while(i <= n):
  fact = fact*i
  sum = sum + 1/fact
  i+=1
print(sum)