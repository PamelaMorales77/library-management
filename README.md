# library-management
Library Management de Odoo que permite gestionar una biblioteca, donde se puede administrar libros, contactos y prestamos, asimismo puede marcar como socio a un usuario, con la finalidad que este pueda ver sus prestamos. 


Pre-requisitos:
Docker
PostgreSQL
Git 

 
Instalación: 

Crear base de datos en Docker en el cmd:
docker run -d ^
-e POSTGRES_USER=odoo ^
-e POSTGRES_PASSWORD=odoo ^
-e POSTGRES_DB=postgres ^
--name db ^
postgres:15

Ejecutar Odoo:
docker run -d -p 8069:8069 --name odoo19 --link db:db odoo:19

Acceder a Odoo:
http://localhost:8069

Crear la base de datos:
Nombre de la datos: library_db
dale click a Create Database

Clonar el repositorio:
git clone git@github.com:PamelaMorales77/library-management.git

Instalar el modulo:
Regresar al navegardor
Activar modo desarrollador
Ir a Apps
Actualizar lista de aplicaciones
Buscar Library Management
Activar 
Ir a Apps
Actualizar lista de aplicaciones
Buscar "Library Management"
Instalar

Pruebas:
Acceso como administrador: 
Activar el modo desarrollador.
Ir a Ajustes/ Usuarios y empresas / Usuarios
Crear un usuario Bibliotecario asignando los siguiente roles: Administrador y Bibliotecario

Inicio de sesión:
Accerder a: http://localhost:8069/web/login
Entrar como el usario Bibliotecario.

Probar gestión de libros:
En la barra lateral ir a: Library Management
Ir al apartado de Libros.
Agregar un nuevo libro.

Probar gestión de Prestamos:
En la barra lateral ir a: Library Management
Ir al apartado de Prestamos.
Agregar un nuevo Prestamo.

Probar gestión de Devoluciones:
En la barra lateral ir a: Library Management
Ir al apartado de Prestamos.
Ver el prestamo que se quiere hacer devolución.
Entrar y precionar Devolver.


Probar gestión de Usuarios:
Ir a: Ajustes / Usuarios y empresas / Usuarios
Crear 2  usuarios:
Usuario público: Seleccionar Usuario Publico y Rol/Portal 
Usurio Socio: Rol/Portal, ir a Library Management y en el apartado Socios buscar el usario recien creado, darle click, selecionae socio y guardar.


Pruebar usuario público: 
Accerder a: http://localhost:8069/web/login
Entrar como el usario Usuario Público
Verificar que puede visualizar el catálogo de libros

Pruebar usuario público: 
Accerder a: http://localhost:8069/web/login
Entrar como el usario Usuario Socio.
Verificar que puede visualizar el catálogo de libros, ver sus prestamos y devoluciones.

Prueba de funcionalidades del sistema
Probar crear un prestamo a un libro que ya tiene un prestamo activo.
Probar hacer un prestamo a un usario con 5 prestamos.




