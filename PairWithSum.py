array1 = [1, 2, 4, 9]
array2 = [1, 2, 4, 4]
sum = 8


def hasPairWithSum1(inputArr, sumOfPair):
    lenofArr = len(inputArr)
    comp = set()
    for index in range(lenofArr):
        if inputArr[index] in comp:
            return True
        else:
            comp.add(sum - inputArr[index])
    return False


def hasPairWithSum(inputArr, sumOfPair):
    for index in range(len(inputArr)):
        initialrangeindex = index + 1
        for index1 in range(initialrangeindex, len(inputArr)):
            if inputArr[index] + inputArr[index1] == sumOfPair:
                return True
    return False


print(hasPairWithSum(array1, sum))
print(hasPairWithSum1(array2, sum))
