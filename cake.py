# coding: utf-8

import sys
import copy

# ピースの取り方
patterns = []
for i in range(5):
	for l in range(1, 5):
		pattern = [False, False, False, False, False,]
		for j in range(l):
			pattern[(i + j) % 5] = True
		patterns.append(pattern)
patterns.append([True, True, True, True, True,])

def search(assignment):
	# print(assignment)
	len_assignment = len(assignment)
	if len_assignment == 5:
		countings = []
		for pattern in patterns:
			counting = 0
			for i in range(5):
				if pattern[i]:
					counting += assignment[i]
			countings.append(counting)
		s = set(countings)
		if all((i in s) for i in range(1, 21)):
			print(assignment)
			sys.exit()
	elif len_assignment == 4:
		num = 21 - sum(assignment)
		assignment2 = copy.deepcopy(assignment)
		assignment2.append(num)
		search(assignment2)
	elif len_assignment < 4:
		limit = 18 + len_assignment - sum(assignment)# 21 - すでに割り当てたいちごの個数 - (4 - ピース数) + 1
		for i in range(1, limit):
			assignment2 = copy.deepcopy(assignment)
			assignment2.append(i)
			search(assignment2)

search([1])
print('not found')
