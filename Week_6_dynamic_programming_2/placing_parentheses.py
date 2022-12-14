def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        print("Only  +  -  *  operators are allowed")
        assert False


def find_min_max(i, j):
    if i != j:
        min_value = float("inf")
        max_value = float("-inf")
    else:
        # Keeps the original values during first iteration of range min and max
        min_value = minimum_vals[i][j]
        max_value = maximum_vals[i][j]

    for k in range(i, j):

        # Calculate all possible combinations of min and max values
        a = evaluate(maximum_vals[i][k], maximum_vals[k+1][j], operator_sequence[k])
        b = evaluate(maximum_vals[i][k], minimum_vals[k+1][j], operator_sequence[k])
        c = evaluate(minimum_vals[i][k], maximum_vals[k+1][j], operator_sequence[k])
        d = evaluate(minimum_vals[i][k], minimum_vals[k+1][j], operator_sequence[k])

        # Update min and max
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)

    return min_value, max_value


def maximum_value(num_digits):

    # Populate with original values
    for i in range(num_digits):
        minimum_vals[i][i] = int(digit_sequence[i])
        maximum_vals[i][i] = int(digit_sequence[i])

    # Loops through all possible index pair combos ( [0,0] [1,1] --> [0,3] [1,4] --> [0, num_digits-1])
    for s in range(num_digits):
        for i in range(num_digits - s):
            # Nested loop to get different ranges of i and j
            j = i + s

            # Update min and max values
            minimum_vals[i][j], maximum_vals[i][j] = find_min_max(i, j)

    # Return final, largest max value
    return maximum_vals[0][num_digits-1]


if __name__ == "__main__":
    # Grader gives equation as a single input, no spaces (e.g. 1+2*7-5+2)
    input_data = list(input())

    # Make sure input is in correct format (digit, operator, digit, etc.)
    length = len(input_data)
    n_raw = (length - 1) / 2
    n = int(n_raw)
    assert float(n) == n_raw

    # Separate digits and operators into two lists
    digit_sequence, operator_sequence = input_data[0:2 * n + 1:2], input_data[1:2 * n:2]
    n_digits = n + 1

    # Initialize min/max memoization arrays
    minimum_vals = [[None] * n_digits for x in range(n_digits)]
    maximum_vals = [[None] * n_digits for x in range(n_digits)]

    print(maximum_value(n_digits))
