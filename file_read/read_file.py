lord_of_the_rings = open('lor.txt', 'r',encoding='utf-8')

#r = tryb do odczytu, argument w jakim trybie chcemy oddtworzyc plik

for line in lord_of_the_rings:
    #print(line, end='')  #nie ma znaku nowej linii
    #print(len(line))
    #print(line.strip(),end='') # tekst w postaci jednej linii, pozbycie sie znaku nowej linii
    #print(line.strip()) #linia po linii
    print(line.rstrip()) #od prawej strony

lord_of_the_rings.close()



#text = "'Trzy Pierścienie dla królów elfów pod otwartym niebem,\n"


#print(len(text)) # liczy dlugosc nawet ze spacjami
