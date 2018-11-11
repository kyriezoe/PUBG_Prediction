# PUBG_Finish_Placement_Prediction
[`Kaggle`](https://www.kaggle.com/c/pubg-finish-placement-prediction) match done in `MadHacks` @[Madison](https://www.madhacks.io/). 
What's the best strategy to win in PUBG? Should you sit in one spot and hide your way into victory, or do you need to be the top shot? This is what we are looking into！

## Data description
Dependent variable:
<br>winPlacePerc - The target of prediction. This is a percentile winning placement, where 1 corresponds to 1st place, and 0 corresponds to last place in the match. It is calculated off of maxPlace, not numGroups, so it is possible to have missing chunks in a match.
<br>Independent variables:
<br>DBNOs - Number of enemy players knocked.
<br>assists - Number of enemy players this player damaged that were killed by teammates.
<br>boosts - Number of boost items used.
<br>damageDealt - Total damage dealt. Note: Self inflicted damage is subtracted.
<br>headshotKills - Number of enemy players killed with headshots.
<br>heals - Number of healing items used.
<br>Id - Player’s Id
<br>killPlace - Ranking in match of number of enemy players killed.
<br>killPoints - Kills-based external ranking of player. (Think of this as an Elo ranking where only kills matter.) If there is a value other than -1 in rankPoints, then any 0 in killPoints should be treated as a “None”.
<br>killStreaks - Max number of enemy players killed in a short amount of time.
<br>kills - Number of enemy players killed.
<br>longestKill - Longest distance between player and player killed at time of death. This may be misleading, as downing a player and driving away may lead to a large longestKill stat.
<br>matchDuration - Duration of match in seconds.
<br>matchId - ID to identify match. There are no matches that are in both the training and testing set.
<br>matchType - String identifying the game mode that the data comes from. The standard modes are “solo”, “duo”, “squad”, “solo-fpp”, “duo-fpp”, and “squad-fpp”; other modes are from events or custom matches.
<br>rankPoints - Elo-like ranking of player. This ranking is inconsistent and is being deprecated in the API’s next version, so use with caution. Value of -1 takes place of “None”.
<br>revives - Number of times this player revived teammates.
<br>rideDistance - Total distance traveled in vehicles measured in meters.
<br>roadKills - Number of kills while in a vehicle.
<br>swimDistance - Total distance traveled by swimming measured in meters.
<br>teamKills - Number of times this player killed a teammate.
<br>vehicleDestroys - Number of vehicles destroyed.
<br>walkDistance - Total distance traveled on foot measured in meters.
<br>weaponsAcquired - Number of weapons picked up.
<br>winPoints - Win-based external ranking of player. (Think of this as an Elo ranking where only winning matters.) If there is a value other than -1 in rankPoints, then any 0 in winPoints should be treated as a “None”.
<br>groupId - ID to identify a group within a match. If the same group of players plays in different matches, they will have a different groupId each time.
<br>numGroups - Number of groups we have data for in the match.
<br>maxPlace - Worst placement we have data for in the match. This may not match with numGroups, as sometimes the data skips over placements.

## Data Preprocessing
Since original .csv files contain entried of different game modes, they are extremely large and time-consuming to handle. Without generality we look into exclusively solo mode (still 181,943 entries though...) on current stage. SoloSelect.py is to delete entries in other modes and output new files as solo_train.csv and solo_test.csv.   

## Correlation analysis
We use SPSS to do linear regression, analysing which are the most important factors in determining Finish Placement.
Results in Output.htm are explained here. As our model works stepwise, the first independent invariable in table Variables Entered/Removed is most relevant to Finish Placement. The walkDistance comes first and heals comes last and so on. <br>Regression equation considering top 5 relevant factors is generated from table Coefficients: <br>`winPlacePerc = .498 * walkDistance - .239 * killPlace + .147 * weaponAcquired + .096 * rideDistance + .114 * boosts` <br>So, don't be too cautious! Walk around and find someone to fight:)

## What's next?
Good question! It's just a kickstart of our fight (yes, fight) in Kaggle. Later we'll see whether we can predict Finish Placement accurately. Of course, that is much less interesting. 
