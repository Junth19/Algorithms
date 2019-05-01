#Author : Junth Basnet
#Implementation of Counting Sort(Linear time sorting algorithm)


def counting_sort(original_array):
    
    k = max(original_array)
    count_array = [0] * (k+1)
    array_b = [None] * len(original_array)

    for j in original_array:
        count_array[j] += 1

    #Finding last element for each element
    #For Zero-Based Indexing
    count_array[0] = count_array[0] - 1
    for i in range(1, k + 1):
        count_array[i] += count_array[i-1]

    for j in reversed(original_array):
        array_b[count_array[j]] = j
        count_array[j] -= 1
        
    original_array = array_b
    return original_array


print(counting_sort([1,5,4,2,9,7,1,5,4,3,2]))
        

    
    
    
