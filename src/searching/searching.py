# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # If target was not found
    if start > end:
        return -1
# Establishing your start point for divide and concquer
    middle = start + end // 2
# If the target happens to be the middle number youre done
    if arr[middle] == target:
        return middle
# if target is less than the middle, call function and start
# iterating over each number -1, repeaat untl middle = target
    if target < arr[middle]:
        return binary_search(arr, target, start, middle - 1)
    # The other option is if its larget than middle, keep adding
    # number and compare until middle = target.
    else:
        return binary_search(arr, target, middle + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here
