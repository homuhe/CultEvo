import random
from recipe_extractor import *

def mutate(recipe):

    actions = ["none", "add", "delete", "substitute"]
    random_number = random.randrange(len(actions))

    action = actions[random_number]

    if action == "none":
        pass
    elif action == "delete":
        x = random.randrange(recipe.ing_size)
        recipe.ingredients.pop(x)
    elif action == "add":
        x = random.randrange(len(all_ingredients))
        recipe.ingredients.append(all_ingredients[x])
    else:
        x = random.randrange(recipe.ing_size)
        recipe.ingredients.pop(x)
        y = random.randrange(len(all_ingredients))
        recipe.ingredients.append(all_ingredients[y])

    return recipe.ingredients

for recipe in recipes[:4]:
    print(recipe.ingredients)
    recipe.ingredients = mutate(recipe)
    print(recipe.ingredients)
