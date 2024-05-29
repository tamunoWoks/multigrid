def main():
    printSquare(getSquare())

def getSquare():
    try:
        dimension = int(input('Enter dimension of square: '))
        return dimension
    except ValueError:
        print('Enter a valid integer')


#LOGIC 1
# def printSquare(dim):
#     try:
#         for i in range(dim):
#             for j in range(dim):
#                 print('#', end='')
#             print()
#     except TypeError:
#         print('Range() needs a valid integer')

#LOGIC 2
# def printSquare(dim):
#     try:
#         for i in range(dim):
#             print('#'* dim)
#     except TypeError:
#         print('Range() needs a valid integer')


#LOGIC 3
def printSquare(dim):
    try:
        for i in range(dim):
            printRow(dim)
    except TypeError:
        print('Range() needs a valid integer')
def printRow(dim):
    print('#' * dim)



if __name__ == '__main__':
    main()