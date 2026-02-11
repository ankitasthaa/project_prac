arr = list(map(int, input().split()))
print(arr)

k = int(input("Enter the number: "))

new_arr = []

for i in range(len(arr) - k, len(arr), k):
    new_arr.append(arr[i])



print(new_arr)

