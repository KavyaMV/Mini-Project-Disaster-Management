-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Nov 07, 2019 at 12:57 PM
-- Server version: 5.5.36
-- PHP Version: 5.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `disaster_management1`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_alert`
--

CREATE TABLE IF NOT EXISTS `tbl_alert` (
  `alert_id` int(11) NOT NULL AUTO_INCREMENT,
  `alert_type` varchar(25) NOT NULL,
  `place` varchar(40) NOT NULL,
  `district` varchar(40) NOT NULL,
  `datee` varchar(25) NOT NULL,
  `timee` varchar(9) NOT NULL,
  `descrption` varchar(40) NOT NULL,
  `reg_id` int(10) NOT NULL,
  PRIMARY KEY (`alert_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `tbl_alert`
--

INSERT INTO `tbl_alert` (`alert_id`, `alert_type`, `place`, `district`, `datee`, `timee`, `descrption`, `reg_id`) VALUES
(9, 'Warning', 'Tiruvangad', 'Kannur', '', '15:28:12.', 'flood', 0),
(10, 'Shift from the area', 'Kuttiyanchal', 'Idukki', '2019-11-20', '10:38:54.', 'Land slide', 0),
(11, 'Warning', 'Amaravati', 'Idukki', '2019-10-30', '16:14:25.', 'EarthQuake', 0);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_allocation`
--

CREATE TABLE IF NOT EXISTS `tbl_allocation` (
  `alloc_id` int(10) NOT NULL AUTO_INCREMENT,
  `request_id` varchar(10) NOT NULL,
  `item_type` varchar(30) NOT NULL,
  `value` varchar(40) NOT NULL,
  UNIQUE KEY `alloc_id` (`alloc_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=39 ;

--
-- Dumping data for table `tbl_allocation`
--

INSERT INTO `tbl_allocation` (`alloc_id`, `request_id`, `item_type`, `value`) VALUES
(1, '23', 'Food Items Provided', 'Rice'),
(2, '23', 'Clothes are Provided', 'ForMen'),
(9, '23', 'shift', '7'),
(12, '23', 'shift', '6'),
(27, '23', 'shift', '8'),
(38, '23', 'shift', '6');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_disaster`
--

CREATE TABLE IF NOT EXISTS `tbl_disaster` (
  `disaster_id` int(10) NOT NULL AUTO_INCREMENT,
  `disaster_type` varchar(30) NOT NULL,
  `disaster_name` varchar(30) NOT NULL,
  PRIMARY KEY (`disaster_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_disasterdetails`
--

CREATE TABLE IF NOT EXISTS `tbl_disasterdetails` (
  `dis_id` int(10) NOT NULL AUTO_INCREMENT,
  `description` varchar(50) NOT NULL,
  `place_id` int(10) NOT NULL,
  `disaster_id` int(10) NOT NULL,
  `wardno` int(10) NOT NULL,
  `lattitude` varchar(10) NOT NULL,
  `longitude` varchar(10) NOT NULL,
  PRIMARY KEY (`dis_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_district`
--

CREATE TABLE IF NOT EXISTS `tbl_district` (
  `district_id` int(10) NOT NULL AUTO_INCREMENT,
  `district_name` varchar(20) NOT NULL,
  `state_id` int(10) NOT NULL,
  PRIMARY KEY (`district_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=22 ;

--
-- Dumping data for table `tbl_district`
--

INSERT INTO `tbl_district` (`district_id`, `district_name`, `state_id`) VALUES
(1, 'Kodagu', 1),
(2, 'Udupi', 1),
(5, 'Kanjipuram', 3),
(6, 'Kanayakumari', 3),
(8, 'Trivandrum', 2),
(9, 'Kollam', 2),
(10, 'Pattanamthitta', 2),
(11, 'Allapuzha', 2),
(12, 'Kottayam', 2),
(13, 'Idukki', 2),
(14, 'Ernakulam', 2),
(15, 'Trissur', 2),
(16, 'Palakad', 2),
(17, 'Calicut', 2),
(18, 'Malapuram', 2),
(19, 'Wayanad', 2),
(20, 'Kanur', 2),
(21, 'Kasorgod', 2);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_emergencyservices`
--

CREATE TABLE IF NOT EXISTS `tbl_emergencyservices` (
  `idenfication_no` int(11) NOT NULL,
  `name_of_head` varchar(30) NOT NULL,
  `no_of_employees` int(10) NOT NULL,
  `emer_id` int(11) NOT NULL,
  `emer_type` varchar(15) NOT NULL,
  `reg_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_helprequest`
--

CREATE TABLE IF NOT EXISTS `tbl_helprequest` (
  `help_id` int(20) NOT NULL AUTO_INCREMENT,
  `help_type` varchar(50) NOT NULL,
  `date` varchar(11) NOT NULL,
  `time` varchar(11) NOT NULL,
  `status` varchar(25) NOT NULL,
  `requester_name` varchar(30) NOT NULL,
  `requested_to` varchar(20) NOT NULL,
  `assigned_to` int(15) NOT NULL,
  `assigned_time` varchar(6) NOT NULL,
  `disaster_id` int(10) NOT NULL,
  UNIQUE KEY `help_id` (`help_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `tbl_helprequest`
--

INSERT INTO `tbl_helprequest` (`help_id`, `help_type`, `date`, `time`, `status`, `requester_name`, `requested_to`, `assigned_to`, `assigned_time`, `disaster_id`) VALUES
(1, 'Land slide', '2019-10-21 ', '12:48:50.50', 'Accept', '30', 'Deepa', 23, '12:50:', 0),
(2, 'Accident to my friend', '2019-10-22 ', '21:09:06.34', 'Accept', '34', 'Sree Partvathi M Sub', 23, '21:24:', 0),
(4, 'Landslide in my friends area', '2019-10-28 ', '09:19:37.10', 'Accept', '34', 'Ammu Das', 8, '20:50:', 0),
(5, 'Cyclone', '2019-10-29 ', '06:51:26.91', 'Accept', '34', 'Mariya Jose', 23, '06:51:', 0),
(6, 'flood', '2019-10-29 ', '09:50:43.80', 'Accept', '30', 'anu', 1, '09:51:', 0),
(7, 'Cyclone', '2019-11-02 ', '12:10:30.80', 'Not Accepted', '36', 'Reshma Raju', 0, '00:00:', 0);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_login`
--

CREATE TABLE IF NOT EXISTS `tbl_login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `usertype` varchar(25) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(15) NOT NULL,
  `status` varchar(15) NOT NULL DEFAULT 'Accept',
  UNIQUE KEY `login_id` (`login_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `tbl_login`
--

INSERT INTO `tbl_login` (`login_id`, `usertype`, `username`, `password`, `status`) VALUES
(1, 'admin', 'admin@gmail.com', 'admin123', 'Accept'),
(2, 'User', 'geethadas@gmail.com', 'geethadas', 'Accept'),
(3, 'Volunteer', 'geethamohan@gmail.com', 'geetha1234', 'Accept'),
(4, 'Police station', 'police10234@gmail.com', '123', 'Accept'),
(5, 'Fire station', 'firestation334455@gmail.com', '123456789', 'Accept'),
(6, 'User', 'anilagopi212@gmail.com', 'anila212', 'Accept'),
(7, 'Volunteer', 'swered@gmail.com', '1234', 'Accept'),
(8, 'Police station', 'police102@gmail.com', '123', 'Accept'),
(9, 'Fire station', 'firestation333@gmail.com', 'firestation333', 'Accept'),
(10, 'User', 'deepa@gmail.com', 'deepa123', 'Accept');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_place`
--

CREATE TABLE IF NOT EXISTS `tbl_place` (
  `place_id` int(10) NOT NULL,
  `place` varchar(50) NOT NULL,
  `district_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_place`
--

INSERT INTO `tbl_place` (`place_id`, `place`, `district_id`) VALUES
(0, 'muvattupuzha', 3);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_registration`
--

CREATE TABLE IF NOT EXISTS `tbl_registration` (
  `regid` int(10) NOT NULL AUTO_INCREMENT,
  `user_type` varchar(15) NOT NULL,
  `user_name` varchar(15) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `dob` date NOT NULL,
  `h_name` varchar(25) NOT NULL,
  `place` varchar(40) NOT NULL,
  `district` varchar(40) NOT NULL,
  `pin` int(6) NOT NULL,
  `place_id` varchar(30) NOT NULL,
  `phone_no` varchar(10) NOT NULL,
  `email_id` varchar(30) NOT NULL,
  PRIMARY KEY (`email_id`),
  UNIQUE KEY `regid` (`regid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=37 ;

--
-- Dumping data for table `tbl_registration`
--

INSERT INTO `tbl_registration` (`regid`, `user_type`, `user_name`, `gender`, `dob`, `h_name`, `place`, `district`, `pin`, `place_id`, `phone_no`, `email_id`) VALUES
(12, 'User', 'thomas', 'male', '2019-08-15', 'test', '', '', 656554, '0', '5432321234', '1@1.11'),
(24, 'Volunteer', 'Aiswarya Sabu', 'female', '1995-03-09', 'Porunnedath', '', '', 686670, '0', '8078195343', 'aiswaryasabu@gmail.com'),
(33, 'Volunteer', 'Ms Akhila PV', 'female', '1995-12-13', 'PV nilayam', 'Pattyam', 'Kannur', 665578, '', '8099232345', 'akhilpv@gmail.com'),
(8, 'Volunteer', 'Amalu', 'female', '1997-02-19', 'kallolikal', '', '', 686663, '0', '9846822921', 'amalu33@gmail.com'),
(34, 'User', 'Anila Gopi', 'female', '2000-02-21', 'Varapettil', 'Kothamangalam', 'Ernakulam', 686670, '', '9956784027', 'anilagopi212@gmail.com'),
(25, 'Volunteer', 'Anju George', 'female', '1995-02-22', 'PEPPATHIYIL HOUSE', '', '', 686670, '0', '9447606683', 'anju@gmail.com'),
(13, 'User', 'Nimmy', 'female', '2019-09-17', 'folvhg', '', '', 686670, '0', '9447606683', 'asdsd@gmail.com'),
(5, 'Volunteer', 'ash', 'female', '2001-08-28', 'ashrvad', '', '', 878787, '0', '9878675645', 'ash55@gmail.com'),
(10, 'Volunteer', 'Beema kassim', 'female', '1997-05-07', 'Mundakal', '', '', 676668, '0', '9886752345', 'beem123@gmail.com'),
(32, 'Volunteer', 'Jose Biju', 'male', '1995-06-14', 'Kalapura', '', '', 698860, 'Vazhakulam', '9766554343', 'bijujose12@gmail.com'),
(36, 'User', 'Deepa Mathew', 'female', '1998-03-12', 'Edaparambil', 'Izhuvattirutti', 'Malappuram', 665588, '', '9876987655', 'deepa@gmail.com'),
(30, 'User', 'Geetha Das', 'female', '1984-10-17', 'Geethanilayam', '', '', 667788, 'Kattanam', '9876987698', 'geethadas@gmail.com'),
(35, 'Volunteer', 'Geetha Mohan', 'female', '1992-04-23', 'Varapettil', 'Talippuzha', 'Wayanad', 345678, '', '9876987699', 'geethamohan@gmail.com'),
(7, 'Volunteer', 'amal', 'male', '2008-08-18', 'thozhuppadan', '', '', 686662, '0', '9446822921', 'mm123@gmail.com'),
(4, 'User', 'mm', 'female', '2019-08-28', 'mmmmmmmmm', '', '', 999999, '0', '9999999999', 'mm@gmail.com'),
(31, 'Volunteer', 'Nirmala Mathew', 'female', '1994-01-12', 'Chembakara', '', '', 656767, 'Kottapadi', '9789678567', 'nirmalamathew1@gmail.com'),
(16, 'Volunteer', 'Dona', 'female', '2019-09-21', 'gggggg', '', '', 232345, '0', '5678493213', 'pphy@gmail.com'),
(29, 'User', 'Reshma Raju', 'female', '1985-07-18', 'Kirshnavillasam', '', '', 689970, '0', '9177886655', 'reshmaraju@gmail.com'),
(9, 'User', 'rohan', 'male', '2003-08-13', 'mattathil', '', '', 560009, '0', '9446822921', 'rohan32@gmail.com'),
(14, 'Volunteer', 'Diana', 'female', '2019-09-21', 'gggggg', '', '', 232345, '0', '5678493213', 'safterty@gmail.com'),
(11, 'Volunteer', 'saku', 'female', '1996-09-11', 'kothayil', '', '', 685584, '0', '9895147584', 'saku@gmail.com'),
(18, 'Volunteer', 'aiswarya', 'female', '2019-09-18', 'assdfsgf', '', '', 686670, '0', '5678493213', 'sdwert@gmail.com'),
(26, 'User', 'Sruthymol M Nai', 'female', '1993-06-16', 'Sruthy mansion', '', '', 686679, '0', '8182839990', 'sruthymol@gmail.com'),
(28, 'User', 'Sruthymol M Nai', 'female', '1993-06-16', 'Sruthy mansion', '', '', 686679, '0', '8182839990', 'sruthymolmnair@gmail.com'),
(23, 'Volunteer', 'shilkka  tomy', 'female', '1992-07-17', 'ddfhgdhgfjd', '', '', 686670, '0', '9865432345', 'swered@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_resources`
--

CREATE TABLE IF NOT EXISTS `tbl_resources` (
  `res_id` int(10) NOT NULL AUTO_INCREMENT,
  `res_type` varchar(30) NOT NULL,
  `res_name` varchar(30) NOT NULL,
  `quantity` varchar(10) NOT NULL,
  `place` varchar(40) NOT NULL,
  `district` varchar(40) NOT NULL,
  `reg_id` int(10) NOT NULL,
  `usertype` varchar(30) NOT NULL,
  UNIQUE KEY `res_id` (`res_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `tbl_resources`
--

INSERT INTO `tbl_resources` (`res_id`, `res_type`, `res_name`, `quantity`, `place`, `district`, `reg_id`, `usertype`) VALUES
(1, 'Equipments', 'motor', '3', '', '', 8, 'Volunteer'),
(2, 'Vehicles', 'car', '2', '', '', 8, 'Volunteer'),
(3, 'Vehicles', 'Jeep', '1', '', '', 8, 'Volunteer'),
(4, 'Vehicles', 'boat', '3', '', '', 8, 'Volunteer'),
(5, 'Vehicles', 'Jeep', '3', '', '', 0, 'Police station'),
(6, 'Vehicles', 'Car', '4', '', '', 23, 'Volunteer'),
(7, 'Vehicles', 'Fire Engine', '4', '', '', 7, 'Fire station');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_services`
--

CREATE TABLE IF NOT EXISTS `tbl_services` (
  `emer_id` int(10) NOT NULL AUTO_INCREMENT,
  `emer_type` varchar(15) NOT NULL,
  `identification_no` varchar(10) NOT NULL,
  `name_of_head` varchar(30) NOT NULL,
  `no_of_employees` varchar(10) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `place` varchar(30) NOT NULL,
  `district` varchar(40) NOT NULL,
  PRIMARY KEY (`email`),
  UNIQUE KEY `emer_id` (`emer_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=16 ;

--
-- Dumping data for table `tbl_services`
--

INSERT INTO `tbl_services` (`emer_id`, `emer_type`, `identification_no`, `name_of_head`, `no_of_employees`, `phone`, `email`, `place`, `district`) VALUES
(9, 'Fire station', 'qwer345', 'Ms Swathy Reddy', '34', '04862225564', 'firesd@gmail.com', 'Rajakkad', 'Idukki'),
(2, 'Fire Station', '9090909', 'Mr Paul Mathew', '15', '04862211345', 'firestation123@gmail.com', 'Vazhakulam', ''),
(7, 'Fire station', 'kfs333', 'Mr James Jacob', '34', '04862211678', 'firestation333@gmail.com', 'Eriyad', ''),
(15, 'Fire station', 'firestn334', 'Mr Tomy Chacko', '09', '04562256578', 'firestation334455@gmail.com', 'Chankaramkulam', 'Malappuram'),
(8, 'Fire station', 'kfs990', 'Mr Jacob Varkey', '15', '04863876799', 'firestn990@gmail.com', 'Udumanthala', ''),
(11, 'Fire station', 'kfirestnid', 'Mr. Abin Joy', '15', '04845299675', 'kfirestnidukki@gmail.com', 'Todupuzha', 'Idukki'),
(14, 'Police station', 'policekera', 'Mr Raju Jose', '12', '04864234546', 'police10234@gmail.com', 'Nelleti', 'Kollam'),
(1, 'Police Station', '9999', 'Mr Prakash Menon', '23', '04862232321', 'police102@gmail.com', 'Vazhakulam', ''),
(6, 'Police station', 'kps112', 'Mr Joseph Vadakkan', '20', '04567234562', 'police112@gmail.com', 'Anjukunnu', ''),
(5, 'Police station', 'kps212', 'Mr Adithyan Menon IPS', '23', '04865211345', 'police212@gmail.com', 'Vellapara', ''),
(10, 'Police station', 'kpolicektm', 'Mr. Jacob George', '13', '04864234546', 'policestnktmerumeli@gmail.com', 'Erumeli', 'Kottayam'),
(12, 'Police station', 'kpolice100', 'Mr Raju Jose', '12', '45679876543', 'swered@gmail.com', 'Olipara', 'Palakkad');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_shelter`
--

CREATE TABLE IF NOT EXISTS `tbl_shelter` (
  `shelter_id` int(10) NOT NULL AUTO_INCREMENT,
  `shelter_type` varchar(25) NOT NULL,
  `shel_name` varchar(60) NOT NULL,
  `people_accomodation` int(10) NOT NULL,
  `facilities` varchar(25) NOT NULL,
  `place` varchar(40) NOT NULL,
  `district` varchar(40) NOT NULL,
  `reg_id` int(10) NOT NULL,
  `usertype` varchar(15) NOT NULL,
  UNIQUE KEY `shelter_id` (`shelter_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `tbl_shelter`
--

INSERT INTO `tbl_shelter` (`shelter_id`, `shelter_type`, `shel_name`, `people_accomodation`, `facilities`, `place`, `district`, `reg_id`, `usertype`) VALUES
(6, 'College', 'Nirmala College', 123, 'Beds', '', '', 0, '8'),
(7, 'Auditoriums', 'Municipal Auditorium', 123, 'Rooms', 'Mukkolla', 'Thiruvananthapuram', 0, '8'),
(8, 'College', 'Viswajyothi  College of Engine', 1000, 'Water availability', 'Vazhakulam', 'Ernakulam', 0, '23');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_state`
--

CREATE TABLE IF NOT EXISTS `tbl_state` (
  `state_id` int(10) NOT NULL AUTO_INCREMENT,
  `state_name` varchar(20) NOT NULL,
  PRIMARY KEY (`state_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tbl_state`
--

INSERT INTO `tbl_state` (`state_id`, `state_name`) VALUES
(2, 'Kerala');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_viewalert`
--

CREATE TABLE IF NOT EXISTS `tbl_viewalert` (
  `view_alertid` int(10) NOT NULL AUTO_INCREMENT,
  `reg_id` varchar(15) NOT NULL,
  `usertype` varchar(20) NOT NULL,
  UNIQUE KEY `view_alertid` (`view_alertid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=19 ;

--
-- Dumping data for table `tbl_viewalert`
--

INSERT INTO `tbl_viewalert` (`view_alertid`, `reg_id`, `usertype`) VALUES
(1, '8', 'Fire station'),
(2, '8', 'Fire station'),
(3, '23', 'Volunteer'),
(4, '23', 'Volunteer'),
(5, '23', 'Volunteer'),
(6, '23', 'Volunteer'),
(7, '1', 'Police station'),
(8, '1', 'Police station'),
(9, '1', 'Police station'),
(10, '1', 'Police station'),
(11, '1', 'Police station'),
(12, '1', 'Police station'),
(13, '1', 'Police station'),
(14, '1', 'Police station'),
(15, '1', 'Police station'),
(16, '1', 'Police station'),
(17, '23', 'Volunteer'),
(18, '23', 'Volunteer');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_volunteer`
--

CREATE TABLE IF NOT EXISTS `tbl_volunteer` (
  `reg_id` int(10) NOT NULL,
  `vol_skills` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_volunteer`
--

INSERT INTO `tbl_volunteer` (`reg_id`, `vol_skills`) VALUES
(8, 'Cleaning'),
(8, 'Communication'),
(8, 'Communication'),
(8, 'Driving'),
(8, 'Driving'),
(8, 'Driving'),
(23, 'Driving'),
(23, 'Driving'),
(23, 'Swimming');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
