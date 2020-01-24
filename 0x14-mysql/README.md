# 0x14. Mysql
Learning Objectives:

At the end of this project, you are expected to be able to explain to anyone, without the help of Google

General
---
- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works
---
Step | Description
--- | ---
0. Install MySQL |  get MySQL installed on both your web-01 and web-02 servers.
1. Let us in! | In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.
2. If only you could see what I've seen with your eyes | In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.
3. Quite an experience to live in fear, isn't it?  | Before you get started with your primary-replica synchronization, you need one more thing in place. On your primary MySQL server (web-01), create a new user for the replica server.
4. Setup a Primary-Replica infrastructure using MySQL| create a replica of one to the other. a replica member on for your MySQL database has many advantages.
5. MySQL backup | What if the data center where both your primary and replica database servers are hosted are down because of a power outage or even worse: flooding, fire? Then all your data would inaccessible or lost. That’s why you want to backup and store them in a different system in another physical location. This can be achieved by dumping your MySQL data, compressing them and storing them in a different data center.

# All scripts used from step 1 onwards
Commands used | Step
--- | ---
CREATE USER IF NOT EXISTS holberton_user@localhost IDENTIFIED BY 'projectcorrection280hbtn'; | 1. Let us in! 
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost'  | 1. Let us in!
CREATE DATABASE IF NOT EXISTS tyrell_corp; | 2. If only you could see what I've seen with your eyes
USE tyrell_corp; | 2. If only you could see what I've seen with your eyes
CREATE TABLE nexus6 (name VARCHAR(80), id INT); | 2. If only you could see what I've seen with your eyes
INSERT INTO nexus6 (name, id) VALUES ("kaiser", 777); | 2. If only you could see what I've seen with your eyes
GRANT SELECT ON tyrell_corp.nexus6 TO holberton_user@localhost; | 2. If only you could see what I've seen with your eyes
CREATE USER IF NOT EXISTS replica_user@'%' IDENTIFIED BY 'root'; | 3. Quite an experience to live in fear, isn't it?
GRANT SELECT ON mysql.user TO holberton_user@localhost; | 3. Quite an experience to live in fear, isn't it?
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%'; | 3. Quite an experience to live in fear, isn't it?



