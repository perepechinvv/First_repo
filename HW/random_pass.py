from random import randint


def get_random_password():

    string_pass = ''
    n = 0    
    
    while n < 8:    
              
        string_pass += chr(randint(40, 126))
        
        n += 1
        
    return string_pass

print(get_random_password())