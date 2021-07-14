
def create_playground_with_dimensions(n) -> list:
    matrix = []
    for y in range(0, (n * 2) + 2):
        row = []
        for x in range(0, (n * 2) + 2):
            if x == 0:
                if (y % 2) == 0 and y != 0:
                    row.append(str(int(y/2)))
                else:
                    row.append(' ')
            elif y == 0:
                if (x % 2) == 0 and x != 0:
                    row.append(str(int(x)))
                else:
                    row.append('!')
            else:
                if (y % 2) == 0 and x % 2 == 0:
                    row.append(' ')
                if (y % 2) == 0 and x % 2 != 0:
                    row.append("|")
                if (y % 2) != 0 and x % 2 == 0:
                    row.append(" --- ")
                if (y % 2) != 0 and x % 2 != 0:
                    row.append("+")
        matrix.append(row)
    return matrix


def print_playground(matrix):
    helper_str = ''
    for index_x, x in enumerate(matrix):
        for index_y, y in enumerate(x):
            if (index_x % 2) == 0 and (index_y % 2) == 0:
                if index_y == 0:
                    helper_str += str(y)
                elif index_x == 0:
                    helper_str += str(y)
                else:
                    helper_str += str('  ' + y + '  ')
            else:
                helper_str += y
        helper_str += '\n'
    print(helper_str)


x = 4
matrix = create_playground_with_dimensions(x)

print_playground(matrix)