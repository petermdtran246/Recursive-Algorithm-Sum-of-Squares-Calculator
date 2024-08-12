# 2a) Recursive Algorithm to Calculate the Sum of Squares
def calculate_sum_of_squares(n):
    """
    Calculates the sum of squares of integers from 1 to n recursively

    :parameter:
    -------------------------------------------------------------------
        n: A positive integer
    :return:
    -------------------------------------------------------------------
        The sum of squares of integers from 1 to n
    """
    if n == 1:
        return 1
    else:
        return calculate_sum_of_squares(n-1) + n**2

# 2b) Running the Code on Problem Instances
if __name__ == "__main__":
    print(f'Sum of squares from 1 to 12: {calculate_sum_of_squares(12)}')
    print(f'Sum of squares from 1 to 20: {calculate_sum_of_squares(20)}')