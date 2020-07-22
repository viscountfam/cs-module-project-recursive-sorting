# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    # Your code here
    #create pointers
    index = 0
    # Traverse both array
    while len(arrA) != 0 and len(arrB) != 0:
        # compare the values of the two arrays
        # add the smaller value to the array
        if arrA[0] > arrB[0]:
            merged_arr[index] = arrB[0]
            arrB.pop(0)
        else:
            merged_arr[index] = arrA[0]
            arrA.pop(0)
        index += 1

    # if one array is empty and the other one is not
    # add the remaining values to the list
    if len(arrA) == 0 and len(arrB) != 0:
        while len(arrB) != 0:
            merged_arr[index] = arrB[0]
            arrB.pop(0)
            index += 1
    elif len(arrB) == 0 and len(arrA) != 0:
        while len(arrA) != 0:
            merged_arr[index] = arrA[0]
            arrA.pop(0)
            index += 1
    return merged_arr
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # check to see if the list is a single element
    if len(arr) > 1:
        # create your pointers
        mid = len(arr) // 2
        # split the list in half
        left = arr[:mid]
        right = arr[mid:]

        # call the function until you reach the base case
        return merge(merge_sort(left), merge_sort(right))
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    # create an alternate start point
    s2 = mid + 1

    # if the merge is sorted
    if arr[mid] <= arr[s2]:
        return
    
    # use pointers to mark
    # where each list began
    while start <= mid and s2 <= end:

        #if the first element is placed correctly
        if arr[start] <= arr[s2]:
            start += 1
        else:
            value = arr[s2]
            index = s2
        
        # shift all elements between your two elements right 1 space
        while index != start:
            arr[index] = arr[index - 1]
            index -= 1
        
        arr[start] = value

        #change pointers
        start += 1
        mid += 1
        s2 += 1
    
    return arr

def merge_sort_in_place(arr, l, r):
    # Your code here
    if (l < r):

        mid = l + (r - 1) // 2

        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)

        merge_in_place(arr, l, m, r)

    return arr
