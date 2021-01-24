def recursive_fibonacci(index):
    """
    Function to get the fibonacci number at given index using only recursion

    :param index: index number
    :type index: int

    :rtype: int
    """
    if index <= 0:
        return "Invalid Input, Index must be greater or equal to 1"

    if index == 1 or index == 2:
        return 1

    return recursive_fibonacci(index-1) + recursive_fibonacci(index-2)


def dp_fibonacci(index, memo={}):
    """
    Function to get the fibonacci number at given index using recursion and dynamic programming

    :param index: index number
    :type index: int

    :rtype: int
    """
    if index <= 0:
        return "Invalid Input, Index must be greater or equal to 1"

    if index == 1 or index == 2:
        return 1
    
    if index in memo.keys():
        return memo[index]

    memo[index] = dp_fibonacci(index-1, memo) + dp_fibonacci(index-2, memo)
    return memo[index]
      
if __name__ == "__main__":
    # Example with recursion
    recursive_fib_5 = recursive_fibonacci(5)
    print(f"Fibonacci number at index 5 is: {recursive_fib_5}")
    recursive_fib_6 = recursive_fibonacci(6)
    print(f"Fibonacci number at index 6 is: {recursive_fib_6}")
    recursive_fib_8 = recursive_fibonacci(8)
    print(f"Fibonacci number at index 8 is: {recursive_fib_8}")

    # Example with dynamic programming
    dp_fib_5 = dp_fibonacci(5)
    print(f"Fibonacci number at index 5 is: {dp_fib_5}")
    dp_fib_6 = dp_fibonacci(6)
    print(f"Fibonacci number at index 6 is: {dp_fib_6}")
    dp_fib_8 = dp_fibonacci(8)
    print(f"Fibonacci number at index 8 is: {dp_fib_8}")
    dp_fib_50 = dp_fibonacci(50)
    print(f"Fibonacci number at index 50 is: {dp_fib_50}")
    dp_fib_80 = dp_fibonacci(80)
    print(f"Fibonacci number at index 80 is: {dp_fib_80}")
