def read_fuente(file):
    data = []
    diccionario_covid = {
        "FECHA_CORTE": [],
        "UUID": [],
        "FECHA_FALLECIMIENTO": [],
        "EDAD_DECLARADA": [],
        "SEXO": [],
        "FECHA_NAC": [],
        "DEPARTAMENTO": [],
        "PROVINCIA": [],
        "DISTRITO": [],
    }
    with open(file, encoding="ISO-8859-1") as f:
        for line in f:  # fic.readlines():
            data.append(line)

    for line in data[1:]:
        string_campos = line.split(";")
        # print(string_campos)
        diccionario_covid["FECHA_CORTE"].append(string_campos[0])
        diccionario_covid["UUID"].append(string_campos[1])
        diccionario_covid["FECHA_FALLECIMIENTO"].append(string_campos[2])
        diccionario_covid["EDAD_DECLARADA"].append(string_campos[3])
        diccionario_covid["SEXO"].append(string_campos[4])
        diccionario_covid["FECHA_NAC"].append(string_campos[5])
        diccionario_covid["DEPARTAMENTO"].append(string_campos[6])
        diccionario_covid["PROVINCIA"].append(string_campos[7])
        diccionario_covid["DISTRITO"].append(string_campos[8])

    return diccionario_covid


# 2.1.Un método o función que calcule la cantidad total de muertos
# en el departamento de Arequipa entre las fechas
# 20200430 – 20201024 (5 PUNTOS)


def total_frios_arequipa(listado):
    total = 0
    for i in listado["DEPARTAMENTO"]:
        if i == "AREQUIPA":
            total += 1

    print(total)

archivo = "fallecidos_covid.txt"
listado = read_fuente(archivo)

total_arequipa = total_frios_arequipa(listado)
