points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

coordinates = [0, 1, 3, 2, 0, 1]

def calculate_distance(coordinates):

    dist = 0
    
    for i in range(len(coordinates) - 1):
     
        x_y = coordinates[i:i + 2]

        print(x_y)

        if len(x_y) == 2:
            
            x_y.sort()
            
            dist += points[tuple(x_y)]
        
    return dist

print(calculate_distance(coordinates))

print(range(len(coordinates) - 1))