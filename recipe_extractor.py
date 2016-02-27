#Extracts recipes from text files of source:
#    http://mc6help.tripod.com/RecipeLibrary/RecipeLibrary.htm
import glob, re, os, pprint, sys

#CHANGE TO YOUR RECIPE DIRECTORY
recipes_dir = os.getcwd()+"/rec_txt/"


recipes_raw = []
recipes = []            #list of all recipe objects
recipesMeat = []
recipesFish = []
recipesVeggi = []

all_ingredients = []    #list of all ingredients of all recipes

class recipe:
    def __init__(self, category, title, prep_time, ingredients):

        if category == "beef" or category == "pork": 
            category = "meat"
        
        self.category = category            #string
        self.title = title                  #string
        self.prep_time = prep_time          #string of format [0-9]:[0-5][0-9]
        self.ingredients = ingredients      #list of ingredients
        self.ing_size = len(ingredients)    #integer
        self.score = 0                      #score of all points assigned in inter-Agent evaluation steps
        # -----------------------------------------------
        self.counter = 0                    #for testing only


def clean_ingredients(ingr_list):
    clean_list = []
    for ingredient in ingr_list:
        ingredient = re.sub("(\(.*\))|( -- .*)|(or .* and .*)|(\*|\;|--)", "", ingredient)
        ingredient = ingredient.split("  ") #splits ingredient from ingredient amount
        ingredient = ingredient[-1].lower().strip()
        clean_list.append(ingredient)
    return clean_list

def recipeDiff(r):
    if r.category=="meat":
        recipesMeat.append(r)
    elif r.category=="fish":
        recipesFish.append(r)
    elif r.category=="veggi":
        recipesVeggi.append(r)
    else:
        sys.exit("Error in recipe_extractor.py, lines 35, wrong recipe type handed over from source txt file.")

#FOR EACH TEXT FILE:
file_list = glob.glob(recipes_dir + "*.txt")


# Windows
if os.name == 'nt':
    for directory in file_list:

        #GET CATEGORY
        category = directory.split("\\") #split up dir path /resources/Recipes/x.txt
        category = category[-1]         #take last level in directory
        category = category.strip(".txt").lower()

        #read file and slice up into recipes
        raw_text = open(directory, mode="r");
        all_recipes = raw_text.read()
        raw_text.close()

        separator = "* Exported from MasterCook *"
        recipes_raw = all_recipes.split(separator)
        #OUTPUT: recipes_raw, list

        for r in recipes_raw[1:]:

            #GET TITLE
            r1 = r.split("\n")
            title = r1[:3][-1].strip()

            #GET PREP TIME
            prep_time = r1[5]
            #time_pattern = re.compile("\d:\d\d\r")
            time_pattern = re.compile("\d:\d\d")
            r1 = time_pattern.findall(prep_time)
            prep_time = r1[0].strip()

            if prep_time == "0:00":
                pass
            else:

                separator2 = "\n--------  ------------  --------------------------------\n"
                ingredients_list = r.split(separator2)

                ingredients_list = ingredients_list[-1].split("\n\n")
                ingredients_list = ingredients_list[0].split("\n")
                ingredients_list = clean_ingredients(ingredients_list)

                r = recipe(category, title, prep_time, ingredients_list)
                recipeDiff(r)
                recipes.append(r)

                #ADDING INGREDIENTS TO GLOBAL LIST
                for ingredient in ingredients_list:
                    if ingredient not in all_ingredients:
                        all_ingredients.append(ingredient)
else:
    # others OS
    for directory in file_list:

        #GET CATEGORY
        category = directory.split("/") #split up dir path /resources/Recipes/x.txt
        category = category[-1]         #take last level in directory
        category = category.strip(".txt").lower()

        #read file and slice up into recipes
        raw_text = open(directory, mode="r");
        all_recipes = raw_text.read()
        raw_text.close()

        separator = "* Exported from MasterCook *"
        recipes_raw = all_recipes.split(separator)
        #OUTPUT: recipes_raw, list

        for r in recipes_raw[1:]:

            #GET TITLE
            r1 = r.split("\n")
            title = r1[:3][-1].strip()

            #GET PREP TIME
            prep_time = r1[5]
            time_pattern = re.compile("\d:\d\d\r")
            r1 = time_pattern.findall(prep_time)
            prep_time = r1[0].strip()

            if prep_time == "0:00": pass
            else:
                separator2 = "\r\n--------  ------------  --------------------------------\r\n"
                ingredients_list = r.split(separator2)

                ingredients_list = ingredients_list[-1].split("\r\n\r\n")
                ingredients_list = ingredients_list[0].split("\r\n")
                ingredients_list = clean_ingredients(ingredients_list)

                r = recipe(category, title, prep_time, ingredients_list)
                recipes.append(r)

                #ADDING INGREDIENTS TO GLOBAL LIST
                for ingredient in ingredients_list:
                    if ingredient not in all_ingredients:
                        all_ingredients.append(ingredient)

def retAllIngreds():
    index = 0
    i = 0
    pprint.pprint(all_ingredients)


if __name__ == "__main__":
           
    for recipe in recipes:
        print("\n"+recipe.category)
        print(recipe.title)
        print(recipe.prep_time)
        print(recipe.ingredients)
        print(recipe.ing_size)
