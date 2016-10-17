def answer(digits):
  dp = dict()
  dp[-1], dp[0] = 1, 1

  for i in range(1, len(digits)):
    dp[i] = dp[i-1] + (dp[i-2] if (i - 2 == -1 or digits[i-2] * 10 + digits[i-1] <= 26) else 0)
    print(dp[i])

  return dp[len(digits) - 1]

print (answer([1,2,3,4]))

