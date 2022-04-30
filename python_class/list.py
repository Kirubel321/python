list_of_name = ['alex','dave','abel','hanna']
list_of_nick_name = ['al','d','ab','h']

# for single_element in list_of_name:
#     print(single_element)

# for single_element in range(len(list_of_name)):
#     print(single_element)

# for single_element in range(len(list_of_name)):
#     print(list_of_name[single_element])

# for single_element in range(len(list_of_name)):
#     print(f'{list_of_name[single_element]} nickname is {list_of_nick_name[single_element]}')

for single_name,single_nick in zip(list_of_name,list_of_nick_name):
    print(f'{list_of_name[single_name]} nickname is {list_of_nick_name[single_nick]}')