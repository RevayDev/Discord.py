# 🐍 Discord.py

Un bot con múltiples funciones para ayudar a los servidores de Discord, ya sean privados o personales, puede enviar mensajes de bienvenida, despedida y proporcionar entretenimiento. Esta es solo la versión de lanzamiento, pero más adelante tendrá muchas más funciones. ¿Qué otras funciones les gustaría que tenga el bot? 🤖🎉

>[!IMPORTANT]
>Este codigo tiene una licensia ``MIT``
<p align="center">
  
<img src="https://img.shields.io/badge/version-2.0-green"/> 
<img src="https://img.shields.io/badge/author-RevayDev-blue"/> 
<img src="https://img.shields.io/badge/licencia-MIT-red"/> 
<img src="https://img.shields.io/badge/aria-Bot de discord.py-yellow"/>
  
</p>

## 💾 Instalacion
 1 Deberás clonar este repositorio. (Lo siguiente es hacerlo desde tu terminal de Git.)
   ```Bash
   git clone https://github.com/RevayDev/Discord.py.git
   ```
   ¿No tienes Git? https://git-scm.com/

  
 2.1 Descargar ``python``
   > Link: https://www.python.org/downloads/

 2.2 Descarga los `pip` y modulos
   >[!TIP]
   >Forma rapida de instalar los paquetes
   > Forma rapida y segura para ti y tu compu
   ```Bash
   python -m venv env
   ```
  + Ruta en windows
       ```Bash
       source env/Scripts/activate
       ```
   Instalar todos los paquetes
  ```Bash
   pip install -r requirements.txt 
  ```
        
## 🎨 Personalización
>[!WARNING]
>Por favor, sigue los siguientes pasos para configurar el bot y evitar cualquier error. Los pasos estarán detallados minuciosamente para aquellas personas que puedan tener dificultades para entender o >asimilar la información. 😊

1. Coloca tu token
>[!TIP]
>Crea un archivo ``.env`` para tu token como el archivo de ejemplo de ``.env.example``
>```.env
>token=TU_TOKEN
>```
  
2. En el archivo `main.py` encontrarás una parte llamada variables como esta:
  ```Python
  #Variables
  class MyBot(commands.Bot):
  def __init__(self, *args, **kwargs):
    
  super().__init__(*args, **kwargs)
  self.color = 0xTU_COLOR
  self.bienvenidas = ID_CHANNEL
  self.chat = ID_CHANNEL
  self.despedidas = ID_CHANNEL

  bot = MyBot(command_prefix="+", intents=discord.Intents.all(), help_command=None)

  ```
  >[!TIP]
  >Tendras que remplasar las varibles segun tu necesidad `TU_COLOR` deveras usar un color hexadecimal
  > por ejemplo blanco: #ffffff en la variable `TU_COLOR` seria 0xffffff
  >
  > Ahora las variables `ID_CHANNEL` lo remplasarias por el id del canal que usaras para cada evento.
  
  >[!IMPORTANT]
  > Fuera de la carpeta `src` está una llamada `template` dentro hay plantillas para que tú mismo crees eventos, comandos, y más.


  4. Personaliza el codigo :)         
  
