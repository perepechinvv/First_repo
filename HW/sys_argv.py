import sys


def parse_args():
    result = ""

    for arg in sys.argv:
        
        if arg == sys.argv[0]:
            continue

        if result != "":
            result += " "

        result += arg    

    print(result)
    return result

print(parse_args())