# PROBLEM
# finding the position of a given number in a list of numbers arranged in decreasing order. also keep the number of times we access the list down

#I/O
#I
#cards: a list of numbers sorted in decreasing order
#query: a number whose position in the array is to be found

#O
#the position of 'query' in the list 'cards'

#test case
#cards = [13, 11, 10, 7, 4, 3, 1, 0]
#query = 7
#output = 3

#EDGE CASES
#query occurs somewhere in the list
#query is the first element in cards
#query is the last element in cards
#cards contains just one element;query
#cards does not contain query 
#cards is empty
#cards contains repeating numbers
#query occurs at more than one position in cards

def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, "mid_number:", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'
    

def locate_card(cards, query):
    
    #LINEAR SEARCH METHOD
    # #create a variable, position, with value 0 
    # position = 0

    # # print('cards', cards)
    # # print('query', query)

    # #create a loop for repetition
    # while position < len(cards):
    #     if cards[position] == query:
    #         #answer found, return and exit
    #         return position
    #     #increment to position
    #     position += 1
    #     #check if we've iterated through the whole array
    # return -1 

    #BINARY SEARCH METHOD
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        print("lo:", lo, "hi:", hi)
        mid = (lo + hi) // 2

        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1


test = {
    'input':{
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output' : 3
}

tests = []
#normal case
tests.append(test)
#query is somewhere in the list
tests.append({
    'input':{
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query' : 1
    },
    'output' : 6
})
#query is first element
tests.append({
    'input':{
        'cards': [4, 2, 1, -1],
        'query' : 4
    },
    'output' : 0
})
#query is last element
tests.append({
    'input':{
        'cards': [3, -1, -9, -127],
        'query' : -127
    },
    'output' : 3
})
#query is last element
tests.append({
    'input':{
        'cards': [3, -1, -9, -127],
        'query' : -127
    },
    'output' : 3
})
#cards contains only query
tests.append({
    'input':{
        'cards': [6],
        'query' : 6
    },
    'output' : 0
})
#cards does not contain query
tests.append({
    'input':{
        'cards': [9, 7, 5, 2, -9],
        'query' : 4
    },
    'output' : -1
})
#cards is empty
tests.append({
    'input':{
        'cards': [],
        'query' : 7
    },
    'output' : -1
})
#repeating numbers in cards
tests.append({
    'input':{
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query' : 3
    },
    'output' : 7
})
#query occurs multiple times..... will return the first instance of query appearing
tests.append({
    'input':{
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query' : 6
    },
    'output' : 2
})
#number lies in the first half of the array 
tests.append({
    'input':{
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query' : 11
    },
    'output' : 1
})
#number lies in the second half of the array 
tests.append({
    'input':{
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query' : 3
    },
    'output' : 5
})


def run_tests(tests, locate_card):
    for i, test in enumerate(tests):
        print(f"Running test {i + 1}")
        result = locate_card(test['input']['cards'], test['input']['query'])
        if result == test['output']:
            print("PASSED")
        else:
            print(f"the test failed. expected {test['output']}, but got {result}")
        print()

run_tests(tests, locate_card)

#THEY BOTH WORK, THE ONE ON TOP JUST WORKS BETTER

# for test in tests:
#     print(locate_card(**test['input']) == test['output'])
