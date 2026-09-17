# Catalogo Pixel

Aplicacion web desarrollada con Django para consultar un catalogo de juegos. La portada muestra todos los juegos, el precio promedio y la cantidad de juegos en oferta. Cada juego tiene una pagina de detalle con su informacion, descuento y etiqueta.

## Requisitos

- Python 3.10 o superior
- Git

## Instalacion desde cero

1. Clona el repositorio y entra en la carpeta del proyecto:

```bash
git clone https://github.com/francisco-ribeiro-varas/evaluacion-1-backend.git
cd evaluacion-1-backend
```

2. Crea un entorno virtual.

En Windows PowerShell:

```powershell
py -m venv .venv
```

En macOS o Linux:

```bash
python3 -m venv .venv
```

3. Activa el entorno virtual.

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

En Windows CMD:

```cmd
.venv\Scripts\activate
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

4. Instala las dependencias:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

5. Comprueba la configuracion del proyecto:

```bash
python manage.py check
```

## Ejecutar el proyecto

Con el entorno virtual activado, inicia el servidor:

```bash
python manage.py runserver
```

Abre [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador.

Para detener el servidor, presiona `Ctrl+C`.

## Rutas disponibles

- `/`: portada con todos los juegos.
- `/juego/<id>/`: detalle del juego indicado por su ID.
- `/admin/`: panel de administracion de Django.

Los datos de los juegos se encuentran en `evaluacion/views.py` y se muestran mediante las vistas y plantillas de la aplicacion.

## Archivos principales

- `manage.py`: comandos de administracion de Django.
- `config/settings.py`: configuracion del proyecto y archivos estaticos.
- `config/urls.py`: rutas principales del proyecto.
- `evaluacion/views.py`: datos y logica de las vistas.
- `evaluacion/urls.py`: rutas propias de la aplicacion.
- `templates/base.html`: plantilla base compartida.
- `evaluacion/templates/evaluacion/`: plantillas de inicio y detalle.
- `static/css/estilos.css`: estilos de la interfaz.
- `static/imagenes/logo.svg`: imagen utilizada en la cabecera.

## Pruebas

Para ejecutar las pruebas automatizadas:

```bash
python manage.py test
```

## Solucion de problemas

Si PowerShell impide activar el entorno virtual, ejecuta PowerShell como usuario normal y usa:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Luego vuelve a activar el entorno con:

```powershell
.\.venv\Scripts\Activate.ps1
```
