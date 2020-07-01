type_list = [12, None, -77, 'True', True, 9.5]


def my_type(chk):
    for chk in range(len(type_list)):
        print(type(type_list[chk]))
    return


my_type(type_list)
