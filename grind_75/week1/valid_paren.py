# Using a stack
# With this solution we can make use of a stack. This is due to the fact we must maintain
# proper order of the brackets coming, ensuring that a open bracket must always be closed
# by its closing bracket in the correct order of what left brackets exist in the string.
# By using stacks and its LIFO (Last in First Out) principal. 
#
# We also make use of a dictionary as a method to check to see if the correct open bracket
# is met by the current closed bracket we iterated upon. So to begin, we will iterate through
# each character within the string using a for loop. If the character matches a key in our 
# dictionary, we know that its an open bracket. If it is an open bracket, we push it  onto
# our stack. If it is not in our dictionary, we know its a closed bracket and then we 
# check if our stack is empty OR if the top of the stack is not the associated open bracket
# through our dictionary. If either is true, we know we can return false as the closing
# bracket is not met with the appropriate open bracket meaning its not in the correct
# order. However if it is, then we pop the stack and continue to iterate. 
# Once we're done iterating if the stack is empty we know that we successfully closed
# every open bracket and can return True, but if the stack has any existing elements 
# left we know an open bracket was not closed in our string and we can return false.


def valid_paren_dictionary(s: str) -> bool:
    stack = []
    dictionary = {'(':')','[':']','{':'}'}
    for char in s:
        if char in dictionary:
            stack.append(char)
        else:
            if len(stack) == 0 or dictionary[stack.pop()] != char:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
    

def valid_paren(s: str) -> bool:
    stack = []
    if len(s) % 2 != 0:
        return False
    if not s:
        return True
    for char in s:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                if char == ")":
                    top = stack.pop()
                    if top != "(":
                        return False
                if char == "]":
                    top = stack.pop()
                    if top != "[":
                        return False
                if char == "}":
                    top = stack.pop()
                    if top != "{":
                        return False
    if not stack:
        return True
    else:
        return False

def main():
    s = "([{}])"
    
    result = valid_paren_dictionary(s)
    # result = valid_paren(s)

    print(result)    

if __name__ == "__main__":
    main()