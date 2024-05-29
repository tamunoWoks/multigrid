def main():
    printSquare(getSquare())

def getSquare():
    try:
        dimension = int(input('Enter dimension of square: '))
        return dimension
    except ValueError:
        print('Enter a valid integer')


#LOGIC 1
def printSquare(dim):
    try:
        for i in range(dim):
            for j in range(dim):
                print('#', end='')
            print()
    except TypeError:
        print('Range() needs a valid integer')


if __name__ == '__main__':
    main()