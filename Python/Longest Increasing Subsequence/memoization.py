def lis(arr, arr_len):
    cache = [1 for i in range(arr_len)]  ## Initially, every element, individually, can be a part of the LIS

    ## For every 0 <= i < arr_len, cache[i] corresponds to the solution of LIS for arr[0 .. i]
    for i in range(1, arr_len):
        for j in range(i):
            if arr[j]<=arr[i]:   ## Current element is greater than iterator element, then, well, it CAN be included in LIS
                already_existing_solution = cache[i] ## Already existing solution till i-th element of the original array
                new_solution = cache[j]+1 ## This is going to be solution if j-th element is added to the LIS (coz well, j-th element is added to the LIS)
                ## Now, let's just see, if we should add j-th element to the solution or not considering if it produces a better solution 
                if new_solution>already_existing_solution: ## But only include it if it produce a higher  number (LIS) than already existing one i.e. cache[j]>cache[i]
                    cache[i] = new_solution

    return max(cache)

n = int(input("Please enter the number of elements in the sequence: "))

arr = []
for i in range (n):
    arr.append(int(input("Please enter the element at index-{}: ".format(i))))

print ("Length of the Longest Increasing Subsequence: {}".format(lis(arr, n)))

