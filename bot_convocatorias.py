# README.md - Bot de Convocatorias sin Cuota (Versión Render.com)

## Descripción
Este bot busca convocatorias de exposiciones y residencias artísticas que no tengan cuota de recuperación en sitios institucionales de México y envía notificaciones por Telegram y correo electrónico.

## Requisitos
- Python 3.10+
- Cuenta de Telegram con un bot creado
- Cuenta de correo para enviar notificaciones (Gmail recomendado con contraseña de aplicación)

## Archivos
- `bot_convocatorias.py` → Script principal
- `requirements.txt` → Dependencias Python
- `Procfile` → Para ejecución en Render (Cron Job)
- `.env` → Variables de entorno con credenciales

## Configuración de `.env`
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```bash
# Telegram
TELEGRAM_BOT_TOKEN=tu_token_de_bot_aqui
TELEGRAM_CHAT_ID=tu_chat_id_aqui

# Correo
EMAIL_SENDER=tu_correo@gmail.com
EMAIL_PASSWORD=tu_contraseña_de_aplicacion
EMAIL_RECEIVER=correo_destinatario@gmail.com

# Opcional (para futuro uso de Instagram)
IG_GRAPH_ACCESS_TOKEN=
IG_USER_ID=
```

## Instalación de dependencias
```bash
pip install -r requirements.txt
```

## Archivos para Render
- `requirements.txt` debe contener:
```
requests
beautifulsoup4
pandas
python-dotenv
```
- `Procfile` debe contener:
```
worker: python bot_convocatorias.py
```

## Despliegue en Render
1. Crear un repositorio Git con todos los archivos (`bot_convocatorias.py`, `requirements.txt`, `Procfile`, `.env` ejemplo).
2. Subir el repositorio a GitHub.
3. En Render.com, crear un nuevo **Cron Job**.
   - Tipo: Python
   - Comando: `python bot_convocatorias.py`
   - Horario: `0 15 * * 1` (Lunes 9:00 AM hora de México)
4. Configurar las variables de entorno en Render: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`, `EMAIL_SENDER`, `EMAIL_PASSWORD`, `EMAIL_RECEIVER`.
5. Guardar y activar el cron job. El bot se ejecutará automáticamente cada semana.

## Uso local (opcional)
Puedes ejecutar el bot manualmente con:
```bash
python bot_convocatorias.py
```
Esto realiza la búsqueda y envía notificaciones inmediatamente.

## Notas
- Asegúrate de que tu correo pueda enviar correos mediante SMTP (Gmail requiere contraseña de aplicación).
- Telegram: obtén tu `chat_id` con [@userinfobot](https://t.me/userinfobot).
- Revisar y agregar nuevas instituciones en `INSTITUTION_SITES` según sea necesario.
# Aquí iría todo el código del bot (versión para cron job en Render)
# Usar el código que ya está en el textdoc 'bot_convocatorias.py'
