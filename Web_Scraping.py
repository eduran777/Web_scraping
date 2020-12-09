from bs4 import BeautifulSoup
from urllib.request import urlopen
import os.path

indices = ['0','1','2','3','4','5','6','7','8','9']  
def obtener_fechas():
    url = "https://www.municipio.com.co/dias-festivos-2020-2021.html"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    texto = soup.get_text()

    festivos =[linea for linea in texto.split('\n') if linea !='']

    contador_2020 = 0

    festivos_text = ['Festivos del 2020']

    for elemento in range(0, len(festivos)):
        if festivos[elemento][0] in indices and contador_2020 <= 18:
            fecha = festivos[elemento] +' '+ festivos[elemento+1] + ' ' + festivos[elemento+2]
            # print(fecha)
            festivos_text.append(fecha)
            elemento = festivos[elemento + 3]
            contador_2020 += 1

        elif festivos[elemento][0] in indices and contador_2020 == 19:
            fecha = festivos[elemento] +' '+ festivos[elemento+1] + ' ' + festivos[elemento+2]
            # print('\n')
            festivos_text.append('Festivos del 2021')
            # print('\n')
            # print(fecha)

            festivos_text.append(fecha)
            elemento = festivos[elemento + 3]
            contador_2020 += 1

        elif festivos[elemento][0] in indices and contador_2020 > 19:
            fecha = festivos[elemento] +' '+ festivos[elemento+1] + ' ' + festivos[elemento+2]
            # print(fecha)
            festivos_text.append(fecha)
            elemento = festivos[elemento + 3]
            contador_2020 += 1
    
    return (festivos_text)


def verificar_guardado():
    file_exists = os.path.isfile('festivos.txt')
    if file_exists:
        pass
    else:
        file = open("festivos.txt", "w+")
        file.close()


def guardar(festivos):
    verificar_guardado()
    archivo_festivos = open('festivos.txt', 'a', newline='')
    for elemento in festivos:
        if elemento == 'Festivos del 2020':
            archivo_festivos.write(elemento)
            archivo_festivos.write('\n')
            archivo_festivos.write('\n')

        elif elemento == 'Festivos del 2021':
            archivo_festivos.write('\n')
            archivo_festivos.write(elemento)
            archivo_festivos.write('\n')

        else:
            archivo_festivos.write(elemento)
            archivo_festivos.write('\n')
            
      
    archivo_festivos.close

def main():
    guardar(obtener_fechas())

main()
