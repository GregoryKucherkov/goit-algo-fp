# Greedy algorithm implementation
def greedy_algorithm(items, budget=100):
    result = []

    for food in items:
        items[food]['ratio'] = items[food]['calories'] / items[food]['cost']
    
    items = sorted(items.items(), key=lambda x: x[1]['ratio'], reverse = True)
    
    for item in items:
        if budget >= item[1]['cost']:
            budget -= item[1]['cost']
            result.append(item[0])
        else:
            break

    return result, budget


# Dynamic programming implementation(bottom up)
def dynamic_programming(items, budget=100):
    # Initialize a 2D array to store the maximum calorie content achievable with given budget and subset of items
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    # Populate the 2D array
    for i, (item_name, item_info) in enumerate(items.items(), 1):
        cost = item_info['cost']
        calories = item_info['calories']
        for j in range(1, budget + 1):
            # If the current item can be included
            if cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Backtrack to find the selected items
    selected_items = []
    j = budget
    for i in range(len(items), 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_name, item_info = list(items.items())[i - 1]
            selected_items.append(item_name)
            j -= item_info['cost']
    
    remaining_budget = j
    return  selected_items, remaining_budget


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


if __name__ =='__main__':
    result = greedy_algorithm(items)
    print('Greedy algorithm:')
    print(f'The best price/calories ratio products: \n{result[:-1]} with the remaining {result[-1]}$')

    selected_items, remainig_budget = dynamic_programming(items)
    print('Dynamic programming:')
    print(f'The best price/calories ratio products: {selected_items}')
    print(f'Remainig budget is:{remainig_budget} $')
    print('Conclusion: Dynamic programming has found more optimal list.')

