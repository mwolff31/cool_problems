import time
start = time.time()
import argparse

def count_one_way(necklace, ind, reverse):
	num_beads = len(necklace)
	first = necklace[ind]
	count = 1
	j = ind
	k = 0
	if reverse:
		it_step = -1
	else:
		it_step = 1

	while k < num_beads-1:

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

		if first == 'w' and necklace[next_idx] in ['b', 'r']:
			first = necklace[next_idx]

		if (necklace[next_idx] == first) or (necklace[next_idx] == 'w'):
			count+=1
		else:
			break

		j += it_step
		k += 1
	return count

def main(necklace):

	num_beads = len(necklace)
	best_count = 0
	best_split = 0

	for i in range(num_beads-1):
		current_count = 0
		forward_count = count_one_way(necklace=necklace, ind=i+1, reverse=False)
		backward_count = count_one_way(necklace=necklace, ind=i, reverse=True)
		current_count = forward_count + backward_count
		if current_count > best_count:
			best_count = current_count
			best_split = i

	if best_count > num_beads:
		best_count = num_beads

	return best_count, best_split, best_split+1

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--necklace')
	args = parser.parse_args()

	count, first_ind, second_ind = main(args.necklace)

	print('number of beads:', len(args.necklace))
	print('best streak:', count)
	print('split between:', [first_ind, second_ind])
	end = time.time()
	print(end - start)