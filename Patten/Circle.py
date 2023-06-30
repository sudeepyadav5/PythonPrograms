import math


def print_circle(radius):
    # Calculate the center of the circle
    center_x = radius
    center_y = radius

    # Iterate over each row and column of a square grid that encloses the circle
    for y in range(radius * 2 + 1):
        for x in range(radius * 2 + 1):
            # Calculate the distance between the current point and the circle's center
            distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)

            # If the distance is less than or equal to the radius, the point is within the circle
            if distance <= radius:
                print("*", end="")
            else:
                print(" ", end="")
        print()


# Example usage
print_circle(5)
