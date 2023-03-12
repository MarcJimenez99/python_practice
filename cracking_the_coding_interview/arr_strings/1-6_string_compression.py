def str_compression(str1):
    str_dict = {}
    sorted_str = sorted(str1)
    for letter in sorted_str:
        if letter in str_dict:
            str_dict[letter] += 1
        else:
            str_dict[letter] = 1

    new_string = ""
    for key in str_dict:
        new_string += key
        new_string += str(str_dict[key])

    if len(new_string) > len(str1):
        return str1
    else:
        return new_string

def str_compression_2(str1):
    sorted_str = sorted(str1)
    count = 0
    new_str = ""
    for i in range(0, len(str1), 1):
        count += 1
        if (i+1 == len(str1)) or sorted_str[i] != sorted_str[i+1]:
            new_str += sorted_str[i]
            new_str += str(count)
            count = 0
    if len(new_str) > len(str1):
        return str1
    return new_str


def main():
    str1 = input("Input:\n")

    result = str_compression_2(str1)

    print(result)


if __name__ == "__main__":
    main()