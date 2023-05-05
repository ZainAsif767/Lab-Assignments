import math

distances = {
    '1': {'2': 10, '3': 15, '4': 20},
    '2': {'1': 10, '3': 35, '4': 25},
    '3': {'1': 15, '2': 35, '4': 30},
    '4': {'1': 20, '2': 25, '3': 30}
}

solution = []


def backtrack(perm, sol, level):
    for i in range(len(perm)):
        temp = []
        sol.append(perm[i])
        for j in range(len(perm)):
            temp.append(perm[j])
        temp.remove(perm[i])
        if len(temp) == 0:
            t_sol = []
            for m in range(len(sol)):
                t_sol.append(sol[m])
            t_sol.append(t_sol[0])
            solution.append(t_sol)
            sol.pop()
            sol.pop()
            return
        else:
            backtrack(temp, sol, level+1)
    if (len(sol) != 0):
        sol.pop()


def minCost(solution, distances):
    min_cost = math.inf

    for i in range(len(solution)):
        cost = 0
        for j in range(len(solution[i]) - 1):
            cost += distances[str(solution[i][j])][str(solution[i][j+1])]
        if cost < min_cost:
            min_cost = cost
    return min_cost


backtrack([1, 2, 3, 4], [], 0)
print(minCost(solution, distances))
