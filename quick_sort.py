from time import perf_counter


def swap(sequence, index1, index2):
	temp = sequence[index1]
	sequence[index1] = sequence[index2]
	sequence[index2] = temp


def swap_pivot(sequence, low, high):
	middle = (low + high) // 2
	if sequence[middle] < sequence[low]:
		swap(sequence, low, middle)
	elif sequence[high] < sequence[low]:
		swap(sequence, high, low)
	elif sequence[high] < sequence[middle]:
		swap(sequence, high, middle)
	swap(sequence, middle, high)


def insertion_sort(sequence, high, low):
	for i in range(low, high + 1):
		current_val = sequence[i]
		j = i - 1
		while j >= low and current_val < sequence[j]:
			sequence[j + 1] = sequence[j]
			j -= 1
		sequence[j + 1] = current_val


def partition(sequence, low, high):
	i = low - 1
	swap_pivot(sequence, low, high)
	pivot = sequence[high]
	for j in range(low, high):
		if sequence[j] <= pivot:
			i += 1
			swap(sequence, i, j)
	swap(sequence, i + 1, high)
	return i + 1


def quicksort(sequence, low, high, transition_point):
	if low + transition_point > high and transition_point != 0:
		insertion_sort(sequence, high, low)
	elif low < high:
		pivot_index = partition(sequence, low, high)
		quicksort(sequence, low, pivot_index - 1, transition_point)
		quicksort(sequence, pivot_index + 1, high, transition_point)


def main():
	sequence = []
	N = int(input())
	for i in range(N):
		sequence += [int(input())]

	"""# ------------------------------- QS ------------------------------- #

	transition_point = 0
	qs = sequence.copy()
	tik = perf_counter()
	quicksort(qs, 0, len(sequence) - 1, transition_point)
	tok = perf_counter()
	total_time = tok - tik
	with open("times/qs" + ".txt", "a") as writing:
		writing.write(str(total_time) + "\n")"""

	# ------------------------------- QS+IS_100 ------------------------------- #

	transition_point = 250
	qs_is_15 = sequence.copy()
	tik = perf_counter()
	quicksort(qs_is_15, 0, len(sequence) - 1, transition_point)
	tok = perf_counter()
	total_time = tok - tik
	print(total_time)
	with open("times/qs_is_250" + ".txt", "a") as writing:
		writing.write(str(total_time) + "\n")

	"""# ------------------------------- QS+IS_200 ------------------------------- #

	transition_point = 200
	qs_is_10 = sequence.copy()
	tik = perf_counter()
	quicksort(qs_is_10, 0, len(sequence) - 1, transition_point)
	tok = perf_counter()
	total_time = tok - tik
	print(total_time)
	with open("times/qs_is_200" + ".txt", "a") as writing:
		writing.write(str(total_time) + "\n")

	# ------------------------------- QS+IS_500 ------------------------------- #

	transition_point = 500
	qs_is_5 = sequence.copy()
	tik = perf_counter()
	quicksort(qs_is_5, 0, len(sequence) - 1, transition_point)
	tok = perf_counter()
	total_time = tok - tik
	print(total_time)
	with open("times/qs_is_500" + ".txt", "a") as writing:
		writing.write(str(total_time) + "\n")

	# ------------------------------- QS+IS_30 ------------------------------- #

	transition_point = 30
	qs_is_30 = sequence.copy()
	tik = perf_counter()
	quicksort(qs_is_30, 0, len(sequence) - 1, transition_point)
	tok = perf_counter()
	total_time = tok - tik
	with open("times/qs_is_30" + ".txt", "a") as writing:
		writing.write(str(total_time) + "\n")"""


if __name__ == "__main__":
	main()
