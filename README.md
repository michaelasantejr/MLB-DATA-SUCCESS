# MLB-DATA-SUCCESS
Using PANDAS and a ELO formula, I attempted to find out which MLB team was the most sucessful.
This project is designed to determine who is the best MLB team given a certain dataset.
In this case, the New York Yankees destroyed its competition by all measure of success. Here is
how to define success and the methodology to determine it.
Success Measure
The method of success that was utilized to determine the best MLB team is as follows:
1. The team with the highest average run differential in their entire career
a. Having the highest run differential demonstrates a team’s defensive and offensive
ability.
b. A high run differential allows individuals to make educated predictions on a total
win of a team.
2. The team with the highest average probability of winning for each game.
a. Using the probabilities computed of the smart men and women in the MLB
analytics team, if the average chances of an MLB team winning is high, then the
players of each team must be very good. Therefore, the team is successful.
b. Getting the average MLB rating is important as it does not provide a bias for the
teams with more games.
3. The team with the most career playoff wins. This is self explanatory.
The one who has the best overall rating regarding these categories is the most successful team.
Methodology
In order to analyze any data, it is required to import it from the fivethrityeight data website.
Furthermore, one must be able to make the teams into a list, then sort the list into a dataframe.
1. Solving the run differential is simple. First, identify the home games and the away games.
Get the general scores of the home and away teams. Afterward, get the overall scores
allowed by getting the sum of scores of the away team from the home section and vice
versa. Then calculate the differential by adding the scores allowed by the home and away
games played.
2. To calculate the highest average probability for each team winning, get the sum of
probabilities of each match in history for the home and away games (similar to run
differential). Afterwhich, add the home sum and the away sum, then divide it by the total
games played.3. To calculate the playoff wins, determine which team won each game by checking which
team had the greater score. Then, group by the home wins and the away wins.
Concatenate the team members to differentiate each game and remove the duplicates and
sort each team. Finally, group by the home team to get each playoff wins
