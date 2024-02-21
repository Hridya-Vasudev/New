#check two lists are rotatable or not
def is_rotatable(list1, list2):
    if len(list1) != len(list2):
        return False

    extended_list1 = list1 + list1
    return set(list2).issubset(extended_list1)
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 1, 2,9]

if is_rotatable(list1, list2):
    print("The lists are rotatable.")
else:
    print("The lists are not rotatable.")


#check one list is rotatable or not
def rotatable(lst):
     if len(lst) < 2:
        return True 
     for i in range(1, len(lst)):
        rotated_list = lst[i:] + lst[:i]
        if rotated_list == lst:
            return True

     return False

# Example usage:
a = [1, 2, 3, 4, 5]

if rotatable(a):
    print("The list is rotatable.")
else:
    print("The list is not rotatable.")

