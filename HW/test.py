def formatted_numbers():

    header = '|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary')

    list_numbers = list()
    list_numbers.append(header)
    
    for i in range(16):
        list_numbers.append('|{:<10}|{:^10}|{:>10}|'.format('{:d}'.format(i), 
                                                              '{:x}'.format(i), 
                                                              '{:b}'.format(i)))
    
    return list_numbers    

for el in formatted_numbers():
    print(el)    