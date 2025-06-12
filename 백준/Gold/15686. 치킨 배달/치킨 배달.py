def find_chicken_stores_index(f_cities, n):
    chicken_stores = []
    for i in range(n):
        for j in range(n):
            if f_cities[i][j] == 2:
                chicken_stores.append([i, j])
    return chicken_stores


def find_house_index(f_cities, n):
    houses = []
    for i in range(n):
        for j in range(n):
            if f_cities[i][j] == 1:
                houses.append([i, j])
    return houses


def get_combinations(arr, m):
    result = []

    def backtrack(start, path):
        if len(path) == m:
            result.append(path[:])
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


N, M = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]
chicken_stores_index_arr = find_chicken_stores_index(cities, N)
houses_index_arr = find_house_index(cities, N)
combinations = get_combinations(chicken_stores_index_arr, M)
min_chicken_distance = 9999999

for combo in combinations:
    temp_distance = 0
    for house_r, house_c in houses_index_arr:
        min_dist = 999999
        for store_r, store_c in combo:
            dist = abs(house_r - store_r) + abs(house_c - store_c)
            min_dist = min(min_dist, dist)
        temp_distance += min_dist
    min_chicken_distance = min(min_chicken_distance, temp_distance)
print(min_chicken_distance)