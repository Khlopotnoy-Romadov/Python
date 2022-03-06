lst = [1, 5, 6.3, 6, None, 2.0, -4, None]
lst_new = [0 if x == None else x for x in lst]
sr_zn = sum(lst_new)/len(lst_new)
print([sr_zn if x == 0 else x for x in lst_new])