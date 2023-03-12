import math

def rotate_image(image):

    layer = math.floor(len(image[0])/2)
    for j in range(0, layer, 1):
        matrix_len = (len(image[0])-1)-(j*2)
        top_edge = []
        for k in range(0, matrix_len+1, 1):
            top_edge.append(image[j][k+j])
        for i in range(0, matrix_len, 1):
            image[0+j][matrix_len-i+j] = image[i+j][0+j] 
            image[i+j][0+j] = image[matrix_len+j][i+j]
            image[matrix_len+j][i+j] = image[matrix_len-i+j][matrix_len+j]
            image[matrix_len-i+j][matrix_len+j] = top_edge[matrix_len-i]
    return image

def main():
    # image = [[1,2,3],
    #         [4,5,6],
    #         [7,8,9]]
    # image = [[1,2,3,4],
    #         [5,6,7,8],
    #         [9,10,11,12],
    #         [13,14,15,16]]
    # image = [[1,2,3,4,5],
    #         [6,7,8,9,10],
    #         [11,12,13,14,15],
    #         [16,17,18,19,20],
    #         [21,22,23,24,25]]
    image = [[1,2,3,4,5,6],
            [7,8,9,10,11,12],
            [13,14,15,16,17,18],
            [19,20,21,22,23,24],
            [25,26,27,28,29,30],
            [31,32,33,34,35,36]]
    print(f'Original image\n')
    for element in image:
        print(f'{element}\n')

    rotated_image = rotate_image(image)

    print(f'Rotated Image\n')
    for element in rotated_image:
        print(f'{element}\n')

if __name__ == "__main__":
    main()