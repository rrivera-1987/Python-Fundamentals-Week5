def linear_search_dictionary (the_dictionary, target):
    for x in the_dictionary:
        if the_dictionary[x] == target:
            print (x)
            return x
    else:
        print("Target not in dictionary")
        return -1
            
my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)