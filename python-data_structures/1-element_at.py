def element_at(my_list, idx):
    for idx in my_list:
        if idx < 0:
            return (None)
        elif len(my_list) <= idx:
            return (None)
        else:
            return (my_list[idx]) 
