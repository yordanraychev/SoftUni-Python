number = int(input())
left_sum = 0
right_sum = 0

for num1 in range(1, number + 1):
    current_number = int(input())
    left_sum += current_number
for num2 in range(1, number + 1):
    current_number = int(input())
    right_sum += current_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
