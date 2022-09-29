heroes_para_reclutar = [
    "Batman", "BatWoman", "BatGirl",
    "Wonder Woman", "Aquaman", "Shazam",
    "Superman", "Super Girl", "Power Girl"
]

heroes_info = {
    "Super Girl": {
        "ID": 1,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
        "Identidad": "Kara Zor-El"
    },
    "Shazam": {
        "ID": 25,
        "Origen": "Tierra",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
        "Identidad": "Billy Batson"
    },
    "Power Girl": {
        "ID": 14,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
        "Identidad": "Karen Starr"
   },
    "Wonder Woman": {
        "ID": 29,
        "Origen": "Amazonia",
        "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
        "Identidad": "Diana Prince"
    }
}

lista_heroe = []
for heroe_recluta in heroes_para_reclutar:
    for heroe in heroes_info:
        if (heroe_recluta == heroe):
            dic_heroe = {}
            dic_heroe["Codename"] = heroe_recluta
            dic_heroe["ID"] = heroes_info[heroe]["ID"]
            dic_heroe["Origen"] = heroes_info[heroe]["Origen"]
            dic_heroe["Habilidades"] = heroes_info[heroe]["Habilidades"]
            dic_heroe["Habilidades"] = set(dic_heroe["Habilidades"])
            dic_heroe["Identidad"] = heroes_info[heroe]["Identidad"]
            lista_heroe.append(dic_heroe)
            
for hero in lista_heroe: 
    print("\nID = {0} | Codename: {1}".format(hero["ID"],hero["Codename"]))
    print("Identidad: {0} | Origen: {1}".format(hero["Identidad"],hero["Origen"]))
    print("Habilidades: {0}".format(hero["Habilidades"]))
    print("--------------------------------------------------------------------------------------------------------")
          

