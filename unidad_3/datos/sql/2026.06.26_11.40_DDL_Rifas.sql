USE rifa_t;

CREATE TABLE IF NOT EXISTS tipos_usuario(
    id_tipo_usuario INTEGER AUTO_INCREMENT,
    tipo_usuario VARCHAR(25) NOT NULL,
    descripcion_tipo_usuario VARCHAR(100) NULL,

    CONSTRAINT pk_tipos_usuario PRIMARY KEY (id_tipo_usuario)
);

CREATE TABLE IF NOT EXISTS nacionalidades(
    id_nacionalidad INTEGER AUTO_INCREMENT,
    pais VARCHAR(60) NOT NULL,
    iso2 VARCHAR(2) NOT NULL,
    iso3 VARCHAR(3) NOT NULL,
    nacionalidad VARCHAR(25) NOT NULL,
    codigo VARCHAR(4) NOT NULL,

    CONSTRAINT pk_nacionalidades PRIMARY KEY (id_nacionalidad)
);

CREATE TABLE IF NOT EXISTS rifas(
    id_rifa INTEGER AUTO_INCREMENT,
    nombre_rifa VARCHAR(50) NOT NULL,
    precio DECIMAL NOT NULL,
    cantidad_rifas INTEGER NOT NULL,
    numeros_rifa INTEGER NOT NULL,
    fecha_creacion DATE DEFAULT CURRENT_DATE,
    fecha_lanzamiento DATE NOT NULL,

    CONSTRAINT pk_rifas PRIMARY KEY (id_rifa)
);

CREATE TABLE IF NOT EXISTS premios(
    id_premio INTEGER AUTO_INCREMENT,
    nombre_premio VARCHAR(50) NOT NULL,
    descripcion_premio VARCHAR(255) NULL,
    rifa_asociada INTEGER NOT NULL,

    CONSTRAINT pk_premio PRIMARY KEY (id_premio),
    CONSTRAINT fk_premios_rifas FOREIGN KEY (rifa_asociada) REFERENCES rifas(id_rifa)
);

CREATE TABLE IF NOT EXISTS usuarios(
    id_usuario INTEGER AUTO_INCREMENT,
    nombre_usuario VARCHAR(100) NOT NULL,
    rut_usuario VARCHAR(12) NULL,
    nacionalidad_usuario INTEGER NULL,
    telefono_usuario VARCHAR(13) NULL,
    email_usuario VARCHAR(255) NULL,
    tipo_usuario INTEGER NOT NULL,
    contrasena VARCHAR(60) NULL,

    CONSTRAINT pk_usuarios PRIMARY KEY (id_usuario),    
    CONSTRAINT fk_usuarios_nacionalidades FOREIGN KEY (nacionalidad_usuario) REFERENCES nacionalidades(id_nacionalidad),
    CONSTRAINT fk_usuarios_tiposusuario FOREIGN KEY (tipo_usuario) REFERENCES tipos_usuario(id_tipo_usuario)
);

-- CREAMOS LA TABLA AUXILIAR PARA UNIR MUCHOS USUARIOS CON MUCHAS RIFAS
CREATE TABLE IF NOT EXISTS rifas_usuarios(
    id_rifa_usuario INTEGER AUTO_INCREMENT,
    rifa INTEGER NOT NULL,
    usuario INTEGER NOT NULL,

    CONSTRAINT pk_rifas_usuarios PRIMARY KEY (id_rifa_usuario),    
    CONSTRAINT fk_usuariosrifas_rifas FOREIGN KEY (rifa) REFERENCES rifas(id_rifa),
    CONSTRAINT fk_usuariosrifas_usuarios FOREIGN KEY (usuario) REFERENCES usuarios(id_usuario)
);