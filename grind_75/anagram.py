def anagram(s, t):

    if len(s) != len(t):
        return False
    dictionary = {}
    for letter in s:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    for letter in t:
        if letter not in dictionary:
            return False
        else:
            dictionary[letter] -= 1
    for key in dictionary:
        if dictionary[key] != 0:
            return False
    return True

def main():

    s = "rac"
    t = "car"

    result = anagram(s, t)

    print(result)

if __name__ == "__main__":
    main()