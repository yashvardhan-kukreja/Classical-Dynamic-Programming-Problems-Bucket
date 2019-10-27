def lcs(str1, str2, l1, l2):
  if l1==0 or l2==0:
    return 0
  if str1[l1-1]==str2[l2-1]:
    return 1 + lcs(str1, str2, l1-1, l2-1)
  return max(lcs(str1, str2, l1-1, l2), lcs(str1, str2, l1, l2-1))

str1 = input("Please enter the first string: ")
str2 = input("Please enter the second string: ")

l1 = len(str1)
l2 = len(str2)

print ("Length of the longest common subsequence is: {}".format(lcs(str1, str2, l1, l2)))
