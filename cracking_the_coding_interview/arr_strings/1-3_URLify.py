def URLify(str_input, true_size):
    newString = ""
    for char in str_input:
        if char == ' ':
            newString += '%20'
        else:
            newString += char
    return newString

def main():

    str_input = input("String Input: ")
    true_size = int(input("True Size: "))

    output = URLify(str_input, true_size)

    print(f'{output}')

if __name__ == "__main__":
    main()