nums = []
while True:
    try:
        user = int(input())
    except ValueError:
        print('Please enter a number')
        continue
    if int(user) < 0:
        break
    else:
        nums.append(int(user))
print(sum(nums) / len(nums) if not nums == [] else 'Terminated')
