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
    measurments = ""
    cutted_message = ""
    for key in drink:
        if "strIngredient" in key:
            if drink[key]:
                ingredients += " " + drink[key] + ";"
        if "strMeasure" in key:
            if drink[key]:
                measurments += " " + drink[key] + ";"
    message += f"{name} \n" \
                f"{image} \n Nesesary ingredients: {ingredients} \n Ammount of the ingredients: {measurments}\n" \
                f"the recipe: {drink['strInstructions']}"
    cutted_message += f"Nesesary ingredients: {ingredients} \n Ammount of the ingredients: {measurments}\n" \
                f"the recipe: {drink['strInstructions']}"
    answers={"Full Message": message, "Dring Name":name, "Image url": image, "Description": cutted_message}
    return answers

def search_by_ingredient( ingredient):
    """Searchs how many drinks you can do with given ingredient"""
    endpoint_url = base_url + "filter.php?i=" + ingredient
    response = requests.get(endpoint_url)
    try:
        drink_list = response.json()
        drink_list = drink_list["drinks"]
        end_list = []
        for i in range(11):
            end_list.append([drink_list[i]["strDrink"], drink_list[i]["strDrinkThumb"]])
        return {"end_message" :end_list, "end_flag": True}
    except:
        return {"end_message" :"You provided bad ingredient name", "end_flag":False}