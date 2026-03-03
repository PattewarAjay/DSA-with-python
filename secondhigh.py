nums = [10, 5, 20, 8, 20]

def second_highest(arr):
    if len(arr) < 2:
        return None  

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    if second == float('-inf'):
        return None  

    return second


print(second_highest(nums))  