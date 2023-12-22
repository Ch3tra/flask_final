-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 22, 2023 at 05:19 PM
-- Server version: 5.7.36
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ss34_proo`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
CREATE TABLE IF NOT EXISTS `category` (
  `categoryId` int(11) NOT NULL AUTO_INCREMENT,
  `categoryName` varchar(100) COLLATE utf8_unicode_520_ci NOT NULL,
  `categoryDesc` varchar(255) COLLATE utf8_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`categoryId`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`categoryId`, `categoryName`, `categoryDesc`) VALUES
(7, 'Electronics', 'Includes devices such as smartphones, laptops, cameras, and televisions that utilize electronic technology for various purposes.'),
(8, 'Home & Kitchen Appliances', 'Encompasses a wide range of products like refrigerators, microwaves, blenders, and vacuum cleaners designed for household use to ease tasks and improve convenience.'),
(9, 'Clothing & Fashion', 'Covers apparel and accessories like shirts, dresses, shoes, and hats, reflecting various styles and trends in the fashion industry.'),
(12, 'Toys & Games', 'Consists of a diverse range of items for entertainment and education, including board games, action figures, puzzles, and remote-controlled toys.'),
(15, 'Furniture & Home Decor', 'Encompasses items such as sofas, tables, lamps, rugs, and decorative pieces to furnish and adorn living spaces.'),
(16, 'Pet Supplies', 'Includes products like pet food, toys, beds, grooming tools, and accessories catering to the needs and well-being of pets.');

-- --------------------------------------------------------

--
-- Table structure for table `credential`
--

DROP TABLE IF EXISTS `credential`;
CREATE TABLE IF NOT EXISTS `credential` (
  `userId` int(11) NOT NULL AUTO_INCREMENT,
  `username` text COLLATE utf8_unicode_520_ci NOT NULL,
  `password_hash` text COLLATE utf8_unicode_520_ci NOT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `credential`
--

INSERT INTO `credential` (`userId`, `username`, `password_hash`) VALUES
(1, 'dev', 'scrypt:32768:8:1$YN64L4HTtujOpf0J$297e869627b41ce07faa550bda5c556944c3145715f95fb0cc7d87a764b65ce83c6b79667f86c4b3b6285280ada11a7e99317519fe380e785d094986a2ea2a90'),
(2, 'admin', 'scrypt:32768:8:1$mffQfEopbIc2NvUS$fe1f5b4c82fcf065d27a0b6c0fbd8aa42a07d1f61bf6b3a7c9d90edd563fde7e0729fcc6ca70a6eb301bcdfc3bc1d25e1f1726408f5c97e17f81166ef94fe765');

-- --------------------------------------------------------

--
-- Table structure for table `currency`
--

DROP TABLE IF EXISTS `currency`;
CREATE TABLE IF NOT EXISTS `currency` (
  `currencyId` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(50) COLLATE utf8_unicode_520_ci NOT NULL,
  `currencyName` varchar(50) COLLATE utf8_unicode_520_ci NOT NULL,
  `currencySymbol` varchar(50) COLLATE utf8_unicode_520_ci NOT NULL,
  `currencyRate` double NOT NULL,
  `is_default` int(11) DEFAULT NULL,
  PRIMARY KEY (`currencyId`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `currency`
--

INSERT INTO `currency` (`currencyId`, `code`, `currencyName`, `currencySymbol`, `currencyRate`, `is_default`) VALUES
(1, 'sadf', 'sdf', 'asdf', 234, NULL),
(2, 'asdf', 'asdf', 'asd', 234, NULL),
(3, '1234', '23', '345', 12, NULL),
(4, 'asdf', '234', 'asdf', 234, 1);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `customerId` int(11) NOT NULL AUTO_INCREMENT,
  `customerName` varchar(255) COLLATE utf8_unicode_520_ci NOT NULL,
  `image` varchar(255) COLLATE utf8_unicode_520_ci NOT NULL DEFAULT 'default_img',
  `status` varchar(50) COLLATE utf8_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`customerId`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customerId`, `customerName`, `image`, `status`) VALUES
(10, 'ABC Company', 'default_img', 'active'),
(11, 'XYZ Corporation', 'default_img', 'active'),
(12, 'Smith & Sons', 'default_img', 'active'),
(13, 'Johnson Enterprises', 'default_img', 'active'),
(14, 'Miller Co.', 'default_img', 'active'),
(15, 'Wilson Ltd.', 'default_img', 'active'),
(16, 'Garcia Group', 'default_img', 'active'),
(17, 'Martinez Inc.', 'default_img', 'active'),
(18, 'Hernandez Enterprises', 'default_img', 'active'),
(19, 'Anderson Corporation', 'default_img', 'active'),
(20, 'Taylor & Co.', 'default_img', 'active'),
(21, 'Thomas Group', 'default_img', 'active'),
(22, 'King Enterprises', 'default_img', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
CREATE TABLE IF NOT EXISTS `product` (
  `productId` int(11) NOT NULL AUTO_INCREMENT,
  `categoryId` int(11) NOT NULL,
  `productName` varchar(60) COLLATE utf8_unicode_520_ci NOT NULL,
  `productDesc` varchar(255) COLLATE utf8_unicode_520_ci NOT NULL,
  `productCost` double NOT NULL,
  `image` varchar(255) COLLATE utf8_unicode_520_ci NOT NULL DEFAULT 'default_img',
  `productPrice` double DEFAULT NULL,
  `status` varchar(50) COLLATE utf8_unicode_520_ci DEFAULT NULL,
  `discount` int(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`productId`),
  KEY `fk_product_category` (`categoryId`)
) ENGINE=MyISAM AUTO_INCREMENT=85 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`productId`, `categoryId`, `productName`, `productDesc`, `productCost`, `image`, `productPrice`, `status`, `discount`) VALUES
(4, 7, 'Smartphone X', 'A high-performance smartphone with advanced features and a sleek design.', 300, 'default_img', 499, NULL, 0),
(5, 7, 'Laptop Pro', 'Powerful laptop suitable for professional use, featuring high-speed processors and ample storage.', 800, 'default_img', 1199, NULL, 0),
(6, 8, 'Refrigerator Elite', 'Spacious and energy-efficient refrigerator with modern features for convenient storage.', 700, 'default_img', 999, NULL, 0),
(7, 8, 'Multi-function Blender', 'Versatile blender capable of handling various food processing tasks with ease.', 50, 'default_img', 89, NULL, 0),
(8, 9, 'Stylish Dress Shirt', 'Elegant and comfortable dress shirt suitable for formal occasions.', 30, 'default_img', 59, NULL, 0),
(9, 9, 'Running Shoes', 'Durable and comfortable shoes designed for running and athletic activities.', 50, 'default_img', 89, NULL, 0),
(29, 16, 'Catnip Toys Variety Pack', 'Assortment of catnip toys to entertain and stimulate cats.', 15, 'default_img', 25, NULL, 0),
(28, 15, 'Bookshelf', 'Sturdy bookshelf for organizing books and displaying decorative items.', 80, 'default_img', 129, NULL, 0),
(27, 12, 'Tabletop Role-playing Game Set', 'Complete set for tabletop role-playing games, including dice and rulebooks.', 50, 'default_img', 89, NULL, 0),
(14, 12, 'Board Game Bundle', 'Collection of popular board games for family entertainment.', 60, 'default_img', 99, NULL, 0),
(15, 12, 'Remote-controlled Car', 'Fun and agile remote-controlled car for enthusiasts of all ages.', 40, 'default_img', 69, NULL, 0),
(26, 9, 'Running Jacket', 'Lightweight and weather-resistant jacket designed for running and outdoor activities.', 45, 'default_img', 79, NULL, 0),
(25, 8, 'Electric Kettle', 'Quick-boil electric kettle with temperature control for precise brewing.', 35, 'default_img', 59, NULL, 0),
(24, 7, 'Smart Home Security Camera', 'Advanced security camera with AI detection for smart home surveillance.', 120, 'default_img', 199, NULL, 0),
(20, 15, 'Sofa Set', 'Comfortable and stylish sofa set for the living room.', 500, 'default_img', 799, NULL, 0),
(21, 15, 'Decorative Table Lamp', 'Elegant table lamp to add ambiance to any room.', 40, 'default_img', 69, NULL, 0),
(22, 16, 'Premium Pet Food', 'Nutritious and high-quality food for pets to ensure their well-being.', 20, 'default_img', 35, NULL, 0),
(23, 16, 'Interactive Pet Toy', 'Engaging toy designed to entertain pets and keep them active.', 15, 'default_img', 25, NULL, 0),
(30, 7, 'Wireless Charging Pad', 'Convenient wireless charging pad compatible with various devices.', 25, 'default_img', 39, NULL, 0),
(31, 8, 'Slow Cooker', 'Versatile slow cooker for preparing flavorful meals with ease.', 60, 'Slow_Cooker.jpg', 99, NULL, 0),
(32, 9, 'Hiking Backpack', 'Durable and spacious backpack designed for hiking and outdoor adventures.', 70, 'Hiking_Backpack.jpg', 119, NULL, 0),
(33, 12, 'Art Supplies Set', 'Comprehensive set of art supplies for aspiring artists and hobbyists.', 40, 'Art_Supplies_Set.jpg', 69, NULL, 0),
(34, 15, 'Floor Lamp', 'Elegant floor lamp with adjustable brightness and modern design.', 90, 'Floor_Lamp.jpg', 149, NULL, 0),
(35, 16, 'Dog Chew Toys Pack', 'Variety pack of durable chew toys to keep dogs entertained and active.', 20, 'Dog_Chew_Toys_Pack.jpg', 35, NULL, 0),
(36, 7, 'Bluetooth Speaker', 'Portable Bluetooth speaker with high-fidelity sound for on-the-go music.', 50, 'Bluetooth_Speaker.jpg', 89, NULL, 0),
(37, 8, 'Rice Cooker', 'Efficient rice cooker for perfect rice preparation every time.', 55, 'Rice_Cooker.jpg', 89, NULL, 0),
(38, 9, 'Leather Wallet', 'Classic leather wallet with multiple compartments for organization.', 30, 'Leather_Wallet.jpg', 49, NULL, 0),
(39, 12, 'DIY Craft Kit', 'Craft kit with assorted materials for creative do-it-yourself projects.', 25, 'DIY_Craft_Kit.jpg', 45, NULL, 0),
(40, 15, 'Vanity Mirror', 'LED-lighted vanity mirror with magnification for makeup application.', 70, 'Vanity_Mirror.jpg', 119, NULL, 0),
(41, 16, 'Bird Feeder', 'Decorative bird feeder to attract and feed various bird species.', 15, 'Bird_Feeder.jpg', 29, NULL, 0),
(42, 7, 'Smart Thermostat', 'Intelligent thermostat for controlling home temperature and energy savings.', 100, 'Smart_Thermostat.jpg', 149, NULL, 0),
(43, 8, 'Food Processor', 'Multi-functional food processor for chopping, blending, and slicing.', 70, 'Food_Processor.png', 119, NULL, 0),
(44, 7, 'Wireless Gaming Mouse', 'High-performance wireless gaming mouse with customizable RGB lighting.', 40, 'Wireless_Gaming_Mouse.jpg', 69, NULL, 0),
(45, 7, 'Portable Power Bank', 'Compact and high-capacity power bank for charging devices on the go.', 30, 'Portable_Power_Bank.jpg', 49, NULL, 0),
(46, 7, 'Smart WiFi Plug', 'Intelligent Wi-Fi plug to control electronic devices remotely via smartphone.', 20, 'Smart_WiFi_Plug.jpg', 35, NULL, 0),
(47, 7, 'Noise Canceling Headphones', 'Premium noise-canceling headphones with immersive sound quality.', 100, 'Noise_Canceling_Headphones.jpg', 179, NULL, 0),
(48, 7, 'Ultra Slim Laptop Sleeve', 'Sleek and protective laptop sleeve for slim and lightweight laptops.', 25, 'Ultra_Slim_Laptop_Sleeve.jpg', 45, NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
CREATE TABLE IF NOT EXISTS `student` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(60) COLLATE utf8_unicode_520_ci NOT NULL,
  `lastName` varchar(60) COLLATE utf8_unicode_520_ci NOT NULL,
  `birthday` varchar(50) COLLATE utf8_unicode_520_ci NOT NULL,
  `gender` varchar(20) COLLATE utf8_unicode_520_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_unicode_520_ci NOT NULL,
  `phoneNumber` varchar(30) COLLATE utf8_unicode_520_ci NOT NULL,
  `subject` varchar(50) COLLATE utf8_unicode_520_ci NOT NULL,
  `image` varchar(255) COLLATE utf8_unicode_520_ci NOT NULL DEFAULT 'default_img',
  PRIMARY KEY (`sid`)
) ENGINE=MyISAM AUTO_INCREMENT=30 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`sid`, `firstName`, `lastName`, `birthday`, `gender`, `email`, `phoneNumber`, `subject`, `image`) VALUES
(10, 'John', 'Doe', '2000-05-15', 'Male', 'johndoe@example.com', '012345678', 'English', 'default_img'),
(11, 'Alice', 'Smith', '1999-08-23', 'Female', 'alicesmith@example.com', '098765432', 'Math', 'default_img'),
(12, 'Michael', 'Johnson', '2001-01-10', 'Male', 'michaeljohnson@example.com', '076543219', 'Science', 'default_img'),
(13, 'Emma', 'Williams', '2002-11-07', 'Female', 'emmawilliams@example.com', '034567890', 'Social', 'default_img'),
(14, 'William', 'Brown', '2000-09-30', 'Male', 'williambrown@example.com', '065432189', 'Graphic Design', 'default_img'),
(15, 'Sophia', 'Jones', '2001-04-18', 'Female', 'sophiajones@example.com', '089012345', 'Programming', 'default_img'),
(16, 'Daniel', 'Garcia', '2000-07-25', 'Male', 'danielgarcia@example.com', '056789012', 'English', 'default_img'),
(17, 'Olivia', 'Martinez', '2001-12-03', 'Female', 'oliviamartinez@example.com', '043210987', 'Math', 'default_img'),
(18, 'Matthew', 'Lopez', '1999-10-11', 'Male', 'matthewlopez@example.com', '078901234', 'Science', 'default_img'),
(19, 'Ava', 'Hernandez', '2002-06-29', 'Female', 'avahernandez@example.com', '032109876', 'Social', 'default_img'),
(20, 'Ethan', 'Gonzalez', '2000-03-05', 'Male', 'ethangonzalez@example.com', '097856341', 'Graphic Design', 'default_img'),
(21, 'Mia', 'Miller', '2001-09-14', 'Female', 'miamiller@example.com', '054321098', 'Programming', 'default_img'),
(22, 'James', 'Lee', '1998-07-02', 'Male', 'jameslee@example.com', '087563210', 'English', 'default_img'),
(23, 'Charlotte', 'Wilson', '2002-04-21', 'Female', 'charlottewilson@example.com', '045678901', 'Math', 'default_img'),
(24, 'Benjamin', 'Anderson', '1999-11-18', 'Male', 'benjaminanderson@example.com', '098765432', 'Science', 'default_img'),
(25, 'Amelia', 'Taylor', '2001-08-07', 'Female', 'ameliataylor@example.com', '023456789', 'Social', 'default_img'),
(26, 'Alexander', 'Thomas', '2000-02-12', 'Male', 'alexanderthomas@example.com', '065432189', 'Graphic Design', 'default_img'),
(27, 'Harper', 'Hill', '2001-10-25', 'Female', 'harperhill@example.com', '012345678', 'Programming', 'default_img'),
(28, 'Logan', 'Moore', '1999-06-14', 'Male', 'loganmoore@example.com', '045678901', 'English', 'default_img'),
(29, 'Evelyn', 'King', '2002-03-19', 'Female', 'evelynking@example.com', '089012345', 'Math', 'default_img');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `userId` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(60) COLLATE utf8_unicode_520_ci NOT NULL,
  `image` varchar(255) COLLATE utf8_unicode_520_ci NOT NULL DEFAULT 'default_img',
  `status` varchar(50) COLLATE utf8_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_520_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userId`, `username`, `image`, `status`) VALUES
(8, 'user3', 'default_img', 'active'),
(6, 'user1', 'default_img', 'active'),
(7, 'user2', 'default_img', 'active'),
(9, 'user4', 'default_img', 'active'),
(10, 'user5', 'default_img', 'active'),
(11, 'user6', 'default_img', 'active'),
(12, 'user7', 'default_img', 'active'),
(13, 'user8', 'default_img', 'active'),
(14, 'user9', 'default_img', 'active'),
(15, 'user10', 'default_img', 'active'),
(16, 'user11', 'default_img', 'active'),
(17, 'user12', 'default_img', 'active');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
