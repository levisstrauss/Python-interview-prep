def pair_sum(numbers, target_sum):
    previousNums = {}
    for index, number in enumerate(numbers):
        complement = target_sum - number
        if complement in previousNums:
            return index, previousNums[complement]
        previousNums[number] = index
