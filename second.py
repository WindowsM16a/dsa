def binary_search(lo, hi, condition):
    while lo <= hi:
        mid_position = (lo + hi)//2
        result = condition(mid_position)
        if result == 'found':
            return mid_position
        elif result == 'left':
            hi = mid_position-1
        else:
            lo = mid_position+1
    return -1

def first_number(nums, target):
    def condition(mid_position):
        if nums[mid_position] == target:
            if mid_position > 0 and nums[mid_position-1] == target:
                return 'left'
            return 'found'
        elif nums[mid_position] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def last_number(nums, target):
    def condition(mid_position):
        if nums[mid_position] == target:
            if mid_position > 0 and nums[mid_position+1] == target:
                return 'right'
            return 'found'
        elif nums[mid_position] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

test = {
    'input':{
        'nums': [13, 11, 10, 7, 4, 3, 1, 0],
        'target': 7
    },
    'first_output' : 3,
    'last_output' : 0
}

large_test = {
    'input':{
        'nums': list(range(0, 10000000)),
        'target': 999
    },
    'first_output': 1000,
    'first_output': 10000000,
}

tests = []
#normal case 1
tests.append(test)
#large test case 2
tests.append(large_test)
#target is somewhere in the list 3
tests.append({
    'input':{
        'nums': [1, 3, 5, 99, 217, 999],
        'target' : 217
    },
    'first_output' : 4
})
#target is first element 4
tests.append({
    'input':{
        'nums': [-1, 1 ,2 ,4, 5, 8 ,9, 89],
        'target' : 4
    },
    'first_output' : 3
})
#target is last element 5
tests.append({
    'input':{
        'nums': [-127, -9, -3, 1, 3],
        'target' : -3
    },
    'first_output' : 4
})
#nums contains only target 6
tests.append({
    'input':{
        'nums': [6],
        'target' : 6
    },
    'first_output' : 0
})
#nums does not contain target 7
tests.append({
    'input':{
        'nums': [-9,2,5,7,9],
        'target' : 4
    },
    'first_output' : -1
})
#nums is empty 8
tests.append({
    'input':{
        'nums': [],
        'target' : 7
    },
    'first_output' : -1
})
#repeating numbers in nums 9
tests.append({
    'input':{
        'nums': [0,0,0,2,2,2,3,6,6,6,6,6,6,8,8],
        'target' : 3
    },
    'first_output' : 6,
    'last_output' : 6
})
#target occurs multiple times..... will return the first instance of target appearing 10
tests.append({
    'input':{
        'nums': [0,0,0,2,2,2,3,6,6,6,6,6,6,8,8],
        'target' : 6
    },
    'first_output' : 7,
    'last_output' : 7
})
#number lies in the first half of the array 11
tests.append({
    'input':{
        'nums': [0, 1, 3, 4, 7, 11, 13],
        'target' : 3
    },
    'first_output' : 2,
    'last_output' : 2
})
#number lies in the second half of the array 12
tests.append({
    'input':{
        'nums': [0, 1, 3, 4, 7, 11, 13],
        'target' : 11
    },
    'first_output' : 5
})

def run_tests(tests, binary_search):
    for i, test in enumerate(tests):
        print(f"Running test {i + 1}")
        result = binary_search(**test['input'])
        if result == test['first_output'] and test['second_output']:
            print("PASSED")
        else:
            print(f"the test failed. expected {test['first_output']}, but got {result}")
        print()

print("first_number")
run_tests(tests, first_number)
print("last number\n")
run_tests(tests, last_number)
