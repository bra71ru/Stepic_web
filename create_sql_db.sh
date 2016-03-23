mysql -u root -p -e "
  CREATE DATABASE qa;
  CREATE USER 'qa_admin'@'localhost';
  GRANT ALL PRIVILEGES ON qa.* TO 'qa_admin'@'localhost';
  FLUSH PRIVILEGES;
  "
