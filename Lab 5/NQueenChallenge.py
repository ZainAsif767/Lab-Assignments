# Storing Solution
solutions = []


def is_safe(row, column):
    # check to place safely on this location
    i = 0
    for i in range(len(solutions)//2):
        if solutions[2*i] == row or abs(row-solutions[2*i]) == abs(column-solutions[2*i+1]):
            return False
    return True


def backtrack(coloumn, queen):
    # if all queens are placed
    if queen == 8:
        return True

    # check and try to place queen in each row of each coloumn
    for row in range(8):
        if is_safe(row, coloumn):
            # place queen in this location
            queen += 1
            solutions.append(row)
            solutions.append(coloumn)
            # check for next coloumn
            if backtrack(coloumn+1, queen):
                return True
            else:
                # backtrack and try other location
                solutions.pop()
                solutions.pop()
                queen -= 1
    # if all row have been tried and no solution is found
    return False


# start from left-most coloumn
queen = 0
backtrack(0, queen)
for i in range(0, len(solutions), 2):
    print("col:", solutions[i], "row:", solutions[i+1])
