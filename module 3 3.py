def print_params(a=1, b='строка', c=True):
    print(a,b,c)

values_list= (2, "Привет учитель", False)
values_dict = {'a': 1984, 'b': 1999, 'c': 2001}
values_list_2=(64, 'Anna')

print_params()
print_params(b=25)
print_params(c = [1,2,3])
print_params (*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)