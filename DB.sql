-- phpMyAdmin SQL Dump
-- version 4.0.10
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 08, 2014 at 04:16 PM
-- Server version: 5.1.56-community
-- PHP Version: 5.2.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `group2`
--

-- --------------------------------------------------------

--
-- Table structure for table `tweets`
--

CREATE TABLE IF NOT EXISTS `tweets` (
  `PK` int(11) NOT NULL AUTO_INCREMENT,
  `ID` text NOT NULL,
  `Tweet` text NOT NULL,
  `ScoreAlgorithm` float NOT NULL,
  `ScoreControl` float NOT NULL,
  `Timestamp` text,
  `Datetime` datetime DEFAULT NULL,
  `Calculated` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`PK`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13897 ;

--
-- Triggers `tweets`
--
DROP TRIGGER IF EXISTS `Convert_Datetime`;
DELIMITER //
CREATE TRIGGER `Convert_Datetime` BEFORE INSERT ON `tweets`
 FOR EACH ROW SET NEW.Datetime = STR_TO_DATE(REPLACE (NEW.TIMESTAMP,"+0000",""),"%a %b %d %H:%i:%S %Y")
//
DELIMITER ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
