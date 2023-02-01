def PalindromePerm(str_input):
    str_dict = {}
    for char in str_input:
        if char != ' ':
            if char in str_dict:
                str_dict[char] += 1
            else:
                str_dict[char] = 1
    
    num_odd = 0
    for key in str_dict:
        if str_dict[key] % 2 == 1:
            num_odd += 1
            if num_odd > 1:
                return False
    return True

def main():

    str_input = input("String Input: ")

    output = PalindromePerm(str_input)

    print(f'{output}')

if __name__ == "__main__":
    main()