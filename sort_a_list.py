def sort_a_list(num_list, a_string):
    #The string should either be "asc", "desc", "none" and it should do any of this according to what is chosen
    if a_string == "asc":
        num1 = sorted(num_list)
        return num1
    elif a_string == "desc":
        num2 = sorted(num_list,reverse=True)
        return num2
    else:
        return num_list
    
result = sort_a_list([10,2,5,6,25,14], "asc")
print(result)