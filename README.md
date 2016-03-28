# ITC SIIBOT
### Bot de Telegram (No Oficial) para acceso al SII

Este es un bot **NO OFICIAL** de Telegram que sirve como intermediario para el SII.
Puedes encontrar al bot en telegram como [**_@itc_siibot._**](http://telegram.me/itc_siibot)
Para instalar en el server, ejecuta **pip install -r requirements.txt** y después ejecuta **python main.py &**.
Este bot se encuentra corriendo en un server de [**Openshift**](https://www.openshift.com/).

**La única información que se guarda en este bot son tus datos de acceso, los cuales eres libre de borrar en cualquier momento.**

### Uso

![demo](https://raw.githubusercontent.com/Dept204/itc_siibot/master/img/bot.PNG)

Una vez iniciada la conversación con el bot, puedes hacer uso de los siguientes comandos:
#### Comandos explícitos
Estos requieren un **/** antes del comando y llevan parámetros
```
/configsii - Sirve para configurar, modificar o borrar tus datos de acceso al SII.
```

##### Ejemplos de uso

```
/configsii set user <usuario> password <contraseña> - Define tus datos de acceso (Debes ingresar los que usas para acceder al SII)
/configsii set user 12345678 password abcdefghijkl

/configsii update user <usuario> password <contraseña> - Actualiza tus datos, en caso de que te hayas equivocado o hayas cambiado
/configsii update user 987654321
/configsii update password opqrstuvwxyz

/configsii delete - Borra tus datos de la base de datos (Sólo de este bot)
```

#### Comandos de mensaje
Estos sólo se escriben como un mensaje normal y también llevan parámetros
```
sii
```

#### Ejemplos de uso
```
sii grades - Te devuelve tus calificaciones
```

### Notas
Para poder hacer tu propia implementación, [debes crear un bot en Telegram](https://telegram.org/blog/bot-revolution)
