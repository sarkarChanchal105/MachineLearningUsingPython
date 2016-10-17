def answer(digits):
  dp = dict()
  dp[-1], dp[0] = 1, 1
  print(dp[-1],dp[0])

  for i in range(1, len(digits)):
    a=dp[i-1]
    b=(dp[i-2] if (i - 2 == -1 or digits[i-2] * 10 + digits[i-1] <= 26) else 0)

    dp[i] =a+b
    print(dp)

  return dp[len(digits) - 1]

print (answer([1,2,3]))