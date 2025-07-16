CREATE DATABASE IF NOT EXISTS `roommanager`;
USE `roommanager`;

CREATE TABLE IF NOT EXISTS `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `displayName` varchar(50) NOT NULL DEFAULT 'New User',
  `email` varchar(80) NOT NULL,
  `login` varchar(40) NOT NULL,
  `password` varchar(100) NOT NULL,
  `token` varchar(150) DEFAULT NULL,
  `isadmin` tinyint DEFAULT '0',
  `isActive` tinyint DEFAULT '1',
  `creationUser` int unsigned DEFAULT NULL,
  `creationDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updateUser` int unsigned DEFAULT NULL,
  `updateTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`creationUser`) REFERENCES `users` (`id`) ON DELETE SET NULL,
  FOREIGN KEY (`updateUser`) REFERENCES `users` (`id`) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS `rooms` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `description` varchar(300) NOT NULL,
  `capacity` int unsigned NOT NULL DEFAULT '10',
  `image` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `color` varchar(20) DEFAULT NULL,
  `creationUser` int unsigned NOT NULL,
  `creationDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updateUser` int unsigned NOT NULL,
  `updateDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`creationUser`) REFERENCES `users` (`id`),
  FOREIGN KEY (`updateUser`) REFERENCES `users` (`id`)
);

CREATE TABLE IF NOT EXISTS `reserves` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `room` INT UNSIGNED NOT NULL,
    `startDate` DATETIME NOT NULL,
    `endDate` DATETIME NOT NULL,
    `reservedFor` INT UNSIGNED NOT NULL,
    `creationUser` INT UNSIGNED DEFAULT NULL,
    `updateUser` INT UNSIGNED DEFAULT NULL,
    `creationDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updateTime` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`room`) REFERENCES `rooms` (`id`) ON DELETE CASCADE,
	FOREIGN KEY (`reservedFor`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`creationUser`) REFERENCES `users` (`id`),
    FOREIGN KEY (`updateUser`) REFERENCES `users` (`id`)
);

CREATE TABLE IF NOT EXISTS `issues` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `room` INT UNSIGNED NOT NULL,
    `type` varchar(40) NOT NULL,    
    `description` varchar(300) NOT NULL,
	`creationUser` INT UNSIGNED DEFAULT NULL,
    `updateUser` INT UNSIGNED DEFAULT NULL,
    `creationDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updateTime` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`room`) REFERENCES `rooms` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`creationUser`) REFERENCES `users` (`id`),
    FOREIGN KEY (`updateUser`) REFERENCES `users` (`id`)
);