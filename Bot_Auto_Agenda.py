from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

def get_formatted_date(date_str):
    day, month, year = map(str, date_str.split())
    
    if len(day) == 1:
        day = "0" + day

    months_dict = {
        "01": "ene.", "02": "feb.", "03": "mar.", "04": "abr.",
        "05": "may.", "06": "jun.", "07": "jul.", "08": "ago.",
        "09": "sept.", "10": "oct.", "11": "nov.", "12": "dic."
    }
    month = months_dict.get(month, month)

    return f"{day} {month} {year}"

def get_formatted_time(hour, minute):
    hour, minute = map(str, [hour, minute])
    
    if len(hour) == 1:
        hour = "0" + hour

    if len(minute) == 1:
        minute = "0" + minute

    return f"{hour}:{minute}"

def get_zonas():
    print('''
    Escriba el número de la zona y
    presione enter para agregar,
    o introduzca 0 para terminar de
    agregar:

    El Bajío = 1
    Pirai = 2 
    Grigota = 3
    Guapay = 4
    Hipermaxi Pampa = 5
    La Alemana = 6
    Norte = 7
    Santos Dumont = 8
    Sevilla = 9
    Villa 1ro de Mayo = 10
    Zona Sur = 11
    Equipetrol = 12
    Fidalga Pampa = 13
    ''')

    zonas = []
    while True:
        numero_zona = str(input())

        if numero_zona.lower() == "0":
            break
        else:
            zonas_dict = {
                "1": "sp_47", "2": "sp_48", "3": "sp_11", "4": "sp_14",
                "5": "sp_18", "6": "sp_3", "7": "sp_9", "8": "sp_13",
                "9": "sp_15", "10": "sp_14", "11": "sp_1", "12": "sp_2",
                "13": "sp_19"
            }
            zona = zonas_dict.get(numero_zona)
            if zona:
                zonas.append(zona)

    return zonas

def buscar_turnos(usuario, password, fecha_inicio, fecha_fin, hora_inicio, hora_fin, tiempo_min, zonas_decision):
    fecha_inicio = get_formatted_date(fecha_inicio)
    fecha_fin = get_formatted_date(fecha_fin)
    hora_inicio = get_formatted_time(*hora_inicio.split())
    hora_fin = get_formatted_time(*hora_fin.split())

    tiempo_min = int(tiempo_min)
    tiempo_min1 = tiempo_min + 1
    tiempo_min2 = tiempo_min + 2
    tiempo_min3 = tiempo_min + 3
    tiempo_min4 = tiempo_min + 4
    tiempo_min5 = tiempo_min + 5
    tiempo_min6 = tiempo_min + 6
    tiempo_min7 = tiempo_min + 7

    tiempo_min = f"({tiempo_min}h"
    tiempo_min1 = f"({tiempo_min1}h"
    tiempo_min2 = f"({tiempo_min2}h"
    tiempo_min3 = f"({tiempo_min3}h"
    tiempo_min4 = f"({tiempo_min4}h"
    tiempo_min5 = f"({tiempo_min5}h"
    tiempo_min6 = f"({tiempo_min6}h"
    tiempo_min7 = f"({tiempo_min7}h"

    zonas = []
    if zonas_decision == 2:
        zonas = get_zonas()

    driver_path = 'chromedriver.exe'
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    #Tiempo maximo de respuesta
    wait = WebDriverWait(driver, 20)

    #Define tamaño de ventana
    width = 150
    height = 640
    driver.set_window_size(width, height)

    # Definir la posición de la ventana
    x = 200
    y = 50
    driver.set_window_position(x, y)

    #Abrimos la pagina
    pagina = "https://bo.usehurrier.com/app/rooster/web/my-shifts"
    driver.get(pagina)

    #Encontramos y mandamos datos de usuario y password
    username_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/form/div/div[1]/input')))
    password_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/form/div/div[2]/input')))
    username_field.send_keys(usuario)
    password_field.send_keys(password)

    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/form/button')))
    submit_button.click()

    btn_menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/header/div/div[1]/button')))
    btn_menu.click()

    btn_horas_conexion_disponibles = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/a[2]')))
    btn_horas_conexion_disponibles.click()

    #Empezar a buscar para aplicar filtros
    while True:
        btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button[1]')))
        div_turnos = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/div/div[2]')))
        txt_no_hay_turnos = "No hay horarios de conexion disponibles para ese día"
        
        if txt_no_hay_turnos in div_turnos.text:
            print("No hay turnos disponibles")
        else:
            print("Se encontraron turnos, aplicando filtros")
            btn_filtros = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[2]/div/button[2]')))
            btn_filtros.click()
            input_desde = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/span/div/div[2]/input')))
            input_desde.send_keys(hora_inicio)
            input_hasta = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/4/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/span/div/div[2]/input')))
            input_hasta.send_keys(hora_fin)

            if zonas_decision == 2 and zonas:
                for zona in zonas:
                    check_zona = driver.find_element(By.XPATH, f'//*[@id="{zona}"]')
                    check_zona.click()

            btn_aplicar_filtros = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[2]/div[2]/div/div[3]/div[1]/button')))
            btn_aplicar_filtros.click()
            break

        if fecha_inicio == fecha_fin and btn_dia_number == 7:
            btn_dia_sig = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button[6]')))
            btn_dia_sig.click()
            btn_dia_actual = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button[7]')))
            btn_dia_actual.click()
        elif fecha_inicio == fecha_fin:
            btn_dia_sig = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/4/div/div[1]/div[2]/button[2]')))
            btn_dia_sig.click()
            btn_dia_actual = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/4/div/div[1]/div[2]/button[3]')))
            btn_dia_actual.click()

        if fecha_inicio != fecha_fin: 
            btn_dia_number = btn_dia_number + 1

        if fecha_inicio != fecha_fin and pag_dia.text == fecha_fin:
            btn_dia_number = btn_dia_numberi

        pag_dia = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']/div[2]')))
        btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/4/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
        btn_dia.click()

    #Buscar con filtros aplicados
    print("Empezando a buscar con filtros aplicados...")
    wait_busqueda = WebDriverWait(driver, 6)
    archivo = open("agendados.txt", "a")
    c_posis = 0

    while True:
        if fecha_inicio != fecha_fin: 
            btn_dia_number = btn_dia_number + 1

        if fecha_inicio != fecha_fin and pag_dia.text == fecha_fin:
            btn_dia_number = btn_dia_numberi

        pag_dia = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']/div[2]')))
        btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/4/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
        btn_dia.click()

        if fecha_inicio == fecha_fin and btn_dia_number == 7:
            btn_dia_sig = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/4/div/div[1]/div[2]/button[6]')))
            btn_dia_sig.click()
            btn_dia_actual = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/4/div/div[1]/div[2]/button[7]')))
            btn_dia_actual.click()
        elif fecha_inicio == fecha_fin:
            btn_dia_sig = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/4/div/div[1]/div[2]/button[2]')))
            btn_dia_sig.click()
            btn_dia_actual = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/4/div/div[1]/div[2]/button[3]')))
            btn_dia_actual.click()

        try:
            btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button[1]')))
            elementos = driver.find_elements(By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[3]/div/div[2]/article')
            c_elementos = len(elementos)

            print("|-----------------NOTA:-----------------|")
            print("|Cantidad de horarios disponibles: ", c_elementos," |")
            print("|Los ",c_elementos," horarios pueden tener cantidad|")
            print("|de horas inferiores a ", tiempo_minimo,"            |")
            print("|---------------------------------------|")

            for i in range(1, c_elementos+1):
                txt_turno = driver.find_element(By.XPATH, f'//*[@id="app"]/div[4]/div/div[2]/div[3]/div/div/article[{i}]/div/div/p')

                if tiempo_minimo in txt_turno.text or tiempo_minimo1 in txt_turno.text or tiempo_minimo2 in txt_turno.text or tiempo_minimo3 in txt_turno.text or tiempo_minimo4 in txt_turno.text or tiempo_minimo5 in txt_turno.text or tiempo_minimo6 in txt_turno.text or tiempo_minimo7 in txt_turno.text:
                    c_posis = c_posis + 1
                    btn_agendar = driver.find_element(By.XPATH, f'//*[@id="app"]/div[4]/div/div[2]/div[3]/div/div/article[{i}]/div/button')
                    btn_agendar.click()
                    time.sleep(0.5)
                    print("|Se encontro un horario:|")
                    print("|-----------------------|")

                    try:
                        div_agendado = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[4]/div/aside/div/div[1]')
                        print(div_agendado.text)
                        linea = f"Horario Agendado:\n{div_agendado.text}\n--------------------------\n\n"
                        archivo.write(linea)
                        btn_confirmar = driver.find_element(By.XPATH, '//*[@id="app"]/div/4/div/div[2]/div[4]/div/aside/div/button[1]')
                        btn_confirmar.click()
                        print("Horario "+str(i)+" Agendado!!!")
                    except:
                        div_tomado = driver.find_element(By.XPATH, '//*[@id="app"]/div/4/div/div[2]/div[5]/div/aside/div/div[1]')
                        print(div_tomado.text)
                        linea = f"Horario Tomado:\n{div_tomado.text}\n--------------------------\n\n"
                        archivo.write(linea)
                        btn_tomar = driver.find_element(By.XPATH, '//*[@id="app"]/div/4/div/div[2]/div[5]/div/aside/div/button[1]')
                        btn_tomar.click()
                        print("Horario "+str(i)+" Tomado!!!")

                    print("|-----------------------|\n")
            print("Horarios tomados o agendados: ", c_posis)

        except:
            btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/4/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
            print("No hay turnos que coincidan con su filtro")

    archivo.close()
    driver.quit()
    print("Proceso finalizado.")

if __name__ == "__main__":
    main()
