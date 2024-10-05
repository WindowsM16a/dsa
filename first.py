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

from jovian.pythondsa import evaluate_test_case


def locate_card(cards, query):
    #create a variable, position, with value 0 
    position = 0

    #create a loop for repetition
    while True:
        if cards[position] == query:
            #answer found, return and exit
            return position
        #increment to position
        position += 1
        #check if we've iterated through the whole array
        if cards[position] == len(cards):
            #number wasn't found, return -1
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
# #query is somewhere in the list
# tests.append({
#     'input':{
#         'cards': [13, 11, 10, 7, 4, 3, 1, 0],
#         'query' : 1
#     },
#     'output' : 6
# })
# #query is first element
# tests.append({
#     'input':{
#         'cards': [4, 2, 1, -1],
#         'query' : 4
#     },
#     'output' : 0
# })
# #query is last element
# tests.append({
#     'input':{
#         'cards': [3, -1, -9, -127],
#         'query' : -127
#     },
#     'output' : 3
# })
# #query is last element
# tests.append({
#     'input':{
#         'cards': [3, -1, -9, -127],
#         'query' : -127
#     },
#     'output' : 3
# })
# #cards contains only query
# tests.append({
#     'input':{
#         'cards': [6],
#         'query' : 6
#     },
#     'output' : 0
# })
# #cards does not contain query
# tests.append({
#     'input':{
#         'cards': [9, 7, 5, 2, -9],
#         'query' : 4
#     },
#     'output' : -1
# })
# #cards is empty
# tests.append({
#     'input':{
#         'cards': [],
#         'query' : 7
#     },
#     'output' : -1
# })
# #repeating numbers in cards
# tests.append({
#     'input':{
#         'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
#         'query' : 3
#     },
#     'output' : 7
# })
# #query occurs multiple times..... will return the first instance of query appearing
# tests.append({
#     'input':{
#         'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
#         'query' : 6
#     },
#     'output' : 2
# })

evaluate_test_case(locate_card, test)

# result = locate_card(**test['input'])
# print(result)

# isSolved = result == test['output']
# print(isSolved)
