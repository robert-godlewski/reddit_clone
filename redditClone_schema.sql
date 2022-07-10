-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema redditclone
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema redditclone
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `redditclone` DEFAULT CHARACTER SET utf8 ;
USE `redditclone` ;

-- -----------------------------------------------------
-- Table `redditclone`.`group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redditclone`.`group` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `group_name` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `redditclone`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redditclone`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(200) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `redditclone`.`admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redditclone`.`admin` (
  `group_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`group_id`, `user_id`),
  INDEX `fk_group_has_user_user1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_group_has_user_group_idx` (`group_id` ASC) VISIBLE,
  CONSTRAINT `fk_group_has_user_group`
    FOREIGN KEY (`group_id`)
    REFERENCES `redditclone`.`group` (`id`),
  CONSTRAINT `fk_group_has_user_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `redditclone`.`user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `redditclone`.`post`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redditclone`.`post` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NULL DEFAULT NULL,
  `group_id` INT NULL DEFAULT NULL,
  `title` VARCHAR(255) NULL DEFAULT NULL,
  `content` VARCHAR(255) NULL DEFAULT NULL,
  `like_count` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `isVideo` TINYINT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_post_user1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_post_group1_idx` (`group_id` ASC) VISIBLE,
  CONSTRAINT `fk_post_group1`
    FOREIGN KEY (`group_id`)
    REFERENCES `redditclone`.`group` (`id`),
  CONSTRAINT `fk_post_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `redditclone`.`user` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 41
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `redditclone`.`comment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redditclone`.`comment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(255) NULL DEFAULT NULL,
  `user_id` INT NULL DEFAULT NULL,
  `post_id` INT NULL DEFAULT NULL,
  `like_count` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_comment_user1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_comment_post1_idx` (`post_id` ASC) VISIBLE,
  CONSTRAINT `fk_comment_post1`
    FOREIGN KEY (`post_id`)
    REFERENCES `redditclone`.`post` (`id`),
  CONSTRAINT `fk_comment_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `redditclone`.`user` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 23
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `redditclone`.`favorite`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redditclone`.`favorite` (
  `user_id` INT NOT NULL,
  `group_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`, `group_id`),
  INDEX `fk_user_has_group_group1_idx` (`group_id` ASC) VISIBLE,
  INDEX `fk_user_has_group_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_group_group1`
    FOREIGN KEY (`group_id`)
    REFERENCES `redditclone`.`group` (`id`),
  CONSTRAINT `fk_user_has_group_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `redditclone`.`user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
