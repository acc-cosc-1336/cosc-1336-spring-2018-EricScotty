'''
Create a function sum_list_values that takes a list parameter and returns the sum of all the numeric values in the list.
Sample Data
joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10
john 14 32 25 16 89
'''

def sum_list_values(data_list):
    index=1 
    sum_list=0
    while index < len(data_list):
        sum_list += data_list[index]
        index+=1

    return sum_list
