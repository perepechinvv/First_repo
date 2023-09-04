employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']] 

def write_employees_to_file(employee_list):

    list_map = list()

    for l in employee_list:
        list_map += l    
   
    # text = "\n".join(list_map)

    # print(text)
    
    fh = open("test.txt", 'w')
    fh.write("\n".join(list_map))
    fh.close()

write_employees_to_file(employee_list)