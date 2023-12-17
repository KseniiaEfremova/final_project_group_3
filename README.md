
# CODE QUEST

Code Quest aims to provide an engaging and challenging gaming experience, assessing players' responsiveness and decision-making skills within a 60-second timeframe. The objective is to create a dynamic and visually appealing game environment that serves as a refreshing break for software engineers and anyone seeking an enjoyable challenge. Leveraging the Pygame library and embracing Object-Oriented Programming (OOP) principles, Code Quest aspires to transcend traditional gaming boundaries and cater to a wide range of audiences. 


## Installation

To successfully run this project locally on your machine you need at least Python 3.11 and PyGame ce 2.3.2 

1. First clone the repository and open project directory:

```bash
git clone https://github.com/KseniiaEfremova/final_project_group_3.git
cd final_project_group_3
```

2. Open your pipenv shell and install dependencies from pipfile:
```bash
pipenv shell
pipenv install
```

3. In db directory create config.py file and type in credentials to your MySql server like that:
```bash
data = {
  "host": <your_host_name>,
  "user": <your_user_name>,
  "passwd": <your_password>
}
```

4. Copy queries from db.game_users_db.sql and run them in your MySql server

5. In order to run the game, run main.py file in root folder

6. In order to run tests, run test_runner.py. Runner will trigger all test cases and prepare coverage report.

    
## Tech Stack

**GUI:** PyGame

**Server:** Python, PyGame CE, numpy, mysql-connector-python

**Tests:** unittest, coverage


## Features

- user can register account in the game, username has to be at least 4 letters long, password has to have at least one uppercase letter, one lowercase letter,  one number, one special character, at least 8 characters long
- user can login to the game in order to play
- user can view instructions to the game under instructions menu
- user can view credits under credits menu
- user can view best 8 scores from history under history menu
- logged in user can move player using left and right arrows or a and d keys
- after collision with points falling items user score points are increasing
- after collision with damage falling item user score points and life points are decreasing
- if user's stats are changing, it is also visible in stats bar at the top of the screen
- user can play a round which takes 60 seconds, there are 3 levels ready to play
- during gameplay there is soundtrack playing in the ground as well as different sounds when colliding with items
- upon successfull completing a level, user can see distinctive picture for 3 secs and he's or her's position is resetted, as well as timer
- upon successfull completion of a game, user can see winning menu and choose to play again or quit the game
- upon loosing, user can see game over menu and choose to play again or quit the game
- player can pause a game play using space bar



## Authors, activity logs, and JIra agile board

- [@KerriTanya](https://github.com/KerriTanya)
- [@KseniiaEfremova](https://github.com/KseniiaEfremova)
- [@NataliaPiotrowska](https://github.com/n-piotrowska)
- [@Sadafh12](https://github.com/Sadafh12)
- [@sandyintxch](https://github.com/sandyintxch)
- [@k-stopczynska](https://github.com/k-stopczynska)
- [Jira](https://docs.google.com/spreadsheets/d/1ykk4cfDl5eZ4_qaTTDKOeW0Db-O5YZWjdCLoPnbx2FA/edit#gid=0)
- [Activity log](https://docs.google.com/spreadsheets/d/1ykk4cfDl5eZ4_qaTTDKOeW0Db-O5YZWjdCLoPnbx2FA/edit#gid=2121606848)

