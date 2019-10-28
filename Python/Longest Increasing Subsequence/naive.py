import sys

def lis(arr, arr_len, current_index, prev_max):
    if arr_len == current_index:
        return 0
    
    case_1 = lis(arr, arr_len, current_index+1, prev_max)  ### When the current element is not included in the LIS

    ## If current element is greater than previous max, then, case 2 will be the case it will be included in the LIS
    if arr[current_index]>prev_max:
        new_max = arr[current_index]
        case_2 = 1 + lis(arr, arr_len, current_index, new_max)
    else:
        ## No point in computing anything for case 2 if the current element itself if still smaller than the previous max (hence, case 1 will dominate i.e when the current element is not included in the LIS) 
        case_2 = 0
    
    ## Determining which of the above two cases produces the longest increasing subsequence
    return max(case_1, case_2)

n_elements = int(input("Please enter the length of the array/sequence: "))
arr = []
for i in range(n_elements):
    arr.append(int(input("Please enter the element of index-{}: ".format(i))))

print ("Length of the Longest Increasing Supersequence is: {}".format(lis(arr, n_elements, 0, -sys.maxsize)))



