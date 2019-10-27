def lcs(str1, str2, l1, l2):
    max_len = -1
    ending_index = 0
    cache = [[0 for i in range(l2+1)] for i in range(l1+1)]  ### An l1 x l2 matrice of 0's. It is going to be the bottom up table
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]:
                cache[i][j] = cache[i-1][j-1] + 1
                if cache[i][j] > max_len:
                    max_len = cache[i][j]
                    ending_index = 1
            else:
                cache[i][j] = 0 ## Irrelevant because by default, cache[i][j] is going to be 0 anyways. But added this, just so that it looks descriptive enough to be understood

    return max_len, str1[ending_index-max_len : ending_index]

str1 = input("Please enter the first string: ")
str2 = input("Please enter the second string: ")

l1 = len(str1)
l2 = len(str2)

print("Longest Common Substring is: {}".format(lcs(str1, str2, l1, l2)))