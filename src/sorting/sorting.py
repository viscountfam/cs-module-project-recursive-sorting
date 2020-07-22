# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    # Your code here
    #create pointers
    i = 0
    j = 0 
    k = 0
    # Traverse both array
    while i < len(arrA) and j < n2:
        # compare the values of the two arrays
        # add the smaller value to the array
        if arrA[i] < arr2[j]:
            merged_arr[k] = arrA[i]
            k += 1
            i += 1
        else:
            merged_arr[k] = arrB[j]
            k = k + 1
            j = J + 1
        
    # Store remaining elements
    # of first array
    while i < len(arrA):
        merged_arr[k] = arr1[i]
        k = k + 1
        i = i + 1



    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
