def mergeandcount(lft,rgt):
	i = len(lft) - 1
	j = len(rgt) - 1
	lft.reverse()
	rgt.reverse()
	x = len(lft)
	inv = 0
	rls = []
	while lft and rgt:
		if rgt[j] < lft[i]:
			inv += x
			item = rgt.pop()
			for i in range(x):
				print '{} conflicts with {}'.format(lft[i], item)
			rls.append(item)
			j -= 1
		else:
			x -= 1
			rls.append(lft.pop())
			i -= 1
	lft.reverse()
	rgt.reverse()
	rls.extend(lft or rgt)
	return (inv, rls)

def sortandcount(seq):
	if len(seq) <= 1:
		return (0, seq)

	mid = len(seq)/2
	lft = seq[:mid]
	rgt = seq[mid:]
	inv1, lft = sortandcount(lft)
	inv2, rgt = sortandcount(rgt)
	inv3, whole = mergeandcount(lft, rgt)
	return (inv3 + inv2 + inv1, whole)


if __name__ == '__main__':
	seq = [2,3,1,8,9,4]
	inv, ls = sortandcount(seq)
	print '# Inversions: {}'.format(inv)