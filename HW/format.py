students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):

    list_grades = []
    n = 1
    
    for name, grade in students.items():

        list_grades.append("{:>4}|{:<10}|{:^5}|{:^5}".format(n, name, grade, grades[grade]))      
    
        n += 1
        
    return list_grades   


for str in formatted_grades(students):
    print(str)    