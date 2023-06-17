while True:
    num = input("Enter a num:")
    nums =[]
    if num == "done":
        break
    if not num.isnumeric():
        print("invalid")
    else:
        nums.append(num)

if len(nums) > 0:
    print("Minimum is :" + min(nums))
    print("Maximum is :" + max(nums))

