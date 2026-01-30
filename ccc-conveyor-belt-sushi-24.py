#each red sushi = 3
#each green sushi 4
#each blue sushi = 5

#goal: determine cost of meal given number 
#of plates of each color

def calculate_sushi_cost(red_plates, green_plates, blue_plates):
    red_cost = red_plates * 3
    green_cost = green_plates * 4
    blue_cost = blue_plates * 5
    total_cost = red_cost + green_cost + blue_cost
    return total_cost


r = int(input(""))
g = int(input(""))
b = int(input(""))

print(calculate_sushi_cost(r, g, b))