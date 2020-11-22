def read_data():
    grades_file = open('hw11Direc/instructors.txt', "r")
    my_list = []
    with grades_file:
        line: List[str] = grades_file.readlines()
        print(line)
        # for line in grades_file:
        #     my_list.append(line)

        #     print(my_list)


read_data()
