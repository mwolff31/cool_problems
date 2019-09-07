import numpy as np
import math

def regular_idx(idx, total):
	if math.copysign(1, idx) < 0:
		idx = total - abs(idx)
	return idx

def count_one_way(necklace, reverse, used_idxs):
	num_beads = len(necklace)

	if reverse:
		it_step = -1
	else:
		it_step = 1
	counts = []
	for i in range(num_beads):
		j = i
		first = necklace[i]
		if not reverse:
			used_idxs_i = [j]
		k = 0
		count_i = 0
		while k < num_beads-2:
			special_case=False
			if j+it_step == num_beads:
				next_idx = 0
				special_case=True
			if j == num_beads:
				j = 0
				next_idx = j + it_step
				special_case=True
			if not special_case:
				next_idx = j + it_step
			streak_condition = (necklace[next_idx]==first) or (necklace[next_idx]=='w')
			used_idx_condition = regular_idx(next_idx, num_beads) not in used_idxs_i
			if streak_condition and used_idx_condition:
				count_i += 1
				if not reverse:
					used_idxs_i.append(next_idx)
			else:
				break
			k+=1
		counts.append(count_i)
		if not reverse:
			used_idxs.append(used_idxs_i)
	return counts, used_idxs

def main(necklace):

	forward_counts, used_idxs = count_one_way(necklace, reverse=False, used_idxs=[])
	used_idxs.reverse()
	backwards_counts, _ = count_one_way(necklace, reverse=False, used_idxs=used_idxs)

	backwards_counts.reverse()

	forward_counts = np.asarray(forward_counts)
	backwards_counts = np.asarray(backwards_counts)

	total_counts = forward_counts + backwards_counts

	print(total_counts.max())

main('brbrrrbbbrrrrrbrrbbrbbbbrrrrb')







