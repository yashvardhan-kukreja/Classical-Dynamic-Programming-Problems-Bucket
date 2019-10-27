def lcs(str1, str2, l1, l2):
  cache = [[0 for i in range(l2+1)] for i in range(l1+1)]
  for i in range(1, l1+1):
    for j in range(1, l2+1):
      if str1[i-1]==str2[j-1]:
        cache[i][j] = 1 + cache[i-1][j-1]
      else:
        cache[i][j] = max(cache[i-1][j], cache[i][j-1])
  return cache[l1][l2], lcs_finder(str1, str2, l1, l2, cache)

## here, the cache is filled after lcs function
def lcs_finder(str1, str2, l1, l2, cache):
  if l1==0 or l2==0:
    return ""
  if str1[l1-1]==str2[l2-1]:
    return lcs_finder(str1, str2, l1-1, l2-1, cache) + str1[l1-1]
  if cache[l1-1][l2] > cache[l1][l2-1]:
    return lcs_finder(str1, str2, l1-1, l2, cache)
  else:
    return lcs_finder(str1, str2, l1, l2-1, cache)


str1 = input("Please enter the first string: ")
str2 = input("Please enter the second string: ")

l1 = len(str1)
l2 = len(str2)

print ("Longest common subsequence is: {}".format(lcs(str1, str2, l1, l2)))

