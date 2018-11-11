# PUBG_Finish_Placement_Prediction
[`Kaggle`](https://www.kaggle.com/c/pubg-finish-placement-prediction) match done in `MadHacks` @[Madison](https://www.madhacks.io/). 
What's the best strategy to win in PUBG? Should you sit in one spot and hide your way into victory, or do you need to be the top shot? This is what we are looking into！

## Data description
Dependent variable and independent variables are described in Variables.txt

## Data Preprocessing
Since original .csv files contain entried of different game modes, they are extremely large and time-consuming to handle. Without generality we look into exclusively solo mode (still 181,943 entries though...) on current stage. SoloSelect.py is to delete entries in other modes and output new files as solo_train.csv and solo_test.csv.   

## Correlation analysis
We use SPSS to do linear regression, analysing which are the most important factors in determining Finish Placement. Only variables related to solo mode are considered. Results in Output.htm are explained here. As our model works stepwise, the first independent invariable in table Variables Entered/Removed is most relevant to Finish Placement. The walkDistance comes first and heals comes last and so on. <br>Regression equation considering top 5 relevant factors is generated from table Coefficients: <br>`winPlacePerc = .498 * walkDistance - .239 * killPlace + .147 * weaponAcquired + .096 * rideDistance + .114 * boosts` <br>So, don't be too cautious! Walk around and find someone to fight:)

## What's next?
Good question! It's just a kickstart of our fight (yes, fight) in Kaggle. Later we'll see whether we can predict Finish Placement accurately. Of course, that is much less interesting. 
