immutable_var = 1, 2, 'a', 'b', True
print (immutable_var)
#immutable_var[0]=0 Операция не выполнима, значения элементов картежа изменить нельзя
mutable_list=[1,2,'a','b',True]
mutable_list[0]=0
print(mutable_list)
mutable_list.append(immutable_var)
print(mutable_list)