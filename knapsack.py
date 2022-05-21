import sys

def solve_with_lp(items, total_knapsack_volume, n, res):
    
    global best_result
    
    weight = total_knapsack_volume
    opt_value = 0

    if n == 1:
        if items[0][2] <= weight:
            res += items[0][1]
        best_result = max(res, best_result)
        return

    for i in range(n - 1, -1, -1):
        if items[i][2] <= weight:
            opt_value += items[i][1]
            weight -= items[i][2]
        else:
            opt_value += int(weight / items[i][2] * items[i][1])
            break

    if opt_value + res < best_result:
        return

    solve_with_lp(items, total_knapsack_volume, n - 1, res)

    if items[n-1][2] <= total_knapsack_volume:
        solve_with_lp(items, total_knapsack_volume - items[n - 1][2], n - 1, res + items[n - 1][1])


# Process the input
total_knapsack_volume = int(input())
number_of_items = int(input())

sys.setrecursionlimit(number_of_items * 3)

weight = [0] * number_of_items
value = [0] * number_of_items

for i in range(number_of_items):
    weight[i], value[i] = [int(i) for i in list(input().split())]

items = [[value[i] / weight[i], value[i], weight[i]] for i in range(number_of_items)]

# Low bound (greedy_opt) is obtained by greedy algorithm
items = sorted(items, reverse = True)

greedy_opt = 0
weight_left = total_knapsack_volume

for i in range(number_of_items):
    if weight_left >= items[i][2]:
        greedy_opt += items[i][1]
        weight_left -= items[i][2]

best_result = greedy_opt

items.reverse() # reverse sort
solve_with_lp(items, total_knapsack_volume, number_of_items, 0)

print(best_result)
