test_numbers = 'numbers.txt'

with open(test_numbers, 'w', encoding='UTF-8') as numbers_file:
    for i in range(10):
        #numbers_file.write(i) #numbers przyjmuje tylko jedna opcje
        print(i,"Funkcja print jest super") # print moze nadpisywac