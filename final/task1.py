# arr = ['Hello', '2', 'world', ':-)']
# arr = ['1234', '1567', '-2', 'computer science'] 
# arr = ['Russia', 'Denmark', 'Kazan']

arr = [i for i in input().split()]
result = []

for element in arr:
    if len(element) <= 3:
        result.append(element)

print(result)