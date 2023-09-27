temp_float_tuple = []
float_tuple = (temp_float_tuple)
string_list = []
int_dict={}

random_list = [105,3.1,"Hello", 737,"Python", 2.7, "World",412, 5.5, "AI"]
for i in random_list:
    if type(i) is str:
        string_list.append(i)
    elif type (i) is float:
        temp_float_tuple.append(i)
    elif type (i) is int:
        satuan = i % 10
        puluhan = (i//10) %10
        ratusan = i//100

        int_dict[i] = {'ratusan': ratusan,'puluhan':puluhan, 'satuan':satuan} 

print(string_list)
print(float_tuple)
print (int_dict)