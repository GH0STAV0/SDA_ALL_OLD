-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 29, 2021 at 02:54 PM
-- Server version: 8.0.13-4
-- PHP Version: 7.2.24-0ubuntu0.18.04.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `f6V3kVwxvH`
--

-- --------------------------------------------------------

--
-- Table structure for table `name_cheap`
--

CREATE TABLE `name_cheap` (
  `id` int(11) NOT NULL,
  `cnf_names` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `used` varchar(11) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `name_cheap`
--

INSERT INTO `name_cheap` (`id`, `cnf_names`, `used`) VALUES
(1, 'NCVPN-NL-Amsterdam-TCP.ovpn', 'n'),
(2, 'NCVPN-US-Seattle-TCP.ovpn', 'n'),
(3, 'NCVPN-US-Charlotte-TCP.ovpn', 'n'),
(4, 'NCVPN-IN-Mumbai-TCP.ovpn', 'n'),
(5, 'NCVPN-MX-Guadalajara-TCP.ovpn', 'n'),
(6, 'NCVPN-BE-Brussels-TCP.ovpn', 'n'),
(7, 'NCVPN-IS-Reykjavik-UDP.ovpn', 'n'),
(8, 'NCVPN-NO-Oslo-UDP.ovpn', 'n'),
(9, 'NCVPN-SI-Ljubljana-UDP.ovpn', 'n'),
(10, 'NCVPN-RS-Belgrade-UDP.ovpn', 'n'),
(11, 'NCVPN-SG-Singapore-UDP.ovpn', 'n'),
(12, 'NCVPN-CR-San_Jose-UDP.ovpn', 'n'),
(13, 'NCVPN-FR-Paris-UDP.ovpn', 'n'),
(14, 'NCVPN-US-Las_Vegas-UDP.ovpn', 'n'),
(15, 'NCVPN-CA-Montreal-UDP.ovpn', 'n'),
(16, 'NCVPN-ES-Valencia-TCP.ovpn', 'n'),
(17, 'NCVPN-FI-Helsinki-UDP.ovpn', 'n'),
(18, 'NCVPN-BG-Sofia-TCP.ovpn', 'n'),
(19, 'NCVPN-US-Dallas-UDP.ovpn', 'n'),
(20, 'NCVPN-PT-Lisbon-TCP.ovpn', 'n'),
(21, 'NCVPN-US-Boston-UDP.ovpn', 'n'),
(22, 'NCVPN-US-Denver-UDP.ovpn', 'n'),
(23, 'NCVPN-CA-Vancouver-UDP.ovpn', 'n'),
(24, 'NCVPN-HR-Zagreb-TCP.ovpn', 'n'),
(25, 'NCVPN-UK-Manchester-TCP.ovpn', 'n'),
(26, 'NCVPN-UK-Glasgow-UDP.ovpn', 'n'),
(27, 'NCVPN-MX-Guadalajara-UDP.ovpn', 'n'),
(28, 'NCVPN-UK-Maidenhead-TCP.ovpn', 'n'),
(29, 'NCVPN-IS-Reykjavik-TCP.ovpn', 'n'),
(30, 'NCVPN-US-Atlanta-TCP.ovpn', 'n'),
(31, 'NCVPN-RO-Bucharest-UDP.ovpn', 'n'),
(32, 'NCVPN-BR-Sao_Paulo-UDP.ovpn', 'n'),
(33, 'NCVPN-AU-Perth-TCP.ovpn', 'n'),
(34, 'NCVPN-KR-Seoul-UDP.ovpn', 'n'),
(35, 'NCVPN-ES-Madrid-TCP.ovpn', 'n'),
(36, 'NCVPN-KR-Seoul-TCP.ovpn', 'n'),
(37, 'NCVPN-US-Chicago-UDP.ovpn', 'n'),
(38, 'NCVPN-AU-Brisbane-TCP.ovpn', 'n'),
(39, 'NCVPN-IE-Dublin-UDP.ovpn', 'n'),
(40, 'NCVPN-CO-Bogota-UDP.ovpn', 'n'),
(41, 'NCVPN-MY-Kuala_Lumpur-TCP.ovpn', 'n'),
(42, 'NCVPN-CL-Santiago-UDP.ovpn', 'n'),
(43, 'NCVPN-US-Phoenix-TCP.ovpn', 'n'),
(44, 'NCVPN-UK-Manchester-UDP.ovpn', 'n'),
(45, 'NCVPN-ES-Valencia-UDP.ovpn', 'n'),
(46, 'NCVPN-US-Cincinnati-TCP.ovpn', 'n'),
(47, 'NCVPN-AL-Tirana-UDP.ovpn', 'n'),
(48, 'NCVPN-US-New_Orleans-TCP.ovpn', 'n'),
(49, 'NCVPN-US-Seattle-UDP.ovpn', 'n'),
(50, 'NCVPN-AU-Perth-UDP.ovpn', 'n'),
(51, 'NCVPN-EE-Tallinn-TCP.ovpn', 'n'),
(52, 'NCVPN-SE-Stockholm-TCP.ovpn', 'n'),
(53, 'NCVPN-IE-Dublin-TCP.ovpn', 'n'),
(54, 'NCVPN-NO-Oslo-TCP.ovpn', 'n'),
(55, 'NCVPN-LV-Riga-TCP.ovpn', 'n'),
(56, 'NCVPN-DE-Frankfurt-TCP.ovpn', 'n'),
(57, 'NCVPN-AU-Sydney-TCP.ovpn', 'n'),
(58, 'NCVPN-FI-Helsinki-TCP.ovpn', 'n'),
(59, 'NCVPN-EE-Tallinn-UDP.ovpn', 'n'),
(60, 'NCVPN-CA-Montreal-TCP.ovpn', 'n'),
(61, 'NCVPN-US-New_York-UDP.ovpn', 'n'),
(62, 'NCVPN-FR-Marseille-UDP.ovpn', 'n'),
(63, 'NCVPN-AR-Buenos_Aires-TCP.ovpn', 'n'),
(64, 'NCVPN-PT-Lisbon-UDP.ovpn', 'n'),
(65, 'NCVPN-RS-Belgrade-TCP.ovpn', 'n'),
(66, 'NCVPN-UK-Maidenhead-UDP.ovpn', 'n'),
(67, 'NCVPN-AU-Adelaide-UDP.ovpn', 'n'),
(68, 'NCVPN-IL-Tel_Aviv-UDP.ovpn', 'n'),
(69, 'NCVPN-GR-Athens-TCP.ovpn', 'n'),
(70, 'NCVPN-US-Chicago-TCP.ovpn', 'n'),
(71, 'NCVPN-AU-Melbourne-TCP.ovpn', 'n'),
(72, 'NCVPN-DK-Copenhagen-UDP.ovpn', 'n'),
(73, 'NCVPN-PL-Warsaw-UDP.ovpn', 'n'),
(74, 'NCVPN-US-Phoenix-UDP.ovpn', 'n'),
(75, 'NCVPN-HR-Zagreb-UDP.ovpn', 'n'),
(76, 'NCVPN-ZA-Johannesburg-UDP.ovpn', 'n'),
(77, 'NCVPN-US-Cincinnati-UDP.ovpn', 'n'),
(78, 'NCVPN-ES-Madrid-UDP.ovpn', 'n'),
(79, 'NCVPN-SI-Ljubljana-TCP.ovpn', 'n'),
(80, 'NCVPN-IT-Milan-TCP.ovpn', 'n'),
(81, 'NCVPN-CZ-Prague-TCP.ovpn', 'n'),
(82, 'NCVPN-RO-Bucharest-TCP.ovpn', 'n'),
(83, 'NCVPN-BR-Sao_Paulo-TCP.ovpn', 'n'),
(84, 'NCVPN-TW-Taipei-TCP.ovpn', 'n'),
(85, 'NCVPN-US-Dallas-TCP.ovpn', 'n'),
(86, 'NCVPN-CH-Zurich-TCP.ovpn', 'n'),
(87, 'NCVPN-CZ-Prague-UDP.ovpn', 'n'),
(88, 'NCVPN-ZA-Johannesburg-TCP.ovpn', 'n'),
(89, 'NCVPN-FR-Marseille-TCP.ovpn', 'n'),
(90, 'NCVPN-US-Los_Angeles-UDP.ovpn', 'n'),
(91, 'NCVPN-US-Atlanta-UDP.ovpn', 'n'),
(92, 'NCVPN-NG-Lagos-UDP.ovpn', 'n'),
(93, 'NCVPN-BG-Sofia-UDP.ovpn', 'n'),
(94, 'NCVPN-US-San_Jose-TCP.ovpn', 'n'),
(95, 'NCVPN-CA-Toronto-TCP.ovpn', 'n'),
(96, 'NCVPN-US-Charlotte-UDP.ovpn', 'n'),
(97, 'NCVPN-NZ-Auckland-UDP.ovpn', 'n'),
(98, 'NCVPN-AU-Brisbane-UDP.ovpn', 'n'),
(99, 'NCVPN-US-Ashburn-UDP.ovpn', 'n'),
(100, 'NCVPN-MD-Chisinau-TCP.ovpn', 'n'),
(101, 'NCVPN-US-Miami-UDP.ovpn', 'n'),
(102, 'NCVPN-US-Ashburn-TCP.ovpn', 'n'),
(103, 'NCVPN-UK-London-TCP.ovpn', 'n'),
(104, 'NCVPN-US-Los_Angeles-TCP.ovpn', 'n'),
(105, 'NCVPN-US-San_Jose-UDP.ovpn', 'n'),
(106, 'NCVPN-PE-Lima-TCP.ovpn', 'n'),
(107, 'NCVPN-NZ-Auckland-TCP.ovpn', 'n'),
(108, 'NCVPN-IN-Mumbai-UDP.ovpn', 'n'),
(109, 'NCVPN-GR-Athens-UDP.ovpn', 'n'),
(110, 'NCVPN-CL-Santiago-TCP.ovpn', 'n'),
(111, 'NCVPN-US-New_York-TCP.ovpn', 'n'),
(112, 'NCVPN-AU-Sydney-UDP.ovpn', 'n'),
(113, 'NCVPN-US-Miami-TCP.ovpn', 'n'),
(114, 'NCVPN-PL-Warsaw-TCP.ovpn', 'n'),
(115, 'NCVPN-BE-Brussels-UDP.ovpn', 'n'),
(116, 'NCVPN-TW-Taipei-UDP.ovpn', 'n'),
(117, 'NCVPN-MD-Chisinau-UDP.ovpn', 'n'),
(118, 'NCVPN-US-New_Orleans-UDP.ovpn', 'n'),
(119, 'NCVPN-IL-Tel_Aviv-TCP.ovpn', 'n'),
(120, 'NCVPN-HU-Budapest-TCP.ovpn', 'n'),
(121, 'NCVPN-MY-Kuala_Lumpur-UDP.ovpn', 'n'),
(122, 'NCVPN-IN-New_Delhi-UDP.ovpn', 'n'),
(123, 'NCVPN-CO-Bogota-TCP.ovpn', 'n'),
(124, 'NCVPN-US-Denver-TCP.ovpn', 'n'),
(125, 'NCVPN-CH-Zurich-UDP.ovpn', 'n'),
(126, 'NCVPN-US-Las_Vegas-TCP.ovpn', 'n'),
(127, 'NCVPN-SE-Stockholm-UDP.ovpn', 'n'),
(128, 'NCVPN-UK-Birmingham-UDP.ovpn', 'n'),
(129, 'NCVPN-PE-Lima-UDP.ovpn', 'n'),
(130, 'NCVPN-US-Houston-TCP.ovpn', 'n'),
(131, 'NCVPN-NG-Lagos-TCP.ovpn', 'n'),
(132, 'NCVPN-SG-Singapore-TCP.ovpn', 'n'),
(133, 'NCVPN-NL-Amsterdam-UDP.ovpn', 'n'),
(134, 'NCVPN-FR-Bordeaux-TCP.ovpn', 'n'),
(135, 'NCVPN-FR-Paris-TCP.ovpn', 'n'),
(136, 'NCVPN-AU-Melbourne-UDP.ovpn', 'n'),
(137, 'NCVPN-AU-Adelaide-TCP.ovpn', 'n'),
(138, 'NCVPN-JP-Tokyo-UDP.ovpn', 'n'),
(139, 'NCVPN-HU-Budapest-UDP.ovpn', 'n'),
(140, 'NCVPN-IT-Milan-UDP.ovpn', 'n'),
(141, 'NCVPN-AL-Tirana-TCP.ovpn', 'n'),
(142, 'NCVPN-AT-Vienna-UDP.ovpn', 'n'),
(143, 'NCVPN-SK-Bratislava-UDP.ovpn', 'n'),
(144, 'NCVPN-SK-Bratislava-TCP.ovpn', 'n'),
(145, 'NCVPN-CA-Toronto-UDP.ovpn', 'n'),
(146, 'NCVPN-CR-San_Jose-TCP.ovpn', 'n'),
(147, 'NCVPN-AE-Dubai-UDP.ovpn', 'n'),
(148, 'NCVPN-CA-Vancouver-TCP.ovpn', 'n'),
(149, 'NCVPN-DE-Frankfurt-UDP.ovpn', 'n'),
(150, 'NCVPN-DK-Copenhagen-TCP.ovpn', 'n'),
(151, 'NCVPN-AR-Buenos_Aires-UDP.ovpn', 'n'),
(152, 'NCVPN-AT-Vienna-TCP.ovpn', 'n'),
(153, 'NCVPN-IN-New_Delhi-TCP.ovpn', 'n'),
(154, 'NCVPN-UK-London-UDP.ovpn', 'n'),
(155, 'NCVPN-US-Houston-UDP.ovpn', 'n'),
(156, 'NCVPN-UK-Birmingham-TCP.ovpn', 'n'),
(157, 'NCVPN-US-Boston-TCP.ovpn', 'n'),
(158, 'NCVPN-UK-Glasgow-TCP.ovpn', 'n'),
(159, 'NCVPN-JP-Tokyo-TCP.ovpn', 'n'),
(160, 'NCVPN-LV-Riga-UDP.ovpn', 'n'),
(161, 'NCVPN-FR-Bordeaux-UDP.ovpn', 'n');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `name_cheap`
--
ALTER TABLE `name_cheap`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `name_cheap`
--
ALTER TABLE `name_cheap`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=162;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
