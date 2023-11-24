# Halo Tracker

It is our goal to create a website that will give us that stats of ourselves and others. And give us aThe application we would like to build is a statistic tracker website for Halo Infinite. The use
case would be for players looking to view their own performance statistics or the performance
statistics of other players from the games they play in Halo Infinite. This is useful for players
trying to track their own performance and/or compare themselves to other players. The
application would enable players to bookmark players or games.

as this is Really just the start of the project we have a set of fetures that we would like:

## Must Have Features:
- As a User, I should be able to login.

- As a User, I should be able to change my password and delete account.

- As a User, I should be able to search for players with an Xbox Live Username

- As a user, I should be able to link my own Xbox Live username for quick access to my

- As a user, I should be able to view the average stats of players (K/D, Win Percentage, Average Damage, etc.)

## Nice to have features:

## Technical Challenges

publicly available API for Halo Infinite player and game statistics, so we are planning on using a custom web scraper tool built in Python to acces player and game data from stat websites such as halotracker.com. This will be the most complicated part of the project and will be the biggest hurdle to overcomeould be able to bookmark specific players for quick access to their stats.
Group Members
- Brandon Herrin (A02336477)
- Jaden Anderson (A02210459).

Requirements
- API: We will require an API that allows us to access player and game statistics.
o API must allow for general stats to be gathered from any public Halo player
profile
- User Accounts: Users should be able to create accounts to login to.
* The user should be able to change their account password.
* The user should be able to delete their account.
* Only the user can access their user profile unless they choose to make it profile
* The user should be able to link an Xbox Live username to their account for quick
access to their stats.
- Player Statistic: Users should be able to search up players’stats based on their Xbox Live
username.
* If the given Xbox Live username is invalid or inaccessible, return error message.
- Bookmarks
