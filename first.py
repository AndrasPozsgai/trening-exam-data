#nobel.csv
#év;típus;keresztnév;vezetéknév
# 0    1      2          3
#2017;fizikai;Rainer;Weiss

with open('nobel.csv','r', encoding='utf-8-sig') as file:
    nobel_lista = [sor.strip().split(';') for sor in file ]
del nobel_lista[0]

# 3. Milyen díjat kapott  Arthur B. McDonald?
[print(f"3. feladat: {sor[1]}") for sor in nobel_lista if sor[2]=='Arthur B.' and sor[3] == 'McDonald']

# 4. Ki kapott 2017-ben irodalmi Nobelt?
[print(f'4. feladat: {sor[2]} {sor[3]}') for sor in nobel_lista if sor[0]=='2017' and sor[1] == 'irodalmi']

# 5. Mely szervezetek kaptak Nobelt 1990-től napjainking.
# Ha szervezet kap díjat, akkor a vezeteknev üres.
print('5. feladat:')
[print(f'{sor[0]}: {sor[2]}') for sor in nobel_lista if sor[3]=='' and int(sor[0]) > 1989]

# 6. A Curie család díjai:
print('6. feladat:')
[print(f"{sor[0]}: {sor[2]} {sor[3]}({sor[1]})" ) for sor in nobel_lista if 'Curie' in sor[3] ]

# 7. Melyik díjból, hány darab?
dijak = {sor[1] for sor in nobel_lista}
nobel_dijak = [sor[1] for sor in nobel_lista]
print('7. feladat:')
[print(f'{"":>8}{dij:15} {nobel_dijak.count(dij):6} db') for dij in dijak]

# 8. Orvosi Nobel díjak:  orvosi.txt
with open('orvosi.txt', 'w') as orvosi_txt:
    [print(f"{sor[0]};{sor[2]} {sor[3]}", file = orvosi_txt) for sor in nobel_lista if sor[1] == 'orvosi']
