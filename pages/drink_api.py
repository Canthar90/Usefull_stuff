import requests
import json

"""Drink recipe api"""

base_url = "http://www.thecocktaildb.com/api/json/v1/1/"

def search_by_name(drink_name):
    """Searches drink or first of drink list by name"""
    endpoint_url = base_url + "search.php?s=" + drink_name
    response = requests.get(endpoint_url)
    return response_refactor(response=response)

def random_drink():
    """Give a random drink recipe"""
    endpoint_url = base_url + "random.php"
    response = requests.get(endpoint_url)
    
    answers = response_refactor(response=response)
    return answers

def response_refactor(response):
    drink = response.json()
    drink = drink["drinks"][0]
    message = ""
    image = drink["strDrinkThumb"].replace("\\", "")
    name = drink["strDrink"]
    ingredients = ""
    ing_list = []
    ingredients_list = []
    mesurs_list = []
    cutted_message = ""
    for key in drink:
        
        if "strIngredient" in key:
            if drink[key]:
                ing_list.append(drink[key])

        if "strMeasure" in key:
            if drink[key]:
                mesurs_list.append(drink[key])
                
    for ing, measur in zip(ing_list, mesurs_list):
        ingredients += f"{ing}: {measur} \n"
        ingredients_list.append(f"{ing}: {measur}")
    if ingredients:
        message += f"{name} \n" \
                    f"{image} \n Nesesary ingredients: \n{ingredients} " \
                    f"the recipe: {drink['strInstructions']}"
        cutted_message += f"Nesesary ingredients: \n{ingredients}"\
                    f"the recipe: {drink['strInstructions']}"
    else:
        message += f"{name} \n" \
                    f"{image} \n " \
                    f"the recipe: {drink['strInstructions']}"
        cutted_message += f"the recipe: {drink['strInstructions']}"
        
    
    answers={"Full Message": message, "Dring Name":name, "Image url": image, "Description": cutted_message,
             "Recipe": drink['strInstructions'], "Ingredients": ingredients, "Ingredients list": ingredients_list}
    return answers

def search_by_ingredient( ingredient):
    """Searchs how many drinks you can do with given ingredient"""
    endpoint_url = base_url + "filter.php?i=" + ingredient
    response = requests.get(endpoint_url)
    try:
        drink_list = response.json()
        drink_list = drink_list["drinks"]
        end_list = []
        for i, v in enumerate(drink_list):
            end_list.append([drink_list[i]["strDrink"], drink_list[i]["strDrinkThumb"]])
        return {"end_message" :end_list, "end_flag": True}
    except:
        return {"end_message" :"You provided bad ingredient name", "end_flag":False}