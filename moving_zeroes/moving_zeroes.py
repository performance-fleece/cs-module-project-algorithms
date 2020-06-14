'''
Input: a List of integers
Returns: a List of integers
'''
def shift_zero(arr, l, r):
    while l < r:
        arr[l+1], arr[l] = arr[l], arr[l+1]
        l += 1

def moving_zeroes(arr):
    # Your code here
    # starting at right side
    index = end = len(arr) -1

    while index >= 0:
        if arr[index] == 0:
            shift_zero(arr, index, end)
            index -= 1
        else:
            index -= 1
    return arr

    



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")