from get_matrix_number import *

def get_flat_list(*array):
    lst = []
    for i in range(len(array)):
        if i % 2 == 0:
            lst += array[i]
        else:
            lst += array[i][::-1]

    return lst

if __name__ == '__main__':
    row, col = input_row_col("Input two integer greater than 0 (separated by space): ")
    array = create_array(row, col)
    print("Initial array:")
    for i in array:
        print(i)

    print(f"Flat list: {get_flat_list(*array)}")