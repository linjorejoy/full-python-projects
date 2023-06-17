nums =[]
while True:
    largest = -1
    smallest = 1000
    num = input("Enter a num:")

    if num == "done":
        break
    try:
        float(num) > -1000.000
        nums.append(num)
    except:
        print("invalid")


if len(nums) > 0:
    # print("Minimum is :" + min(nums))
    # print("Maximum is :" + max(nums))
    smallest = nums[0]
    largest = nums[0]
    for i in range(len(nums)):
        if int(nums[i]) > int(largest):
            largest = nums[i]
        elif int(nums[i]) < int(smallest):
            smallest = nums[i]
    print("Minimum is " + largest)
    print("Maximum is " + smallest)