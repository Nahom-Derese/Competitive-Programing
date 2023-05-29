def shortest_path_of_king(x, y, x1, y1):
    path = ""
    # Compute horizontal and vertical distances
    dx = x1 - x
    dy = y1 - y

    # Move horizontally
    if dx > 0:
        path += "R" * dx
    elif dx < 0:
        path += "L" * abs(dx)

    # Move vertically
    if dy > 0:
        path += "U" * dy
    elif dy < 0:
        path += "D" * abs(dy)

    return path


# Input
x, y, x1, y1 = map(int, input().split())

# Call the function and print the result
print(shortest_path_of_king(x, y, x1, y1))
