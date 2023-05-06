filename = 'ingredients.csv'



ingredients = []
with open(filename, encoding='utf-8') as ingredients_file:
    for line in country_file:
        data = line.strip().split(';')
        name, calories, protein, fat, carbs, fiber, type = data

