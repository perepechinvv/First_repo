""" Множина set()"""

pin_codes = ['1101', '9034', '1101']

def is_valid_pin_codes(pin_codes):

    if len(pin_codes) > 0:
        string_set = set(pin_codes)
    else:
        return False
    
    if len(pin_codes) != len(string_set):
        return False

    for pin in pin_codes:
    
        if type(pin) != str:
            return False
        elif len(pin) != 4:
            return False            
        
        try:
            val = int(pin)
        except ValueError:
            return False

    return True

result = is_valid_pin_codes(pin_codes)

print(result)