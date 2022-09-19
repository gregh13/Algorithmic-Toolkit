from itertools import combinations


def inversions_better(sequence):
    def calc_max_indices(elements):
        # Single pass to find all index values of the max value in a list
        if not elements:
            return []
        max_indices = [0]
        max = elements[0]
        for i, value in enumerate(elements):
            if value < max:
                continue
            elif value == max:
                max_indices.append(i)
            else:
                max = value
                max_indices = [i]
        return max, max_indices
    inversions = 0

    while True:
        max_val, max_index_list = calc_max_indices(sequence)
        seq_length = len(sequence)
        index_length = len(max_index_list)
        # In event that only remaining values in list are all the same (or just one value in list)
        if seq_length <= index_length:
            return inversions
        multiplier = 1
        for index_val in max_index_list:
            # Remove current iteration from list length
            index_length -= 1
            # Minus 1 from seq_len to account for index/len issue, check range from max to end of seq, minus duplicates
            inversions += (seq_length - 1) - ((index_val - index_length) * multiplier)
            # Multiplier accounts for previous max values that would create inversions in subsequent ranges in sequence
            multiplier += 1
            # Remove the item from the original sequence
            sequence.remove(max_val)
    return inversions


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        print("i: {0}, j: {1}".format(i, j))
        print("a[i]: {0}, a[j]: {1}".format(a[i], a[j]))
        if a[i] > a[j]:
            print("Inversion!")
            number_of_inversions += 1
    return number_of_inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    # print(inversions_naive(elements))
    print(inversions_better(elements))
