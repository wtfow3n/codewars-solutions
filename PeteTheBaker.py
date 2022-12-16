# ow3n
# 
# December 15, 2022
# 

from math import floor

def cakes(recipe, available):
    
    list = []

    for ingredient, amount in recipe.items():
        if ingredient in available.keys():
            list.append(floor(available.get(ingredient) / recipe.get(ingredient)))
        elif ingredient not in available.keys():
            return 0

    return min(list)
