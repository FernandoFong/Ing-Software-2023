use ing_soft;

CREATE TABLE `usuario` (
  `id_usuario` varchar(200) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `passwd` blob,
  PRIMARY KEY (`id_usuario`)
) ;

CREATE TABLE `pedidos` (
  `id_pedido` int NOT NULL AUTO_INCREMENT,
  `id_usuario` varchar(200) NOT NULL,
  `producto` varchar(45) DEFAULT NULL,
  `precio` varchar(45) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `estatus` tinyint DEFAULT NULL,
  PRIMARY KEY (`id_pedido`),
  KEY `usuario_idx` (`id_usuario`),
  CONSTRAINT `usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE
);

insert into usuario (id_usuario, nombre)
values ("fernandofong@ciencias.unam.mx", "Fernando");

insert into usuario 
values ("vale@ciencias.unam.mx", "Valeria", null, null, null);

select * from usuario;

select * from pedidos;