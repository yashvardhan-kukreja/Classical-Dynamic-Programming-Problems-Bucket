###
#
#       TODO: Generate shortest common supersequence (string) as well through this naive approach
#
###

output = ""

def scs(str1, str2, l1, l2, update_output=False):
    global output
    if l1 == 0:
        #output = str2[:l2] + output if update_output else output
        return l2
    if l2 == 0:
        #output = str1[:l1] + output if update_output else output
        return l1
    if str1[l1-1] == str2[l2-1]:
        #output = str1[l1-1] + output if update_output else output
        return 1+scs(str1, str2, l1-1, l2-1, True) 
    else:
        case_1 = 1+scs(str1, str2, l1-1, l2)
        case_2 = 1+scs(str1, str2, l1, l2-1)
        if case_1 < case_2:
            #output = str1[l1-1] + output if update_output else output
            return case_1
        else:
            #output = str2[l2-1] + output if update_output else output
            return case_2

str1 = input("Please enter the first string: ")
str2 = input("Please enter the second string: ")

l1 = len(str1)
l2 = len(str2)

print ("Length of the Shortest Common Supersequence: {}, {}".format(scs(str1, str2, l1, l2), output))