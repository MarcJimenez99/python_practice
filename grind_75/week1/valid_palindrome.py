def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))

# alphaNumeric helper function that we will call in our optimized palindrome
# question that will make use of ASCII values with the ord function. It
# checks if the ASCII value is between either uppercase A and uppercase Z, 
# between lowercase A and lowercase Z, and between the digits 0 and 9. 
# This works because ASCII values are contingius thus telling us that if 
# the ASCII value of the character is not between one these three subranges
# that the character is not an alphaNumeric.

def valid_palindrome_optimized(s):
    leftPtr, rightPtr = 0, len(s) - 1
    while leftPtr < rightPtr:
        while leftPtr < rightPtr and not alphaNum(s[leftPtr]):
            leftPtr += 1
        while rightPtr > leftPtr and not alphaNum(s[rightPtr]):
            rightPtr -= 1
        if s[leftPtr].lower() != s[rightPtr].lower():
            return False
        leftPtr, rightPtr = leftPtr + 1, rightPtr - 1
    return True
        
# Makes use of two pointers and ascii values to help prevent the need
# to build a string and using a built in function to remove non alpha
# numerical character. 
# First we will set our left and right ptr at the opposite end of the string.
# Next we will create our outside while loop which will continue to iterate
# while the leftPtr is less than our rightPtr. Next we want to check if the 
# characters at both our leftPtr and rightPtr are alphanumeric characters. 
# If not we want to continue to iterate and decrement the respective 
# pointers until we hit a valid alphanumeric character. We can do this
# by using two seperate while loops that make use of our custom alphanumeric
# function to check whether the character is valid but also making sure
# that the pointers never pass one another or exit the range of the string.
# We do this by also making sure to only iterate if left < right for the
# leftPtr and right > left for the rightPtr. Once we have valid alphanumerics
# to compare we will then check if the two characters are equal if not 
# immediately return false. Also at the end of the outside while loop we want
# to iterate our leftPtr and decrement our rightPtr. 
# Finally if we exit our loop we know that the string is a valid palindrome.

def valid_palindrome(s):
    newStr = ""
    for char in s:
        if char.isalnum():
            newStr += char.lower()
    if newStr == newStr[::-1]:
        return True
    else:
        return False
# Makes use of the isalnum() built in python function to remove white
# space and non alpha numeric characters from our string. We also
# add all these alpha numeric characters to a string in lower case so 
# we can then reverse the string and if the reverse of our new string equals
# the string in forward order, then you have a palindrome
#
# Not ideal since it uses extra memory by creating a new string
# and reversing a string. Also makes use of a built in function which
# can slow down the program.

def main():
    s = "A man, a plan, a canal: Panama"
    print(s)

    if valid_palindrome(s) and valid_palindrome_optimized(s):
        print("Is a Palindrome")
    else:
        print("Not a Palindrome")


if __name__ == "__main__":
    main()