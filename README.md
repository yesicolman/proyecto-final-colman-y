# proyecto-final-colman-y

Objetivos generales
PreEntrega Nro 3
Nombre: Yesica Colman

Desarrollar una WEB Django con patrón MVT subida a Github.
Se debe entregar

1. Link de GitHub con el proyecto totalmente subido a la plataforma --> https://github.com/yesicolman/proyecto-final-colman-y.git
2. Proyecto Web Django con patrón MVT que incluya: El proyecto se llama "ProyectoFinalYC" y se agregó Startapp "MiApp"
        a. Herencia de HTML
        Se incorporó dentro de la carpeta templates/MiApp el archivo --> baseweb.html con el header y footer que serán heredados por el resto de templates y navegación dentro de la página web -->  {% extends 'MiApp/baseweb.html'%}
        
        b. URL que se pueden consultar:

        destinos/
        usuarios/
        post/


        form_contacto/
        agregar_destino/
        buscar_destino/
        agregar_comentario/
        agregar_guía/

3. Por lo menos 3 clases en models:
La idea es empezar a trabar con un blog de viajes y se crearon en principio 3 modelos, y para la re entrega 2 adicionales para incorporar formularios:

        Destinos
        Usuarios
        Post
        Guias
        Comentario
        Respuesta

4. Un formulario para insertar datos a todas las clases de tu models --> 
        Entrega 1: Se crearon las funciones de form_contacto y agregar_destino (se pueden acceder por la Nav)
        REENTREGA: Ademas del formulario de Contacto y Agregar Destino se incorporó la opción de: 
                agregar_comentario/
                agregar_guía/
                
                Se acceden a ambos por NAV

5. Un formulario para buscar algo en la BD ---> La url es /buscar_destino o se puede acceder por la nav 

6. Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.


