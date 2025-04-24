numbers = [-6, -300, -723, 0, 3]

def findMaxInList(listy):
    MaxValue = numbers[0]
    for number in listy:
        if number > MaxValue:
            MaxValue = number
        elif number < MaxValue:
            MaxValue > number
        else:
            MaxValue = number
    print(MaxValue)   
    return MaxValue
findMaxInList(numbers)