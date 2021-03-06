-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: whatabook
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `book_name` varchar(75) NOT NULL,
  `details` varchar(500) NOT NULL,
  `author` varchar(200) NOT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'Skullduggery Pleasent','Stephanie Edgley\'s uncle passed away leaving her a fortune including his mansion. While staying there, she was attacked by a strange man and was rescued by Skulduggery Pleasant, a mysterious skeleton mage. Together with Ghastly Bespoke, China Sorrows and Tanith Low, Stephanie and Skulduggery tried to stop a plot for world domination of Serpine, an evil wizard.','Derek Landy'),(2,'PLaying with Fire','With Serpine dead, the world is safe once more. At least, that\'s what Valkyrie and Skulduggery think, until the notorious Baron Vengeous makes a bloody escape from prison, and dead bodies and vampires start showing up all over Ireland. With Baron Vengeous after the deadly armour of Lord Vile, and pretty much everyone out to kill Valkyrie, the daring detective duo face their biggest challenge yet. But what if the greatest threat to Valkyrie is just a little closer to homeΓÇª?','Derek Landy'),(3,'The Faceless Ones','As a number of teleporters are mysteriously murdered, Valkyrie and Skulduggery learn that it is quickly linked to a fanatical cult named the Diablerie, who seek to open a portal with the goal of returning the Faceless Ones to the world. With the assistance of cocky young teleporter Fletcher Renn, Valkyrie and Skulduggery have very little time to track down a mysterious man named Batu, stop the Diablerie, and prevent the return of the Faceless Ones.','Derek Landy'),(4,'Dark Days','Skulduggery Pleasant is gone, sucked into a parallel dimension overrun by the Faceless Ones. If his bones havenΓÇÖt already been turned to dust, chances are heΓÇÖs insane, driven out of his mind by the horror of the ancient gods. There is no official, Sanctuary-approved rescue mission. There is no official plan to save him. But Valkyrie\'s never had much time for plans. The problem is, even if she can get Skulduggery back, there might not be much left for him to return to.','Derek Landy'),(5,'Mortal Coil','ASkulduggery Pleasant and Valkyrie Cain are back ΓÇö just in time to see their whole world get turned upside down! While they struggle to protect a known killer from an unstoppable assassin, Valkyrie is on a secret mission of her own. This quest, to prevent her dark and murderous destiny, threatens to take her to the brink of death and beyond.','Derek Landy'),(6,'Death Bringer','The Necromancers no longer need Valkyrie to be their Death Bringer, and thatΓÇÖs a good thing. There\'s just one catch. The reason the Necromancers don\'t need her anymore. Because they\'ve found their Death Bringer already, the person who will dissolve the doors between life and death. And that\'s a very, very bad thingΓÇª Skulduggery and Valkyrie have seven days to uncover the Necromancers\' secret before it\'s too late. The clock is ticking. Lord Vile is loose.','Derek Landy'),(7,'Kingdom of the Wicked','Magic is a disease. Across the land, normal people are suddenly developing wild and unstable powers. Infected by a rare strain of magic, they are unwittingly endangering their own lives and the lives of the people around them. Terrified and confused, their only hope lies with the Sanctuary. Skulduggery Pleasant and Valkyrie Cain are needed now more than ever.','Derek Landy'),(8,'Last Stand of Dead Men','War has finally come. But it\'s not a war between good and evil, or light and dark ΓÇô it\'s a war between Sanctuaries. For too long, the Irish Sanctuary has teetered on the brink of world-ending disaster.','Derek Landy'),(9,'The Dying of the Light','The War of the Sanctuaries has been won, but not without its casualties. Following the loss of Valkyrie Cain, Skulduggery Pleasant must use any and all means to track down and stop Darquesse before she turns the world into a charred, lifeless cinder, drawing together a team of soldiers, monster hunters, killers, criminalsΓÇª and Valkyrie\'s own murderous reflection. The war may be over, but the final battle is about to begin.','Derek Landy');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store`
--

DROP TABLE IF EXISTS `store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store` (
  `store_id` int NOT NULL,
  `locale` varchar(500) NOT NULL,
  `store_hours` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`store_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store`
--

LOCK TABLES `store` WRITE;
/*!40000 ALTER TABLE `store` DISABLE KEYS */;
INSERT INTO `store` VALUES (1,'123 Maple Street - Council Bluffs, IA 51503','0800 - 1700');
/*!40000 ALTER TABLE `store` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(75) NOT NULL,
  `last_name` varchar(75) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Skulduggery','Pleasent'),(2,'Valkyrie','Cain'),(3,'Ghastly','Bespoke');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wishlist`
--

DROP TABLE IF EXISTS `wishlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wishlist` (
  `user_id` int NOT NULL,
  `book_id` int NOT NULL,
  KEY `user_id` (`user_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `wishlist_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `wishlist_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `book` (`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wishlist`
--

LOCK TABLES `wishlist` WRITE;
/*!40000 ALTER TABLE `wishlist` DISABLE KEYS */;
INSERT INTO `wishlist` VALUES (1,1),(2,4),(3,2);
/*!40000 ALTER TABLE `wishlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-02 22:42:44
