##Requisitos:

Python2.7

bibliotecas de python: flask, urllib, json

La mejor forma de instalar estas es a través de pip
Ejemplo: pip install flask


##Como correr la API

Ejecutar el siguiente comando en el directorio:

FLASK_APP=api.py flask run

De esta forma se levantará el server usualmente en http://127.0.0.1:8080

##Como utilizarla

La API cuenta con un solo endpoint, siendo este /applicant/:username

Ejemplo de uso: curl 'http://localhost:8080/applicant/pato24s

Si el username no existe en GitHub la Api devolverá un 404 con un mensaje de eror correspondiente, dado que esta es la respuesta dada por la API de GitHub

Caso contrario la API devolverá un 200 mostrando con que equipo tiene más afinidad el usuario buscado.

##Decisiones

Se decidió crear un diccionario en el que los pares (clave,valor) corresponden a pares (lenguaje de programacion, equipo). Este se encuentra en el archivo diccLanguages.py
Como se puede apreciar, dicho archivo se encuentra incompleto dado que github no ofrece una forma sencilla de obtener todos los lenguajes de programación reconocidos por este. Más adelante explicaré una posible solución.

El criterio de elección de equipo es el siguiente: Se recorre sobre todos los repos del usuario, se ve que lenguaje es el más utilizado en cada uno, y ese lenguaje se traduce en un potencial equipo. El equipo que tenga más traducciones hechas es el elegido. En caso de empate se devuelve uno de los dos.

No se utilizó caché

Se agregó un caso que chequea si se obtuvo un 403 de parte de GitHub ya que, si bien es una API pública, puede ocurrir que se exceda el rate limit de dicha API



##Trabajo pendiente

Se podría ampliar el diccionario utilizando la información que brinda este archivo https://github.com/github/linguist/blob/master/lib/linguist/languages.yml

Agregar el uso de una pequeña caché

Arreglar los tests (poder mockear respuests y generar los tests detallados anteriormente)

Ver si se prefiere otro tipo de respuesta por parte de la API. Ejemplo: devolver los 3 equipos con un % de afinidad. Siendo este 100*(cantidad de repos que matchean con el equipo)/(cantidad total de repos)