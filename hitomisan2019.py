for i in range(1, 10):
	for j in range(10):
		for k in range(10):
			for l in range(10):
				x = i * 100 + j * 10 + k
				# y = 90 + l
				a = l * x
				if not (100 <= (a % 1000) <= 199):
					continue
				b = 9 * x
				if not (0 <= (b % 1000) <= 99):
					continue
				ans = a + b * 10
				if 20000 <= ans <= 29999 and ans % 10 == k:
					print(ans)
