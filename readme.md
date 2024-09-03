# Proyecto Urban Routes

Urban Routes es una app en la que puedes realizar tu pedido de transporte, este puede ser un taxi, un automovil para rentar, un automovil compartido, bicicleta o un scooter.

## Descripción

El proyecto de estas pruebas automatizadas, se basan en la solicitud de un taxi de tipo comfort, que es uno de los tipos de servicios que la aplicación tiene disponible.

- La prueba realizada en este proyecto, está basada en el ciclo de solicitud de un taxi, de tipo comfort 

## Características

- El proyecto se ha realizado en Python - Selenium
- Se ha tenido en cuenta las pruebas de ciclo de solicitud de un taxi de tipo comfort
- Se tuvo en cuenta la creación de funciones para reducir el código y así reducir el tiempo de ejecución de las pruebas
- Se organizó el proyecto por medio de una estructura para su facil mantenimiento
- Se necesita de una URL del Servidor disponible y activa

## Pasos

- Clona el proyecto
- Instala Python, en caso de no tenerlo
- Instala selenium, en caso de no tenerlo
- Reinicia el servidor (utilizar la URL actual disponible)
- Ejecuta prueba a prueba o todas las pruebas directamente desde RUN en Pycharm desde el archivo "main"

## Tecnologías utilizadas

En el proyecto, se realizaron las pruebas usando Selenium y el lenguaje de programación Python.
Se necesitó importar las librerías:
- webdriver
- time
- By
- expected_conditions
- WebDriverWait
- WebDriverException
- json

El código se organizó según el patrón de diseño POM (Page Object Model) y Helper classes, por lo que se inluyeron los siguientes archivos.
- Main: como el archivo donde se encuentran los test listos para ejecutarse
- TestUrbanRoutes: como el archivo donde se crearon las funciones tests para cada paso en el ciclo o proceso de solicitud de un taxi de tipo comfort
- UrbanRoutesPage: es el archivo donde se encuentra cada uno de los localizadores de la página y de cada modal que se muestra a lo largo del proceso de solicitud del taxi de tipo comfort, tambien en donde se desarrolla cada función del proceso para cada acción.
  los procesos son los siguientes:
  - Seleccionar la ruta del punto de partida al punto de llegada
  - Seleccionar el taxi de tipo comfort
  - Llenar el campo teléfono, con el proceso de verificación del número de teléfono
  - Llenar el campo de método de pago, para el uso de tarjeta, en el que se agrega una tarjeta como medio de pago.
  - Dejar un comentario al conductor
  - Se pide una manta y pañuelos
  - Se pide 2 helados
- Actions: es el archivo en donde se crearon todas las funciones básicas para reducir el código al máximo.
  las acciones son:
  - Escribir en un campo de texto
  - Obtener el texto de un campo de texto
  - Obtener el texto de un elemento
  - Hacer click en un elemento
  - Esperar a que un elemento se localice
  - Conocer si un elemento se encuentre visible
  - Conocer si un elemento esté seleccionado
  - Hacer scroll hasta el elemento para que se encuentre visible en pantalla
  - Verificar si un elemento ha sido seleccionado
  - Verificar si un elemento está visible
  - Verificar que el texto actual coincide con el esperado
  - Verificar que un texto es parte o está contenido en otro texto
  - Obtener el código de verificación para el número de teléfono

## Creditos

- Jenny Nataly Pabón Yañez, QA Engineer - Proyecto - Creación de pruebas automatizadas del ciclo o proceso de solicitud de un taxi tipo comfort
