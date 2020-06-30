dishes = ["pizza", "salad", "soup"]
ingredients = [["Margarita,", "Four Seasons,", "Neapoletana,", "Vegetarian,", "Spicy"],
               ["Caesar salad,", "Green salad,", "Tuna salad,", "Fruit salad"],
               ["Chicken soup,", "Ramen,", "Tomato soup,", "Mushroom cream soup"]]
order = input()

if order in dishes:
    for i in range(3):
        if order == dishes[i]:
            for j in ingredients[i]:
                print(j + " ", end='')
else:
    print("Sorry, we don't have it in the menu")
