from src.midterm.exam import new_string
#write import statement for reverse string function

'''
10 points
Write a main function to ....
Loop as long as user types y.
Prompt user for a string (assume user will always give you good data).
Pass the string to the reverse string function and display the reversed string

'''
def main():
    keep_going = 'Y'
    new_string = []
    while keep_going == 'Y':
        list1 = input("Enter a list: ")
        new = new_string(list1)
        keep_going = input("Enter Y to continue: ")
return new_string
