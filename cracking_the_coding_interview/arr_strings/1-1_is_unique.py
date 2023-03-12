from operator import is_
from pickle import FALSE


def is_unique(str_input):
    if len(str_input) > 128:
        return False
    str_dict = {}
    for letter in str_input:
        if letter in str_dict:
            return False
        str_dict[letter] = 1
    return True

def main():
    
    str_input = input("Input string to test if it has all unique letters:\n")
    result = is_unique(str_input)
    if result:
        print("String is unique")
    else:
        print("String is not unique")



if __name__ == "__main__":
    main()