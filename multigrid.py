def main():
    ...

def getSquare():
    try:
        dimension = int(input('Enter dimension of square: '))
        return dimension
    except ValueError:
        print('Enter a valid integer')

if __name__ == '__main__':
    main()