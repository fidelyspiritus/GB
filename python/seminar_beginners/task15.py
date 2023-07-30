watermelon_number = int(input())
watermelon_weight = [int(input()) for i in range(watermelon_number)]
min, max = watermelon_weight[0], watermelon_weight[0]
for weight in watermelon_weight:
    if weight < min:
        min = weight
    elif weight > max:
        max = weight
print(f"Вес арбуза для себя {max}, вес арбуза для тещи {min}")