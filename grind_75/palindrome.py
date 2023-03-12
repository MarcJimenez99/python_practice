def palindrome(s):
    s = s.lower().replace(" ", "")
    s = ''.join(filter(str.isalnum, s))
    print(s)
    dictionary = {}
    for letter in s:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    print (dictionary)
    print (dictionary.values())
    oddCount = 0
    for value in dictionary.values():    
        if value % 2 != 0:
            oddCount += 1
            if oddCount > 1:
                return False

    return True

def valid_palindrome(s):
    s = s.lower().replace(" ", "")
    s = ''.join(filter(str.isalnum, s))
    
    print(s)
    print(s[::-1])

    if s == s[::-1]:
        return True
    else:
        return False

def main():

    string = "abb"
    # result = palindrome(string)
    result = valid_palindrome(string)
    print(result)

if __name__ == "__main__":
    main()