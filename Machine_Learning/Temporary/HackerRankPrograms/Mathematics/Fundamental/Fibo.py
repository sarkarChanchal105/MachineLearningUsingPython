
mod = 1000000007
def mul(A, B):
	res = [[0, 0], [0, 0]]
	for i in range(2):
		for j in range(2):
			for h in range(2):
				res[i][j] = res[i][j] + A[i][h] * B[h][j]
				#res[i][j] %= mod

	return res


t = int(input())
#t=1
for i in range(t):
    a, b, n = map(int, input().split(' '))
    res = [[1, 0], [0, 1]]
    x = [[0, 1], [1, 1]]

    while n:
        if (n % 2) == 1:
            res = mul(res, x)
        x = mul(x, x)
        n //= 2
        print(res)
    print((res[0][0] * a + res[0][1] * b) % mod)
