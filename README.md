## Installation:

Here are concise instructions for using the config.py file to store MySQL database credentials securely:
1. Create a file named config.py (and don't add this file to Git) in your project directory with the following format:
```
data = {
  "host": "your_host",
  "user": "your_username",
  "passwd": "your_password"
}
```

Replace `your_host`with your hostname, `"your_username"` with your MySQL username and `"your_password"` with your MySQL password. 

---

Here are step-by-step instructions on how to use the game_users_db.sql file in MySQL Workbench:

1. Launch MySQL Workbench on your system.
2. Connect to your MySQL server using the appropriate connection settings (hostname, username, password, etc.).
3. In MySQL Workbench navigate to the location where game_users_db.sql is saved and open the file.
4. Execute the SQL Statements.
5. Now, your game_users_db database and tables are set up and ready to use.