CREATE DATABASE servicios;
 USE servicios;

CREATE TABLE loguin
(
    id_loguin INT AUTO_INCREMENT NOT NULL , 
    usuario_id_usuario VARCHAR (15) NOT NULL, 
    contrasena VARCHAR(20) NOT NULL,

    PRIMARY KEY(id_loguin)
);
 
CREATE TABLE rol
(
    id_rol VARCHAR(10) NOT NULL, 
    desc_rol VARCHAR(50) NOT NULL, 
    estado_rol BOOLEAN NOT NULL,

    PRIMARY KEY(id_rol)
);

CREATE TABLE usuario
(
    id_usuario VARCHAR (15) NOT NULL, 
    nombre VARCHAR(50) NOT NULL, 
    apellido VARCHAR(50) NOT NULL, 
    correo_electronico VARCHAR(60) NOT NULL, 
    telefono VARCHAR(15) NOT NULL,
    rol_id_rol VARCHAR(10) NOT NULL,
    permisos_id_permisos VARCHAR(10) NOT NULL,

    PRIMARY KEY (id_usuario)
);

CREATE TABLE modulos 
(
    id_modulo VARCHAR(50) NOT NULL,  
    nombre VARCHAR(80) NOT NULL, 
    proyecto VARCHAR(80) NOT NULL, 
    fabricante VARCHAR(80) NOT NULL, 
    proveedor VARCHAR(80) NOT NULL, 
    cliente VARCHAR(80) NOT NULL, 
    modelo VARCHAR(80) NOT NULL, 
    fecha_creacion DATE NOT NULL, 
    fecha_inicio_operacion DATE NOT NULL, 
    ubicacion VARCHAR(40) NOT NULL, 
    estado_modulo BOOLEAN NOT NULL,

    PRIMARY KEY(id_modulo)
);

CREATE TABLE permisos 
(
    id_permisos VARCHAR(10) NOT NULL, 
    desc_permisos VARCHAR(100) NOT NULL,

    PRIMARY KEY(id_permisos)
); 


CREATE  TABLE   historial
(
    modulos_id_modulo VARCHAR(50) NOT NULL,    
    usuario_id_usuario VARCHAR(15) NOT NULL,
    almacenes_id_almacen VARCHAR(30) NOT NULL,    
    fecha_translado DATE NOT NULL,    
    desc_translado LONGTEXT NOT NULL,    

    PRIMARY KEY (modulos_id_modulo, usuario_id_usuario)
);


CREATE  TABLE   almacenes
(
    id_almacen VARCHAR(30) NOT NULL,  
    usuario_id_usuario VARCHAR(15) NOT NULL,   
    desc_almacen LONGTEXT NOT NULL,    
    estado_almacen BOOLEAN NOT NULL,

    PRIMARY KEY (id_almacen)
);

alter table loguin add constraint loguin_usuario
foreign key (usuario_id_usuario) references usuario(id_usuario);

alter table usuario add constraint usuario_permisos
foreign key (permisos_id_permisos) references permisos(id_permisos);

alter table usuario add constraint usuario_rol
foreign key (rol_id_rol) references rol(id_rol);

alter table almacenes add constraint almacenes_usuario
foreign key (usuario_id_usuario) references usuario(id_usuario);  