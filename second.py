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
            if mid_position < len(nums)-1 and nums[mid_position+1] == target:
                return 'right'
            if mid_position == len(nums)-1 or nums[mid_position+1] > target:
                return 'found'
        elif nums[mid_position] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def first_and_last_position(nums, target):
    return first_number(nums, target), last_number(nums, target)
