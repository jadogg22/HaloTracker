# Halo Player Tracker

The application we would like to build is a statistic tracker website for Halo Infinite. The use case would be for players looking to view their own performance statistics or the performance statistics of other players from the games they play in Halo Infinite. This is useful for players trying to track their own performance and/or compare themselves to other players. 

Development Plan (Revision 1.1)

## Must Have Features:
- As a user, I should be able to login.
- As a user, I should be able to delete my account.
- As a user, I should be able to search for players by their Xbox Live username.
- As a user, I should be able to link my own Xbox Live username for quick access to my stats.
- As a user, I should be able to view the average stats of players (K/D, Win Percentage, Average Damage, etc.)

## Nice to Have Features:
- As a user, I should be able to view my bookmarked players when I am logged in.
- As a user, I should be able to view a player’s stats from individual games.
- As a user, I should be able to bookmark individual games.
- As a user, I should be able to follow other users to see what players and games they have bookmarked

## Technical Challenges

The largest technical challenge we foresee is accessing player and game data. There is no publicly available API for Halo Infinite player and game statistics, so we are planning on using a custom web scraper tool built in Python to access player and game data from stat websites such as halotracker.com. This will be the most complicated part of the project and will be the biggest hurdle to overcome.

## Group Members
- Brandon Herrin (A02336477)
- Jaden Anderson (A02210459).

## Overall Project Requirements
- API: We will require an API that allows us to access player and game statistics.
    - API must allow for general stats to be gathered from any public Halo player profile
- User Accounts: Users should be able to create accounts to login to.
    - The user should be able to delete their account.
    - The user should be able to link an Xbox Live username to their account for quick access to their stats.
- Player Statistic: Users should be able to search up players’ stats based on their Xbox Live username.
    - If the given Xbox Live username is invalid or inaccessible, return error message.
- Bookmarks
    - Users should be able to bookmark specific players for quick access to their stats.