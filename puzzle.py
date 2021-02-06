'''
https://github.com/iamthewalrus67/lab1-puzzle-hw
'''


def validate_board(board: list) -> bool:
    '''
    Check if board is set up correctly.

    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    '''
    return row_check(board) and column_check(board) and color_check(board)


def row_check(board: list) -> bool:
    '''
    Check if all rows contain unique numbers.

    >>> row_check(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    '''
    numbers = '123456789'
    for row in board:
        for number in numbers:
            if row.count(number) > 1:
                return False

    return True


def column_check(board: list) -> bool:
    '''
    Check if all columns countain unique numbers.

    >>> column_check(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    '''
    numbers = '123456789'
    for i in range(len(board[0])):
        for _ in board:
            column = ''
            for row in board:
                column += row[i]
            for number in numbers:
                if column.count(number) > 1:
                    return False

    return True


def color_check(board: list) -> bool:
    '''
    Check if all colors contain unique numbers

    >>> color_check(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
 "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    '''
    numbers = '123456789'

    for i in range(5):
        color_numbers = ''
        for j in range(5):
            color_numbers += board[8-i-j][i]

        for j in range(1, 5):
            color_numbers += board[8-i][i+j]

        for number in numbers:
            if color_numbers.count(number) > 1:
                return False

    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
