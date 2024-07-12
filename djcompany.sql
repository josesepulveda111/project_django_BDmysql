-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3307
-- Tiempo de generación: 12-07-2024 a las 23:11:33
-- Versión del servidor: 11.3.2-MariaDB
-- Versión de PHP: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `djcompany`
--

DELIMITER $$
--
-- Procedimientos
--
DROP PROCEDURE IF EXISTS `activarartistas`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `activarartistas` (IN `idartistas` INT)   BEGIN

UPDATE artistas SET estado_contrato='Vigente' WHERE id=idartistas;

END$$

DROP PROCEDURE IF EXISTS `actualizaralbum`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `actualizaralbum` (IN `idalbum` INT, IN `nombrea` VARCHAR(255), IN `duraciona` VARCHAR(255), IN `cantidad_canciones` VARCHAR(255), IN `idioma` VARCHAR(255), IN `genero_musical` VARCHAR(255), IN `ventas` VARCHAR(255), IN `fecha_lanzamiento` DATE, IN `foto` VARCHAR(255), IN `colaboraciones` VARCHAR(255), IN `artistasid` INT)   BEGIN

UPDATE album SET nombrea=nombrea, duraciona=duraciona, cantidad_canciones=cantidad_canciones, idioma=idioma, genero_musical=genero_musical, ventas=ventas, fecha_lanzamiento=fecha_lanzamiento, foto=foto, colaboraciones=colaboraciones, artistas_id=artistasid WHERE id=idalbum;

END$$

DROP PROCEDURE IF EXISTS `actualizarartistas`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `actualizarartistas` (IN `idartistas` INT, IN `nombrea` VARCHAR(255), IN `edada` VARCHAR(20), IN `nacionalidada` VARCHAR(255), IN `celulara` VARCHAR(255), IN `correoa` VARCHAR(255), IN `premiosa` VARCHAR(255), IN `fecha_firmaa` DATE, IN `fotoa` VARCHAR(255), IN `genero_musicala` VARCHAR(255))   BEGIN

UPDATE artistas SET nombre=nombrea, edad=edada, nacionalidad=nacionalidada, celular=celulara, correo=correoa, premios=premiosa, fecha_firma=fecha_firmaa, foto=fotoa, genero_musical=genero_musicala WHERE id=idartistas;

END$$

DROP PROCEDURE IF EXISTS `albumsdestacados`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `albumsdestacados` ()   BEGIN

SELECT * FROM album WHERE estado='Destacado';

END$$

DROP PROCEDURE IF EXISTS `albumsnodestacados`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `albumsnodestacados` ()   BEGIN

SELECT * FROM album WHERE estado='No destacado';

END$$

DROP PROCEDURE IF EXISTS `cancelartour`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `cancelartour` (IN `idtour` INT)   BEGIN

UPDATE tours SET estado_tour='Cancelado' WHERE id=idtour;

END$$

DROP PROCEDURE IF EXISTS `completartour`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `completartour` (IN `idtour` INT)   BEGIN

UPDATE tours SET estado_tour='Completado' WHERE id=idtour;

END$$

DROP PROCEDURE IF EXISTS `desactivarartistas`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `desactivarartistas` (IN `idartistas` INT)   BEGIN

UPDATE artistas SET estado_contrato='Cancelado' WHERE id=idartistas;

END$$

DROP PROCEDURE IF EXISTS `destacaralbum`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `destacaralbum` (IN `idalbum` INT)   BEGIN

UPDATE album SET estado='Destacado' WHERE id=idalbum;

END$$

DROP PROCEDURE IF EXISTS `encursotour`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `encursotour` (IN `idtour` INT)   BEGIN

UPDATE tours SET estado_tour='En curso' WHERE id=idtour;

END$$

DROP PROCEDURE IF EXISTS `insertaralbum`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `insertaralbum` (IN `nombrea` VARCHAR(255), IN `duraciona` VARCHAR(255), IN `cantidad_canciones` VARCHAR(255), IN `idioma` VARCHAR(255), IN `genero_musical` VARCHAR(255), IN `ventas` VARCHAR(255), IN `fecha_lanzamiento` DATE, IN `foto` VARCHAR(255), IN `colaboraciones` VARCHAR(255), IN `artistas` INT)   BEGIN

INSERT INTO album (nombrea,duraciona,cantidad_canciones,idioma,genero_musical,ventas,fecha_lanzamiento,foto,colaboraciones,estado,artistas_id) VALUES (nombrea,duraciona,cantidad_canciones,idioma,genero_musical,ventas,fecha_lanzamiento,foto,colaboraciones,'Destacado',artistas);

END$$

DROP PROCEDURE IF EXISTS `insertarartista`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `insertarartista` (IN `nombre` VARCHAR(255), IN `edad` VARCHAR(20), IN `nacionalidad` VARCHAR(255), IN `celular` VARCHAR(255), IN `correo` VARCHAR(255), IN `premios` VARCHAR(255), IN `fecha_firma` DATE, IN `foto` VARCHAR(255), IN `genero_musical` VARCHAR(255))   BEGIN

INSERT INTO artistas (nombre,edad,nacionalidad,celular,correo,premios,fecha_firma,foto,genero_musical,estado_contrato) VALUES (nombre,edad,nacionalidad,celular,correo,premios,fecha_firma,foto,genero_musical,'Vigente');

END$$

DROP PROCEDURE IF EXISTS `listadoartista`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `listadoartista` ()   BEGIN

SELECT * FROM artistas WHERE estado_contrato='Vigente';

END$$

DROP PROCEDURE IF EXISTS `listadoartistasactivos`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `listadoartistasactivos` ()   BEGIN

SELECT * FROM artistas WHERE estado_contrato='Vigente';

END$$

DROP PROCEDURE IF EXISTS `listadoartistasinactivos`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `listadoartistasinactivos` ()   BEGIN

SELECT * FROM artistas WHERE estado_contrato='Cancelado';

END$$

DROP PROCEDURE IF EXISTS `listadotourcan`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `listadotourcan` ()   BEGIN

SELECT * FROM tours WHERE estado_tour='Cancelado';

END$$

DROP PROCEDURE IF EXISTS `listadotourcom`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `listadotourcom` ()   BEGIN

SELECT * FROM tours WHERE estado_tour='Completado';

END$$

DROP PROCEDURE IF EXISTS `listadotourcur`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `listadotourcur` ()   BEGIN

SELECT * FROM tours WHERE estado_tour='En curso';

END$$

DROP PROCEDURE IF EXISTS `nodestacaralbum`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `nodestacaralbum` (IN `idalbum` INT)   BEGIN

UPDATE album SET estado='No destacado' WHERE id=idalbum;

END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `album`
--

DROP TABLE IF EXISTS `album`;
CREATE TABLE IF NOT EXISTS `album` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombrea` varchar(255) NOT NULL,
  `duraciona` varchar(255) NOT NULL,
  `cantidad_canciones` varchar(255) NOT NULL,
  `idioma` varchar(255) NOT NULL,
  `genero_musical` varchar(255) NOT NULL,
  `ventas` varchar(255) NOT NULL,
  `fecha_lanzamiento` date NOT NULL,
  `foto` varchar(255) NOT NULL,
  `colaboraciones` varchar(255) NOT NULL,
  `estado` varchar(255) NOT NULL,
  `artistas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `artistas_id` (`artistas_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `album`
--

INSERT INTO `album` (`id`, `nombrea`, `duraciona`, `cantidad_canciones`, `idioma`, `genero_musical`, `ventas`, `fecha_lanzamiento`, `foto`, `colaboraciones`, `estado`, `artistas_id`) VALUES
(1, 'Easy Money Baby', '55:32', '18 ', 'español', 'urbano', '5 millones', '2020-05-08', 'easymoney.jfif', 'Arcangel la maravisha', 'Destacado', 4),
(2, 'La Vida Es Una', '1h', '23', 'español', 'urbano', '5 millones', '2023-01-15', 'lavidaesuna.jfif', 'nomeacuerdo', 'No destacado', 4),
(3, 'Las Leyendas Nunca Mueren', '1h y 17m', '16', 'Español', 'Urbano Latino', '50M', '2021-11-26', 'LLNM.jpg', 'Jhayco, Myke Towers, Eladio Carrion, Mora', 'Destacado', 2),
(4, 'Emmanuel', '1h y 39m', '23', 'Español', 'Urbano Latino', '50M', '2020-05-29', 'emmanuel.jfif', 'Daddy Yankee, KarolG, Tego Calderon, Bad Bunny, Kendo Kaponi, Yandel', 'No destacado', 2),
(5, 'media', '1h', '20', 'ingles', 'regueton', '40M', '2024-04-04', 'lykemyke.jpg', 'isaza, victor', 'Destacado', 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `artistas`
--

DROP TABLE IF EXISTS `artistas`;
CREATE TABLE IF NOT EXISTS `artistas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `edad` varchar(20) NOT NULL,
  `nacionalidad` varchar(255) NOT NULL,
  `celular` varchar(255) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `premios` varchar(255) NOT NULL,
  `fecha_firma` date NOT NULL,
  `foto` varchar(255) NOT NULL,
  `genero_musical` varchar(255) NOT NULL,
  `estado_contrato` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `artistas`
--

INSERT INTO `artistas` (`id`, `nombre`, `edad`, `nacionalidad`, `celular`, `correo`, `premios`, `fecha_firma`, `foto`, `genero_musical`, `estado_contrato`) VALUES
(1, 'Feid', '30', 'Colombia', '3044417012', 'ferxxo@gmail.com', 'nose', '2024-03-31', 'ferxxo.jpg', 'urbano', 'Cancelado'),
(2, 'Anuel aa', '34', 'Puerto Rico', '345678903', 'doblea@gmail.com', 'gramys 3', '2024-04-03', 'anuel.jpg', 'versatilidad', 'Vigente'),
(3, 'jbalvin', 'hgfdgf', 'hgfd', '8765432', 'jajajja@gmail.com', 'gramys 3', '2024-04-04', 'jbalvin.webp', 'regueton', 'Cancelado'),
(4, 'Young KINGZ', '34', 'colombia', '8765432', 'YKZ@gmail.com', 'gramys 3', '2024-03-31', 'myke.jpg', 'regueton', 'Vigente'),
(5, 'Blessd', '24', 'colombia', '09876543', 'jajajja@gmail.com', 'yonose', '2024-01-01', 'blessd.jpg', 'regueton', 'Vigente'),
(6, 'test', '13', 'mexico', '333232', 'jaajajaja@jaja.com', 'aaaaa', '2024-04-11', 'blessd.jpg', 'aaa', 'Cancelado'),
(7, 'SAMUEL', '20', 'colombia', '6666666', 'luis@gmail.com', 'nose', '2024-04-02', 'lavidaesuna.jfif', 'Urbano Latino', 'Vigente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tours`
--

DROP TABLE IF EXISTS `tours`;
CREATE TABLE IF NOT EXISTS `tours` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombret` varchar(255) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `pais_visitar` varchar(255) NOT NULL,
  `ciudades_visitar` varchar(255) NOT NULL,
  `ventas_boletas` varchar(255) NOT NULL,
  `gananciast` varchar(255) NOT NULL,
  `patrocinadorest` varchar(255) NOT NULL,
  `estado_tour` varchar(255) NOT NULL,
  `artistas_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `artistas_id` (`artistas_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tours`
--

INSERT INTO `tours` (`id`, `nombret`, `fecha_inicio`, `fecha_fin`, `pais_visitar`, `ciudades_visitar`, `ventas_boletas`, `gananciast`, `patrocinadorest`, `estado_tour`, `artistas_id`) VALUES
(1, 'YKZFest', '2024-04-02', '2024-05-11', 'Colombia', 'Medellin,  Bogota, Cali', '200.000', '50 Millones', 'Postobon, Ron Caldas,  Aguardiente', 'Completado', 4),
(2, 'LEGOFest', '2024-04-01', '2024-05-01', 'Colombia', 'Medellin,  Bogota, Cali', '200.000', '30 Millones', 'Postobon, Ron Caldas,  Aguardiente', 'Cancelado', 3),
(3, 'BenditoFEST', '2024-04-15', '2024-04-30', 'Colombia', 'Medellin,  Bogota, Cali', '200.000', '40 Millones', 'Postobon, Ron Caldas,  Aguardiente', 'Completado', 5),
(4, 'jajajajajaaj', '2024-04-03', '2024-04-01', 'Venezuela', 'Maracaibo', '200.000', '5618181', 'SUABUELITA', 'Cancelado', 4),
(5, 'fest', '2024-04-02', '2024-05-02', 'mexico', 'ciudad de mexico', '100.000', '60M', 'Postobon ', 'Completado', 7);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `album`
--
ALTER TABLE `album`
  ADD CONSTRAINT `album_ibfk_1` FOREIGN KEY (`artistas_id`) REFERENCES `artistas` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `tours`
--
ALTER TABLE `tours`
  ADD CONSTRAINT `tours_ibfk_1` FOREIGN KEY (`artistas_id`) REFERENCES `artistas` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
