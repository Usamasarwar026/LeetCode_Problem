arrays = [5,1,5]
num=33
def replaceChalk(chalk,k):
    ArraySum = 0 #initialize sum with 0 that store all sum of the array values
    for i in chalk:
        ArraySum += i

    reminder = k % ArraySum  

    n = len(chalk)

    for i in range(n):
        if chalk[i] > reminder:
            return i
        else:
            reminder -= chalk[i]

    return reminder

returnvalue = replaceChalk(arrays,num)
print(returnvalue)