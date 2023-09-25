gallows = [
    [" ", "+", "-", "+", " "],
    [" ", "|", " ", "|", " "],
    [" ", "|", " ", " ", " "],
    [" ", "|", " ", " ", " "],
    ["/", " ", "\\", " ", " "]
]

def draw_gallows(param=0)
    
    gallows_for_print = []

    for row in gallows:
        result = "".join(row)
        gallows_for_print.append(result)

    print("\n".join(gallows_for_print))

    while row in gallows:
        user_input = input(">>>")
        if user_input == "1":
            gallows[2][3] = "0"

        gallows_for_print = []

        for row in gallows:
            result = "".join(row)
            gallows_for_print.append(result)
    
    print("\n".join(gallows_for_print))