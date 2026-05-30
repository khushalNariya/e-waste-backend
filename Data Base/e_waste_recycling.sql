-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 30, 2026 at 12:52 PM
-- Server version: 11.8.2-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `e_waste_recycling`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user_profile`
--

CREATE TABLE `accounts_user_profile` (
  `id` int(11) NOT NULL,
  `table_auth_user_id` int(11) NOT NULL,
  `Show_Password` varchar(300) NOT NULL,
  `mobile_number` varchar(15) DEFAULT NULL,
  `address_line_1` varchar(255) DEFAULT NULL,
  `address_line_2` varchar(255) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `pincode` varchar(10) DEFAULT NULL,
  `user_created_on` datetime DEFAULT current_timestamp(),
  `user_updated_on` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounts_user_profile`
--

INSERT INTO `accounts_user_profile` (`id`, `table_auth_user_id`, `Show_Password`, `mobile_number`, `address_line_1`, `address_line_2`, `city`, `state`, `pincode`, `user_created_on`, `user_updated_on`) VALUES
(1, 1, '123', '1234567890', 'abc', '', 'Ranchi', 'gujarat', '360370', '2026-01-18 14:06:47', '2026-05-18 12:33:15'),
(52, 52, '123', '1234567890', 'abc fadsgvklwdngklwn  fklnfkl  kqnfkln vm nmfklv  kaf kl f  kan flka v21156454  qwf68864654', '', 'Ranchi', 'gujarat', '360370', '2026-02-06 16:39:40', '2026-02-28 06:14:44'),
(53, 53, '123', '1234567890', '123', 'abc', 'Bokaro', 'gujarat', '360370', '2026-02-06 16:42:40', '2026-05-03 17:44:52'),
(54, 54, '123', '1234567890', 'abc', '', 'Jetpur Navagadh', 'gujarat', '360300', '2026-02-07 15:46:07', '2026-05-03 17:45:03'),
(55, 55, '123', '1234567890', 'abc', '', 'Jetpur Navagadh', 'gujarat', '360300', '2026-02-07 15:47:43', '2026-02-07 18:02:38'),
(56, 56, '123', '1234567890', 'abc', '', 'Ranchi', 'gujarat', '360370', '2026-02-07 15:48:43', '2026-02-07 15:48:43'),
(57, 57, '123', '1234567890', 'abc', '', 'Ranchi', 'gujarat', '360370', '2026-02-07 15:52:46', '2026-02-07 15:52:46'),
(58, 58, '123', '1234567890', 'abc', '', 'Ranchi', 'gujarat', '360370', '2026-02-07 15:57:45', '2026-02-07 15:57:45'),
(59, 59, '123', '1234567890', 'abc123', 'abc', 'jetpur', 'gujarat', '360370', '2026-02-07 15:58:23', '2026-05-18 12:33:05'),
(60, 60, 'a123', '1234567890', 'abc', '', 'ranchi', 'gujarat', '360300', '2026-02-07 15:59:23', '2026-02-07 15:59:23'),
(61, 61, 'k1234', '1234567890', 'dfhdfh', '', 'jetpur', 'gujarat', '367000', '2026-02-07 16:00:01', '2026-02-07 16:00:01'),
(62, 62, '123', '1234567890', 'abc', '', 'Ranchi', 'gujarat', '360370', '2026-02-07 16:04:21', '2026-03-15 16:45:05'),
(63, 63, '123', '1234567890', 'abc', 'abc', 'Bokaro', 'gujarat', '360300', '2026-02-07 16:05:00', '2026-02-07 17:58:27'),
(64, 64, 'k123', '1234567890', 'abc', '', 'jetpur', 'gujarat', '360300', '2026-02-07 17:59:37', '2026-02-08 05:58:35'),
(65, 65, 'a123', '1234567890', 'abc', '', 'Bokaro', 'gujarat', '360300', '2026-02-07 18:06:48', '2026-02-08 05:57:32'),
(67, 67, '456', '1234567890', 'sdbsd', '', 'rachi', 'gujarat', '367000', '2026-02-07 18:12:54', '2026-02-07 18:17:04'),
(68, 68, 'admin123', '1234567890', 'Admin Office', 'Main Building', 'Indore', 'MP', '452001', '2026-03-04 15:25:10', '1970-01-01 00:00:00'),
(69, 69, '123', '1234567890', 'sdbsd', 'abc', 'jetpur', 'gujarat', '360370', '2026-03-15 17:00:37', '1970-01-01 00:00:00'),
(70, 70, '456', '1234567890', 'dfhdfh', 'abc', 'Ranchi', 'gujarat', '360300', '2026-03-17 11:24:42', '1970-01-01 00:00:00'),
(71, 71, '123', '1234567890', 'abc', 'abc', 'ranchi', 'gujarat', '360370', '2026-03-17 11:29:14', '1970-01-01 00:00:00'),
(72, 72, '123', '1234567890', 'sdbsd', 'abc', 'Jetpur Navagadh', 'gujarat', '367000', '2026-03-17 11:45:04', '1970-01-01 00:00:00'),
(73, 73, '123', '1234567890', 'gsgh', 'abc', 'Ranchi', 'gujarat', '360300', '2026-03-17 12:01:56', '1970-01-01 00:00:00'),
(74, 74, '123', '1234567890', 'dfhdfh', 'abc', 'rachi', 'gujarat', '360370', '2026-03-17 12:02:36', '1970-01-01 00:00:00'),
(75, 75, '123', '1234567890', 'abc', 'abc', 'rachi', 'gujarat', '360300', '2026-03-17 12:03:42', '1970-01-01 00:00:00'),
(76, 76, '123456', '1234567890', 'dfhdfh', 'abc', 'Bokaro', 'gujarat', '360370', '2026-03-17 12:55:22', '1970-01-01 00:00:00'),
(78, 78, 'Admin@123', '1234567890', 'Test Address', '', 'Test City', 'Test State', '123456', '2026-04-20 10:06:00', '1970-01-01 00:00:00'),
(79, 80, 'Admin@123', '1234567890', '123 Tech Park', 'Silicon Valley', 'Test City', 'Test State', '123456', '2026-04-20 20:28:46', '1970-01-01 00:00:00'),
(80, 81, 'Test@1234', '9876543210', '123 Green Street', '', 'San Francisco', 'CA', '941020', '2026-05-22 05:53:56', '1970-01-01 00:00:00'),
(81, 82, 'Password123!', '9876543210', '123 Main Street', '', 'Mumbai', 'Maharashtra', '400001', '2026-05-22 13:26:20', '1970-01-01 00:00:00'),
(82, 83, 'Password123', '9876543210', '123 Main Street', 'Apt 4B', 'Mumbai', 'Maharashtra', '400001', '2026-05-25 11:31:02', '1970-01-01 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `app_1_users_user`
--

CREATE TABLE `app_1_users_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `username` varchar(150) DEFAULT NULL,
  `user_type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `app_1_users_user_groups`
--

CREATE TABLE `app_1_users_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `app_1_users_user_user_permissions`
--

CREATE TABLE `app_1_users_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `app_2_e_facility_user`
--

CREATE TABLE `app_2_e_facility_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `username` varchar(150) DEFAULT NULL,
  `user_type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `app_2_e_facility_user_groups`
--

CREATE TABLE `app_2_e_facility_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `app_2_e_facility_user_user_permissions`
--

CREATE TABLE `app_2_e_facility_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add user', 7, 'add_user'),
(26, 'Can change user', 7, 'change_user'),
(27, 'Can delete user', 7, 'delete_user'),
(28, 'Can view user', 7, 'view_user'),
(29, 'Can add sign_up', 8, 'add_sign_up'),
(30, 'Can change sign_up', 8, 'change_sign_up'),
(31, 'Can delete sign_up', 8, 'delete_sign_up'),
(32, 'Can view sign_up', 8, 'view_sign_up'),
(33, 'Can add sign_up_model', 9, 'add_sign_up_model'),
(34, 'Can change sign_up_model', 9, 'change_sign_up_model'),
(35, 'Can delete sign_up_model', 9, 'delete_sign_up_model'),
(36, 'Can view sign_up_model', 9, 'view_sign_up_model'),
(37, 'Can add user_model', 10, 'add_user_model'),
(38, 'Can change user_model', 10, 'change_user_model'),
(39, 'Can delete user_model', 10, 'delete_user_model'),
(40, 'Can view user_model', 10, 'view_user_model'),
(41, 'Can add user profile', 11, 'add_userprofile'),
(42, 'Can change user profile', 11, 'change_userprofile'),
(43, 'Can delete user profile', 11, 'delete_userprofile'),
(44, 'Can view user profile', 11, 'view_userprofile'),
(45, 'Can add facility', 12, 'add_facility'),
(46, 'Can change facility', 12, 'change_facility'),
(47, 'Can delete facility', 12, 'delete_facility'),
(48, 'Can view facility', 12, 'view_facility'),
(49, 'Can add user submission', 13, 'add_usersubmission'),
(50, 'Can change user submission', 13, 'change_usersubmission'),
(51, 'Can delete user submission', 13, 'delete_usersubmission'),
(52, 'Can view user submission', 13, 'view_usersubmission'),
(53, 'Can add brand', 14, 'add_brand'),
(54, 'Can change brand', 14, 'change_brand'),
(55, 'Can delete brand', 14, 'delete_brand'),
(56, 'Can view brand', 14, 'view_brand'),
(57, 'Can add recycle category', 15, 'add_recyclecategory'),
(58, 'Can change recycle category', 15, 'change_recyclecategory'),
(59, 'Can delete recycle category', 15, 'delete_recyclecategory'),
(60, 'Can view recycle category', 15, 'view_recyclecategory');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$1000000$PNghYMvIie1Xafju12g9pD$+TzeFv+R1cv7LKy2LLIYYRqFPABacP+1GmXdO475wN4=', '2026-05-22 18:49:59.629669', 1, 'user1', 'KHUSHAL', 'nariya', 'khushalnariya912@gmail.com', 1, 1, '2026-01-18 14:06:46.303888'),
(52, 'pbkdf2_sha256$1000000$Oz6bM1VcDbovsMJnsefTKE$+Sqceim39CdGbK4Jp4NRld6Ybpy43RTpIIWbfe/fEt8=', '2026-03-23 16:04:38.176464', 1, 'user2', 'KHUSHAL-1', 'nariya', 'abc@gmail.com', 1, 1, '2026-02-06 16:39:40.144785'),
(53, 'pbkdf2_sha256$1000000$QSHOUBoQdtIGRrIIJB2Z2v$3Ves6ZD4W/jCk4O+w0BbC6cQEsWuFXgPDRZY3pcu2As=', NULL, 0, 'user53', 'KHUSHAL', 'nariya - 2', 'abc2@gmail.com', 0, 1, '2026-02-06 16:42:40.104138'),
(54, 'pbkdf2_sha256$1000000$laPkYqQed6kEyFqAeHfuAq$vM3ZipK8as/SNREcpH3B/Ob+wNmtOZuqf3uhQ3L+v50=', '2026-05-20 16:21:00.123664', 0, 'user54', 'Khushal', 'Nariya - 3', 'abc3@gmail.com', 0, 1, '2026-02-07 15:46:06.586921'),
(55, 'pbkdf2_sha256$1000000$s54zhVo4DCnPAY48somhbp$XTppJGHaLVVcS8hV+UNY+b4057zSpzptCw8cFBbIa9Q=', NULL, 0, 'user55', 'Khushal', 'Nariya', 'abc4@gmail.com', 0, 1, '2026-02-07 15:47:42.909507'),
(56, 'pbkdf2_sha256$1000000$vSIVgKlc8M1dE7nvZ8wXBq$xKsWN42yEs9qCw1YJiNZwXsqvRFiEtLnGLqc/4SfmOE=', NULL, 0, 'user56', 'Khushal', 'Nariya', 'abc5@gmail.com', 0, 1, '2026-02-07 15:48:42.360685'),
(57, 'pbkdf2_sha256$1000000$WaOLhrdBWVEwEKxhveh0KC$JZRp99q1wm+7wdP1vIqyta6stP7LM929HRDTV7xfIpQ=', NULL, 0, 'user57', 'KHUSHAL', 'nariya', 'abc6@gmail.com', 0, 1, '2026-02-07 15:52:45.222739'),
(58, 'pbkdf2_sha256$1000000$kEWse5bEdFnSamz4uABWgt$Le54L5MmZ4oYIeh2MBteohIVc+/YvrP6B095Tx2g3uk=', NULL, 0, 'user58', 'Khushal', 'Nariya', 'abc7@gmail.com', 0, 1, '2026-02-07 15:57:45.166413'),
(59, 'pbkdf2_sha256$1000000$Z11caKfgi8zPWcBX0fCrQy$sH3eRNuVZrRvU5wl3GnZ/Uxia7/uc50yjT726yAsj9I=', NULL, 0, 'user59', 'Khushal', 'Nariya', 'khushalnariya12@gmail.com', 0, 1, '2026-02-07 15:58:22.309108'),
(60, 'pbkdf2_sha256$1000000$T7VThJzVA9qw1oF6ZRCYsq$eXdTLxd31L1ld/lKHEN3MKA/MhrLl47K1WTuL8Tdmyc=', NULL, 0, 'user60', 'Khushal', 'Nariya', 'abc8@gmail.com', 0, 1, '2026-02-07 15:59:22.444682'),
(61, 'pbkdf2_sha256$1000000$0L3HquUF0jq5CdSBt2WzWQ$q1knp4VFoTbZsZE+34wQP29zUqHRdX+Lp9F9UV8hmyo=', NULL, 0, 'user61', 'Khushal', 'Nariya', 'abc9@gmail.com', 0, 1, '2026-02-07 16:00:00.459114'),
(62, 'pbkdf2_sha256$1000000$n2dqChx55e6n0flNeFdbgP$KL6YoeziMzO9n9RXUmdZwNrQZdRfrHPAci7ramSGImw=', NULL, 0, 'user62', 'KHUSHAL-10', 'nariya', 'abc10@gmail.com', 0, 0, '2026-02-07 16:04:20.399304'),
(63, 'pbkdf2_sha256$1000000$GMJ01wvqyWUxuj122hHn5V$IEFpdFOgdj1ey+W6futhNXibYxN3SRf9GDHUahGT6CQ=', NULL, 0, 'user63', 'Khushal', 'Nariya', 'abc13@gmail.com', 0, 1, '2026-02-07 16:04:59.303868'),
(64, 'pbkdf2_sha256$1000000$8Iel7Hv22d76JEAthcI12C$C6H9KzpITF0i3PiS+tWxApFjZ4L7qBZBWQNd/GzC3aA=', NULL, 0, 'user64', 'Khushal', 'Nariya', 'abc11@gmail.com', 0, 1, '2026-02-07 17:59:36.458922'),
(65, 'pbkdf2_sha256$1000000$2dtJ6YbYrc1V6zyHPm3Z6S$mXkhS4SQlbarPe0rvb6i1Ux3611i++1Q7PK5K/0zFCw=', NULL, 0, 'user65', 'Khushal', 'Nariya', 'abc12@gmail.com', 0, 1, '2026-02-07 18:06:47.842454'),
(67, 'pbkdf2_sha256$1000000$4sADeKoeawqOLaxAz2qEDg$Ra+65zp+NyK0XG42BUwwhz/51Xr2z13L/Qax3ZZ6ZBg=', NULL, 1, 'user67', 'Khushal', 'Nariya', 'abc15@gmail.com', 1, 1, '2026-02-07 18:12:53.314554'),
(68, 'pbkdf2_sha256$1000000$08eWd3Y0vS7st7wI1mDQNL$blACmiHFkeM7u83QcMYvz7ZPdiFdbqnPN1YorFp3bk8=', NULL, 0, 'user68', 'Admin', 'User', 'admin@ewaste.com', 0, 1, '2026-03-04 15:25:08.780107'),
(69, 'pbkdf2_sha256$1000000$gn2JZTsCHzR0BhkUlaaMfk$x1dO6FMvPf4kUPiTe7P7Qml5qHgNADKtv2S/zQKdt1s=', NULL, 0, 'user69', 'Khushal', 'Nariya', 'khushalnariya@gmail.com', 0, 1, '2026-03-15 17:00:36.245179'),
(70, 'pbkdf2_sha256$1000000$H142XReg8cres3WrQiXSHZ$aX6vCrk0x+P/Vffqex2JZjdov1PWwlzBVN5pHTWdfoM=', NULL, 0, 'user70', 'Khushal', 'Nariya', 'khushalnariya912222@gmail.com', 0, 1, '2026-03-17 11:24:40.875653'),
(71, 'pbkdf2_sha256$1000000$G05CvrCqkEg3WTHAXPiz7b$TcdOrugA/T1pgJe3scD2N6e6hF7iUU4LsBFwp97QWi4=', NULL, 0, 'user71', 'Khushal', 'Nariya', 'khushalnariya912a@gmail.com', 0, 1, '2026-03-17 11:29:13.496758'),
(72, 'pbkdf2_sha256$1000000$Wz1FXgUvFSi1FNYlqeO1lM$xhuGSbXFZJFgDpfQoUH+I/HmqBdmylaM/2+4lYQvya8=', NULL, 0, 'user72', 'Khushal', 'Nariya', 'khushalnariya912q@gmail.com', 0, 1, '2026-03-17 11:45:03.516750'),
(73, 'pbkdf2_sha256$1000000$VZpPufpVICTbqj2eoptyBg$RgjBXVr3yq0w4zll2Um4o2GcYn0xHVDQCZhpTzNo9Js=', NULL, 1, 'user73', 'Khushal', 'Nariya', 'khushalnariya912k@gmail.com', 1, 1, '2026-03-17 12:01:55.873842'),
(74, 'pbkdf2_sha256$1000000$snevL16DaLsWFZobSxEWXa$hu2UaS+2TG3shqdA9q50ot6fV5e5QcyY7ciqgTCQdY4=', NULL, 0, 'user74', 'Khushal', 'Nariya', 'khushalnariya9121@gmail.com', 0, 1, '2026-03-17 12:02:36.120154'),
(75, 'pbkdf2_sha256$1000000$1UMZx9qZZ3YLLtgqTpNRGA$bPKMxHJvHbiWI2wbwbNDYikGR1oIgaK+qzMfHrZUzMU=', NULL, 0, 'user75', 'Khushal', 'Nariya', 'khushalnariya91211@gmail.com', 0, 1, '2026-03-17 12:03:41.731872'),
(76, 'pbkdf2_sha256$1000000$jlgkWMUnCJKBbp3KmXjZXM$NcseTDYcXp9w/fUHCchadTgIkRvSXo5FslshFPGy9Zc=', NULL, 0, 'user76', 'Khushal', 'Nariya', 'khushalnariya912111@gmail.com', 0, 1, '2026-03-17 12:55:21.038092'),
(78, 'pbkdf2_sha256$1000000$nhEtCryDuVwzNHpWeBMOC3$Pqq6dC06b/4b1wuwsVuyLw0nAkg6r5WrKQMPiM9w38Q=', NULL, 1, 'user77', 'Admin', 'User', 'admin@test.com', 1, 1, '2026-04-20 10:05:58.764814'),
(80, 'pbkdf2_sha256$1000000$Jqc3FGVI5TumbndVWuXLiw$ZbKmYB4LdtHcEP6vIbTcDtKmzuA6rCPNc//iaQol6bs=', NULL, 1, 'user79', 'Antigravity', 'Admin', 'antigravity_admin@ewaste.com', 1, 1, '2026-04-20 20:28:45.217010'),
(81, 'pbkdf2_sha256$1000000$88ammBpPv3VdvEeHFXZN5i$IQ5J/5AIRFv0jp6t1m5JEzyHfcvOkwnG8qFH7gZ89Sg=', NULL, 0, 'user81', 'Jane', 'Doe', 'testuser_replaces_123@example.com', 0, 1, '2026-05-22 05:53:55.657608'),
(82, 'pbkdf2_sha256$1000000$jNbcfNij2WZdakypM2ukVs$6tEGct1G/vZ+J904F0ZZpZM5sFBm2a6W3c3QgDCD1Zo=', NULL, 0, 'user82', 'Test', 'User', 'testuser@gmail.com', 0, 1, '2026-05-22 13:26:19.348626'),
(83, 'pbkdf2_sha256$1000000$9I7g6F505Tt08OVLAcqc9v$rfnzjyiu9LyZ2dmTjoNI4qztKlXFcEhlFb9bjcmCfOQ=', NULL, 0, 'user83', 'John', 'Doe', 'johndoe@gmail.com', 0, 1, '2026-05-25 11:31:01.001881');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `brand`
--

CREATE TABLE `brand` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `brand`
--

INSERT INTO `brand` (`id`, `name`, `created_at`, `updated_at`) VALUES
(1, 'Apple', '2026-03-23 16:05:09', '2026-03-25 07:07:12'),
(2, 'SAMSUNG', '2026-03-23 16:05:24', '2026-03-23 16:05:24'),
(3, 'LG', '2026-03-23 16:05:40', '2026-03-23 16:05:40'),
(4, 'Xiaomi', '2026-03-23 16:07:40', '2026-03-23 16:07:40'),
(5, 'Google Pixel', '2026-03-23 16:13:07', '2026-03-23 16:13:07'),
(6, 'Realme', '2026-03-23 16:13:31', '2026-03-23 16:13:31'),
(7, 'OnePlus', '2026-03-23 16:13:39', '2026-03-23 16:13:39'),
(8, 'Oppo', '2026-03-23 16:13:48', '2026-03-23 16:13:48'),
(9, 'Vivo', '2026-03-23 16:13:55', '2026-03-23 16:13:55'),
(10, 'Motorola', '2026-03-23 16:14:01', '2026-03-23 16:14:01'),
(11, 'Nokia', '2026-03-23 16:14:10', '2026-03-25 07:07:50'),
(18, 'Lenovo', '2026-04-06 10:13:55', '2026-04-06 10:13:55'),
(19, 'Dell', '2026-04-06 10:13:55', '2026-04-06 10:13:55'),
(20, 'HP', '2026-04-06 10:13:55', '2026-04-06 10:13:55'),
(21, 'Asus', '2026-04-06 10:13:55', '2026-04-06 10:13:55'),
(22, 'Whirlpool', '2026-04-06 10:13:55', '2026-04-06 10:13:55'),
(23, 'Sony', '2026-04-06 10:13:55', '2026-04-06 10:13:55'),
(24, 'Panasonic', '2026-04-06 10:13:55', '2026-04-06 10:13:55'),
(25, 'Exide', '2026-04-06 10:13:55', '2026-04-06 10:13:55'),
(26, 'Amaron', '2026-04-06 10:13:55', '2026-04-06 10:13:55'),
(27, 'Canon', '2026-04-06 10:13:55', '2026-04-06 10:13:55'),
(28, 'Nikon', '2026-04-06 10:13:55', '2026-04-06 10:13:55');

-- --------------------------------------------------------

--
-- Table structure for table `category_brand_mapping`
--

CREATE TABLE `category_brand_mapping` (
  `id` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `brand_id` int(11) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category_brand_mapping`
--

INSERT INTO `category_brand_mapping` (`id`, `category_id`, `brand_id`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 1, 1, 1, '2026-03-23 16:44:06', '2026-04-05 17:00:46'),
(2, 1, 7, 1, '2026-03-23 17:24:20', '2026-04-05 16:59:26'),
(3, 1, 6, 1, '2026-03-23 17:33:17', '2026-04-06 09:21:54'),
(4, 1, 4, 1, '2026-03-23 17:38:54', '2026-03-23 17:38:54'),
(5, 1, 2, 1, '2026-03-23 18:00:46', '2026-03-31 06:39:46'),
(6, 1, 5, 1, '2026-03-23 18:01:13', '2026-03-30 07:16:21'),
(7, 1, 3, 1, '2026-03-29 17:53:17', '2026-04-05 17:25:49'),
(8, 1, 8, 1, '2026-04-04 19:08:34', '2026-04-05 16:59:58'),
(9, 1, 9, 1, '2026-04-05 17:00:09', '2026-04-05 17:00:09'),
(10, 1, 10, 1, '2026-04-05 17:00:16', '2026-04-05 17:00:16'),
(11, 1, 11, 1, '2026-04-05 17:00:22', '2026-04-05 17:27:35'),
(12, 2, 1, 1, '2026-04-06 04:46:35', '2026-04-06 04:46:35'),
(13, 2, 18, 1, '2026-04-06 04:46:53', '2026-04-06 04:46:53'),
(14, 2, 19, 1, '2026-04-06 04:46:59', '2026-04-06 04:46:59'),
(15, 2, 20, 1, '2026-04-06 04:47:09', '2026-04-06 04:47:09'),
(16, 2, 21, 1, '2026-04-06 04:47:33', '2026-04-06 04:47:33'),
(17, 3, 22, 1, '2026-04-06 04:55:06', '2026-04-06 04:55:06'),
(18, 3, 2, 1, '2026-04-06 04:55:15', '2026-04-06 04:55:15'),
(19, 3, 3, 1, '2026-04-06 04:55:25', '2026-04-06 04:55:25'),
(20, 3, 24, 1, '2026-04-06 04:55:46', '2026-04-06 04:55:46'),
(21, 4, 23, 1, '2026-04-06 04:56:43', '2026-04-06 04:56:43'),
(22, 4, 24, 1, '2026-04-06 04:56:50', '2026-04-06 04:56:50'),
(23, 4, 3, 1, '2026-04-06 04:57:05', '2026-04-06 04:57:05'),
(24, 4, 2, 1, '2026-04-06 04:57:23', '2026-04-06 04:58:28'),
(25, 5, 25, 1, '2026-04-06 04:58:57', '2026-04-06 04:58:57'),
(26, 5, 26, 1, '2026-04-06 04:59:06', '2026-04-06 04:59:06'),
(27, 6, 27, 1, '2026-04-06 04:59:28', '2026-04-06 04:59:28'),
(28, 6, 28, 1, '2026-04-06 04:59:38', '2026-04-06 04:59:38');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(8, 'app_1_users', 'sign_up'),
(9, 'app_1_users', 'sign_up_model'),
(7, 'app_1_users', 'user'),
(11, 'app_1_users', 'userprofile'),
(10, 'app_1_users', 'user_model'),
(12, 'app_2_e_Facility', 'facility'),
(14, 'app_6_E_Waste_Submission', 'brand'),
(15, 'app_6_E_Waste_Submission', 'recyclecategory'),
(13, 'app_6_E_Waste_Submission', 'usersubmission'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-01-18 10:22:18.962314'),
(2, 'auth', '0001_initial', '2026-01-18 10:22:24.899444'),
(3, 'admin', '0001_initial', '2026-01-18 10:22:25.746934'),
(4, 'admin', '0002_logentry_remove_auto_add', '2026-01-18 10:22:25.759039'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2026-01-18 10:22:25.890880'),
(6, 'contenttypes', '0002_remove_content_type_name', '2026-01-18 10:22:26.517480'),
(7, 'auth', '0002_alter_permission_name_max_length', '2026-01-18 10:22:27.164106'),
(8, 'auth', '0003_alter_user_email_max_length', '2026-01-18 10:22:27.867203'),
(9, 'auth', '0004_alter_user_username_opts', '2026-01-18 10:22:27.904685'),
(10, 'auth', '0005_alter_user_last_login_null', '2026-01-18 10:22:28.751043'),
(11, 'auth', '0006_require_contenttypes_0002', '2026-01-18 10:22:28.784380'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2026-01-18 10:22:28.818215'),
(13, 'auth', '0008_alter_user_username_max_length', '2026-01-18 10:22:29.226461'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2026-01-18 10:22:29.593425'),
(15, 'auth', '0010_alter_group_name_max_length', '2026-01-18 10:22:29.856747'),
(16, 'auth', '0011_update_proxy_permissions', '2026-01-18 10:22:29.868995'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2026-01-18 10:22:30.168436'),
(18, 'app_1_users', '0001_initial', '2026-01-18 10:22:33.133020'),
(19, 'app_1_users', '0002_sign_up_sign_up_model_user_model_userprofile_and_more', '2026-01-18 10:22:33.148951'),
(20, 'sessions', '0001_initial', '2026-01-18 10:22:33.691671'),
(21, 'app_2_e_Facility', '0001_initial', '2026-03-22 11:50:37.962063'),
(22, 'app_2_e_Facility', '0002_sign_up_sign_up_model_user_model_userprofile_and_more', '2026-03-22 11:50:38.041169'),
(23, 'app_2_e_Facility', '0003_facility_submission_dependencies', '2026-03-22 11:50:38.075208'),
(24, 'app_6_E_Waste_Submission', '0001_initial', '2026-03-22 11:51:43.535141'),
(25, 'app_10_E_Waste_Submissions', '0001_initial', '2026-04-20 09:54:57.186008');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0y6y2tkt9s6ibxqlutf6varlvyvu9mcg', '.eJxVjEEOwiAQRe_C2hAGSiku3fcMZDozlaqhSWlXxrsbki50-997_60SHntOR5UtLayuCtTld5uQnlIa4AeW-6ppLfu2TLop-qRVjyvL63a6fwcZa261Q3AezCwUTQhhQjs7tjMN0vcwcDQk0lHH3nmCAboYiH0LIPpgWX2-5uA3pQ:1wDME7:1CscW0bl0f24_lvMDTVuMuVu1vVtyY4ynDXO1T7oWns', '2026-04-30 12:53:47.188715'),
('2g0wvb90t1vbkf4u0g0mezf9vhl2jj9w', '.eJxVjDsOwjAQBe_iGlkx2TVeSnrOYD1_ggPIkeKkQtwdIqWA9s3MeymPdSl-bXn2Y1JnxaQOv2NAfOS6kXRHvU06TnWZx6A3Re-06euU8vOyu38HBa18axgSQeTkHJG14gBGwqkfHCN0FJnFUEgCFrEhm2OHHHsOJjLxIOr9AQjMOBY:1wPjZA:0zLhzt1aef-RcQR3Z-nYvRQmjv3hbK0E8aLL4PGjPVQ', '2026-06-03 16:14:40.192783'),
('5did6o5zeksq7zqo4j1frvd5mdsv81bj', '.eJxVjEEOwiAQRe_C2hAGSiku3fcMZDozlaqhSWlXxrsbki50-997_60SHntOR5UtLayuCtTld5uQnlIa4AeW-6ppLfu2TLop-qRVjyvL63a6fwcZa261Q3AezCwUTQhhQjs7tjMN0vcwcDQk0lHH3nmCAboYiH0LIPpgWX2-5uA3pQ:1wL4U3:D8wLHDrW_l7Lsq_qyVzrWArxgZANDo88sjLprBYTQNg', '2026-05-21 19:34:07.613059'),
('awfqqr8j0u0s9c64wmwubmucgob59bxu', '.eJxVjEEOwiAQRe_C2hAGSiku3fcMZDozlaqhSWlXxrsbki50-997_60SHntOR5UtLayuCtTld5uQnlIa4AeW-6ppLfu2TLop-qRVjyvL63a6fwcZa261Q3AezCwUTQhhQjs7tjMN0vcwcDQk0lHH3nmCAboYiH0LIPpgWX2-5uA3pQ:1w9Qh7:V_ODDdCvi6MQoSQ540HZihy4ThMgu7qZtkiZ7xNJN8Q', '2026-04-19 16:51:29.307399'),
('azj6bc6h6395of0sb1vpx6jha9bcla6k', '.eJxVjEEOwiAQRe_C2hAGSiku3fcMZDozlaqhSWlXxrsbki50-997_60SHntOR5UtLayuCtTld5uQnlIa4AeW-6ppLfu2TLop-qRVjyvL63a6fwcZa261Q3AezCwUTQhhQjs7tjMN0vcwcDQk0lHH3nmCAboYiH0LIPpgWX2-5uA3pQ:1w6lof:kTI4UhHY96Mew5ZRgx6j_C3GCoV4BrmCVHkMLZWc8PU', '2026-04-12 08:48:17.924889'),
('bpgmbhjjz1htkbyr24f34i9rttp7r4b0', '.eJxVjEEOwiAQRe_C2hAGSiku3fcMZDozlaqhSWlXxrsbki50-997_60SHntOR5UtLayuCtTld5uQnlIa4AeW-6ppLfu2TLop-qRVjyvL63a6fwcZa261Q3AezCwUTQhhQjs7tjMN0vcwcDQk0lHH3nmCAboYiH0LIPpgWX2-5uA3pQ:1w4hlr:t5zn4LmCkyCYdQOG2IDXYjhN1C4QpZVCmsRZ6y_jTwg', '2026-04-06 16:04:51.498525'),
('dabjtyz27tsb5opgmcb5vtrmh8p3ugdb', '.eJxVjDsOwjAQBe_iGlkx2TVeSnrOYD1_ggPIkeKkQtwdIqWA9s3MeymPdSl-bXn2Y1JnxaQOv2NAfOS6kXRHvU06TnWZx6A3Re-06euU8vOyu38HBa18axgSQeTkHJG14gBGwqkfHCN0FJnFUEgCFrEhm2OHHHsOJjLxIOr9AQjMOBY:1wPjfI:1ZW3HQMdZcezVgyqhWh1aIDhatBV0g62_TBZZo2EmCo', '2026-06-03 16:21:00.131948'),
('dm96lkzdqrhkoax7jfm699u6memnyr4o', '.eJxVjEEOwiAQRe_C2hAGSiku3fcMZDozlaqhSWlXxrsbki50-997_60SHntOR5UtLayuCtTld5uQnlIa4AeW-6ppLfu2TLop-qRVjyvL63a6fwcZa261Q3AezCwUTQhhQjs7tjMN0vcwcDQk0lHH3nmCAboYiH0LIPpgWX2-5uA3pQ:1w7rar:XEnFnWJksI5Ixe4fOsD1NRxVt-MuNFanTdNkJ_615M8', '2026-04-15 09:10:33.945402'),
('j5lswyk56bmaxodzq5kuvvn76d1u0xsk', '.eJxVjEEOwiAQAP_C2RBggVKP3vsGAuwiVQNJaU_GvxuSHvQ6M5k38-HYiz86bX5FdmWSXX5ZDOlJdQh8hHpvPLW6b2vkI-Gn7XxpSK_b2f4NSuhlbG0Gq7VDgonIQNDGSEySZhvnTEEkiFliTgoQIEohTJycMEAKknKZfb7oHDf0:1wQPV7:-i4-JQkfOmre2k_hXVk_3qKLQdtH1HVvn-EXTAi2tZU', '2026-06-05 13:01:17.673142'),
('oci47glnci9fzbosyajjwqp0ishgr091', '.eJxVjEEOwiAQRe_C2hAGSiku3fcMZDozlaqhSWlXxrsbki50-997_60SHntOR5UtLayuCtTld5uQnlIa4AeW-6ppLfu2TLop-qRVjyvL63a6fwcZa261Q3AezCwUTQhhQjs7tjMN0vcwcDQk0lHH3nmCAboYiH0LIPpgWX2-5uA3pQ:1wIWEJ:9TdrbhOf_BgyLjm5WzQugeh1Y6FmmicYBW5oQLX9UDI', '2026-05-14 18:35:19.104515'),
('w4wh8x8ak72nf05m42xuk02e36lsoim0', '.eJxVjEEOwiAQRe_C2hAGSiku3fcMZDozlaqhSWlXxrsbki50-997_60SHntOR5UtLayuCtTld5uQnlIa4AeW-6ppLfu2TLop-qRVjyvL63a6fwcZa261Q3AezCwUTQhhQjs7tjMN0vcwcDQk0lHH3nmCAboYiH0LIPpgWX2-5uA3pQ:1vxTVb:gzCzZ_OSLAmN5QULqNrZlZui-RabGFez7xJDzXXpW64', '2026-03-17 17:26:11.601921'),
('wq3llct91m33kg3fuobw7b2948e1o54o', '.eJxVjDsOwjAQBe_iGlkx2TVeSnrOYD1_ggPIkeKkQtwdIqWA9s3MeymPdSl-bXn2Y1JnxaQOv2NAfOS6kXRHvU06TnWZx6A3Re-06euU8vOyu38HBa18axgSQeTkHJG14gBGwqkfHCN0FJnFUEgCFrEhm2OHHHsOJjLxIOr9AQjMOBY:1wPjZu:o6tkRa4lIvJvdAQJkZZjdJsuAIgEt5mEy_GMz-7qCmg', '2026-06-03 16:15:26.943201'),
('z6goam3lwczry13ebusnzi8wxrufyuwr', '.eJxVjEEOwiAQAP_C2RBggVKP3vsGAuwiVQNJaU_GvxuSHvQ6M5k38-HYiz86bX5FdmWSXX5ZDOlJdQh8hHpvPLW6b2vkI-Gn7XxpSK_b2f4NSuhlbG0Gq7VDgonIQNDGSEySZhvnTEEkiFliTgoQIEohTJycMEAKknKZfb7oHDf0:1wQUwZ:RyLR7pPsGcrbLZECgXzQhYIxSnsAs352I7DARaQVJCg', '2026-06-05 18:49:59.688637');

-- --------------------------------------------------------

--
-- Table structure for table `education_article`
--

CREATE TABLE `education_article` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `image` varchar(500) NOT NULL,
  `category` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `readTime` varchar(20) DEFAULT NULL,
  `isFeatured` tinyint(1) DEFAULT 0,
  `Education_Create_at` datetime NOT NULL DEFAULT current_timestamp(),
  `Education_Update_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `education_article`
--

INSERT INTO `education_article` (`id`, `title`, `slug`, `description`, `image`, `category`, `author`, `date`, `readTime`, `isFeatured`, `Education_Create_at`, `Education_Update_at`) VALUES
(1, 'The Growing E-Waste Crisis', 'the-growing-e-waste-crisis', 'The rapid pace of technological advancement has transformed modern life, but it comes with a hidden cost.', 'app_4_Education/education_images/download_xN2sbHK_59NNfJV.jpg', 'Education', 'ELocate Research Team', '2025-06-12', '8 min read', 0, '2026-02-15 19:20:13', '2026-03-04 11:50:37'),
(2, 'Lifecycle of Electronic Devices', 'lifecycle-of-electronic-devices', 'Journey through the complete lifecycle of electronics from manufacturing to disposal.', 'app_4_Education/education_images/images_3_UxV1ZAv.jpg', 'Sustainability', 'Dr. Sarah Chen', '2025-07-05', '10 min read', 0, '2026-02-15 19:20:13', '2026-04-12 18:13:58'),
(3, 'Responsible E-Waste Disposal Methods', 'responsible-e-waste-disposal-methods', 'Discover the proper ways to dispose of your electronic waste safely.', 'app_4_Education/education_images/process-recycle-1536x640-1_pAsmphT.webp', 'Guide', 'Green Earth NGO', '2025-08-01', '6 min read', 1, '2026-02-15 19:20:13', '2026-03-04 11:49:57'),
(4, 'Health Risks of Improper E-Waste Handling', 'health-risks-of-improper-e-waste-handling', 'Improper disposal of electronics can lead to serious health hazards.', 'app_4_Education/education_images/images_2_AZliBHF.jpg', 'Health', 'WHO Research Team', '2025-07-20', '7 min read', 1, '2026-02-15 19:20:13', '2026-03-07 14:15:02'),
(5, 'Global Impact of E-Waste Pollution', 'global-impact-of-e-waste-pollution', 'Electronic waste is one of the fastest growing waste streams globally.', 'app_4_Education/education_images/images_1_Gvg7pey.jpg', 'Global Issues', 'UN Environment', '2025-09-10', '9 min read', 0, '2026-02-15 19:20:13', '2026-03-04 11:48:22'),
(11, 'E-Wast Solution', 'e-wast-collect', 'abc', 'app_4_Education/education_images/images.jpg', 'New', 'e-wast', '2025-11-14', '5', 0, '2026-02-15 19:20:13', '2026-03-27 13:50:01'),
(12, 'E-Waste Management Awareness', 'e-waste-management-awareness', 'Learn how to recycle electronic waste safely and protect environment.', 'app_4_Education/education_images/668c40c7ae0d948899914cde_051224_GPcrOkd.1.jpg', 'Environment', 'Khushal Nariya', '2026-02-14', '5', 1, '2026-02-15 19:20:13', '2026-04-12 18:13:43'),
(15, 'Responsible E-Waste Disposal Methods', 'responsible-e-waste-disposal-methods-1', 'E-waste consists of discarded electronic products such as computers, televisions, smartphones, and household appliances. These devices contain valuable materials like gold, silver, copper, and platinum, but also contain hazardous substances including lead, mercury, cadmium, and brominated flame retardants.\r\n\r\n                    <p>Improper disposal of e-waste leads to serious environmental consequences. When electronics are dumped in landfills, toxic materials can leach into soil and groundwater, contaminating ecosystems and posing health risks to living organisms.</p>', 'app_4_Education/education_images/images_1_Gvg7pey_oYDhupM.jpg', 'new Topic', 'Khushal n', '2026-02-18', '5', 1, '2026-02-18 12:27:33', '2026-03-04 12:08:25');

-- --------------------------------------------------------

--
-- Table structure for table `e_waste_status_history`
--

CREATE TABLE `e_waste_status_history` (
  `id` int(11) NOT NULL,
  `submission_id` int(11) NOT NULL COMMENT 'FK to e_waste_submission.id',
  `status` varchar(50) NOT NULL COMMENT 'Status name (Requested, Picked, Evaluated, Completed)',
  `changed_by` int(11) DEFAULT NULL COMMENT 'Admin/User ID who changed status',
  `remarks` text DEFAULT NULL COMMENT 'Optional notes (e.g., damage found)',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'When status changed',
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `e_waste_status_history`
--

INSERT INTO `e_waste_status_history` (`id`, `submission_id`, `status`, `changed_by`, `remarks`, `created_at`, `updated_at`) VALUES
(90, 33, 'requested', 1, NULL, '2026-04-30 13:07:00', '2026-04-30 18:37:00'),
(103, 33, 'picked_up_dropped_off', 1, NULL, '2026-04-30 13:42:52', '2026-04-30 19:12:52'),
(104, 33, 'evaluating', 1, NULL, '2026-04-30 13:42:53', '2026-04-30 19:12:53'),
(105, 33, 'recycled', 1, NULL, '2026-04-30 13:42:54', '2026-04-30 19:12:54'),
(106, 33, 'rewarded', 1, NULL, '2026-04-30 13:42:56', '2026-04-30 19:12:56'),
(107, 34, 'requested', 53, NULL, '2026-05-03 17:19:37', '2026-05-03 22:49:37'),
(108, 34, 'picked_up_dropped_off', 1, NULL, '2026-05-03 17:35:36', '2026-05-03 23:05:36'),
(109, 34, 'evaluating', 1, NULL, '2026-05-03 17:35:59', '2026-05-03 23:05:59'),
(110, 34, 'recycled', 1, NULL, '2026-05-03 17:36:01', '2026-05-03 23:06:01'),
(111, 34, 'rewarded', 1, NULL, '2026-05-03 17:36:02', '2026-05-03 23:06:02'),
(112, 35, 'requested', 54, NULL, '2026-05-03 17:46:34', '2026-05-03 23:16:34'),
(113, 35, 'picked_up_dropped_off', 1, NULL, '2026-05-03 17:55:48', '2026-05-03 23:25:48'),
(114, 35, 'evaluating', 1, NULL, '2026-05-03 17:55:49', '2026-05-03 23:25:49'),
(115, 35, 'recycled', 1, NULL, '2026-05-03 17:55:52', '2026-05-03 23:25:52'),
(116, 35, 'rewarded', 1, NULL, '2026-05-03 17:56:04', '2026-05-03 23:26:04'),
(117, 36, 'requested', 54, NULL, '2026-05-03 18:07:49', '2026-05-03 23:37:49'),
(118, 36, 'picked_up_dropped_off', 1, NULL, '2026-05-03 18:09:06', '2026-05-03 23:39:06'),
(119, 36, 'evaluating', 1, NULL, '2026-05-03 18:09:08', '2026-05-03 23:39:08'),
(120, 36, 'recycled', 1, NULL, '2026-05-03 18:09:09', '2026-05-03 23:39:09'),
(121, 36, 'rewarded', 1, NULL, '2026-05-03 18:09:10', '2026-05-03 23:39:10'),
(122, 37, 'requested', 54, NULL, '2026-05-03 18:10:30', '2026-05-03 23:40:30'),
(123, 37, 'picked_up_dropped_off', 1, NULL, '2026-05-03 18:10:38', '2026-05-03 23:40:38'),
(124, 37, 'evaluating', 1, NULL, '2026-05-03 18:11:37', '2026-05-03 23:41:37'),
(125, 37, 'recycled', 1, NULL, '2026-05-03 18:11:38', '2026-05-03 23:41:38'),
(126, 37, 'rewarded', 1, NULL, '2026-05-03 18:11:39', '2026-05-03 23:41:39'),
(127, 38, 'requested', 54, NULL, '2026-05-04 12:35:08', '2026-05-04 18:05:08'),
(128, 38, 'picked_up_dropped_off', 1, NULL, '2026-05-04 12:35:33', '2026-05-04 18:05:33'),
(129, 38, 'evaluating', 1, NULL, '2026-05-04 12:35:34', '2026-05-04 18:05:34'),
(130, 38, 'recycled', 1, NULL, '2026-05-04 12:35:36', '2026-05-04 18:05:36'),
(131, 38, 'rewarded', 1, NULL, '2026-05-04 12:35:38', '2026-05-04 18:05:38'),
(132, 39, 'requested', 54, NULL, '2026-05-04 12:53:23', '2026-05-04 18:23:23'),
(133, 39, 'picked_up_dropped_off', 1, NULL, '2026-05-04 12:54:53', '2026-05-04 18:24:53'),
(134, 39, 'evaluating', 1, NULL, '2026-05-04 12:55:23', '2026-05-04 18:25:23'),
(135, 39, 'rejected', 1, 'Wrong Product', '2026-05-04 12:55:43', '2026-05-04 18:26:17'),
(136, 40, 'requested', 54, NULL, '2026-05-04 14:01:55', '2026-05-04 19:31:55'),
(137, 40, 'picked_up_dropped_off', 1, NULL, '2026-05-04 14:03:09', '2026-05-04 19:33:09'),
(138, 40, 'evaluating', 1, NULL, '2026-05-04 14:03:10', '2026-05-04 19:33:10'),
(139, 40, 'recycled', 1, NULL, '2026-05-04 14:03:12', '2026-05-04 19:33:12'),
(140, 40, 'rewarded', 1, NULL, '2026-05-04 14:03:15', '2026-05-04 19:33:15'),
(151, 43, 'requested', 1, NULL, '2026-05-09 19:09:13', '2026-05-10 00:39:13'),
(152, 43, 'picked_up_dropped_off', 1, NULL, '2026-05-09 19:09:23', '2026-05-10 00:39:23'),
(153, 43, 'evaluating', 1, NULL, '2026-05-09 19:09:24', '2026-05-10 00:39:24'),
(154, 43, 'recycled', 1, NULL, '2026-05-09 19:09:25', '2026-05-10 00:39:25'),
(155, 43, 'rewarded', 1, NULL, '2026-05-09 19:09:26', '2026-05-10 00:39:26'),
(156, 44, 'requested', 54, NULL, '2026-05-09 19:13:02', '2026-05-10 00:43:02'),
(157, 44, 'picked_up_dropped_off', 1, NULL, '2026-05-09 19:13:27', '2026-05-10 00:43:27'),
(158, 44, 'evaluating', 1, NULL, '2026-05-09 19:13:28', '2026-05-10 00:43:28'),
(159, 44, 'recycled', 1, NULL, '2026-05-09 19:13:29', '2026-05-10 00:43:29'),
(160, 44, 'rewarded', 1, NULL, '2026-05-09 19:13:30', '2026-05-10 00:43:30'),
(161, 45, 'requested', 54, NULL, '2026-05-22 12:13:46', '2026-05-22 17:43:46'),
(162, 46, 'requested', 54, NULL, '2026-05-24 13:29:25', '2026-05-24 18:59:25'),
(163, 46, 'picked_up_dropped_off', 1, NULL, '2026-05-24 13:33:06', '2026-05-24 19:03:06'),
(164, 46, 'evaluating', 1, NULL, '2026-05-24 13:33:09', '2026-05-24 19:03:09'),
(165, 46, 'recycled', 1, NULL, '2026-05-24 13:33:11', '2026-05-24 19:03:11'),
(166, 46, 'rewarded', 1, NULL, '2026-05-24 13:33:21', '2026-05-24 19:03:21');

-- --------------------------------------------------------

--
-- Table structure for table `e_waste_submission`
--

CREATE TABLE `e_waste_submission` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL COMMENT 'FK to auth_user.id',
  `category_id` int(11) NOT NULL COMMENT 'FK to recycling_info.id',
  `category_brand_mapping_id` int(11) NOT NULL COMMENT 'FK to category_brand_mapping.id',
  `model_id` int(11) NOT NULL COMMENT 'FK to product_model_name.id',
  `user_condition_id` int(11) NOT NULL COMMENT 'Condition selected by USER',
  `final_condition_id` int(11) DEFAULT NULL COMMENT 'Condition updated by ADMIN',
  `weight` decimal(10,2) DEFAULT NULL COMMENT 'Weight in KG used for reward calculation',
  `pickup_type` enum('pickup','dropoff') NOT NULL,
  `facility_id` int(11) NOT NULL COMMENT 'FK to facility.id',
  `address` text NOT NULL,
  `pickup_date` date NOT NULL,
  `pickup_time` time NOT NULL,
  `phone` varchar(20) NOT NULL,
  `notes` text DEFAULT NULL,
  `status` varchar(50) DEFAULT 'Requested',
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `e_waste_submission`
--

INSERT INTO `e_waste_submission` (`id`, `user_id`, `category_id`, `category_brand_mapping_id`, `model_id`, `user_condition_id`, `final_condition_id`, `weight`, `pickup_type`, `facility_id`, `address`, `pickup_date`, `pickup_time`, `phone`, `notes`, `status`, `created_at`, `updated_at`) VALUES
(33, 1, 3, 17, 68, 3, 3, 84.99, 'pickup', 9, 'bsfsfhs', '2026-05-09', '18:36:00', '1234567890', 'ghsgh', 'rewarded', '2026-04-30 13:07:00', '2026-04-30 13:43:10'),
(34, 53, 2, 13, 53, 1, 4, NULL, 'pickup', 4, 'Ahmedabad', '2026-05-10', '22:49:00', '1234567890', 'null not', 'rewarded', '2026-05-03 17:19:36', '2026-05-03 17:36:02'),
(35, 54, 3, 19, 72, 5, 5, 80.50, 'pickup', 5, 'Rajkot', '2026-05-04', '23:16:00', '1234567890', 'check', 'rewarded', '2026-05-03 17:46:34', '2026-05-03 17:57:01'),
(36, 54, 6, 27, 84, 3, 3, NULL, 'pickup', 7, 'Surat', '2026-05-04', '11:37:00', '1234567890', 'please check', 'rewarded', '2026-05-03 18:07:49', '2026-05-03 18:09:10'),
(37, 54, 5, 26, 82, 1, 4, 100.50, 'pickup', 5, 'Delhi', '2026-05-04', '11:40:00', '1234567890', 'please check', 'rewarded', '2026-05-03 18:10:30', '2026-05-03 18:11:39'),
(38, 54, 6, 27, 84, 3, 1, NULL, 'pickup', 2, 'Ahmedabad', '2026-05-05', '10:04:00', '1234567890', 'noo...', 'rewarded', '2026-05-04 12:35:08', '2026-05-04 12:35:50'),
(39, 54, 2, 14, 56, 3, 3, NULL, 'pickup', 2, 'Rajkot', '2026-05-06', '10:23:00', '1234567890', 'not', 'rejected', '2026-05-04 12:53:23', '2026-05-04 12:56:53'),
(40, 54, 4, 24, 76, 4, 4, 95.81, 'pickup', 3, 'Rajkot', '2026-05-05', '10:31:00', '1234567890', 'no', 'rewarded', '2026-05-04 14:01:54', '2026-05-04 14:03:32'),
(43, 1, 3, 17, 67, 2, 3, 80.00, 'pickup', 8, 'vn xn', '2026-05-16', '12:38:00', '1234567890', 'xxbx', 'rewarded', '2026-05-09 19:09:13', '2026-05-09 19:11:21'),
(44, 54, 2, 13, 53, 3, 3, NULL, 'pickup', 5, 'zvdv', '2026-05-10', '12:42:00', '1234567890', 'dvdav', 'rewarded', '2026-05-09 19:13:02', '2026-05-09 19:14:08'),
(45, 54, 2, 13, 53, 2, NULL, NULL, 'pickup', 6, 'Ahmedabad', '2026-05-24', '17:43:00', '1234567890', 'no', 'requested', '2026-05-22 12:13:45', '2026-05-22 12:13:45'),
(46, 54, 1, 1, 1, 3, 3, NULL, 'pickup', 4, 'abc', '2026-05-30', '18:58:00', '1234567890', 'null', 'rewarded', '2026-05-24 13:29:25', '2026-05-24 13:34:04');

-- --------------------------------------------------------

--
-- Table structure for table `e_waste_submission_images`
--

CREATE TABLE `e_waste_submission_images` (
  `id` int(11) NOT NULL,
  `submission_id` int(11) NOT NULL COMMENT 'FK to e_waste_submission.id',
  `image` varchar(255) NOT NULL COMMENT 'Stored image path',
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `e_waste_submission_images`
--

INSERT INTO `e_waste_submission_images` (`id`, `submission_id`, `image`, `created_at`) VALUES
(109, 33, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_1_KHUSHAL_nariya/submission_33/2026-04-30/Screenshot_342.png', '2026-04-30 13:07:00'),
(110, 33, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_1_KHUSHAL_nariya/submission_33/2026-04-30/Screenshot_343.png', '2026-04-30 13:07:00'),
(111, 33, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_1_KHUSHAL_nariya/submission_33/2026-04-30/Screenshot_344.png', '2026-04-30 13:07:00'),
(112, 34, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_53_KHUSHAL_nariya/submission_34/2026-05-03/Screenshot_342.png', '2026-05-03 17:19:36'),
(113, 34, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_53_KHUSHAL_nariya/submission_34/2026-05-03/Screenshot_343.png', '2026-05-03 17:19:36'),
(114, 34, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_53_KHUSHAL_nariya/submission_34/2026-05-03/Screenshot_344.png', '2026-05-03 17:19:36'),
(115, 35, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_35/2026-05-03/Screenshot_350.png', '2026-05-03 17:46:34'),
(116, 35, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_35/2026-05-03/Screenshot_351.png', '2026-05-03 17:46:34'),
(117, 35, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_35/2026-05-03/Screenshot_352.png', '2026-05-03 17:46:34'),
(118, 36, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_36/2026-05-03/Screenshot_370.png', '2026-05-03 18:07:49'),
(119, 36, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_36/2026-05-03/Screenshot_371.png', '2026-05-03 18:07:49'),
(120, 36, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_36/2026-05-03/Screenshot_372.png', '2026-05-03 18:07:49'),
(121, 36, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_36/2026-05-03/Screenshot_373.png', '2026-05-03 18:07:49'),
(122, 37, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_37/2026-05-03/Screenshot_342.png', '2026-05-03 18:10:30'),
(123, 37, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_37/2026-05-03/Screenshot_343.png', '2026-05-03 18:10:30'),
(124, 37, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_37/2026-05-03/Screenshot_344.png', '2026-05-03 18:10:30'),
(125, 37, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_37/2026-05-03/Screenshot_345.png', '2026-05-03 18:10:30'),
(126, 37, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_37/2026-05-03/Screenshot_346.png', '2026-05-03 18:10:30'),
(127, 38, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_38/2026-05-04/Screenshot_338.png', '2026-05-04 12:35:08'),
(128, 38, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_38/2026-05-04/Screenshot_339.png', '2026-05-04 12:35:08'),
(129, 38, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_38/2026-05-04/Screenshot_340.png', '2026-05-04 12:35:08'),
(130, 39, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_39/2026-05-04/Screenshot_342.png', '2026-05-04 12:53:23'),
(131, 39, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_39/2026-05-04/Screenshot_343.png', '2026-05-04 12:53:23'),
(132, 39, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_39/2026-05-04/Screenshot_344.png', '2026-05-04 12:53:23'),
(133, 39, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_39/2026-05-04/Screenshot_345.png', '2026-05-04 12:53:23'),
(134, 40, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_40/2026-05-04/Screenshot_350.png', '2026-05-04 14:01:54'),
(135, 40, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_40/2026-05-04/Screenshot_351.png', '2026-05-04 14:01:54'),
(136, 40, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_40/2026-05-04/Screenshot_354.png', '2026-05-04 14:01:54'),
(146, 43, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_1_KHUSHAL_nariya/submission_43/2026-05-09/Screenshot_338.png', '2026-05-09 19:09:13'),
(147, 43, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_1_KHUSHAL_nariya/submission_43/2026-05-09/Screenshot_339.png', '2026-05-09 19:09:13'),
(148, 43, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_1_KHUSHAL_nariya/submission_43/2026-05-09/Screenshot_340.png', '2026-05-09 19:09:13'),
(149, 43, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_1_KHUSHAL_nariya/submission_43/2026-05-09/Screenshot_341.png', '2026-05-09 19:09:13'),
(150, 44, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_44/2026-05-09/Screenshot_342.png', '2026-05-09 19:13:02'),
(151, 44, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_44/2026-05-09/Screenshot_343.png', '2026-05-09 19:13:02'),
(152, 44, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_44/2026-05-09/Screenshot_344.png', '2026-05-09 19:13:02'),
(153, 45, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_45/2026-05-22/Screenshot_342.png', '2026-05-22 12:13:45'),
(154, 45, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_45/2026-05-22/Screenshot_343.png', '2026-05-22 12:13:45'),
(155, 45, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_45/2026-05-22/Screenshot_344.png', '2026-05-22 12:13:46'),
(156, 46, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_46/2026-05-24/Screenshot_347.png', '2026-05-24 13:29:25'),
(157, 46, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_46/2026-05-24/Screenshot_343.png', '2026-05-24 13:29:25'),
(158, 46, 'app_10_E_Waste_Submission/e_waste_form_submit_images/user_54_Khushal_Nariya_-_3/submission_46/2026-05-24/Screenshot_344.png', '2026-05-24 13:29:25');

-- --------------------------------------------------------

--
-- Table structure for table `facility`
--

CREATE TABLE `facility` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `address` text NOT NULL,
  `phone` varchar(20) NOT NULL,
  `open_time` varchar(50) NOT NULL,
  `lat` double NOT NULL,
  `lon` double NOT NULL,
  `verified` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `facility`
--

INSERT INTO `facility` (`id`, `name`, `address`, `phone`, `open_time`, `lat`, `lon`, `verified`) VALUES
(1, 'Eco E-Waste Recycling Center', 'Rajkot Industrial Area, Gujarat', '9876543210', '9AM - 6PM', 22.3039, 70.8022, 1),
(2, 'Green Earth Recycling', '150 Feet Ring Road, Rajkot', '9825012345', '10AM - 7PM', 22.29, 70.78, 1),
(3, 'Clean Tech E-Waste Solutions', 'Ahmedabad GIDC Phase 2', '9898989898', '9AM - 5PM', 23.0225, 72.5714, 1),
(4, 'Recycle India Pvt Ltd', 'Surat Industrial Estate', '9012345678', '8AM - 4PM', 21.1702, 72.8311, 1),
(5, 'EcoDrop Recycling Point', 'University Road, Rajkot', '9988776655', '10AM - 6PM', 22.305, 70.79, 0),
(6, 'Green Planet Waste Hub', 'Vadodara GIDC Area', '9123456780', '9AM - 5PM', 22.3072, 73.1812, 1),
(7, 'Smart E-Waste Collectors', 'Satellite Road, Ahmedabad', '9090909090', '11AM - 7PM', 23.03, 72.55, 0),
(8, 'Urban Recycling Center', 'Ring Road, Surat', '9345678901', '9AM - 6PM', 21.1959, 72.7933, 1),
(9, 'Eco Smart Disposal', 'Kalawad Road, Rajkot', '9871234560', '8AM - 3PM', 22.31, 70.76, 1),
(10, 'Future Green Recycling', 'Morbi Road, Rajkot', '9811111111', '10AM - 5PM', 22.32, 70.81, 0);

-- --------------------------------------------------------

--
-- Table structure for table `home_page_hero_image`
--

CREATE TABLE `home_page_hero_image` (
  `id` int(11) NOT NULL,
  `image` varchar(255) NOT NULL,
  `is_active` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `home_page_hero_image`
--

INSERT INTO `home_page_hero_image` (`id`, `image`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 'app_5_Home/hero/Screenshot_396.png', 0, '2026-03-03 11:56:54', '2026-04-12 12:42:10'),
(2, 'app_5_Home/hero/screencapture-localhost-2000-FacilityMap-2026-03-20-11_46_53.png', 0, '2026-03-03 12:09:42', '2026-03-28 03:18:23'),
(3, 'app_5_Home/hero/E_Waste_Management_MEeiMGH.png', 1, '2026-03-06 11:39:17', '2026-03-28 03:15:52');

-- --------------------------------------------------------

--
-- Table structure for table `home_page_how_it_works`
--

CREATE TABLE `home_page_how_it_works` (
  `id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` text NOT NULL,
  `icon` varchar(50) NOT NULL,
  `order` int(11) DEFAULT 0,
  `is_active` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `home_page_how_it_works`
--

INSERT INTO `home_page_how_it_works` (`id`, `title`, `description`, `icon`, `order`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 'Drop Your E-Waste', 'Bring your old electronics to our certified drop points spread across your city.', 'bi-trash3-fill', 1, 1, '2026-02-27 13:09:41', '2026-04-12 12:37:56'),
(2, 'Eco Processing', 'We route your items safely to verified recyclers, ensuring zero landfill impact.', 'bi-arrow-repeat', 2, 1, '2026-02-27 13:09:41', '2026-03-02 06:35:59'),
(3, 'Earn Rewards', 'Get reward points for every contribution. Redeem them for discounts and perks!', 'bi-gift-fill', 3, 1, '2026-02-27 13:09:41', '2026-03-27 08:18:24');

-- --------------------------------------------------------

--
-- Table structure for table `item_conditions`
--

CREATE TABLE `item_conditions` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `display_name` varchar(100) NOT NULL,
  `is_active` tinyint(4) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `item_conditions`
--

INSERT INTO `item_conditions` (`id`, `name`, `display_name`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 'like_new', 'Like New', 1, '2026-04-01 07:27:24', '2026-05-26 08:30:16'),
(2, 'working', 'Working', 1, '2026-04-01 07:27:24', '2026-04-01 10:53:42'),
(3, 'minor_damage', 'Minor Damage', 1, '2026-04-01 07:27:24', '2026-04-01 10:53:50'),
(4, 'not_working', 'Not Working', 1, '2026-04-01 07:27:24', '2026-04-01 07:27:24'),
(5, 'scrap', 'Scrap', 1, '2026-04-01 10:20:20', '2026-04-01 10:53:34');

-- --------------------------------------------------------

--
-- Table structure for table `product_model`
--

CREATE TABLE `product_model` (
  `id` int(11) NOT NULL,
  `category_brand_mapping_id` int(11) NOT NULL COMMENT '   -- Mapping reference (Category + Brand --- mapping) Table (id)\r\n\r\n  ',
  `model_name` varchar(100) NOT NULL COMMENT '-- Model name (e.g., iPhone X,samsung s26,oppo A30,Vivo v30)',
  `is_active` tinyint(1) DEFAULT 1 COMMENT '-- Status (1 = Active, 0 = Inactive)',
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_model`
--

INSERT INTO `product_model` (`id`, `category_brand_mapping_id`, `model_name`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 3, 'iPhone 6', 1, '2026-04-04 23:07:32', '2026-04-04 23:07:32'),
(2, 3, 'iPhone 7', 1, '2026-04-04 23:07:32', '2026-04-04 23:07:32'),
(3, 3, 'iPhone X', 1, '2026-04-04 23:07:32', '2026-04-04 23:07:32'),
(4, 3, 'iPhone 11', 1, '2026-04-04 23:07:32', '2026-04-04 23:07:32'),
(5, 5, 'Galaxy S20', 1, '2026-04-04 23:07:32', '2026-04-04 23:07:32'),
(6, 5, 'Galaxy S21', 1, '2026-04-04 23:07:32', '2026-04-04 23:07:32'),
(7, 5, 'Galaxy S22', 1, '2026-04-04 23:07:32', '2026-04-04 23:07:32');

-- --------------------------------------------------------

--
-- Table structure for table `product_model_name`
--

CREATE TABLE `product_model_name` (
  `id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL COMMENT '-- Foreign Key::: References (recycle_category) table (e.g., Mobile, Laptop)\r\n',
  `brand_id` int(11) NOT NULL COMMENT '-- Foreign Key: References (brand) table (e.g., Apple, Samsung)\r\n',
  `model_name` varchar(100) NOT NULL COMMENT '    -- Model name (e.g., iPhone X, Galaxy S21)\r\n',
  `is_active` tinyint(1) DEFAULT 1 COMMENT '    -- Status: 1 = Active, 0 = Inactive (used to hide models without deleting)\r\n',
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_model_name`
--

INSERT INTO `product_model_name` (`id`, `category_id`, `brand_id`, `model_name`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 1, 1, 'iPhone 6', 1, '2026-04-04 18:59:21', '2026-04-04 18:59:21'),
(2, 1, 1, 'iPhone 6s', 1, '2026-04-04 18:59:21', '2026-04-06 07:22:25'),
(3, 1, 1, 'iPhone 7', 1, '2026-04-04 18:59:21', '2026-04-04 18:59:21'),
(4, 1, 1, 'iphone 8', 1, '2026-04-04 18:59:21', '2026-04-06 09:15:10'),
(5, 1, 1, 'iPhone X', 1, '2026-04-04 18:59:21', '2026-04-04 18:59:21'),
(6, 1, 1, 'iPhone 11', 1, '2026-04-04 18:59:21', '2026-04-04 18:59:21'),
(7, 1, 1, 'iPhone 12', 1, '2026-04-04 18:59:21', '2026-04-04 18:59:21'),
(8, 1, 1, 'iPhone 13', 1, '2026-04-04 18:59:21', '2026-04-04 18:59:21'),
(9, 1, 1, 'iphone 14', 1, '2026-04-04 13:35:13', '2026-04-04 13:35:13'),
(10, 1, 2, 'Galaxy S23', 1, '2026-04-06 11:09:46', '2026-04-06 09:09:57'),
(11, 1, 2, 'Galaxy S22', 1, '2026-04-06 11:09:46', '2026-04-06 09:19:55'),
(12, 1, 2, 'Galaxy S21', 1, '2026-04-06 11:09:46', '2026-04-06 09:20:01'),
(13, 1, 2, 'Galaxy A53', 1, '2026-04-06 11:09:46', '2026-04-06 07:12:36'),
(14, 1, 2, 'Galaxy M33', 1, '2026-04-06 11:09:46', '2026-04-06 07:14:18'),
(15, 1, 3, 'LG Wing', 1, '2026-04-06 18:56:14', '2026-04-06 18:56:14'),
(16, 1, 3, 'LG Velvet', 1, '2026-04-06 18:56:14', '2026-04-06 18:56:14'),
(17, 1, 3, 'LG K92', 1, '2026-04-06 18:56:14', '2026-04-06 18:56:14'),
(18, 1, 3, 'LG V60', 1, '2026-04-06 18:56:14', '2026-04-06 18:56:14'),
(19, 1, 4, 'Redmi Note 12', 1, '2026-04-06 18:56:37', '2026-04-06 18:56:37'),
(20, 1, 4, 'Redmi Note 11', 1, '2026-04-06 18:56:37', '2026-04-06 18:56:37'),
(21, 1, 4, 'Mi 11', 1, '2026-04-06 18:56:37', '2026-04-06 18:56:37'),
(22, 1, 4, 'Poco X5', 1, '2026-04-06 18:56:37', '2026-04-06 18:56:37'),
(23, 1, 4, 'Xiaomi 13', 1, '2026-04-06 18:56:37', '2026-04-06 18:56:37'),
(24, 1, 5, 'Pixel 7', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(25, 1, 5, 'Pixel 6', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(26, 1, 5, 'Pixel 6a', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(27, 1, 5, 'Pixel 5', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(28, 1, 6, 'Realme 11', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(29, 1, 6, 'Realme 10 Pro', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(30, 1, 6, 'Realme Narzo 60', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(31, 1, 6, 'Realme GT 2', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(32, 1, 7, 'OnePlus 11', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(33, 1, 7, 'OnePlus 10 Pro', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(34, 1, 7, 'OnePlus Nord 3', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(35, 1, 7, 'OnePlus 9', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(36, 1, 8, 'Oppo Reno 10', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(37, 1, 8, 'Oppo F21', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(38, 1, 8, 'Oppo A78', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(39, 1, 8, 'Oppo Find X6', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(40, 1, 9, 'Vivo V27', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(41, 1, 9, 'Vivo Y200', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(42, 1, 9, 'Vivo X90', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(43, 1, 9, 'Vivo T2', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(44, 1, 10, 'Moto G73', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(45, 1, 10, 'Moto Edge 40', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(46, 1, 10, 'Moto G32', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(47, 1, 10, 'Moto E32', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(48, 1, 11, 'Nokia G60', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(49, 1, 11, 'Nokia X100', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(50, 1, 11, 'Nokia 2720', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(51, 1, 11, 'Nokia C31', 1, '2026-04-06 18:57:25', '2026-04-06 18:57:25'),
(52, 2, 18, 'ThinkPad X1 Carbon', 1, '2026-04-06 18:58:47', '2026-04-06 18:58:47'),
(53, 2, 18, 'IdeaPad 3', 1, '2026-04-06 18:58:47', '2026-04-06 18:58:47'),
(54, 2, 18, 'Legion 5', 1, '2026-04-06 18:58:47', '2026-04-06 18:58:47'),
(55, 2, 19, 'Inspiron 15', 1, '2026-04-06 18:58:47', '2026-04-06 18:58:47'),
(56, 2, 19, 'XPS 13', 1, '2026-04-06 18:58:47', '2026-04-06 18:58:47'),
(57, 2, 19, 'Latitude 5420', 1, '2026-04-06 18:58:47', '2026-04-06 18:58:47'),
(58, 2, 20, 'HP Pavilion 15', 1, '2026-04-06 18:58:47', '2026-04-06 18:58:47'),
(59, 2, 20, 'HP Envy 13', 1, '2026-04-06 18:58:47', '2026-04-06 18:58:47'),
(60, 2, 20, 'HP Omen 16', 1, '2026-04-06 18:58:47', '2026-04-06 18:58:47'),
(61, 2, 21, 'Asus VivoBook 15', 1, '2026-04-06 18:58:47', '2026-04-06 18:58:47'),
(62, 2, 21, 'Asus ROG Strix', 1, '2026-04-06 18:58:47', '2026-04-06 18:58:47'),
(63, 2, 21, 'Asus ZenBook 14', 1, '2026-04-06 18:58:47', '2026-04-06 18:58:47'),
(64, 2, 1, 'MacBook Air M1', 1, '2026-04-06 18:58:47', '2026-04-06 18:58:47'),
(65, 2, 1, 'MacBook Air M2', 1, '2026-04-06 18:58:47', '2026-04-06 18:58:47'),
(66, 2, 1, 'MacBook Pro 14', 1, '2026-04-06 18:58:47', '2026-04-06 18:58:47'),
(67, 3, 22, 'Whirlpool 260L Fridge', 1, '2026-04-06 18:59:51', '2026-04-06 18:59:51'),
(68, 3, 22, 'Whirlpool 1.5 Ton AC', 1, '2026-04-06 18:59:51', '2026-04-06 18:59:51'),
(69, 3, 2, 'Samsung 253L Fridge', 1, '2026-04-06 18:59:51', '2026-04-06 18:59:51'),
(70, 3, 2, 'Samsung 1.5 Ton AC', 1, '2026-04-06 18:59:51', '2026-04-06 18:59:51'),
(71, 3, 3, 'LG 260L Fridge', 1, '2026-04-06 18:59:51', '2026-04-06 18:59:51'),
(72, 3, 3, 'LG Dual Inverter AC', 1, '2026-04-06 18:59:51', '2026-04-06 18:59:51'),
(73, 3, 24, 'Panasonic 1.5 Ton AC', 1, '2026-04-06 18:59:51', '2026-04-06 18:59:51'),
(74, 4, 23, 'Sony Bravia 55 inch TV', 1, '2026-04-06 19:00:05', '2026-04-06 19:00:05'),
(75, 4, 23, 'Sony Home Theatre', 1, '2026-04-06 19:00:05', '2026-04-06 19:00:05'),
(76, 4, 2, 'Samsung Smart TV 50 inch', 1, '2026-04-06 19:00:05', '2026-04-06 19:00:05'),
(77, 4, 3, 'LG OLED TV', 1, '2026-04-06 19:00:05', '2026-04-06 19:00:05'),
(78, 4, 24, 'Panasonic LED TV', 1, '2026-04-06 19:00:05', '2026-04-06 19:00:05'),
(79, 5, 25, 'Exide Car Battery', 1, '2026-04-06 19:00:21', '2026-04-06 19:00:21'),
(80, 5, 25, 'Exide Inverter Battery', 1, '2026-04-06 19:00:21', '2026-04-06 19:00:21'),
(81, 5, 26, 'Amaron Car Battery', 1, '2026-04-06 19:00:21', '2026-04-06 19:00:21'),
(82, 5, 26, 'Amaron Bike Battery', 1, '2026-04-06 19:00:21', '2026-04-06 19:00:21'),
(83, 6, 27, 'Canon EOS 1500D', 1, '2026-04-06 19:00:46', '2026-04-06 19:00:46'),
(84, 6, 27, 'Canon Pixma Printer', 1, '2026-04-06 19:00:46', '2026-04-06 19:00:46'),
(85, 6, 28, 'Nikon D3500', 1, '2026-04-06 19:00:46', '2026-04-06 19:00:46'),
(86, 6, 28, 'Nikon D5600', 1, '2026-04-06 19:00:46', '2026-04-12 18:18:18');

-- --------------------------------------------------------

--
-- Table structure for table `recycle_category`
--

CREATE TABLE `recycle_category` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `recycling_info`
--

CREATE TABLE `recycling_info` (
  `id` int(11) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `process` text DEFAULT NULL,
  `instruction` text DEFAULT NULL,
  `benefits` text DEFAULT NULL,
  `button_text` varchar(100) DEFAULT NULL,
  `icon` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `recycling_info`
--

INSERT INTO `recycling_info` (`id`, `title`, `description`, `process`, `instruction`, `benefits`, `button_text`, `icon`, `created_at`, `updated_at`) VALUES
(1, 'Smartphone', 'Responsibly recycle your outdated or non-functional smartphones and recover valuable materials while protecting the environment. gag sd gd gsdg sd g s g s  ghr h rdth dr h d j  n j  j  j jm yj rt j rt j  hser her h ersh serh er h serh esrh esr h ser h ser', 'Data wiping → Component dismantling → Precious metal recovery → Safe hazardous disposal', 'Back up and factory reset device. Remove SIM and memory cards before recycling.', 'Recycling one smartphone helps recover precious metals and reduces mining waste.', 'Recycle Smartphone Now', 'fa-mobile', '2026-03-26 22:18:48', '2026-05-15 04:58:00'),
(2, 'Laptops/PCs', 'Give your old laptops and computers a sustainable afterlife through specialized electronics recycling.', 'Secure data destruction → Component disassembly → Circuit board processing → LCD & battery management', 'Back up files, securely wipe storage drives, remove external batteries.', 'Recycling laptops recovers up to 95 percent materials including gold and rare earth metals.', 'Recycle Laptop Now', 'fa-laptop', '2026-03-26 22:18:48', '2026-04-04 06:51:44'),
(3, 'Home Appliances (Fridge/AC)', 'Dispose cables, chargers, headphones, keyboards and other electronic accessories safely.', 'Material sorting → Metal separation → Plastic processing → Hazardous material handling', 'Bundle similar accessories together and remove batteries from wireless devices.', 'Prevents toxic waste entering landfills and reduces need for new raw materials.', 'Recycle Home Appliances Now', 'fa-headphones', '2026-03-26 22:18:48', '2026-04-04 06:59:45'),
(4, 'Consumer Electronics (TV/Audio)', 'Recycle TVs, monitors and display devices using environmentally responsible processes.', 'Screen separation → Hazard containment → Circuit board recovery → Plastic & metal recycling', 'Transport screen facing down. Include cables and accessories if possible.', 'Prevents lead, mercury and harmful chemicals from contaminating soil and water.', 'Recycle Consumer Electronics Now', 'fa-tv', '2026-03-26 22:18:48', '2026-04-04 06:59:57'),
(5, 'Batteries & Bulky Scrap', 'Dispose refrigerators and cooling appliances through specialized recycling programs.', 'Refrigerant extraction → Insulation recovery → Metal separation → Hazard handling', 'Clean and defrost unit completely before recycling.', 'Prevents greenhouse gas release and recovers valuable metals and plastics.', 'Recycle Batteries Now', 'fa-snowflake', '2026-03-26 22:18:48', '2026-04-04 07:00:44'),
(6, 'Other Electronics', 'Recycle any electronic device not covered in other categories through complete e-waste management.', 'Device assessment → Disassembly → Material recovery → Safe disposal', 'Include manuals and accessories if available for better recycling.', 'Ensures uncommon electronics are properly processed and kept out of landfills.', 'Recycle Other Now', 'fa-recycle', '2026-03-26 22:18:48', '2026-04-12 18:16:17');

-- --------------------------------------------------------

--
-- Table structure for table `reward_cart`
--

CREATE TABLE `reward_cart` (
  `id` int(11) NOT NULL COMMENT 'Unique cart ID',
  `user_id` int(11) NOT NULL COMMENT 'Reference to auth_user table',
  `status` enum('active','checked_out','abandoned') NOT NULL DEFAULT 'active' COMMENT 'Cart status: active, checked_out, abandoned',
  `total_points` int(11) NOT NULL DEFAULT 0 COMMENT 'Total points of all items in cart',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Cart created date and time',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Cart last updated date and time'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Stores user shopping cart main information';

--
-- Dumping data for table `reward_cart`
--

INSERT INTO `reward_cart` (`id`, `user_id`, `status`, `total_points`, `created_at`, `updated_at`) VALUES
(1, 54, 'checked_out', 8900, '2026-05-07 19:17:16', '2026-05-09 18:52:55'),
(2, 1, 'active', 0, '2026-05-07 19:34:07', '2026-05-07 19:34:07'),
(3, 54, 'checked_out', 1700, '2026-05-09 18:52:55', '2026-05-10 04:08:40'),
(4, 54, 'checked_out', 1000, '2026-05-10 04:08:40', '2026-05-10 07:14:30'),
(5, 54, 'checked_out', 500, '2026-05-10 07:14:30', '2026-05-11 05:33:27'),
(6, 54, 'checked_out', 2500, '2026-05-11 05:33:28', '2026-05-11 06:22:34'),
(7, 52, 'checked_out', 6500, '2026-05-11 06:17:12', '2026-05-11 06:19:01'),
(8, 52, 'active', 1600, '2026-05-11 06:19:01', '2026-05-11 06:19:11'),
(9, 54, 'checked_out', 2500, '2026-05-11 06:22:34', '2026-05-11 06:23:12'),
(10, 54, 'checked_out', 2500, '2026-05-11 06:23:12', '2026-05-11 06:23:46'),
(11, 54, 'checked_out', 800, '2026-05-11 06:23:46', '2026-05-16 14:46:10'),
(12, 53, 'active', 0, '2026-05-14 12:43:12', '2026-05-14 12:43:12'),
(13, 54, 'checked_out', 1300, '2026-05-16 14:46:10', '2026-05-16 16:47:12'),
(14, 54, 'checked_out', 3300, '2026-05-16 16:47:12', '2026-05-16 17:01:58'),
(15, 54, 'checked_out', 1700, '2026-05-16 17:01:59', '2026-05-16 17:24:41'),
(16, 54, 'checked_out', 1700, '2026-05-16 17:24:41', '2026-05-16 17:26:40'),
(17, 54, 'checked_out', 800, '2026-05-16 17:26:40', '2026-05-16 17:38:46'),
(18, 54, 'checked_out', 1500, '2026-05-16 17:38:46', '2026-05-16 17:42:01'),
(19, 54, 'checked_out', 1600, '2026-05-16 17:42:01', '2026-05-16 17:42:40'),
(20, 54, 'checked_out', 2500, '2026-05-16 17:42:40', '2026-05-16 17:44:12'),
(21, 54, 'checked_out', 1600, '2026-05-16 17:44:12', '2026-05-16 18:01:41'),
(22, 54, 'checked_out', 2500, '2026-05-16 18:01:41', '2026-05-16 18:17:58'),
(23, 54, 'checked_out', 2600, '2026-05-16 18:17:58', '2026-05-20 16:00:07'),
(24, 54, 'checked_out', 800, '2026-05-20 16:00:07', '2026-05-20 17:38:25'),
(25, 54, 'checked_out', 1900, '2026-05-20 17:38:25', '2026-05-20 17:41:10'),
(26, 54, 'checked_out', 2200, '2026-05-20 17:41:10', '2026-05-21 12:25:09'),
(27, 54, 'checked_out', 4500, '2026-05-21 12:25:09', '2026-05-21 12:38:45'),
(28, 54, 'checked_out', 1100, '2026-05-21 12:38:45', '2026-05-22 16:22:23'),
(29, 81, 'active', 0, '2026-05-22 05:54:51', '2026-05-22 05:54:51'),
(30, 82, 'active', 0, '2026-05-22 13:27:17', '2026-05-22 13:27:17'),
(31, 54, 'checked_out', 3300, '2026-05-22 16:22:23', '2026-05-23 17:18:53'),
(32, 54, 'checked_out', 13100, '2026-05-23 17:18:53', '2026-05-24 04:56:00'),
(33, 54, 'checked_out', 9700, '2026-05-24 04:56:00', '2026-05-24 12:00:36'),
(34, 54, 'checked_out', 1200, '2026-05-24 12:00:36', '2026-05-24 12:11:17'),
(35, 54, 'checked_out', 1000, '2026-05-24 12:11:17', '2026-05-24 13:41:08'),
(36, 54, 'checked_out', 6500, '2026-05-24 13:41:08', '2026-05-26 12:24:24'),
(37, 83, 'active', 0, '2026-05-25 11:32:04', '2026-05-25 11:32:04'),
(38, 54, 'active', 0, '2026-05-26 12:24:24', '2026-05-26 12:50:20');

-- --------------------------------------------------------

--
-- Table structure for table `reward_cart_items`
--

CREATE TABLE `reward_cart_items` (
  `id` int(11) NOT NULL COMMENT 'Unique cart item ID',
  `cart_id` int(11) NOT NULL COMMENT 'Reference to reward_cart table',
  `product_id` int(11) NOT NULL COMMENT 'Reference to reward_products table',
  `quantity` int(11) NOT NULL DEFAULT 1 COMMENT 'Quantity of product added in cart',
  `points` int(11) NOT NULL COMMENT 'Single product points at add-to-cart time',
  `subtotal_points` int(11) NOT NULL COMMENT 'Total points for this cart item',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Cart item creation date and time',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Cart item last updated date and time'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Stores all products added inside user cart';

--
-- Dumping data for table `reward_cart_items`
--

INSERT INTO `reward_cart_items` (`id`, `cart_id`, `product_id`, `quantity`, `points`, `subtotal_points`, `created_at`, `updated_at`) VALUES
(12, 1, 4, 2, 500, 1000, '2026-05-08 17:16:47', '2026-05-08 18:43:07'),
(35, 1, 17, 5, 1100, 5500, '2026-05-08 18:40:57', '2026-05-08 18:42:51'),
(39, 1, 14, 1, 500, 500, '2026-05-09 17:53:47', '2026-05-09 17:53:47'),
(40, 1, 29, 1, 1900, 1900, '2026-05-09 18:22:29', '2026-05-09 18:22:29'),
(41, 3, 5, 1, 1200, 1200, '2026-05-10 04:06:53', '2026-05-10 04:06:53'),
(42, 3, 4, 1, 500, 500, '2026-05-10 04:06:56', '2026-05-10 04:06:56'),
(43, 4, 4, 2, 500, 1000, '2026-05-10 07:04:48', '2026-05-10 07:14:00'),
(44, 5, 4, 1, 500, 500, '2026-05-11 05:04:48', '2026-05-11 05:04:48'),
(45, 6, 7, 1, 2500, 2500, '2026-05-11 05:42:29', '2026-05-11 05:42:29'),
(46, 7, 5, 1, 1200, 1200, '2026-05-11 06:18:03', '2026-05-11 06:18:03'),
(47, 7, 11, 1, 1800, 1800, '2026-05-11 06:18:16', '2026-05-11 06:18:16'),
(48, 7, 10, 1, 3500, 3500, '2026-05-11 06:18:17', '2026-05-11 06:18:17'),
(49, 8, 28, 1, 1600, 1600, '2026-05-11 06:19:11', '2026-05-11 06:19:11'),
(50, 9, 27, 1, 2500, 2500, '2026-05-11 06:22:41', '2026-05-11 06:22:41'),
(51, 10, 27, 1, 2500, 2500, '2026-05-11 06:23:20', '2026-05-11 06:23:20'),
(52, 11, 12, 1, 800, 800, '2026-05-16 14:45:20', '2026-05-16 14:45:20'),
(54, 13, 4, 1, 500, 500, '2026-05-16 16:46:32', '2026-05-16 16:46:32'),
(56, 13, 21, 2, 400, 800, '2026-05-16 16:46:55', '2026-05-16 16:46:57'),
(57, 14, 21, 1, 400, 400, '2026-05-16 17:01:13', '2026-05-16 17:01:13'),
(58, 14, 13, 2, 600, 1200, '2026-05-16 17:01:18', '2026-05-16 17:01:20'),
(59, 14, 5, 1, 1200, 1200, '2026-05-16 17:01:22', '2026-05-16 17:01:22'),
(60, 14, 4, 1, 500, 500, '2026-05-16 17:01:23', '2026-05-16 17:01:23'),
(61, 15, 5, 1, 1200, 1200, '2026-05-16 17:24:31', '2026-05-16 17:24:31'),
(62, 15, 4, 1, 500, 500, '2026-05-16 17:24:32', '2026-05-16 17:24:32'),
(63, 16, 5, 1, 1200, 1200, '2026-05-16 17:26:33', '2026-05-16 17:26:33'),
(64, 16, 4, 1, 500, 500, '2026-05-16 17:26:33', '2026-05-16 17:26:33'),
(65, 17, 12, 1, 800, 800, '2026-05-16 17:27:58', '2026-05-16 17:27:58'),
(66, 18, 16, 1, 1500, 1500, '2026-05-16 17:41:55', '2026-05-16 17:41:55'),
(67, 19, 28, 1, 1600, 1600, '2026-05-16 17:42:34', '2026-05-16 17:42:34'),
(68, 20, 27, 1, 2500, 2500, '2026-05-16 17:44:02', '2026-05-16 17:44:02'),
(69, 21, 28, 1, 1600, 1600, '2026-05-16 18:01:32', '2026-05-16 18:01:32'),
(70, 22, 27, 1, 2500, 2500, '2026-05-16 18:17:48', '2026-05-16 18:17:48'),
(71, 23, 5, 1, 1200, 1200, '2026-05-20 15:59:20', '2026-05-20 15:59:20'),
(72, 23, 13, 1, 600, 600, '2026-05-20 15:59:41', '2026-05-20 15:59:41'),
(73, 23, 12, 1, 800, 800, '2026-05-20 15:59:42', '2026-05-20 15:59:42'),
(74, 24, 12, 1, 800, 800, '2026-05-20 17:38:12', '2026-05-20 17:38:12'),
(76, 25, 21, 1, 400, 400, '2026-05-20 17:40:45', '2026-05-20 17:40:45'),
(77, 25, 14, 2, 500, 1000, '2026-05-20 17:40:48', '2026-05-20 17:40:56'),
(78, 25, 4, 1, 500, 500, '2026-05-20 17:40:59', '2026-05-20 17:40:59'),
(79, 26, 5, 1, 1200, 1200, '2026-05-21 12:24:23', '2026-05-21 12:25:04'),
(80, 26, 4, 2, 500, 1000, '2026-05-21 12:24:23', '2026-05-21 12:24:45'),
(81, 27, 9, 1, 1200, 1200, '2026-05-21 12:38:35', '2026-05-21 12:38:35'),
(82, 27, 7, 1, 2500, 2500, '2026-05-21 12:38:36', '2026-05-21 12:38:36'),
(83, 27, 12, 1, 800, 800, '2026-05-21 12:38:40', '2026-05-21 12:38:40'),
(84, 28, 13, 1, 600, 600, '2026-05-22 16:22:01', '2026-05-22 16:22:01'),
(85, 28, 4, 1, 500, 500, '2026-05-22 16:22:14', '2026-05-22 16:22:14'),
(86, 31, 26, 2, 900, 1800, '2026-05-23 17:18:32', '2026-05-23 17:18:34'),
(87, 31, 14, 1, 500, 500, '2026-05-23 17:18:38', '2026-05-23 17:18:38'),
(88, 31, 4, 2, 500, 1000, '2026-05-23 17:18:42', '2026-05-23 17:18:43'),
(89, 32, 5, 2, 1200, 2400, '2026-05-24 04:53:44', '2026-05-24 04:54:17'),
(90, 32, 4, 1, 500, 500, '2026-05-24 04:53:47', '2026-05-24 04:53:47'),
(92, 32, 12, 1, 800, 800, '2026-05-24 04:53:53', '2026-05-24 04:53:53'),
(93, 32, 8, 1, 5000, 5000, '2026-05-24 04:53:57', '2026-05-24 04:53:57'),
(94, 32, 15, 2, 2200, 4400, '2026-05-24 04:54:00', '2026-05-24 04:54:03'),
(98, 33, 26, 1, 900, 900, '2026-05-24 11:59:04', '2026-05-24 11:59:04'),
(99, 33, 9, 2, 1200, 2400, '2026-05-24 11:59:10', '2026-05-24 11:59:35'),
(100, 33, 5, 2, 1200, 2400, '2026-05-24 11:59:12', '2026-05-24 11:59:15'),
(101, 33, 4, 2, 500, 1000, '2026-05-24 11:59:14', '2026-05-24 11:59:19'),
(102, 33, 16, 1, 1500, 1500, '2026-05-24 11:59:45', '2026-05-24 11:59:45'),
(103, 33, 14, 3, 500, 1500, '2026-05-24 11:59:46', '2026-05-24 12:00:00'),
(104, 34, 5, 1, 1200, 1200, '2026-05-24 12:11:08', '2026-05-24 12:11:08'),
(105, 35, 4, 2, 500, 1000, '2026-05-24 13:39:14', '2026-05-24 13:39:23'),
(109, 36, 28, 1, 1600, 1600, '2026-05-26 12:23:18', '2026-05-26 12:23:18'),
(111, 36, 22, 1, 700, 700, '2026-05-26 12:23:26', '2026-05-26 12:23:26'),
(112, 36, 12, 1, 800, 800, '2026-05-26 12:23:30', '2026-05-26 12:23:30'),
(113, 36, 5, 2, 1200, 2400, '2026-05-26 12:23:32', '2026-05-26 12:23:35'),
(114, 36, 4, 2, 500, 1000, '2026-05-26 12:23:33', '2026-05-26 12:23:34');

-- --------------------------------------------------------

--
-- Table structure for table `reward_category`
--

CREATE TABLE `reward_category` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL COMMENT 'Category name (e.g., Electronics, Gift Cards)',
  `slug` varchar(150) NOT NULL COMMENT 'URL-friendly name used in frontend (e.g., electronics)',
  `is_active` tinyint(1) DEFAULT 1 COMMENT 'Status of category (1 = Active, 0 = Inactive)',
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reward_category`
--

INSERT INTO `reward_category` (`id`, `name`, `slug`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 'Gift Cards', 'gift-cards', 1, '2026-04-09 18:01:37', '2026-05-26 13:06:18'),
(2, 'Electronics', 'Electronics', 1, '2026-04-13 10:53:57', '2026-04-13 13:59:20'),
(3, 'Eco Friendly Products', 'Eco-Friendly-Products', 1, '2026-04-13 10:54:11', '2026-04-13 13:59:23'),
(4, 'Accessories', 'Accessories', 1, '2026-04-13 10:54:25', '2026-04-13 13:59:26'),
(5, 'Home Appliances', 'Home-Appliances', 1, '2026-04-13 10:54:52', '2026-04-13 13:59:29'),
(6, 'Mobile Gadgets', 'Mobile-Gadgets', 1, '2026-04-13 10:56:56', '2026-04-13 13:59:34'),
(7, 'Gaming', 'Gaming', 1, '2026-04-13 10:57:09', '2026-04-13 13:59:42'),
(8, 'Fitness Products', 'Fitness-Products', 1, '2026-04-13 10:57:18', '2026-04-13 13:59:48'),
(11, 'New Bon Baby', 'New', 1, '2026-05-06 13:22:25', '2026-05-06 13:33:31');

-- --------------------------------------------------------

--
-- Table structure for table `reward_orders`
--

CREATE TABLE `reward_orders` (
  `id` int(11) NOT NULL COMMENT 'Primary key of order table',
  `order_number` varchar(50) NOT NULL COMMENT 'Unique order number shown to user (example: ORD1001)',
  `user_id` int(11) NOT NULL COMMENT 'User who placed this reward order',
  `cart_id` int(11) DEFAULT NULL COMMENT 'Reference of original (Reward_cart) Table used to create this order',
  `total_points` int(11) NOT NULL COMMENT 'Total reward points used in this order',
  `order_status` enum('pending','confirmed','processing','packed','shipped','out_for_delivery','delivered','cancelled','returned','failed') DEFAULT 'pending' COMMENT 'Current order status',
  `delivered_at` datetime DEFAULT NULL COMMENT '-- stores date and time when order is delivered\r\n',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Order creation date and time',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Last update date and time'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Stores main (reward order) details';

--
-- Dumping data for table `reward_orders`
--

INSERT INTO `reward_orders` (`id`, `order_number`, `user_id`, `cart_id`, `total_points`, `order_status`, `delivered_at`, `created_at`, `updated_at`) VALUES
(45, 'ECO-20260524120036', 54, 33, 9700, 'delivered', '2026-05-24 12:00:53', '2026-05-24 12:00:36', '2026-05-24 17:30:53'),
(46, 'ECO-20260524121117', 54, 34, 1200, 'delivered', '2026-05-24 12:11:32', '2026-05-24 12:11:17', '2026-05-24 17:41:32'),
(47, 'ECO-20260524134108', 54, 35, 1000, 'delivered', '2026-05-24 13:47:20', '2026-05-24 13:41:08', '2026-05-24 19:17:20'),
(48, 'ECO-20260526122424', 54, 36, 6500, 'delivered', '2026-05-26 12:25:05', '2026-05-26 12:24:24', '2026-05-26 18:21:01');

-- --------------------------------------------------------

--
-- Table structure for table `reward_order_address`
--

CREATE TABLE `reward_order_address` (
  `id` int(11) NOT NULL COMMENT 'Primary key of address table',
  `order_id` int(11) NOT NULL COMMENT 'Reference to (reward_order) Table ',
  `full_name` varchar(100) DEFAULT NULL COMMENT 'Receiver full name',
  `phone` varchar(20) DEFAULT NULL COMMENT 'Receiver mobile number',
  `address` text DEFAULT NULL COMMENT 'Full delivery address',
  `state` varchar(100) DEFAULT NULL COMMENT 'Delivery state',
  `city` varchar(100) DEFAULT NULL COMMENT 'Delivery city',
  `pincode` varchar(20) DEFAULT NULL COMMENT 'Delivery area pincode',
  `landmark` varchar(255) DEFAULT NULL COMMENT 'Nearby landmark for easy delivery',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Address saved date/time',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Order last updated date and time'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Stores delivery address snapshot';

--
-- Dumping data for table `reward_order_address`
--

INSERT INTO `reward_order_address` (`id`, `order_id`, `full_name`, `phone`, `address`, `state`, `city`, `pincode`, `landmark`, `created_at`, `updated_at`) VALUES
(31, 45, 'Khushal Nariya', '1234567890', 'shreejischool near', 'Gujarat', 'jetpur', '360370', 'Shreeeji school', '2026-05-24 17:30:36', '2026-05-24 17:30:36'),
(32, 46, 'Khushal Nariya', '1234567890', 'shreejischool near', 'Gujarat', 'jetpur', '360370', 'Shreeeji school', '2026-05-24 17:41:17', '2026-05-24 17:41:17'),
(33, 47, 'Khushal Nariya', '1234567890', 'shreejischool near', 'Gujarat', 'jetpur', '360370', 'Shreeeji school', '2026-05-24 19:11:08', '2026-05-24 19:11:08'),
(34, 48, 'Khushal Nariya', '1234567890', 'shreejischool near', 'Gujarat', 'jetpur', '360370', 'Shreeeji school', '2026-05-26 17:54:24', '2026-05-26 17:54:24');

-- --------------------------------------------------------

--
-- Table structure for table `reward_order_items`
--

CREATE TABLE `reward_order_items` (
  `id` int(11) NOT NULL COMMENT 'Primary key of order item table',
  `order_id` int(11) NOT NULL COMMENT 'Reference to parent (Reward_order) Table',
  `product_id` int(11) NOT NULL COMMENT 'Original (reward_product) Table (id)',
  `product_name` varchar(255) NOT NULL COMMENT 'Product name copied at order time (freeze)',
  `quantity` int(11) NOT NULL COMMENT 'Product quantity ordered (ex:: 1,2,3,4,5)',
  `points` int(11) NOT NULL COMMENT 'Single product point value',
  `subtotal_points` int(11) NOT NULL COMMENT 'quantity × points (Total Points)',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Order item created date/time',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Order last updated date and time'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Stores all ordered products (permanently)';

--
-- Dumping data for table `reward_order_items`
--

INSERT INTO `reward_order_items` (`id`, `order_id`, `product_id`, `product_name`, `quantity`, `points`, `subtotal_points`, `created_at`, `updated_at`) VALUES
(116, 45, 26, 'Console Skin Wrap', 1, 900, 900, '2026-05-24 12:00:36', '2026-05-24 17:30:36'),
(117, 45, 9, 'Wireless Optical Mouse', 2, 1200, 2400, '2026-05-24 12:00:36', '2026-05-24 17:30:36'),
(118, 45, 5, 'Recycled Plastic Laptop Sleeve', 2, 1200, 2400, '2026-05-24 12:00:36', '2026-05-24 17:30:36'),
(119, 45, 4, 'Eco-Friendly Bamboo Coffee Cup', 2, 500, 1000, '2026-05-24 12:00:36', '2026-05-24 17:30:36'),
(120, 45, 16, 'Waterproof Laptop Sleeve', 1, 1500, 1500, '2026-05-24 12:00:36', '2026-05-24 17:30:36'),
(121, 45, 14, 'Organic Cotton Tote Bag', 3, 500, 1500, '2026-05-24 12:00:36', '2026-05-24 17:30:36'),
(122, 46, 5, 'Recycled Plastic Laptop Sleeve', 1, 1200, 1200, '2026-05-24 12:11:17', '2026-05-24 17:41:17'),
(123, 47, 4, 'Eco-Friendly Bamboo Coffee Cup', 2, 500, 1000, '2026-05-24 13:41:08', '2026-05-24 19:11:08'),
(124, 48, 28, 'Resistance Band Set', 1, 1600, 1600, '2026-05-26 12:24:24', '2026-05-26 17:54:24'),
(125, 48, 22, 'Adjustable Phone Stand', 1, 700, 700, '2026-05-26 12:24:24', '2026-05-26 17:54:24'),
(126, 48, 12, 'Bamboo Cutlery Set', 1, 800, 800, '2026-05-26 12:24:24', '2026-05-26 17:54:24'),
(127, 48, 5, 'Recycled Plastic Laptop Sleeve', 2, 1200, 2400, '2026-05-26 12:24:24', '2026-05-26 17:54:24'),
(128, 48, 4, 'Eco-Friendly Bamboo Coffee Cup', 2, 500, 1000, '2026-05-26 12:24:24', '2026-05-26 17:54:24');

-- --------------------------------------------------------

--
-- Table structure for table `reward_order_payments`
--

CREATE TABLE `reward_order_payments` (
  `id` int(11) NOT NULL COMMENT 'Primary key of payment table',
  `order_id` int(11) NOT NULL COMMENT 'Reference to (reward_order) Table',
  `payment_method` varchar(50) DEFAULT NULL COMMENT 'Payment method (points/cod/upi/card)',
  `payment_status` varchar(50) DEFAULT NULL COMMENT 'Payment current status (paid/pending/failed)',
  `amount_points` int(11) DEFAULT 0 COMMENT 'Reward points used for payment',
  `amount_money` decimal(10,2) DEFAULT 0.00 COMMENT 'Extra money paid if needed',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Payment created date/time',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Payment last updated date and time'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Stores payment information of (reward Product order)';

--
-- Dumping data for table `reward_order_payments`
--

INSERT INTO `reward_order_payments` (`id`, `order_id`, `payment_method`, `payment_status`, `amount_points`, `amount_money`, `created_at`, `updated_at`) VALUES
(31, 45, 'points', 'success', 9700, 0.00, '2026-05-24 17:30:36', '2026-05-24 17:30:36'),
(32, 46, 'points', 'success', 1200, 0.00, '2026-05-24 17:41:17', '2026-05-24 17:41:17'),
(33, 47, 'upi', 'success', 1000, 0.00, '2026-05-24 19:11:08', '2026-05-24 19:11:08'),
(34, 48, 'points', 'success', 6500, 0.00, '2026-05-26 17:54:24', '2026-05-26 17:54:24');

-- --------------------------------------------------------

--
-- Table structure for table `reward_order_replace_images`
--

CREATE TABLE `reward_order_replace_images` (
  `id` int(11) NOT NULL COMMENT 'Unique ID for each replace image (auto-generated)',
  `replace_request_id` int(11) NOT NULL COMMENT 'Links this image to its parent replace request. FK to reward_order_replace_requests.id. One request can have multiple images.',
  `image_path` varchar(255) NOT NULL COMMENT 'File system path where image is stored. Format: app15_reward_replaces/user_{id}_{name}/replace_{id}/{date}/{filename}',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Timestamp when this image was uploaded by user.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci COMMENT='Stores proof photos uploaded by user for replace request. Admin reviews these images before approving or rejecting the request.';

--
-- Dumping data for table `reward_order_replace_images`
--

INSERT INTO `reward_order_replace_images` (`id`, `replace_request_id`, `image_path`, `created_at`) VALUES
(23, 10, 'app_15_reward_replaces/replace_images/user_54_Khushal_Nariya_-_3/replace_10/2026-05-24/Screenshot_345.png', '2026-05-24 12:02:22'),
(24, 10, 'app_15_reward_replaces/replace_images/user_54_Khushal_Nariya_-_3/replace_10/2026-05-24/Screenshot_346.png', '2026-05-24 12:02:22'),
(25, 10, 'app_15_reward_replaces/replace_images/user_54_Khushal_Nariya_-_3/replace_10/2026-05-24/Screenshot_347.png', '2026-05-24 12:02:22'),
(26, 11, 'app_15_reward_replaces/replace_images/user_54_Khushal_Nariya_-_3/replace_11/2026-05-24/Screenshot_348.png', '2026-05-24 12:13:22'),
(27, 12, 'app_15_reward_replaces/replace_images/user_54_Khushal_Nariya_-_3/replace_12/2026-05-24/Screenshot_343.png', '2026-05-24 13:49:56'),
(28, 13, 'app_15_reward_replaces/replace_images/user_54_Khushal_Nariya_-_3/replace_13/2026-05-25/Screenshot_342.png', '2026-05-25 13:16:01'),
(29, 14, 'app_15_reward_replaces/replace_images/user_54_Khushal_Nariya_-_3/replace_14/2026-05-25/Screenshot_345.png', '2026-05-25 15:01:46'),
(30, 15, 'app_15_reward_replaces/replace_images/user_54_Khushal_Nariya_-_3/replace_15/2026-05-26/Screenshot_345.png', '2026-05-26 12:26:37');

-- --------------------------------------------------------

--
-- Table structure for table `reward_order_replace_items`
--

CREATE TABLE `reward_order_replace_items` (
  `id` int(11) NOT NULL COMMENT 'Unique ID for each replace item row (auto-generated)',
  `replace_request_id` int(11) NOT NULL COMMENT 'Links this item to its parent replace request. FK to reward_order_replace_requests.id.',
  `order_item_id` int(11) NOT NULL COMMENT 'Links to the original order item being replaced. FK to reward_order_items.id. Used for history and audit.',
  `product_id` int(11) NOT NULL COMMENT 'FK to reward_products table. Refers to the ORIGINAL product the user received and wants to replace.',
  `product_name` varchar(255) NOT NULL COMMENT 'Snapshot of the original product name at the time of request. Stored separately in case product name changes later.',
  `quantity` int(11) NOT NULL DEFAULT 1 COMMENT 'How many units of this product the user wants to replace.',
  `points` int(11) NOT NULL COMMENT 'Points value per unit of this product at time of order.',
  `subtotal_points` int(11) NOT NULL COMMENT 'Total points for this item: quantity × points.',
  `item_condition` varchar(100) DEFAULT NULL COMMENT 'Condition or issue reported by user for this item. Values: wrong_item, defective, damaged, wrong_color, wrong_size.',
  `replacement_product_id` int(11) DEFAULT NULL COMMENT 'FK to reward_products. The NEW product to be sent as replacement. NULL if same product is requested (replace_type = same_item).',
  `replacement_product_name` varchar(255) DEFAULT NULL COMMENT 'Snapshot of the replacement product name. NULL if same item. Stored separately for history.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci COMMENT='Stores item-level details of each replace request. Tracks which product is being replaced, its condition, and what replacement product will be sent.';

--
-- Dumping data for table `reward_order_replace_items`
--

INSERT INTO `reward_order_replace_items` (`id`, `replace_request_id`, `order_item_id`, `product_id`, `product_name`, `quantity`, `points`, `subtotal_points`, `item_condition`, `replacement_product_id`, `replacement_product_name`) VALUES
(17, 10, 116, 26, 'Console Skin Wrap', 1, 900, 900, 'defective', NULL, 'Console Skin Wrap'),
(18, 10, 117, 9, 'Wireless Optical Mouse', 2, 1200, 2400, 'defective', NULL, 'Wireless Optical Mouse'),
(19, 11, 122, 5, 'Recycled Plastic Laptop Sleeve', 1, 1200, 1200, 'defective', NULL, 'Recycled Plastic Laptop Sleeve'),
(20, 12, 123, 4, 'Eco-Friendly Bamboo Coffee Cup', 2, 500, 1000, 'wrong_item', NULL, 'Eco-Friendly Bamboo Coffee Cup'),
(21, 13, 118, 5, 'Recycled Plastic Laptop Sleeve', 2, 1200, 2400, 'wrong_item', NULL, 'Recycled Plastic Laptop Sleeve'),
(22, 14, 118, 5, 'Recycled Plastic Laptop Sleeve', 2, 1200, 2400, 'defective', NULL, 'Recycled Plastic Laptop Sleeve'),
(23, 15, 124, 28, 'Resistance Band Set', 1, 1600, 1600, 'wrong_color', NULL, 'Resistance Band Set (size -- xl)');

-- --------------------------------------------------------

--
-- Table structure for table `reward_order_replace_pickups`
--

CREATE TABLE `reward_order_replace_pickups` (
  `id` int(11) NOT NULL COMMENT 'Unique ID for each pickup record (auto-generated)',
  `replace_request_id` int(11) NOT NULL COMMENT 'Links this pickup record to its parent replace request. FK to reward_order_replace_requests.id.',
  `order_address_id` int(11) NOT NULL COMMENT 'Address where OLD item will be picked up from. FK to reward_order_address.id. Usually same as delivery address.',
  `pickup_status` varchar(30) NOT NULL DEFAULT 'scheduled' COMMENT 'Status of the old-item pickup. Values: scheduled → picked_up. Or: failed, rescheduled if courier could not collect.',
  `delivery_address_id` int(11) DEFAULT NULL COMMENT 'Address where NEW replacement item will be delivered. FK to reward_order_address.id. Usually same as pickup address. NULL if not yet decided.',
  `courier_name` varchar(100) DEFAULT NULL COMMENT 'Name of the courier/logistics partner. Example: BlueDart, Delhivery, DTDC. Set by admin when dispatching replacement.',
  `tracking_number` varchar(100) DEFAULT NULL COMMENT 'Tracking ID for the replacement shipment. Set when replacement item is dispatched. User can use this to track delivery.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci COMMENT='Tracks pickup and delivery details for Amazon-style replace. One trip: delivery boy delivers new item AND collects old item simultaneously.';

--
-- Dumping data for table `reward_order_replace_pickups`
--

INSERT INTO `reward_order_replace_pickups` (`id`, `replace_request_id`, `order_address_id`, `pickup_status`, `delivery_address_id`, `courier_name`, `tracking_number`) VALUES
(10, 10, 31, 'picked_up', 31, NULL, NULL),
(11, 11, 32, 'picked_up', 32, NULL, NULL),
(12, 12, 33, 'picked_up', 33, NULL, NULL),
(13, 13, 31, 'scheduled', 31, NULL, NULL),
(14, 14, 31, 'scheduled', 31, NULL, NULL),
(15, 15, 34, 'picked_up', 34, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `reward_order_replace_requests`
--

CREATE TABLE `reward_order_replace_requests` (
  `id` int(11) NOT NULL COMMENT 'Unique ID for each replace request (auto-generated)',
  `replace_number` varchar(50) NOT NULL COMMENT 'Human-readable unique replace ID. Example: REP-2025-001. Admin aur user dono is number se track karte hain.',
  `order_id` int(11) NOT NULL COMMENT 'Links replace request to original order. FK to reward_orders.id. Sirf delivered orders pe replace allowed hai.',
  `user_id` int(11) NOT NULL COMMENT 'Links replace request to the user who submitted it. FK to auth_user.id.',
  `replace_status` varchar(30) NOT NULL DEFAULT 'requested' COMMENT 'Current status of this replace request. Flow: requested → approved → replacement_dispatched → replacement_delivered → quality_checked → closed. Exit state: rejected.',
  `replace_reason` varchar(255) NOT NULL COMMENT 'Primary reason for replacement. Example: wrong_item_delivered, defective, damaged_packaging, wrong_color.',
  `replace_note` text DEFAULT NULL COMMENT 'Optional extra note from user explaining the issue. Example: I ordered blue color but received red.',
  `replace_type` varchar(30) NOT NULL DEFAULT 'same_item' COMMENT 'Type of replacement requested. Values: same_item (exact same product), different_variant (different size/color of same product).',
  `replace_date` datetime DEFAULT NULL COMMENT 'Scheduled date-time for replacement delivery + old item pickup. Admin sets this after approving. Both happen in one trip (Amazon style).',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Timestamp when replace request was first submitted by user.',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Timestamp of last status or field update.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci COMMENT='Main table storing all Replace Requests. Amazon-style flow: New item delivers first, old item picked up at same time, warehouse inspects after.';

--
-- Dumping data for table `reward_order_replace_requests`
--

INSERT INTO `reward_order_replace_requests` (`id`, `replace_number`, `order_id`, `user_id`, `replace_status`, `replace_reason`, `replace_note`, `replace_type`, `replace_date`, `created_at`, `updated_at`) VALUES
(10, 'REP-20260524120222', 45, 54, 'replacement_delivered', 'damaged_on_arrival', 'please check', 'same_item', NULL, '2026-05-24 12:02:22', '2026-05-24 12:02:50'),
(11, 'REP-20260524121322', 46, 54, 'replacement_delivered', 'defective_parts', 'no', 'same_item', NULL, '2026-05-24 12:13:22', '2026-05-24 12:13:31'),
(12, 'REP-20260524134956', 47, 54, 'replacement_delivered', 'defective_parts', 'ok', 'same_item', NULL, '2026-05-24 13:49:56', '2026-05-24 13:54:42'),
(13, 'REP-20260525131601', 45, 54, 'rejected', 'incorrect_item_sent', 'please check', 'same_item', NULL, '2026-05-25 13:16:01', '2026-05-25 13:34:22'),
(14, 'REP-20260525150146', 45, 54, 'rejected', 'defective_parts', 'ok', 'same_item', NULL, '2026-05-25 15:01:46', '2026-05-25 15:03:44'),
(15, 'REP-20260526122637', 48, 54, 'replacement_delivered', 'other', 'ok', 'different_variant', NULL, '2026-05-26 12:26:37', '2026-05-26 12:27:59');

-- --------------------------------------------------------

--
-- Table structure for table `reward_order_replace_status_history`
--

CREATE TABLE `reward_order_replace_status_history` (
  `id` int(11) NOT NULL COMMENT 'Unique ID for each status history log entry (auto-generated)',
  `replace_request_id` int(11) NOT NULL COMMENT 'Links this log entry to its parent replace request. FK to reward_order_replace_requests.id.',
  `status` varchar(50) NOT NULL COMMENT 'The new status this request was changed TO. Example: requested, approved, replacement_dispatched, replacement_delivered, quality_checked, closed, rejected.',
  `changed_by` int(11) DEFAULT NULL COMMENT 'FK to auth_user.id. Who made this status change — could be user (initial submit) or admin (approve/dispatch/close). NULL if system-generated.',
  `remarks` text DEFAULT NULL COMMENT 'Internal note or reason for this status change. Example: Approved - wrong color confirmed from photos. Visible only to admin.',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Timestamp when this status change was logged.',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Timestamp of last update to this log entry.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci COMMENT='Full audit trail of all status changes for replace requests. Every status transition is recorded here with who changed it and why.';

--
-- Dumping data for table `reward_order_replace_status_history`
--

INSERT INTO `reward_order_replace_status_history` (`id`, `replace_request_id`, `status`, `changed_by`, `remarks`, `created_at`, `updated_at`) VALUES
(38, 10, 'requested', 54, 'Replace request submitted by user. Awaiting admin review.', '2026-05-24 12:02:22', '2026-05-24 12:02:22'),
(39, 10, 'approved', 1, 'Replace request approved. Replacement item will be dispatched shortly.', '2026-05-24 12:02:45', '2026-05-24 12:02:45'),
(40, 10, 'replacement_dispatched', 1, 'Replacement item dispatched via courier. Agent will deliver new item and collect old item at the same time.', '2026-05-24 12:02:49', '2026-05-24 12:02:49'),
(41, 10, 'replacement_delivered', 1, 'Replacement delivered to customer. Old item collected by courier agent.', '2026-05-24 12:02:50', '2026-05-24 12:02:50'),
(42, 11, 'requested', 54, 'Replace request submitted by user. Awaiting admin review.', '2026-05-24 12:13:22', '2026-05-24 12:13:22'),
(43, 11, 'approved', 1, 'Replace request approved. Replacement item will be dispatched shortly.', '2026-05-24 12:13:28', '2026-05-24 12:13:28'),
(44, 11, 'replacement_dispatched', 1, 'Replacement item dispatched via courier. Agent will deliver new item and collect old item at the same time.', '2026-05-24 12:13:29', '2026-05-24 12:13:29'),
(45, 11, 'replacement_delivered', 1, 'Replacement delivered to customer. Old item collected by courier agent.', '2026-05-24 12:13:31', '2026-05-24 12:13:31'),
(46, 12, 'requested', 54, 'Replace request submitted by user. Awaiting admin review.', '2026-05-24 13:49:56', '2026-05-24 13:49:56'),
(47, 12, 'approved', 1, 'Replace request approved. Replacement item will be dispatched shortly.', '2026-05-24 13:54:39', '2026-05-24 13:54:39'),
(48, 12, 'replacement_dispatched', 1, 'Replacement item dispatched via courier. Agent will deliver new item and collect old item at the same time.', '2026-05-24 13:54:40', '2026-05-24 13:54:40'),
(49, 12, 'replacement_delivered', 1, 'Replacement delivered to customer. Old item collected by courier agent.', '2026-05-24 13:54:42', '2026-05-24 13:54:42'),
(50, 13, 'requested', 54, 'Replace request submitted by user. Awaiting admin review.', '2026-05-25 13:16:01', '2026-05-25 13:16:01'),
(51, 13, 'rejected', 54, 'Replace request cancelled by customer.', '2026-05-25 13:34:22', '2026-05-25 13:34:22'),
(52, 14, 'requested', 54, 'Replace request submitted by user. Awaiting admin review.', '2026-05-25 15:01:46', '2026-05-25 15:01:46'),
(53, 14, 'rejected', 54, 'Replace request cancelled by customer. Reason: Issue resolved by customer support', '2026-05-25 15:03:44', '2026-05-25 15:03:44'),
(54, 14, 'rejected', 54, 'Replace request cancelled by customer. Reason: Issue resolved by customer support', '2026-05-25 15:03:44', '2026-05-25 15:03:44'),
(55, 15, 'requested', 54, 'Replace request submitted by user. Awaiting admin review.', '2026-05-26 12:26:37', '2026-05-26 12:26:37'),
(56, 15, 'approved', 1, 'Replace request approved. Replacement item will be dispatched shortly.', '2026-05-26 12:26:59', '2026-05-26 12:26:59'),
(57, 15, 'replacement_dispatched', 1, 'Replacement item dispatched via courier. Agent will deliver new item and collect old item at the same time.', '2026-05-26 12:27:01', '2026-05-26 12:27:01'),
(58, 15, 'replacement_delivered', 1, 'Replacement delivered to customer. Old item collected by courier agent.', '2026-05-26 12:27:59', '2026-05-26 12:27:59');

-- --------------------------------------------------------

--
-- Table structure for table `reward_order_return_images`
--

CREATE TABLE `reward_order_return_images` (
  `id` int(11) NOT NULL COMMENT 'Unique ID for each return image',
  `return_request_id` int(11) NOT NULL COMMENT 'Links image to return request. FK to reward_order_return_requests.id',
  `image_path` varchar(255) NOT NULL COMMENT 'File path or URL where image is saved',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Time when the image was uploaded',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Time when the image was updated'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `reward_order_return_images`
--

INSERT INTO `reward_order_return_images` (`id`, `return_request_id`, `image_path`, `created_at`, `updated_at`) VALUES
(18, 12, 'app_14_reward_returns/reward_return_images/user_54_Khushal_Nariya_-_3/return_12/2026-05-24/Screenshot_342.png', '2026-05-24 12:05:03', '2026-05-24 17:35:03'),
(19, 13, 'app_14_reward_returns/reward_return_images/user_54_Khushal_Nariya_-_3/return_13/2026-05-24/Screenshot_345.png', '2026-05-24 13:59:09', '2026-05-24 19:29:09'),
(20, 14, 'app_14_reward_returns/reward_return_images/user_54_Khushal_Nariya_-_3/return_14/2026-05-25/Screenshot_345.png', '2026-05-25 12:23:32', '2026-05-25 17:53:32'),
(21, 15, 'app_14_reward_returns/reward_return_images/user_54_Khushal_Nariya_-_3/return_15/2026-05-25/Screenshot_345.png', '2026-05-25 12:59:13', '2026-05-25 18:29:13'),
(22, 16, 'app_14_reward_returns/reward_return_images/user_54_Khushal_Nariya_-_3/return_16/2026-05-25/Screenshot_344.png', '2026-05-25 14:49:10', '2026-05-25 20:19:10');

-- --------------------------------------------------------

--
-- Table structure for table `reward_order_return_items`
--

CREATE TABLE `reward_order_return_items` (
  `id` int(11) NOT NULL COMMENT 'Primary key',
  `return_request_id` int(11) NOT NULL COMMENT 'FK to reward_order_return_requests.id',
  `order_item_id` int(11) NOT NULL COMMENT 'FK to reward_order_items.id',
  `product_id` int(11) NOT NULL COMMENT 'FK to reward_products.id',
  `product_name` varchar(255) NOT NULL COMMENT 'Product snapshot',
  `quantity` int(11) NOT NULL DEFAULT 1 COMMENT 'Returned qty',
  `points` int(11) NOT NULL COMMENT 'Single item points',
  `subtotal_points` int(11) NOT NULL COMMENT 'Total refund points',
  `item_condition` varchar(100) DEFAULT NULL COMMENT 'damaged / wrong_item / used'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `reward_order_return_items`
--

INSERT INTO `reward_order_return_items` (`id`, `return_request_id`, `order_item_id`, `product_id`, `product_name`, `quantity`, `points`, `subtotal_points`, `item_condition`) VALUES
(27, 12, 117, 9, 'Wireless Optical Mouse', 2, 1200, 2400, 'wrong_item'),
(28, 13, 123, 4, 'Eco-Friendly Bamboo Coffee Cup', 2, 500, 1000, 'size_issue'),
(29, 14, 122, 5, 'Recycled Plastic Laptop Sleeve', 1, 1200, 1200, 'damaged'),
(30, 15, 122, 5, 'Recycled Plastic Laptop Sleeve', 1, 1200, 1200, 'wrong_item'),
(31, 16, 122, 5, 'Recycled Plastic Laptop Sleeve', 1, 1200, 1200, 'wrong_item');

-- --------------------------------------------------------

--
-- Table structure for table `reward_order_return_pickups`
--

CREATE TABLE `reward_order_return_pickups` (
  `id` int(11) NOT NULL COMMENT 'Primary key',
  `return_request_id` int(11) NOT NULL COMMENT 'FK to reward_order_return_requests.id',
  `order_address_id` int(11) NOT NULL COMMENT 'FK to reward_order_address.id',
  `pickup_status` enum('scheduled','picked_up','failed','rescheduled') DEFAULT 'scheduled' COMMENT 'Pickup status'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `reward_order_return_pickups`
--

INSERT INTO `reward_order_return_pickups` (`id`, `return_request_id`, `order_address_id`, `pickup_status`) VALUES
(8, 12, 31, 'picked_up'),
(9, 13, 33, 'picked_up'),
(10, 14, 32, 'failed'),
(11, 15, 32, 'scheduled'),
(12, 16, 32, 'scheduled');

-- --------------------------------------------------------

--
-- Table structure for table `reward_order_return_requests`
--

CREATE TABLE `reward_order_return_requests` (
  `id` int(11) NOT NULL COMMENT 'Primary key',
  `return_number` varchar(50) NOT NULL COMMENT 'Unique return number like RET-001',
  `order_id` int(11) NOT NULL COMMENT 'FK to reward_orders.id',
  `user_id` int(11) NOT NULL COMMENT 'FK to auth_user.id',
  `return_status` enum('requested','approved','rejected','pickup_scheduled','picked_up','received','inspected','refund_approved','refunded','closed') DEFAULT 'requested' COMMENT 'Current return status',
  `return_reason` varchar(255) NOT NULL COMMENT 'Reason selected by user',
  `return_note` text DEFAULT NULL COMMENT 'Extra note by user',
  `refund_points` int(11) DEFAULT 0 COMMENT 'How many points to refund',
  `return_date` datetime DEFAULT NULL COMMENT 'Pickup date/time',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Created time',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Updated time'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci COMMENT='This is a (Main Table) For (Return Request)';

--
-- Dumping data for table `reward_order_return_requests`
--

INSERT INTO `reward_order_return_requests` (`id`, `return_number`, `order_id`, `user_id`, `return_status`, `return_reason`, `return_note`, `refund_points`, `return_date`, `created_at`, `updated_at`) VALUES
(12, 'RET-20260524120503', 45, 54, 'refunded', 'damaged_on_arrival', 'please check', 2400, NULL, '2026-05-24 12:05:03', '2026-05-24 12:07:42'),
(13, 'RET-20260524135909', 47, 54, 'refunded', 'incorrect_item_sent', 'ok', 1000, NULL, '2026-05-24 13:59:09', '2026-05-24 14:01:44'),
(14, 'RET-20260525122332', 46, 54, 'rejected', 'damaged_on_arrival', 'please check', 1200, NULL, '2026-05-25 12:23:32', '2026-05-25 12:29:48'),
(15, 'RET-20260525125911', 46, 54, 'rejected', 'damaged_on_arrival', 'ok', 1200, NULL, '2026-05-25 12:59:11', '2026-05-25 13:36:19'),
(16, 'RET-20260525144909', 46, 54, 'rejected', 'damaged_on_arrival', 'ok', 1200, NULL, '2026-05-25 14:49:09', '2026-05-25 15:04:25');

-- --------------------------------------------------------

--
-- Table structure for table `reward_order_return_status_history`
--

CREATE TABLE `reward_order_return_status_history` (
  `id` int(11) NOT NULL COMMENT 'Primary key',
  `return_request_id` int(11) NOT NULL COMMENT 'FK to reward_order_return_requests.id',
  `status` varchar(50) NOT NULL COMMENT 'Status name',
  `changed_by` int(11) DEFAULT NULL COMMENT 'Admin/User ID',
  `remarks` text DEFAULT NULL COMMENT 'Optional note',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Status changed time',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `reward_order_return_status_history`
--

INSERT INTO `reward_order_return_status_history` (`id`, `return_request_id`, `status`, `changed_by`, `remarks`, `created_at`, `updated_at`) VALUES
(52, 12, 'requested', 54, 'Return request registered successfully by user. Awaiting admin approval.', '2026-05-24 12:05:03', '2026-05-24 12:05:03'),
(53, 12, 'approved', 1, 'Return request approved by administrator. Pickup agent will schedule courier shortly.', '2026-05-24 12:05:18', '2026-05-24 12:05:18'),
(54, 12, 'pickup_scheduled', 1, 'Pickup scheduled successfully. Date of courier visit set.', '2026-05-24 12:05:19', '2026-05-24 12:05:19'),
(55, 12, 'picked_up', 1, 'Courier picked up the product successfully. Transit to warehouse initiated.', '2026-05-24 12:05:21', '2026-05-24 12:05:21'),
(56, 12, 'received', 1, 'Returned item received safely at processing warehouse.', '2026-05-24 12:05:22', '2026-05-24 12:05:22'),
(57, 12, 'inspected', 1, 'Inspection completed by quality check agent. Product condition verified.', '2026-05-24 12:05:40', '2026-05-24 12:05:40'),
(58, 12, 'refund_approved', 1, 'Refund approved by administrator. Wallet points settlement queued.', '2026-05-24 12:05:48', '2026-05-24 12:05:48'),
(59, 12, 'refunded', 1, 'Points successfully refunded to wallet. Settled points value: 2400 pts.', '2026-05-24 12:07:42', '2026-05-24 12:07:42'),
(60, 13, 'requested', 54, 'Return request registered successfully by user. Awaiting admin approval.', '2026-05-24 13:59:09', '2026-05-24 13:59:09'),
(61, 13, 'approved', 1, 'Return request approved by administrator. Pickup agent will schedule courier shortly.', '2026-05-24 13:59:28', '2026-05-24 13:59:28'),
(62, 13, 'pickup_scheduled', 1, 'Pickup scheduled successfully. Date of courier visit set.', '2026-05-24 13:59:29', '2026-05-24 13:59:29'),
(63, 13, 'picked_up', 1, 'Courier picked up the product successfully. Transit to warehouse initiated.', '2026-05-24 13:59:30', '2026-05-24 13:59:30'),
(64, 13, 'received', 1, 'Returned item received safely at processing warehouse.', '2026-05-24 13:59:32', '2026-05-24 13:59:32'),
(65, 13, 'inspected', 1, 'Inspection completed by quality check agent. Product condition verified.', '2026-05-24 13:59:33', '2026-05-24 13:59:33'),
(66, 13, 'refund_approved', 1, 'Refund approved by administrator. Wallet points settlement queued.', '2026-05-24 13:59:36', '2026-05-24 13:59:36'),
(67, 13, 'refunded', 1, 'Points successfully refunded to wallet. Settled points value: 1000 pts.', '2026-05-24 14:01:44', '2026-05-24 14:01:44'),
(68, 14, 'requested', 54, 'Return request registered successfully by user. Awaiting admin approval.', '2026-05-25 12:23:32', '2026-05-25 12:23:32'),
(69, 14, 'approved', 1, 'Return request approved by administrator. Pickup agent will schedule courier shortly.', '2026-05-25 12:29:10', '2026-05-25 12:29:10'),
(70, 14, 'rejected', 1, 'Return request rejected by administrator due to inspection failure or policy violation.', '2026-05-25 12:29:48', '2026-05-25 12:29:48'),
(71, 15, 'requested', 54, 'Return request registered successfully by user. Awaiting admin approval.', '2026-05-25 12:59:13', '2026-05-25 12:59:13'),
(72, 15, 'rejected', 54, 'Return request cancelled by customer.', '2026-05-25 13:36:19', '2026-05-25 13:36:19'),
(73, 16, 'requested', 54, 'Return request registered successfully by user. Awaiting admin approval.', '2026-05-25 14:49:11', '2026-05-25 14:49:11'),
(74, 16, 'rejected', 54, 'Return request cancelled by customer. Reason: Decided to keep the product', '2026-05-25 15:04:25', '2026-05-25 15:04:25');

-- --------------------------------------------------------

--
-- Table structure for table `reward_order_status_history`
--

CREATE TABLE `reward_order_status_history` (
  `id` int(11) NOT NULL COMMENT 'Primary key',
  `order_id` int(11) NOT NULL COMMENT 'FK to reward_orders.id',
  `status` varchar(50) NOT NULL COMMENT 'Status name (e.g. pending, shipped)',
  `changed_by` int(11) DEFAULT NULL COMMENT 'Admin or User ID',
  `remarks` text DEFAULT NULL COMMENT 'Optional note about status change',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Log creation time',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reward_order_status_history`
--

INSERT INTO `reward_order_status_history` (`id`, `order_id`, `status`, `changed_by`, `remarks`, `created_at`, `updated_at`) VALUES
(126, 45, 'pending', 54, 'Order placed successfully via Reward Store.', '2026-05-24 12:00:36', '2026-05-24 12:00:36'),
(127, 45, 'confirmed', 1, 'Status updated to Confirmed by administrator.', '2026-05-24 12:00:45', '2026-05-24 12:00:45'),
(128, 45, 'processing', 1, 'Status updated to Processing by administrator.', '2026-05-24 12:00:48', '2026-05-24 12:00:48'),
(129, 45, 'packed', 1, 'Status updated to Packed by administrator.', '2026-05-24 12:00:49', '2026-05-24 12:00:49'),
(130, 45, 'shipped', 1, 'Status updated to Shipped by administrator.', '2026-05-24 12:00:50', '2026-05-24 12:00:50'),
(131, 45, 'out_for_delivery', 1, 'Status updated to Out For Delivery by administrator.', '2026-05-24 12:00:52', '2026-05-24 12:00:52'),
(132, 45, 'delivered', 1, 'Status updated to Delivered by administrator.', '2026-05-24 12:00:53', '2026-05-24 12:00:53'),
(133, 46, 'pending', 54, 'Order placed successfully via Reward Store.', '2026-05-24 12:11:17', '2026-05-24 12:11:17'),
(134, 46, 'confirmed', 1, 'Status updated to Confirmed by administrator.', '2026-05-24 12:11:25', '2026-05-24 12:11:25'),
(135, 46, 'processing', 1, 'Status updated to Processing by administrator.', '2026-05-24 12:11:27', '2026-05-24 12:11:27'),
(136, 46, 'packed', 1, 'Status updated to Packed by administrator.', '2026-05-24 12:11:28', '2026-05-24 12:11:28'),
(137, 46, 'shipped', 1, 'Status updated to Shipped by administrator.', '2026-05-24 12:11:29', '2026-05-24 12:11:29'),
(138, 46, 'out_for_delivery', 1, 'Status updated to Out For Delivery by administrator.', '2026-05-24 12:11:31', '2026-05-24 12:11:31'),
(139, 46, 'delivered', 1, 'Status updated to Delivered by administrator.', '2026-05-24 12:11:32', '2026-05-24 12:11:32'),
(140, 47, 'pending', 54, 'Order placed successfully via Reward Store.', '2026-05-24 13:41:08', '2026-05-24 13:41:08'),
(141, 47, 'confirmed', 1, 'Status updated to Confirmed by administrator.', '2026-05-24 13:44:42', '2026-05-24 13:44:42'),
(142, 47, 'processing', 1, 'Status updated to Processing by administrator.', '2026-05-24 13:46:23', '2026-05-24 13:46:23'),
(143, 47, 'packed', 1, 'Status updated to Packed by administrator.', '2026-05-24 13:47:16', '2026-05-24 13:47:16'),
(144, 47, 'shipped', 1, 'Status updated to Shipped by administrator.', '2026-05-24 13:47:17', '2026-05-24 13:47:17'),
(145, 47, 'out_for_delivery', 1, 'Status updated to Out For Delivery by administrator.', '2026-05-24 13:47:19', '2026-05-24 13:47:19'),
(146, 47, 'delivered', 1, 'Status updated to Delivered by administrator.', '2026-05-24 13:47:20', '2026-05-24 13:47:20'),
(147, 48, 'pending', 54, 'Order placed successfully via Reward Store.', '2026-05-26 12:24:24', '2026-05-26 12:24:24'),
(148, 48, 'confirmed', 1, 'Status updated to Confirmed by administrator.', '2026-05-26 12:24:57', '2026-05-26 12:24:57'),
(149, 48, 'processing', 1, 'Status updated to Processing by administrator.', '2026-05-26 12:24:59', '2026-05-26 12:24:59'),
(150, 48, 'packed', 1, 'Status updated to Packed by administrator.', '2026-05-26 12:25:00', '2026-05-26 12:25:00'),
(151, 48, 'shipped', 1, 'Status updated to Shipped by administrator.', '2026-05-26 12:25:02', '2026-05-26 12:25:02'),
(152, 48, 'out_for_delivery', 1, 'Status updated to Out For Delivery by administrator.', '2026-05-26 12:25:03', '2026-05-26 12:25:03'),
(153, 48, 'delivered', 1, 'Status updated to Delivered by administrator.', '2026-05-26 12:25:05', '2026-05-26 12:25:05');

-- --------------------------------------------------------

--
-- Table structure for table `reward_products`
--

CREATE TABLE `reward_products` (
  `id` int(11) NOT NULL COMMENT 'Unique product ID',
  `name` varchar(255) NOT NULL COMMENT 'Product name shown in store and detail page',
  `slug` varchar(255) NOT NULL COMMENT 'URL-friendly product name for detail page',
  `category_id` int(11) NOT NULL COMMENT 'Reference to reward_category table',
  `points` int(11) NOT NULL COMMENT 'Points required to redeem this product',
  `stock` int(11) NOT NULL COMMENT 'Available quantity in inventory',
  `description` text NOT NULL COMMENT 'Full product description',
  `terms` text DEFAULT NULL COMMENT 'Terms and conditions of product',
  `tag` varchar(50) DEFAULT NULL COMMENT 'Label like Popular, New, Best Seller',
  `delivery_days` varchar(50) DEFAULT NULL COMMENT 'Estimated delivery time (e.g., 5-7 days)',
  `rating` decimal(2,1) DEFAULT 0.0 COMMENT 'Average user rating (e.g., 4.5)',
  `total_redeemed` int(11) DEFAULT 0 COMMENT 'How many times product redeemed',
  `is_active` tinyint(1) DEFAULT 1 COMMENT 'Product status (1 = Active, 0 = Inactive)',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Product creation time',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Last updated time'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reward_products`
--

INSERT INTO `reward_products` (`id`, `name`, `slug`, `category_id`, `points`, `stock`, `description`, `terms`, `tag`, `delivery_days`, `rating`, `total_redeemed`, `is_active`, `created_at`, `updated_at`) VALUES
(4, 'Eco-Friendly Bamboo Coffee Cup', 'eco-friendly-bamboo-coffee-cup', 3, 500, 2, 'Reusable bamboo coffee cup to reduce plastic waste.', 'Can be redeemed once per month.', 'Popular', '3-5', 4.8, 0, 1, '2026-04-30 14:00:21', '2026-05-08 17:16:41'),
(5, 'Recycled Plastic Laptop Sleeve', 'recycled-plastic-laptop-sleeve', 3, 1200, 50, 'Sleek modern laptop sleeve made from recycled ocean plastics.', 'Non-refundable.', 'Premium', '5-7', 4.9, 50, 1, '2026-04-30 14:00:21', '2026-05-06 12:39:22'),
(6, '$50 Amazon Gift Card', '50-amazon-gift-card', 1, 5000, 100, 'Redeemable for millions of items on Amazon.com.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:54', '2026-05-26 13:04:54'),
(7, '$25 Starbucks Gift Card', '25-starbucks-gift-card', 1, 2500, 50, 'Enjoy your favorite coffee and treats at Starbucks.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:54', '2026-05-26 13:04:54'),
(8, '$50 Netflix Gift Card', '50-netflix-gift-card', 1, 5000, 30, 'Watch your favorite movies and shows on Netflix.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-05-26 13:04:53'),
(9, 'Wireless Optical Mouse', 'wireless-optical-mouse', 2, 1200, 40, 'Ergonomic 2.4GHz wireless mouse with adjustable DPI.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(10, '10-in-1 USB-C Hub', '10-in-1-usb-c-hub', 2, 3500, 25, 'Expand your laptop connectivity with HDMI, USB 3.0, and SD card slots.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(11, '65W Fast Wall Charger', '65w-fast-wall-charger', 2, 1800, 60, 'Compact GaN charger for fast charging your laptop and phone.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(12, 'Bamboo Cutlery Set', 'bamboo-cutlery-set', 3, 800, 80, 'Reusable bamboo spoon, fork, and knife set with a travel pouch.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(13, 'Stainless Steel Straws', 'stainless-steel-straws', 3, 600, 150, 'Set of 4 reusable straws with a cleaning brush.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(14, 'Organic Cotton Tote Bag', 'organic-cotton-tote-bag', 3, 500, 200, 'Durable and eco-friendly shopping bag made from 100% organic cotton.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(15, 'Slim RFID Leather Wallet', 'slim-rfid-leather-wallet', 4, 2200, 35, 'Premium leather wallet with RFID blocking technology.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(16, 'Waterproof Laptop Sleeve', 'waterproof-laptop-sleeve', 4, 1500, 45, 'Sleek and protective sleeve for 13-15 inch laptops.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(17, 'Cable Management Box', 'cable-management-box', 4, 1100, 55, 'Hide messy cables and power strips for a clean desk setup.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(18, 'Portable Air Purifier', 'portable-air-purifier', 5, 4500, 10, 'HEPA filter air purifier for personal use in small rooms.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(19, 'Smart Electric Kettle', 'smart-electric-kettle', 5, 3200, 20, 'Temperature controlled kettle with smartphone integration.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(20, 'Ultrasonic Humidifier', 'ultrasonic-humidifier', 5, 2800, 25, 'Quiet mist humidifier for better air quality at home.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(21, 'Tempered Glass Protector', 'tempered-glass-protector', 6, 400, 300, 'High-clarity screen protector for latest smartphone models.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(22, 'Adjustable Phone Stand', 'adjustable-phone-stand', 6, 700, 100, 'Multi-angle foldable stand for phones and tablets.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(23, 'Bluetooth Selfie Stick', 'bluetooth-selfie-stick', 6, 1300, 40, 'Extendable selfie stick with a detachable remote control.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(24, 'Mechanical RGB Keyboard', 'mechanical-rgb-keyboard', 7, 5500, 15, 'Tactile mechanical keys with customizable RGB lighting.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(25, 'Gaming Mouse Pad (Large)', 'gaming-mouse-pad-large', 7, 1400, 50, 'Extended mouse pad with a smooth surface for precision gaming.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(26, 'Console Skin Wrap', 'console-skin-wrap', 7, 900, 70, 'Protective vinyl wrap for your favorite gaming console.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(27, 'Non-Slip Yoga Mat', 'non-slip-yoga-mat', 8, 2500, 30, 'High-density yoga mat for better cushioning and grip.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55'),
(28, 'Resistance Band Set', 'resistance-band-set', 8, 1600, 60, 'Set of 5 resistance bands for home workouts.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-05-06 11:47:35'),
(29, 'Digital Jump Rope', 'digital-jump-rope', 8, 1900, 40, 'Jump rope with a built-in counter for tracking your fitness.', NULL, NULL, NULL, 0.0, 0, 1, '2026-04-30 15:35:55', '2026-04-30 15:35:55');

-- --------------------------------------------------------

--
-- Table structure for table `reward_product_images`
--

CREATE TABLE `reward_product_images` (
  `id` int(11) NOT NULL COMMENT 'Unique image ID',
  `product_id` int(11) NOT NULL COMMENT 'Reference to reward_products table',
  `image` varchar(255) NOT NULL COMMENT 'Image file path or URL',
  `is_primary` tinyint(1) DEFAULT 0 COMMENT 'Main image for product listing',
  `display_order` int(11) DEFAULT 1 COMMENT 'Order of image display (1 = first image)',
  `is_active` tinyint(1) NOT NULL DEFAULT 1 COMMENT '-- Status (1 = Active, 0 = Inactive)	',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Image upload time',
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Last updated time when image or order changes'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reward_product_images`
--

INSERT INTO `reward_product_images` (`id`, `product_id`, `image`, `is_primary`, `display_order`, `is_active`, `created_at`, `updated_at`) VALUES
(24, 4, 'app_9_Reward_Products/Reward_Product_images/product_4_Eco-Friendly_Bamboo_Coffee_Cup/bam_PtJq3rP.png', 1, 1, 1, '2026-04-30 14:00:21', '2026-05-06 12:51:11'),
(25, 5, 'app_9_Reward_Products/Reward_Product_images/product_5_Recycled_Plastic_Laptop_Sleeve/rec_mPu9Kkq.png', 1, 1, 1, '2026-04-30 14:00:21', '2026-05-24 14:17:26'),
(26, 4, 'app_9_Reward_Products/Reward_Product_images/product_4_Eco-Friendly_Bamboo_Coffee_Cup/bam_6jEQrKN.png', 0, 2, 1, '2026-04-30 14:10:29', '2026-05-06 18:21:11'),
(27, 4, 'app_9_Reward_Products/Reward_Product_images/product_4_Eco-Friendly_Bamboo_Coffee_Cup/bam_kDD4umc.png', 0, 3, 1, '2026-04-30 14:10:29', '2026-04-30 14:10:29'),
(28, 4, 'app_9_Reward_Products/Reward_Product_images/product_4_Eco-Friendly_Bamboo_Coffee_Cup/bam_VdVI21R.png', 0, 4, 1, '2026-04-30 14:10:29', '2026-04-30 14:10:29'),
(29, 4, 'app_9_Reward_Products/Reward_Product_images/product_4_Eco-Friendly_Bamboo_Coffee_Cup/bam_UTAfqQs.png', 0, 5, 1, '2026-04-30 14:10:29', '2026-04-30 17:33:27'),
(30, 4, 'app_9_Reward_Products/Reward_Product_images/product_4_Eco-Friendly_Bamboo_Coffee_Cup/bam_5WClTdo.png', 0, 6, 1, '2026-04-30 14:10:29', '2026-04-30 14:10:29'),
(31, 5, 'app_9_Reward_Products/Reward_Product_images/product_5_Recycled_Plastic_Laptop_Sleeve/rec_DUJBDE0.png', 0, 2, 1, '2026-04-30 14:10:29', '2026-05-24 19:47:26'),
(32, 5, 'app_9_Reward_Products/Reward_Product_images/product_5_Recycled_Plastic_Laptop_Sleeve/rec_JE0GsbU.png', 0, 3, 1, '2026-04-30 14:10:29', '2026-04-30 14:10:29'),
(33, 5, 'app_9_Reward_Products/Reward_Product_images/product_5_Recycled_Plastic_Laptop_Sleeve/rec_8YHxiia.png', 0, 4, 1, '2026-04-30 14:10:29', '2026-04-30 14:10:29'),
(34, 5, 'app_9_Reward_Products/Reward_Product_images/product_5_Recycled_Plastic_Laptop_Sleeve/rec_iBeIshr.png', 0, 5, 1, '2026-04-30 14:10:29', '2026-04-30 14:10:29'),
(35, 5, 'app_9_Reward_Products/Reward_Product_images/product_5_Recycled_Plastic_Laptop_Sleeve/rec_Zd6VJua.png', 0, 6, 1, '2026-04-30 14:10:29', '2026-04-30 14:10:29'),
(39, 6, 'app_9_Reward_Products/Reward_Product_images/product_6_$50_Amazon_Gift_Card/p6_img1.jpg', 1, 1, 1, '2026-04-30 15:53:27', '2026-04-30 15:53:27'),
(40, 6, 'app_9_Reward_Products/Reward_Product_images/product_6_$50_Amazon_Gift_Card/p6_img2.jpg', 0, 2, 1, '2026-04-30 15:53:32', '2026-04-30 15:53:32'),
(41, 6, 'app_9_Reward_Products/Reward_Product_images/product_6_$50_Amazon_Gift_Card/p6_img3.jpg', 0, 3, 1, '2026-04-30 15:53:38', '2026-04-30 15:53:38'),
(42, 6, 'app_9_Reward_Products/Reward_Product_images/product_6_$50_Amazon_Gift_Card/p6_img4.jpg', 0, 4, 1, '2026-04-30 15:53:42', '2026-04-30 15:53:42'),
(43, 6, 'app_9_Reward_Products/Reward_Product_images/product_6_$50_Amazon_Gift_Card/p6_img5.jpg', 0, 5, 1, '2026-04-30 15:53:48', '2026-04-30 15:53:48'),
(44, 6, 'app_9_Reward_Products/Reward_Product_images/product_6_$50_Amazon_Gift_Card/p6_img6.jpg', 0, 6, 1, '2026-04-30 15:53:52', '2026-04-30 15:53:52'),
(45, 7, 'app_9_Reward_Products/Reward_Product_images/product_7_$25_Starbucks_Gift_Card/p7_img1.jpg', 0, 1, 1, '2026-04-30 15:53:53', '2026-05-22 11:16:30'),
(46, 7, 'app_9_Reward_Products/Reward_Product_images/product_7_$25_Starbucks_Gift_Card/p7_img2.jpg', 1, 2, 1, '2026-04-30 15:53:56', '2026-05-22 05:46:30'),
(47, 7, 'app_9_Reward_Products/Reward_Product_images/product_7_$25_Starbucks_Gift_Card/p7_img3.jpg', 0, 3, 1, '2026-04-30 15:54:01', '2026-04-30 15:54:01'),
(48, 7, 'app_9_Reward_Products/Reward_Product_images/product_7_$25_Starbucks_Gift_Card/p7_img4.jpg', 0, 4, 1, '2026-04-30 15:54:05', '2026-04-30 15:54:05'),
(49, 7, 'app_9_Reward_Products/Reward_Product_images/product_7_$25_Starbucks_Gift_Card/p7_img5.jpg', 0, 5, 1, '2026-04-30 15:54:08', '2026-04-30 15:54:08'),
(51, 8, 'app_9_Reward_Products/Reward_Product_images/product_8_$50_Netflix_Gift_Card/p8_img1.jpg', 1, 1, 1, '2026-04-30 15:54:17', '2026-05-26 13:05:15'),
(52, 8, 'app_9_Reward_Products/Reward_Product_images/product_8_$50_Netflix_Gift_Card/p8_img2.jpg', 0, 2, 1, '2026-04-30 15:54:23', '2026-05-26 13:05:26'),
(53, 8, 'app_9_Reward_Products/Reward_Product_images/product_8_$50_Netflix_Gift_Card/p8_img3.jpg', 0, 4, 1, '2026-04-30 15:54:26', '2026-05-26 13:05:44'),
(54, 8, 'app_9_Reward_Products/Reward_Product_images/product_8_$50_Netflix_Gift_Card/p8_img4.jpg', 0, 3, 1, '2026-04-30 15:54:29', '2026-05-26 18:35:44'),
(55, 8, 'app_9_Reward_Products/Reward_Product_images/product_8_$50_Netflix_Gift_Card/p8_img5.jpg', 0, 5, 1, '2026-04-30 15:54:31', '2026-05-26 13:05:29'),
(56, 8, 'app_9_Reward_Products/Reward_Product_images/product_8_$50_Netflix_Gift_Card/p8_img6.jpg', 0, 6, 1, '2026-04-30 15:54:33', '2026-05-26 13:05:32'),
(57, 9, 'app_9_Reward_Products/Reward_Product_images/product_9_Wireless_Optical_Mouse/p9_img1.jpg', 1, 1, 1, '2026-04-30 15:54:39', '2026-04-30 15:54:39'),
(58, 9, 'app_9_Reward_Products/Reward_Product_images/product_9_Wireless_Optical_Mouse/p9_img2.jpg', 0, 2, 1, '2026-04-30 15:54:42', '2026-04-30 15:54:42'),
(59, 9, 'app_9_Reward_Products/Reward_Product_images/product_9_Wireless_Optical_Mouse/p9_img3.jpg', 0, 3, 1, '2026-04-30 15:54:47', '2026-04-30 15:54:47'),
(60, 9, 'app_9_Reward_Products/Reward_Product_images/product_9_Wireless_Optical_Mouse/p9_img4.jpg', 0, 4, 1, '2026-04-30 15:54:49', '2026-04-30 15:54:49'),
(61, 9, 'app_9_Reward_Products/Reward_Product_images/product_9_Wireless_Optical_Mouse/p9_img5.jpg', 0, 5, 1, '2026-04-30 15:54:50', '2026-04-30 15:54:50'),
(62, 9, 'app_9_Reward_Products/Reward_Product_images/product_9_Wireless_Optical_Mouse/p9_img6.jpg', 0, 6, 1, '2026-04-30 15:54:52', '2026-04-30 15:54:52'),
(63, 10, 'app_9_Reward_Products/Reward_Product_images/product_10_10-in-1_USB-C_Hub/p10_img1.jpg', 1, 1, 1, '2026-04-30 15:54:55', '2026-04-30 15:54:55'),
(64, 10, 'app_9_Reward_Products/Reward_Product_images/product_10_10-in-1_USB-C_Hub/p10_img2.jpg', 0, 2, 1, '2026-04-30 15:55:00', '2026-04-30 15:55:00'),
(65, 10, 'app_9_Reward_Products/Reward_Product_images/product_10_10-in-1_USB-C_Hub/p10_img3.jpg', 0, 3, 1, '2026-04-30 15:55:07', '2026-04-30 15:55:07'),
(66, 10, 'app_9_Reward_Products/Reward_Product_images/product_10_10-in-1_USB-C_Hub/p10_img4.jpg', 0, 4, 1, '2026-04-30 15:55:13', '2026-04-30 15:55:13'),
(67, 10, 'app_9_Reward_Products/Reward_Product_images/product_10_10-in-1_USB-C_Hub/p10_img5.jpg', 0, 5, 1, '2026-04-30 15:55:19', '2026-04-30 15:55:19'),
(68, 10, 'app_9_Reward_Products/Reward_Product_images/product_10_10-in-1_USB-C_Hub/p10_img6.jpg', 0, 6, 1, '2026-04-30 15:55:21', '2026-04-30 15:55:21'),
(69, 11, 'app_9_Reward_Products/Reward_Product_images/product_11_65W_Fast_Wall_Charger/p11_img1.jpg', 1, 1, 1, '2026-04-30 15:55:22', '2026-05-23 12:31:53'),
(70, 11, 'app_9_Reward_Products/Reward_Product_images/product_11_65W_Fast_Wall_Charger/p11_img2.jpg', 0, 2, 1, '2026-04-30 15:55:24', '2026-04-30 15:55:24'),
(71, 11, 'app_9_Reward_Products/Reward_Product_images/product_11_65W_Fast_Wall_Charger/p11_img3.jpg', 0, 3, 1, '2026-04-30 15:55:30', '2026-05-01 13:10:17'),
(72, 11, 'app_9_Reward_Products/Reward_Product_images/product_11_65W_Fast_Wall_Charger/p11_img4.jpg', 0, 4, 1, '2026-04-30 15:55:35', '2026-04-30 15:55:35'),
(73, 11, 'app_9_Reward_Products/Reward_Product_images/product_11_65W_Fast_Wall_Charger/p11_img5.jpg', 0, 5, 1, '2026-04-30 15:55:41', '2026-04-30 15:55:41'),
(75, 12, 'app_9_Reward_Products/Reward_Product_images/product_12_Bamboo_Cutlery_Set/p12_img1.jpg', 1, 1, 1, '2026-04-30 15:55:45', '2026-04-30 15:55:45'),
(76, 12, 'app_9_Reward_Products/Reward_Product_images/product_12_Bamboo_Cutlery_Set/p12_img2.jpg', 0, 2, 1, '2026-04-30 15:55:47', '2026-04-30 15:55:47'),
(77, 12, 'app_9_Reward_Products/Reward_Product_images/product_12_Bamboo_Cutlery_Set/p12_img3.jpg', 0, 3, 1, '2026-04-30 15:55:48', '2026-04-30 15:55:48'),
(78, 12, 'app_9_Reward_Products/Reward_Product_images/product_12_Bamboo_Cutlery_Set/p12_img4.jpg', 0, 4, 1, '2026-04-30 15:55:50', '2026-04-30 15:55:50'),
(79, 12, 'app_9_Reward_Products/Reward_Product_images/product_12_Bamboo_Cutlery_Set/p12_img5.jpg', 0, 5, 1, '2026-04-30 15:55:52', '2026-04-30 15:55:52'),
(80, 12, 'app_9_Reward_Products/Reward_Product_images/product_12_Bamboo_Cutlery_Set/p12_img6.jpg', 0, 6, 1, '2026-04-30 15:55:54', '2026-04-30 15:55:54'),
(81, 13, 'app_9_Reward_Products/Reward_Product_images/product_13_Stainless_Steel_Straws/p13_img1.jpg', 1, 1, 1, '2026-04-30 15:55:57', '2026-04-30 15:55:57'),
(82, 13, 'app_9_Reward_Products/Reward_Product_images/product_13_Stainless_Steel_Straws/p13_img2.jpg', 0, 2, 1, '2026-04-30 15:56:01', '2026-04-30 15:56:01'),
(83, 13, 'app_9_Reward_Products/Reward_Product_images/product_13_Stainless_Steel_Straws/p13_img3.jpg', 0, 3, 1, '2026-04-30 15:56:02', '2026-04-30 15:56:02'),
(84, 13, 'app_9_Reward_Products/Reward_Product_images/product_13_Stainless_Steel_Straws/p13_img4.jpg', 0, 4, 1, '2026-04-30 15:56:04', '2026-04-30 15:56:04'),
(85, 13, 'app_9_Reward_Products/Reward_Product_images/product_13_Stainless_Steel_Straws/p13_img5.jpg', 0, 5, 1, '2026-04-30 15:56:06', '2026-04-30 15:56:06'),
(86, 13, 'app_9_Reward_Products/Reward_Product_images/product_13_Stainless_Steel_Straws/p13_img6.jpg', 0, 6, 1, '2026-04-30 15:56:11', '2026-04-30 15:56:11'),
(87, 14, 'app_9_Reward_Products/Reward_Product_images/product_14_Organic_Cotton_Tote_Bag/p14_img1.jpg', 1, 1, 1, '2026-04-30 15:56:14', '2026-04-30 15:56:14'),
(88, 14, 'app_9_Reward_Products/Reward_Product_images/product_14_Organic_Cotton_Tote_Bag/p14_img2.jpg', 0, 2, 1, '2026-04-30 15:56:18', '2026-04-30 15:56:18'),
(89, 14, 'app_9_Reward_Products/Reward_Product_images/product_14_Organic_Cotton_Tote_Bag/p14_img3.jpg', 0, 3, 1, '2026-04-30 15:56:21', '2026-04-30 15:56:21'),
(90, 14, 'app_9_Reward_Products/Reward_Product_images/product_14_Organic_Cotton_Tote_Bag/p14_img4.jpg', 0, 4, 1, '2026-04-30 15:56:23', '2026-04-30 15:56:23'),
(91, 14, 'app_9_Reward_Products/Reward_Product_images/product_14_Organic_Cotton_Tote_Bag/p14_img5.jpg', 0, 5, 1, '2026-04-30 15:56:24', '2026-04-30 15:56:24'),
(92, 14, 'app_9_Reward_Products/Reward_Product_images/product_14_Organic_Cotton_Tote_Bag/p14_img6.jpg', 0, 6, 1, '2026-04-30 15:56:26', '2026-04-30 15:56:26'),
(93, 15, 'app_9_Reward_Products/Reward_Product_images/product_15_Slim_RFID_Leather_Wallet/p15_img1.jpg', 1, 1, 1, '2026-04-30 15:56:29', '2026-04-30 15:56:29'),
(94, 15, 'app_9_Reward_Products/Reward_Product_images/product_15_Slim_RFID_Leather_Wallet/p15_img2.jpg', 0, 2, 1, '2026-04-30 15:56:31', '2026-04-30 15:56:31'),
(95, 15, 'app_9_Reward_Products/Reward_Product_images/product_15_Slim_RFID_Leather_Wallet/p15_img3.jpg', 0, 3, 1, '2026-04-30 15:56:37', '2026-04-30 15:56:37'),
(96, 15, 'app_9_Reward_Products/Reward_Product_images/product_15_Slim_RFID_Leather_Wallet/p15_img4.jpg', 0, 4, 1, '2026-04-30 15:56:42', '2026-04-30 15:56:42'),
(97, 15, 'app_9_Reward_Products/Reward_Product_images/product_15_Slim_RFID_Leather_Wallet/p15_img5.jpg', 0, 5, 1, '2026-04-30 15:56:47', '2026-04-30 15:56:47'),
(98, 15, 'app_9_Reward_Products/Reward_Product_images/product_15_Slim_RFID_Leather_Wallet/p15_img6.jpg', 0, 6, 1, '2026-04-30 15:56:52', '2026-04-30 15:56:52'),
(99, 16, 'app_9_Reward_Products/Reward_Product_images/product_16_Waterproof_Laptop_Sleeve/p16_img1.jpg', 1, 1, 1, '2026-04-30 15:56:55', '2026-04-30 15:56:55'),
(100, 16, 'app_9_Reward_Products/Reward_Product_images/product_16_Waterproof_Laptop_Sleeve/p16_img2.jpg', 0, 2, 1, '2026-04-30 15:56:57', '2026-04-30 15:56:57'),
(101, 16, 'app_9_Reward_Products/Reward_Product_images/product_16_Waterproof_Laptop_Sleeve/p16_img3.jpg', 0, 3, 1, '2026-04-30 15:56:58', '2026-04-30 15:56:58'),
(102, 16, 'app_9_Reward_Products/Reward_Product_images/product_16_Waterproof_Laptop_Sleeve/p16_img4.jpg', 0, 4, 1, '2026-04-30 15:56:59', '2026-04-30 15:56:59'),
(103, 16, 'app_9_Reward_Products/Reward_Product_images/product_16_Waterproof_Laptop_Sleeve/p16_img5.jpg', 0, 5, 1, '2026-04-30 15:57:01', '2026-04-30 15:57:01'),
(104, 16, 'app_9_Reward_Products/Reward_Product_images/product_16_Waterproof_Laptop_Sleeve/p16_img6.jpg', 0, 6, 1, '2026-04-30 15:57:04', '2026-04-30 15:57:04'),
(105, 17, 'app_9_Reward_Products/Reward_Product_images/product_17_Cable_Management_Box/p17_img1.jpg', 1, 1, 1, '2026-04-30 15:57:08', '2026-04-30 15:57:08'),
(106, 17, 'app_9_Reward_Products/Reward_Product_images/product_17_Cable_Management_Box/p17_img2.jpg', 0, 2, 1, '2026-04-30 15:57:13', '2026-04-30 15:57:13'),
(107, 17, 'app_9_Reward_Products/Reward_Product_images/product_17_Cable_Management_Box/p17_img3.jpg', 0, 3, 1, '2026-04-30 15:57:20', '2026-04-30 15:57:20');

-- --------------------------------------------------------

--
-- Table structure for table `reward_rules`
--

CREATE TABLE `reward_rules` (
  `id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL COMMENT 'FK: recycling_info id',
  `condition_id` int(11) NOT NULL COMMENT 'FK: item_conditions id',
  `points` int(11) NOT NULL COMMENT 'Base points for calculation',
  `unit` enum('Item','Kg') NOT NULL COMMENT 'item = fixed, kg = per kg calculation',
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Stores reward points based on category and item condition';

--
-- Dumping data for table `reward_rules`
--

INSERT INTO `reward_rules` (`id`, `category_id`, `condition_id`, `points`, `unit`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 2, 1, 1500, 'Item', 1, '2026-04-01 13:55:24', '2026-04-04 01:03:55'),
(2, 2, 2, 1000, 'Item', 1, '2026-04-03 11:38:16', '2026-04-04 06:37:00'),
(3, 2, 3, 600, 'Item', 1, '2026-04-03 12:36:33', '2026-04-04 01:46:26'),
(4, 2, 4, 300, 'Item', 1, '2026-04-04 01:46:58', '2026-04-04 01:46:58'),
(5, 2, 5, 150, 'Item', 1, '2026-04-04 01:47:12', '2026-04-04 01:47:12'),
(6, 1, 1, 800, 'Item', 1, '2026-04-04 06:35:00', '2026-04-04 06:35:00'),
(7, 1, 2, 500, 'Item', 1, '2026-04-04 06:35:11', '2026-04-04 06:35:11'),
(8, 1, 3, 300, 'Item', 1, '2026-04-04 06:35:33', '2026-04-04 06:35:33'),
(9, 1, 4, 150, 'Item', 1, '2026-04-04 06:35:43', '2026-04-04 06:35:43'),
(10, 1, 5, 80, 'Item', 1, '2026-04-04 06:35:57', '2026-04-04 06:37:24'),
(11, 3, 1, 120, 'Kg', 1, '2026-04-04 06:39:35', '2026-04-04 06:39:35'),
(12, 3, 2, 100, 'Kg', 1, '2026-04-04 06:39:48', '2026-04-04 06:39:48'),
(13, 3, 3, 80, 'Kg', 1, '2026-04-04 06:40:05', '2026-04-04 06:40:05'),
(14, 3, 4, 60, 'Kg', 1, '2026-04-04 06:40:22', '2026-04-04 06:40:22'),
(15, 3, 5, 45, 'Kg', 1, '2026-04-04 06:40:36', '2026-04-04 06:40:36'),
(16, 4, 1, 100, 'Kg', 1, '2026-04-04 06:41:03', '2026-04-04 06:41:03'),
(17, 4, 2, 80, 'Kg', 1, '2026-04-04 06:41:17', '2026-04-04 06:41:17'),
(18, 4, 3, 60, 'Kg', 1, '2026-04-04 06:41:40', '2026-04-04 06:41:40'),
(19, 4, 4, 40, 'Kg', 1, '2026-04-04 06:41:53', '2026-04-04 06:41:53'),
(20, 4, 5, 30, 'Kg', 1, '2026-04-04 06:42:05', '2026-04-04 06:42:05'),
(21, 5, 1, 60, 'Kg', 1, '2026-04-04 06:42:31', '2026-04-04 06:42:31'),
(22, 5, 2, 50, 'Kg', 1, '2026-04-04 06:42:45', '2026-04-04 06:42:45'),
(23, 5, 3, 40, 'Kg', 1, '2026-04-04 06:43:03', '2026-04-04 06:43:03'),
(24, 5, 4, 30, 'Kg', 1, '2026-04-04 06:43:32', '2026-04-04 06:43:32'),
(25, 5, 5, 25, 'Kg', 1, '2026-04-04 06:43:41', '2026-04-04 06:43:41'),
(26, 6, 1, 400, 'Item', 1, '2026-05-04 07:01:38', '2026-05-04 07:01:38'),
(27, 6, 2, 250, 'Item', 1, '2026-05-04 07:01:55', '2026-05-04 07:01:55'),
(28, 6, 3, 150, 'Item', 1, '2026-05-04 07:02:34', '2026-05-04 07:02:34'),
(29, 6, 4, 80, 'Item', 1, '2026-05-04 07:02:53', '2026-05-04 07:02:53'),
(30, 6, 5, 40, 'Item', 1, '2026-05-04 07:03:06', '2026-05-26 08:03:25');

-- --------------------------------------------------------

--
-- Table structure for table `reward_transactions`
--

CREATE TABLE `reward_transactions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL COMMENT 'FK to auth_user.id',
  `submission_id` int(11) DEFAULT NULL,
  `order_id` int(11) DEFAULT NULL,
  `points` int(11) NOT NULL COMMENT 'Points earned',
  `type` enum('credit','debit') DEFAULT 'credit',
  `description` varchar(255) DEFAULT NULL COMMENT 'Reason for points (e.g., Recycling Reward)',
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reward_transactions`
--

INSERT INTO `reward_transactions` (`id`, `user_id`, `submission_id`, `order_id`, `points`, `type`, `description`, `created_at`) VALUES
(25, 1, 33, NULL, 6870, 'credit', 'Base: 80 × 84kg = 6720 | Bonus: 34kg extra → 3×50 = 150 | Total = 6870', '2026-04-30 13:43:10'),
(26, 53, 34, NULL, 300, 'credit', 'Base: 300 (per item)', '2026-05-03 17:36:02'),
(27, 54, 35, NULL, 3750, 'credit', 'Base: 45 × 80kg = 3600 | Bonus: 30kg extra → 3×50 = 150 | Total = 3750', '2026-05-03 17:56:04'),
(28, 54, 37, NULL, 3250, 'credit', 'Base: 30 × 100kg = 3000 | Bonus: 50kg extra → 5×50 = 250 | Total = 3250', '2026-05-03 18:11:39'),
(29, 54, 38, NULL, 400, 'credit', 'Base: 400 (per item)', '2026-05-04 12:35:50'),
(30, 54, 40, NULL, 4000, 'credit', 'Base: 40 × 95kg = 3800 | Bonus: 45kg extra → 4×50 = 200 | Total = 4000', '2026-05-04 14:03:32'),
(32, 1, 43, NULL, 6550, 'credit', 'Base: 80 × 80kg = 6400 | Bonus: 30kg extra → 3×50 = 150 | Total = 6550', '2026-05-09 19:11:21'),
(33, 54, 44, NULL, 600, 'credit', 'Base: 600 (per item)', '2026-05-09 19:14:08'),
(34, 54, NULL, NULL, 8900, 'credit', 'Refund for cancelled order ECO-20260509185255', '2026-05-10 03:55:58'),
(43, 54, NULL, NULL, 800, 'credit', 'Refund for cancelled order ECO-20260516144610', '2026-05-16 14:52:30'),
(47, 54, NULL, NULL, 1700, 'credit', 'Refund for cancelled order ECO-20260516172441', '2026-05-16 17:25:47'),
(58, 54, NULL, NULL, 1600, 'credit', 'Refund for cancelled order ECO-20260516180141', '2026-05-16 18:17:18'),
(60, 54, NULL, NULL, 2500, 'credit', 'Refund for cancelled order ECO-20260516181758', '2026-05-16 18:18:35'),
(73, 54, NULL, 45, 9700, 'debit', 'Reward order ECO-20260524120036', '2026-05-24 12:00:36'),
(74, 54, NULL, 45, 2400, 'credit', 'Points Refunded for Return Request RET-20260524120503', '2026-05-24 12:07:42'),
(75, 54, NULL, 46, 1200, 'debit', 'Reward order ECO-20260524121117', '2026-05-24 12:11:17'),
(76, 54, 46, NULL, 300, 'credit', 'Base: 300 (per item)', '2026-05-24 13:34:04'),
(77, 54, NULL, 47, 1000, 'debit', 'Reward order ECO-20260524134108', '2026-05-24 13:41:08'),
(78, 54, NULL, 47, 1000, 'credit', 'Points Refunded for Return Request RET-20260524135909', '2026-05-24 14:01:44'),
(79, 54, NULL, 48, 6500, 'debit', 'Reward order ECO-20260526122424', '2026-05-26 12:24:24');

-- --------------------------------------------------------

--
-- Table structure for table `user_wallet`
--

CREATE TABLE `user_wallet` (
  `id` int(11) NOT NULL COMMENT 'Wallet record ID',
  `user_id` int(11) NOT NULL COMMENT 'Reference to user (auth user id)',
  `total_points` int(11) DEFAULT 0 COMMENT 'Current available points balance',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Wallet created time',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Last updated time'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_wallet`
--

INSERT INTO `user_wallet` (`id`, `user_id`, `total_points`, `created_at`, `updated_at`) VALUES
(1, 1, 22450, '2026-04-27 15:24:18', '2026-05-09 19:11:21'),
(2, 52, 2300, '2026-04-28 16:01:28', '2026-05-11 06:19:01'),
(3, 53, 300, '2026-05-03 17:36:02', '2026-05-03 17:36:02'),
(4, 54, 300, '2026-05-03 17:56:04', '2026-05-26 12:24:24');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_user_profile`
--
ALTER TABLE `accounts_user_profile`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_user_profile_user` (`table_auth_user_id`) USING BTREE;

--
-- Indexes for table `app_1_users_user`
--
ALTER TABLE `app_1_users_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `app_1_users_user_groups`
--
ALTER TABLE `app_1_users_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `app_1_users_user_groups_user_id_group_id_4dc1e809_uniq` (`user_id`,`group_id`),
  ADD KEY `app_1_users_user_groups_group_id_28cfac3e_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `app_1_users_user_user_permissions`
--
ALTER TABLE `app_1_users_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `app_1_users_user_user_pe_user_id_permission_id_93ee56ee_uniq` (`user_id`,`permission_id`),
  ADD KEY `app_1_users_user_use_permission_id_3f68ea7f_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `app_2_e_facility_user`
--
ALTER TABLE `app_2_e_facility_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `app_2_e_facility_user_groups`
--
ALTER TABLE `app_2_e_facility_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `app_2_e_Facility_user_groups_user_id_group_id_14ff19ad_uniq` (`user_id`,`group_id`),
  ADD KEY `app_2_e_Facility_user_groups_group_id_381e3f22_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `app_2_e_facility_user_user_permissions`
--
ALTER TABLE `app_2_e_facility_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `app_2_e_Facility_user_us_user_id_permission_id_1c479953_uniq` (`user_id`,`permission_id`),
  ADD KEY `app_2_e_Facility_use_permission_id_81b35a2d_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `brand`
--
ALTER TABLE `brand`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `category_brand_mapping`
--
ALTER TABLE `category_brand_mapping`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_category_brand` (`category_id`,`brand_id`),
  ADD KEY `brand_id` (`brand_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `education_article`
--
ALTER TABLE `education_article`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `e_waste_status_history`
--
ALTER TABLE `e_waste_status_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `submission_id` (`submission_id`),
  ADD KEY `changed_by` (`changed_by`);

--
-- Indexes for table `e_waste_submission`
--
ALTER TABLE `e_waste_submission`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `category_id` (`category_id`),
  ADD KEY `category_brand_mapping_id` (`category_brand_mapping_id`),
  ADD KEY `model_id` (`model_id`),
  ADD KEY `user_condition_id` (`user_condition_id`),
  ADD KEY `final_condition_id` (`final_condition_id`),
  ADD KEY `facility_id` (`facility_id`);

--
-- Indexes for table `e_waste_submission_images`
--
ALTER TABLE `e_waste_submission_images`
  ADD PRIMARY KEY (`id`),
  ADD KEY `submission_id` (`submission_id`);

--
-- Indexes for table `facility`
--
ALTER TABLE `facility`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `home_page_hero_image`
--
ALTER TABLE `home_page_hero_image`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `home_page_how_it_works`
--
ALTER TABLE `home_page_how_it_works`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `item_conditions`
--
ALTER TABLE `item_conditions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product_model`
--
ALTER TABLE `product_model`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_brand_mapping_id` (`category_brand_mapping_id`);

--
-- Indexes for table `product_model_name`
--
ALTER TABLE `product_model_name`
  ADD PRIMARY KEY (`id`),
  ADD KEY `brand_id` (`brand_id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `recycle_category`
--
ALTER TABLE `recycle_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `recycling_info`
--
ALTER TABLE `recycling_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reward_cart`
--
ALTER TABLE `reward_cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_reward_cart_user` (`user_id`);

--
-- Indexes for table `reward_cart_items`
--
ALTER TABLE `reward_cart_items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_cart_items_cart` (`cart_id`),
  ADD KEY `fk_cart_items_product` (`product_id`);

--
-- Indexes for table `reward_category`
--
ALTER TABLE `reward_category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `reward_orders`
--
ALTER TABLE `reward_orders`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `order_number` (`order_number`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `cart_id` (`cart_id`);

--
-- Indexes for table `reward_order_address`
--
ALTER TABLE `reward_order_address`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`);

--
-- Indexes for table `reward_order_items`
--
ALTER TABLE `reward_order_items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `reward_order_payments`
--
ALTER TABLE `reward_order_payments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`);

--
-- Indexes for table `reward_order_replace_images`
--
ALTER TABLE `reward_order_replace_images`
  ADD PRIMARY KEY (`id`),
  ADD KEY `replace_request_id` (`replace_request_id`);

--
-- Indexes for table `reward_order_replace_items`
--
ALTER TABLE `reward_order_replace_items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `replace_request_id` (`replace_request_id`),
  ADD KEY `order_item_id` (`order_item_id`);

--
-- Indexes for table `reward_order_replace_pickups`
--
ALTER TABLE `reward_order_replace_pickups`
  ADD PRIMARY KEY (`id`),
  ADD KEY `replace_request_id` (`replace_request_id`),
  ADD KEY `order_address_id` (`order_address_id`);

--
-- Indexes for table `reward_order_replace_requests`
--
ALTER TABLE `reward_order_replace_requests`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `replace_number` (`replace_number`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `reward_order_replace_status_history`
--
ALTER TABLE `reward_order_replace_status_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `replace_request_id` (`replace_request_id`),
  ADD KEY `changed_by` (`changed_by`);

--
-- Indexes for table `reward_order_return_images`
--
ALTER TABLE `reward_order_return_images`
  ADD PRIMARY KEY (`id`),
  ADD KEY `return_request_id` (`return_request_id`);

--
-- Indexes for table `reward_order_return_items`
--
ALTER TABLE `reward_order_return_items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `return_request_id` (`return_request_id`),
  ADD KEY `order_item_id` (`order_item_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `reward_order_return_pickups`
--
ALTER TABLE `reward_order_return_pickups`
  ADD PRIMARY KEY (`id`),
  ADD KEY `return_request_id` (`return_request_id`),
  ADD KEY `order_address_id` (`order_address_id`);

--
-- Indexes for table `reward_order_return_requests`
--
ALTER TABLE `reward_order_return_requests`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `return_number` (`return_number`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `reward_order_return_status_history`
--
ALTER TABLE `reward_order_return_status_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `return_request_id` (`return_request_id`);

--
-- Indexes for table `reward_order_status_history`
--
ALTER TABLE `reward_order_status_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_history_order_id` (`order_id`),
  ADD KEY `fk_history_changed_by` (`changed_by`);

--
-- Indexes for table `reward_products`
--
ALTER TABLE `reward_products`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `fk_product_category` (`category_id`);

--
-- Indexes for table `reward_product_images`
--
ALTER TABLE `reward_product_images`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_product_images` (`product_id`);

--
-- Indexes for table `reward_rules`
--
ALTER TABLE `reward_rules`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_rule` (`category_id`,`condition_id`),
  ADD KEY `fk_reward_condition` (`condition_id`);

--
-- Indexes for table `reward_transactions`
--
ALTER TABLE `reward_transactions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `submission_id` (`submission_id`);

--
-- Indexes for table `user_wallet`
--
ALTER TABLE `user_wallet`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_user_profile`
--
ALTER TABLE `accounts_user_profile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=83;

--
-- AUTO_INCREMENT for table `app_1_users_user`
--
ALTER TABLE `app_1_users_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_1_users_user_groups`
--
ALTER TABLE `app_1_users_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_1_users_user_user_permissions`
--
ALTER TABLE `app_1_users_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_2_e_facility_user`
--
ALTER TABLE `app_2_e_facility_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_2_e_facility_user_groups`
--
ALTER TABLE `app_2_e_facility_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_2_e_facility_user_user_permissions`
--
ALTER TABLE `app_2_e_facility_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `brand`
--
ALTER TABLE `brand`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `category_brand_mapping`
--
ALTER TABLE `category_brand_mapping`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `education_article`
--
ALTER TABLE `education_article`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `e_waste_status_history`
--
ALTER TABLE `e_waste_status_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=167;

--
-- AUTO_INCREMENT for table `e_waste_submission`
--
ALTER TABLE `e_waste_submission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `e_waste_submission_images`
--
ALTER TABLE `e_waste_submission_images`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=159;

--
-- AUTO_INCREMENT for table `facility`
--
ALTER TABLE `facility`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `home_page_hero_image`
--
ALTER TABLE `home_page_hero_image`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `home_page_how_it_works`
--
ALTER TABLE `home_page_how_it_works`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `item_conditions`
--
ALTER TABLE `item_conditions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `product_model`
--
ALTER TABLE `product_model`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `product_model_name`
--
ALTER TABLE `product_model_name`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;

--
-- AUTO_INCREMENT for table `recycle_category`
--
ALTER TABLE `recycle_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `recycling_info`
--
ALTER TABLE `recycling_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `reward_cart`
--
ALTER TABLE `reward_cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique cart ID', AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `reward_cart_items`
--
ALTER TABLE `reward_cart_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique cart item ID', AUTO_INCREMENT=116;

--
-- AUTO_INCREMENT for table `reward_category`
--
ALTER TABLE `reward_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `reward_orders`
--
ALTER TABLE `reward_orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key of order table', AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `reward_order_address`
--
ALTER TABLE `reward_order_address`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key of address table', AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `reward_order_items`
--
ALTER TABLE `reward_order_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key of order item table', AUTO_INCREMENT=129;

--
-- AUTO_INCREMENT for table `reward_order_payments`
--
ALTER TABLE `reward_order_payments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key of payment table', AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `reward_order_replace_images`
--
ALTER TABLE `reward_order_replace_images`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for each replace image (auto-generated)', AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `reward_order_replace_items`
--
ALTER TABLE `reward_order_replace_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for each replace item row (auto-generated)', AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `reward_order_replace_pickups`
--
ALTER TABLE `reward_order_replace_pickups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for each pickup record (auto-generated)', AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `reward_order_replace_requests`
--
ALTER TABLE `reward_order_replace_requests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for each replace request (auto-generated)', AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `reward_order_replace_status_history`
--
ALTER TABLE `reward_order_replace_status_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for each status history log entry (auto-generated)', AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT for table `reward_order_return_images`
--
ALTER TABLE `reward_order_return_images`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique ID for each return image', AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `reward_order_return_items`
--
ALTER TABLE `reward_order_return_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key', AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `reward_order_return_pickups`
--
ALTER TABLE `reward_order_return_pickups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key', AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `reward_order_return_requests`
--
ALTER TABLE `reward_order_return_requests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key', AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `reward_order_return_status_history`
--
ALTER TABLE `reward_order_return_status_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key', AUTO_INCREMENT=75;

--
-- AUTO_INCREMENT for table `reward_order_status_history`
--
ALTER TABLE `reward_order_status_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary key', AUTO_INCREMENT=154;

--
-- AUTO_INCREMENT for table `reward_products`
--
ALTER TABLE `reward_products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique product ID', AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `reward_product_images`
--
ALTER TABLE `reward_product_images`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique image ID', AUTO_INCREMENT=108;

--
-- AUTO_INCREMENT for table `reward_rules`
--
ALTER TABLE `reward_rules`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `reward_transactions`
--
ALTER TABLE `reward_transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=80;

--
-- AUTO_INCREMENT for table `user_wallet`
--
ALTER TABLE `user_wallet`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Wallet record ID', AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts_user_profile`
--
ALTER TABLE `accounts_user_profile`
  ADD CONSTRAINT `fk_user_profile_user` FOREIGN KEY (`table_auth_user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `app_1_users_user_groups`
--
ALTER TABLE `app_1_users_user_groups`
  ADD CONSTRAINT `app_1_users_user_groups_group_id_28cfac3e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `app_1_users_user_groups_user_id_0997190c_fk_app_1_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `app_1_users_user` (`id`);

--
-- Constraints for table `app_1_users_user_user_permissions`
--
ALTER TABLE `app_1_users_user_user_permissions`
  ADD CONSTRAINT `app_1_users_user_use_permission_id_3f68ea7f_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `app_1_users_user_use_user_id_98d2cc4b_fk_app_1_use` FOREIGN KEY (`user_id`) REFERENCES `app_1_users_user` (`id`);

--
-- Constraints for table `app_2_e_facility_user_groups`
--
ALTER TABLE `app_2_e_facility_user_groups`
  ADD CONSTRAINT `app_2_e_Facility_use_user_id_21ddb771_fk_app_2_e_F` FOREIGN KEY (`user_id`) REFERENCES `app_2_e_facility_user` (`id`),
  ADD CONSTRAINT `app_2_e_Facility_user_groups_group_id_381e3f22_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `app_2_e_facility_user_user_permissions`
--
ALTER TABLE `app_2_e_facility_user_user_permissions`
  ADD CONSTRAINT `app_2_e_Facility_use_permission_id_81b35a2d_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `app_2_e_Facility_use_user_id_8c943e69_fk_app_2_e_F` FOREIGN KEY (`user_id`) REFERENCES `app_2_e_facility_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `category_brand_mapping`
--
ALTER TABLE `category_brand_mapping`
  ADD CONSTRAINT `category_brand_mapping_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `recycling_info` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `category_brand_mapping_ibfk_2` FOREIGN KEY (`brand_id`) REFERENCES `brand` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `e_waste_status_history`
--
ALTER TABLE `e_waste_status_history`
  ADD CONSTRAINT `e_waste_status_history_ibfk_1` FOREIGN KEY (`submission_id`) REFERENCES `e_waste_submission` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `e_waste_status_history_ibfk_2` FOREIGN KEY (`changed_by`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `e_waste_submission`
--
ALTER TABLE `e_waste_submission`
  ADD CONSTRAINT `e_waste_submission_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `e_waste_submission_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `recycling_info` (`id`),
  ADD CONSTRAINT `e_waste_submission_ibfk_3` FOREIGN KEY (`category_brand_mapping_id`) REFERENCES `category_brand_mapping` (`id`),
  ADD CONSTRAINT `e_waste_submission_ibfk_4` FOREIGN KEY (`model_id`) REFERENCES `product_model_name` (`id`),
  ADD CONSTRAINT `e_waste_submission_ibfk_5` FOREIGN KEY (`user_condition_id`) REFERENCES `item_conditions` (`id`),
  ADD CONSTRAINT `e_waste_submission_ibfk_6` FOREIGN KEY (`final_condition_id`) REFERENCES `item_conditions` (`id`),
  ADD CONSTRAINT `e_waste_submission_ibfk_7` FOREIGN KEY (`facility_id`) REFERENCES `facility` (`id`);

--
-- Constraints for table `e_waste_submission_images`
--
ALTER TABLE `e_waste_submission_images`
  ADD CONSTRAINT `e_waste_submission_images_ibfk_1` FOREIGN KEY (`submission_id`) REFERENCES `e_waste_submission` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `product_model`
--
ALTER TABLE `product_model`
  ADD CONSTRAINT `product_model_ibfk_1` FOREIGN KEY (`category_brand_mapping_id`) REFERENCES `category_brand_mapping` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `product_model_name`
--
ALTER TABLE `product_model_name`
  ADD CONSTRAINT `product_model_name_ibfk_1` FOREIGN KEY (`brand_id`) REFERENCES `brand` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `product_model_name_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `recycling_info` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_cart`
--
ALTER TABLE `reward_cart`
  ADD CONSTRAINT `fk_reward_cart_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_cart_items`
--
ALTER TABLE `reward_cart_items`
  ADD CONSTRAINT `fk_cart_items_cart` FOREIGN KEY (`cart_id`) REFERENCES `reward_cart` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_cart_items_product` FOREIGN KEY (`product_id`) REFERENCES `reward_products` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_orders`
--
ALTER TABLE `reward_orders`
  ADD CONSTRAINT `reward_orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `reward_orders_ibfk_2` FOREIGN KEY (`cart_id`) REFERENCES `reward_cart` (`id`);

--
-- Constraints for table `reward_order_address`
--
ALTER TABLE `reward_order_address`
  ADD CONSTRAINT `reward_order_address_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `reward_orders` (`id`);

--
-- Constraints for table `reward_order_items`
--
ALTER TABLE `reward_order_items`
  ADD CONSTRAINT `reward_order_items_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `reward_orders` (`id`),
  ADD CONSTRAINT `reward_order_items_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `reward_products` (`id`);

--
-- Constraints for table `reward_order_payments`
--
ALTER TABLE `reward_order_payments`
  ADD CONSTRAINT `reward_order_payments_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `reward_orders` (`id`);

--
-- Constraints for table `reward_order_replace_images`
--
ALTER TABLE `reward_order_replace_images`
  ADD CONSTRAINT `reward_order_replace_images_ibfk_1` FOREIGN KEY (`replace_request_id`) REFERENCES `reward_order_replace_requests` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_order_replace_items`
--
ALTER TABLE `reward_order_replace_items`
  ADD CONSTRAINT `reward_order_replace_items_ibfk_1` FOREIGN KEY (`replace_request_id`) REFERENCES `reward_order_replace_requests` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `reward_order_replace_items_ibfk_2` FOREIGN KEY (`order_item_id`) REFERENCES `reward_order_items` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_order_replace_pickups`
--
ALTER TABLE `reward_order_replace_pickups`
  ADD CONSTRAINT `reward_order_replace_pickups_ibfk_1` FOREIGN KEY (`replace_request_id`) REFERENCES `reward_order_replace_requests` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `reward_order_replace_pickups_ibfk_2` FOREIGN KEY (`order_address_id`) REFERENCES `reward_order_address` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_order_replace_requests`
--
ALTER TABLE `reward_order_replace_requests`
  ADD CONSTRAINT `reward_order_replace_requests_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `reward_orders` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `reward_order_replace_requests_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_order_replace_status_history`
--
ALTER TABLE `reward_order_replace_status_history`
  ADD CONSTRAINT `reward_order_replace_status_history_ibfk_1` FOREIGN KEY (`replace_request_id`) REFERENCES `reward_order_replace_requests` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `reward_order_replace_status_history_ibfk_2` FOREIGN KEY (`changed_by`) REFERENCES `auth_user` (`id`) ON DELETE SET NULL;

--
-- Constraints for table `reward_order_return_images`
--
ALTER TABLE `reward_order_return_images`
  ADD CONSTRAINT `reward_order_return_images_ibfk_1` FOREIGN KEY (`return_request_id`) REFERENCES `reward_order_return_requests` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_order_return_items`
--
ALTER TABLE `reward_order_return_items`
  ADD CONSTRAINT `reward_order_return_items_ibfk_1` FOREIGN KEY (`return_request_id`) REFERENCES `reward_order_return_requests` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `reward_order_return_items_ibfk_2` FOREIGN KEY (`order_item_id`) REFERENCES `reward_order_items` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `reward_order_return_items_ibfk_3` FOREIGN KEY (`product_id`) REFERENCES `reward_products` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_order_return_pickups`
--
ALTER TABLE `reward_order_return_pickups`
  ADD CONSTRAINT `reward_order_return_pickups_ibfk_1` FOREIGN KEY (`return_request_id`) REFERENCES `reward_order_return_requests` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `reward_order_return_pickups_ibfk_2` FOREIGN KEY (`order_address_id`) REFERENCES `reward_order_address` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_order_return_requests`
--
ALTER TABLE `reward_order_return_requests`
  ADD CONSTRAINT `reward_order_return_requests_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `reward_orders` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `reward_order_return_requests_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_order_return_status_history`
--
ALTER TABLE `reward_order_return_status_history`
  ADD CONSTRAINT `reward_order_return_status_history_ibfk_1` FOREIGN KEY (`return_request_id`) REFERENCES `reward_order_return_requests` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_order_status_history`
--
ALTER TABLE `reward_order_status_history`
  ADD CONSTRAINT `fk_history_changed_by` FOREIGN KEY (`changed_by`) REFERENCES `auth_user` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `fk_history_order_id` FOREIGN KEY (`order_id`) REFERENCES `reward_orders` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_products`
--
ALTER TABLE `reward_products`
  ADD CONSTRAINT `fk_product_category` FOREIGN KEY (`category_id`) REFERENCES `reward_category` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_product_images`
--
ALTER TABLE `reward_product_images`
  ADD CONSTRAINT `fk_product_images` FOREIGN KEY (`product_id`) REFERENCES `reward_products` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_rules`
--
ALTER TABLE `reward_rules`
  ADD CONSTRAINT `fk_reward_category` FOREIGN KEY (`category_id`) REFERENCES `recycling_info` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_reward_condition` FOREIGN KEY (`condition_id`) REFERENCES `item_conditions` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `reward_transactions`
--
ALTER TABLE `reward_transactions`
  ADD CONSTRAINT `reward_transactions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `reward_transactions_ibfk_2` FOREIGN KEY (`submission_id`) REFERENCES `e_waste_submission` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
