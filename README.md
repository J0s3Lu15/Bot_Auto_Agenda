# Bot Auto Agenda
Este bot programado en Python puede tomar/agendar turnos de forma automática y rápida para los repartidores de de Pedidos Ya.
El programa utiliza la biblioteca Selenium para realizar acciones automatizadas en un navegador web y busca horarios disponibles que cumplan con ciertos criterios definidos por el usuario.

# Autor:
José Luis Flores Tito - Analista de Ciberseguridad

## Requisitos:
Antes de ejecutar el programa, asegúrese de tener instalado lo siguiente:
- Python 3.x
- La biblioteca Selenium para Python. Puede instalarlo usando el siguiente comando:
```bash
pip install selenium
```
- Chromedriver (para controlar Google Chrome) en el mismo directorio que el script principal.
## Instrucciones de Uso:
Descargue el código fuente de Bot_Auto_Agenda y asegúrese de haber instalado los requisitos mencionados anteriormente.
Ejecute el programa utilizando el siguiente comando:

```bash
python Bot_Auto_Agenda.py
```
El programa le pedirá que ingrese varios datos:
- URL del sitio web: Proporcione la URL del sitio web donde desea buscar y agendar horarios.
- Fecha de inicio: Ingrese la fecha de inicio del período de búsqueda.
- Fecha de fin: Ingrese la fecha de fin del período de búsqueda.
- Hora de inicio: Ingrese la hora de inicio del período de búsqueda.
- Hora de fin: Ingrese la hora de fin del período de búsqueda.
- Tiempo mínimo: Ingrese la duración mínima del horario que desea buscar.
El programa luego aplicará los filtros según los datos proporcionados y realizará la búsqueda de horarios disponibles que cumplan con los criterios establecidos.

Los horarios disponibles que cumplan con el tiempo mínimo especificado se guardarán en un archivo llamado "agendados.txt" en el directorio del script.

## Notas importantes:
El programa utiliza el navegador Google Chrome para realizar la automatización. Asegúrese de tener instalado Google Chrome en su sistema.
Asegúrese de tener una conexión a Internet activa mientras se ejecuta el programa, ya que depende de la interacción con el sitio web en línea para realizar la búsqueda y el agendamiento.
## Advertencia
Este programa fue creado con fines educativos y de demostración. No se recomienda utilizarlo para automatizar acciones en sitios web sin el permiso explícito del propietario del sitio. El uso indebido del programa para fines no autorizados puede violar los términos de servicio del sitio web y podría estar sujeto a consecuencias legales.

## Licencia:
Este proyecto cuenta con la licencia Creative Commons "Atribución-NoComercial" (CC BY-NC), osea que puedes usarlo con fines de prueba y demostrativos, pero no puedes venderlo, copiarlo o usarlo con fines comerciales.

## Contactos:
Si te gusta mi trabajo o estás buscando consultoría para tus proyectos, Pentesting, servicios de RED TEAM - BLUE TEAM, implementación de normas de seguridad e ISOs, controles IDS - IPS, gestión de SIEM, implementación de topologías de red seguras, entrenamiento e implementación de modelos de IA, desarrollo de sistemas, Apps Móviles, Diseño Gráfico, Marketing Digital y todo lo relacionado con la tecnología, no dudes en contactarme al +591 75764248 y con gusto trabajare contigo.
