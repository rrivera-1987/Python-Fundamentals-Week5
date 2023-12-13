def binary_search(the_list, target):
    lower_bound = 0 # Our current search interval is the entire list. We need to find the upper bound.
    upper_bound = len(the_list) - 1 # Use the len function to get the number of items in the list.
        
    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2 # To figure out pivot value, add both values then use floor division to divide by 2.
        # floor division means that any floating point value get removed from the answer so that only an integer remains.
        pivot_value = the_list[pivot] # We compare the pivot and target values against each other.

        if pivot_value == target:
            return pivot
        if pivot_value > target: # If pivot value not == to target, we check if pivot is greater than target. 
            upper_bound = pivot - 1  # If yes it must be somewhere in the half that is less than the pivot.
            # We then change the upper bound value to -1 than the pivot.
        else: 
            lower_bound = pivot + 1
           
    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, 10))
print(binary_search(my_list, 4))
print(binary_search(my_list, 33))