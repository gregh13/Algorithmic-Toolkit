from itertools import combinations
from random import randint


def inversions_quick3_sort_way(sequence):
    def partition3(array, left, right, inversions):
        # My implementation of the Quick3 sorting algorithm
        print("\nNew Batch")
        mid_1 = left  # left bound of same block
        mid_2 = left + 1  # right bound of same block
        pivot = array[left]
        for i in range(left, right):
            # Debugging statements
            print("Pivot: ", pivot)
            print("Mid_1: ", mid_1)
            print("Mid_2: ", mid_2)
            print("array[i+1]: ", array[i+1])
            print("Array Before: ", array[left:right+1])
            print("Inversions Before: ", inversions)
            if array[i + 1] == pivot:
                # Swap items
                array[mid_2], array[i + 1] = array[i + 1], array[mid_2]

                # Update inversions
                inversions[0] += (i + 1) - mid_2

                # Prepare for next iteration
                mid_2 += 1
            if array[i + 1] < pivot:
                # Found number less than pivot element, perform swap to add block to "smaller than" section
                array[mid_1], array[i + 1] = array[i + 1], array[mid_1]

                # Update inversions
                inversions[0] += (i + 1) - mid_1

                # Swap again to return the duplicate pivot value back
                array[mid_2], array[i + 1] = array[i + 1], array[mid_2]
                # Update the index for the mid-block
                mid_1 += 1
                mid_2 += 1
            print("Array After:  ", array[left:right+1])
            print("Inversions After: ", inversions)
            print("---------------")

        return mid_1, mid_2

    def randomized_quick_sort(array, left, right, inversions):
        if left >= right:
            return
        k = randint(left, right)
        # swap random index to the start of list as the pivot element
        array[left], array[k] = array[k], array[left]
        m1, m2 = partition3(array, left, right, inversions)
        randomized_quick_sort(array, left, m1, inversions)
        randomized_quick_sort(array, m2, right, inversions)

    # Initialize inversions - use value inside array for better manipulation within local function scopes
    inversions = [0]

    # Call recursive function
    randomized_quick_sort(sequence, 0, len(sequence) - 1, inversions)
    return inversions[0]


def inversions_best(sequence):
    def calc_indices(elements):
        # Single pass to find all index values of the both the max and min value in a list
        if not elements:
            return 0, [], 0, []
        max_indices = [0]
        min_indices = [0]
        max_val = elements[0]
        min_val = elements[0]
        for i, value in enumerate(elements[1:]):
            # print("Value: ", value)
            # print("Min List: ", min_indices)
            # print("Max List: ", max_indices)
            if value < max_val:
                if value < min_val:
                    min_val = value
                    min_indices = [i+1]
                    continue
                elif value == min_val:
                    min_indices.append(i+1)
                    continue
                else:
                    continue
            elif value == max_val:
                max_indices.append(i+1)
            else:
                max_val = value
                max_indices = [i+1]
        return max_val, max_indices, min_val, min_indices

    inversions = 0

    while True:
        # print("Sequence: ", sequence)
        # Calculate the current max value and all the indices where the max is located
        max_val, max_index_list, min_val, min_index_list = calc_indices(sequence)

        # Used to calculate the number of inversion
        seq_length = len(sequence)
        max_index_length = len(max_index_list)
        min_index_used = 0

        # End check to exit while loop when all maxes have been accounted for
        if seq_length <= max_index_length:
            return inversions

        for max_index_val in max_index_list:
            # print("MAX LOOOP")
            # Subtract duplicates from sequence length, the get the range from max index to end of sequence
            inversions += ((seq_length - max_index_length) - max_index_val)

            # print("inversions: ", inversions)
            # Prepare for next iteration
            max_index_length -= 1

        # print(min_index_list)
        for min_index_val in min_index_list:
            # print("\nMIN LOOOP")

            # Subtract duplicates from sequence length, the get the range from min index to end of sequence
            inversions += (min_index_val - min_index_used)

            # print("inversions pre_correction: ", inversions)
            # Prepare for next iteration
            min_index_used += 1

            # Calculate duplicate counts from above max_index iteration
            correction_val = 0
            for max_i in max_index_list:
                if max_i < min_index_val:
                    correction_val += 1

            # Correct inversion count
            inversions -= correction_val

        # Combine index lists to prepare for removal
        all_indices = max_index_list + min_index_list
        all_indices.sort(reverse=True)

        # Del in reverse order so that the previous indices don't get affected
        for index in all_indices:
            # Remove the current max value from the original sequence, preparing for next iteration with smaller list
            del sequence[index]



def inversions_better_elegant(sequence):
    # More elegant algorithm, but runs around same time as earlier algorithm. Not fast enough for large input sequences
    number_dict = {}
    inversions = 0
    for val in sequence:
        print(sorted(number_dict.keys()))
        for key in number_dict:
            if key > val:
                inversions += number_dict[key]
        if val in number_dict:
            number_dict[val] += 1
        else:
            number_dict[val] = 1
    return inversions


def inversions_better(sequence):
    # Correct and more efficient than naive, but not fast enough for large input sequences
    def calc_max_indices(elements):
        # Single pass to find all index values of the max value in a list
        if not elements:
            return []
        max_indices = []
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

    # Initialize inversion count
    inversions = 0

    while True:
        # Calculate the current max value and all the indices where the max is located
        max_val, max_index_list = calc_max_indices(sequence)

        # Used to calculate the number of inversion
        seq_length = len(sequence)
        index_length = len(max_index_list)

        # End check to exit while loop when all maxes have been accounted for
        if seq_length <= index_length:
            return inversions

        for index_val in max_index_list:
            # print(f"Max_val: ", max_val)
            # print(f"Max_index_list: ", max_index_list)
            # print(f"Sequence: ", sequence)
            # print(f"Inversions: ", inversions)

            # Subtract duplicates from sequence length, the get the range from max index to end of sequence
            inversions += ((seq_length - index_length) - index_val)

            # Prepare for next iteration
            index_length -= 1

        # # Remove the current max value from the original sequence, preparing for next iteration with smaller list
        # sequence.remove(max_val)

        for index in reversed(max_index_list):
            del sequence[index]


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        # Debug print statements
        # print("i: {0}, j: {1}".format(i, j))
        # print("a[i]: {0}, a[j]: {1}".format(a[i], a[j]))
        if a[i] > a[j]:
            # print("Inversion!")
            number_of_inversions += 1
    return number_of_inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_naive(elements))
    # print(inversions_better(elements))
    # print(inversions_better_elegant(elements))
    print(inversions_best(elements))
