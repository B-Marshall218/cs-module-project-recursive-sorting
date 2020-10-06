# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # The elements are consisting of two arrays combined
    elements = len(arrA) + len(arrB)
    # The merge array value would be an empty array multipled
    # by the elements value
    merged_arr = [0] * elements

    # Your code here
    # Range returns a list of integers. We want the intigers
    # within the elements

    # ?? What determines which array the element/number would be in?
    for i in range(elements):
        # If the number isn't arrayA then we are passing in
        # a number into the merged array and removing a number
        # from the B array located in the first position
        if not arrA:
            merged_arr[i] = arrB.pop(0)
        # If its not the B array add number to array A and
        # remove the first value in that array
        elif not arrB:
            merged_arr[i] = arrA.pop(0)
        # otherwise if array A is smaller than B we are
        # removing first value in array A
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
            # Else its larger than B and we remove B
        else:
            merged_arr[i] = arrB.pop(0)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    # Set up base
    if len(arr) <= 1:
        return arr

    #  middle is my piviot
    middle = len(arr) // 2
    # left is to the left of the middle/pivot
    left = arr[:middle]  # why do I need the : after middle?
    right = arr[middle:]

    # Your calling the merge function and actually just sorting the
    # data correctly here.
    return merge(merge_sort(left), merge_sort(right))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
    # Your code here

    # def merge_sort_in_place(arr, l, r):
    # Your code here
