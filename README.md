# Python dice game
A simple dice game built in python using IDLE, involving authentication and score keeping, which can:
- Allow users to login, check that password matches authorised password
- Allow two players to roll two 6-sided dice
- Allow each player to play 5 rounds
- Add up a score for each player, based on their roll
- Display a winner, and store this in an external file

Players roll two 6-sided dice each, earning points based on the roll. Across 5 rounds, every player rolls dice.<br>
The rules are as follows:
- Dice points are added to that player's score
- Even totals gain 10 extra points
- Odd totals lose 5 points
- Doubles allow an extra roll with points added
- Score never drops below 0
- The highest 5-round score wins
- Ties involve a 1-die roll-off for the winner. Only authorized players participate

A valid login to be able to play is:<br>
Username: ```test```<br>
Password: ```test123```
