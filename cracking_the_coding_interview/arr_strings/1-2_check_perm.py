from pickletools import string1


def check_perm(str1, str2):
    if len(str1) != len(str2):
        return False
    str_dict = {}
    str1 = str1.lower()
    str2 = str2.lower()
    for char in str1:
        if char in str_dict:
            str_dict[char] += 1
        else:
            str_dict[char] = 1
    for char in str2:
        if char in str_dict:
            str_dict[char] -= 1
        else:
            return False
    for key in str_dict:
        if str_dict[key] != 0:
            return False
    return True


def main():
    str1 = input("String 1:\n")
    str2 = input("String 2:\n")

    result = check_perm(str1, str2)
    if result:
        print(f"{str1} is a permutation of {str2}")
    else:
        print(f"{str1} is not a permutation of {str2}")


if __name__ == "__main__":
    main()