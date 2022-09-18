habilidades = [
    {
        "Nombre": "Vision-X",
        "Poder": 64
    },
    {
        "Nombre": "Vuelo",
        "Poder": 32
    },
    {
        "Nombre": "Inteligencia",
        "Poder": 256
    },
    {
        "Nombre": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Nombre": "Super Velocidad",
        "Poder": 128
    },
    {
        "Nombre": "Magia",
        "Poder": 512
    }
]


habilidades_UTN = []
for habilidad in habilidades:
    habilidades_selec = {}
    habilidades_selec["Nombre"] = habilidad["Nombre"]
    habilidades_selec["Poder"] = int(habilidad["Poder"])
    habilidades_UTN.append(habilidades_selec)

for poder in habilidades_UTN:
    print(poder) 


