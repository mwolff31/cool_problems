import argparse
import math

def regular_idx(idx, total):
	if math.copysign(1, idx) < 0:
		idx = total - abs(idx)
	return idx

# necklace & split index --> count from one side
def count_one_way(necklace, ind, reverse, idxs_covered):
	num_beads = len(necklace)
	first = necklace[ind]
	count = 0
	j = ind
	k = 0
	if reverse:
		it_step = -1
	else:
		it_step = 1

	idxs_covered.append(regular_idx(ind, num_beads))

	while k < num_beads:

		special_case = False

		if j == num_beads-1:
			next_idx = 0
			special_case = True

		if j > num_beads-1:
			j = 0
			next_idx = j + it_step
			special_case = True

		if not special_case:
			next_idx = j + it_step

		if ((necklace[next_idx] == first) or (necklace[next_idx] == 'w')) and (regular_idx(next_idx, num_beads) not in idxs_covered):
			count+=1
		else:
			break

		j += it_step
		k += 1
	print('done')
	return count, idxs_covered

def main(necklace):

	num_beads = len(necklace)
	best_count = 0
	best_split = 0


	for i in range(num_beads-1):
		idxs = []
		current_count = 2
		forward_count, idxs = count_one_way(necklace=necklace, ind=i+1, reverse=False, idxs_covered=idxs)
		print(idxs)
		backward_count, _ = count_one_way(necklace=necklace, ind=i, reverse=True, idxs_covered=idxs)
		current_count = forward_count + backward_count
		print(forward_count)
		print(backward_count)
		if current_count > best_count:
			best_count = current_count
			best_split = i

	return best_count, best_split, best_split+1

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--necklace')
	args = parser.parse_args()

	count, first_ind, second_ind = main(args.necklace)

	print('best streak:', count)
	print('split between:', [first_ind, second_ind])