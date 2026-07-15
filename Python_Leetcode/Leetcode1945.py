
s = "leetcode"
k = 2
def getlucky(s: str, k: int) -> int:
    position = [str(ord(char) - ord('a') + 1) for char in s]          # find the letter postion using ASCI code
    stringJoin = "".join(position)             #join the string into single string
    convert_into_number = int(stringJoin)        #convert join string into integer  

    def get_single_number(number: int) -> int:
        return sum(int(digit) for digit in str(number))    #find the sum of all number first we convert number into string and then we convert in to integer an find sum
    
    for _ in range(k):                 # iterate loop kth time underscore is used when we variable is not required then we used _
        single_number = get_single_number(convert_into_number)        # call the function and then store in a variable
        convert_into_number = single_number             #the variable is again store into argument by incrementing the given number

    return convert_into_number   #return final number this number in a single integer


number = getlucky(s,k)         # call the function
print(number)                #print the single number
