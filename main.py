# Zadanie 1

lista = {"Piekarnia": ["chleb","bulki","paczek"], "Warzywniak" : ["marchew","seler","rukola"]}
count = 0

print("Lista zakupow:")
for sklep, rzeczy in lista.items():
    print(f"Idę do {sklep}, kupię tu natępujące rzeczy:{rzeczy}")
    count += len(rzeczy)
print(f"W sumie kupuję {count} rzeczy")    


#%% Zadanie 2

podzielne_przez_5 = []

for num in range(1,101):
    if(num%5)==0:
        podzielne_przez_5.append(num)

print(podzielne_przez_5)  

print(list(map(lambda x: x**3, podzielne_przez_5)))   

#%% 

podzielne_przez_3 = []

for num in range(1,101):
    if(num%3)==0:
        podzielne_przez_3.append(num)

print(podzielne_przez_3)  

print(list(map(lambda x: x/2, podzielne_przez_5)))   
