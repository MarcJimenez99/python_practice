def zero_matrix(matrix):
    for element in

def main():
    matrix = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    for element in matrix:
        print(f'{element}\n')

    new_matrix = zero_matrix(matrix)

    for element in new_matrix:
        print(f'{element}\n')

if __name__ == "__main__":
    main()