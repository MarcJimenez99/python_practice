def one_edit(str1, str2):
    diff = 0
    for i in range(0, len(str1), 1):
        if str1[i] != str2[i]:
            diff += 1
            if diff > 1:
                return False
    return True

def one_insert_delete(str1, str2):
    print("Delete\n")
    index1 = 0
    index2 = 0
    diff = 0
    while(index1 < len(str1) and index2 < len(str2)):
        print(str1[index1])
        print(str2[index2])
        if str1[index1] != str2[index2]:
            print("Difference\n")
            diff += 1
            if (diff == 2):
                return False
            index1 += 1
        else:
            print("Same\n")
            index1 += 1
            index2 += 1
    return True

def main():
    
    str1 = input("First String: ")
    str2 = input("Second String: ")

    diff = abs(len(str1) - len(str2))
    result = False
    if diff == 0:
        result = one_edit(str1, str2)
    elif diff == 1:
        if len(str1) > len(str2):
            result = one_insert_delete(str1, str2)
        else:
            result = one_insert_delete(str2, str1)
    
    print(result)


    

if __name__ == "__main__":
    main()