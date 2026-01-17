# Create your own code here
def main():
    print("\nCreating Matrix 1")
    matrix1 = get_matrix()
    print("\nCreating Matrix 2")
    matrix2 = get_matrix()

    print("\nMatrix 1:")
    for row in matrix1:
        print(row)

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    matrix3 = add_matrix(matrix1, matrix2)

    if matrix3:
        print("\nMatrix 3:")
        for row in matrix3:
            print(row)

def add_matrix(matrix1, matrix2):
    # Create empty matrix
    matrix3 = []

    # If the size of both matrices are the same
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        
        # Iterate through the length of matrix1 since they are both the same size
        for i in range(len(matrix1)):
            # Initialize a new row array
            new_row = []
            # Iterate through the length of the row of matrix 1 since they are both the same size
            for j in range(len(matrix1[i])):
                # Create and append the new element to the new row
                element = matrix1[i][j] + matrix2[i][j]
                new_row.append(element)

            # Once it has been iterated through, append the new row to the new matrix
            matrix3.append(new_row)
    else:
        print("Can not add.")

    return matrix3


def get_matrix():
    # Create empty matrix
    matrix = []

    # Ask user to input the number of rows and columns that will fill the matrix
    number_of_rows = int(input("How many rows are in the matrix? "))
    number_of_columns = int(input("How many columns are in the matrix? "))

    # Loop until the number of rows has been reached
    while len(matrix) < number_of_rows:

        # Create empty list that will be filled with elements
        new_row = []
        # Loop until the number of columns has been reached
        while len(new_row) < number_of_columns:
            # Prompt user to enter element
            element = int(input("Which element would you like to add to position" + str(len(matrix) + 1) + str(len(new_row) + 1) + "? "))
            # Append the element to the empty row list
            new_row.append(element)

        #Append the new row to the matrix
        matrix.append(new_row)

    return matrix


if __name__ == '__main__':
    main()