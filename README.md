# library-management
Library Management de Odoo que permite gestionar una biblioteca, donde se puede administrar libros, contactos y prestamos, asimismo puede marcar como socio a un usuario, con la finalidad que este pueda ver sus prestamos. 


Pre-requisitos:
Tener Docker, PostgreSQL y git onar el repositorio

 
Instalación: 

Desde el cmd crear la base de datos con 
docker run -d ^
-e POSTGRES_USER=odoo ^
-e POSTGRES_PASSWORD=odoo ^
-e POSTGRES_DB=postgres ^
--name db ^
postgres:15

Descargar Odoo
docker run -d -p 8069:8069 --name odoo19 --link db:db odoo:19

Poner en le navegador http://localhost:8069

Aparecera una vista con un formulario 
Nombre de la datos: library_db
dale click a Create Database

Ir a la carpeta donde se desea clonar 
y ejercutar 
git clone git@github.com:PamelaMorales77/library-management.git

Regresar al navegardor 

Activar modo desarrollador
Ir a Apps
Actualizar lista de aplicaciones
Buscar "Library Management"
Instalar


