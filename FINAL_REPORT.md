# Project Title: JeoparDIY

## Team Members
Andrew Byrnes, Cameron Braatz, Ben Little, Amber Tin, Kori Price

## Project Tracker Link:
[JeoparDIY Trello](https://trello.com/b/H7kuLDWW/teamtbdsdtmspr2024)

## Demo Video

## Repository Link
[JeoparDIY Repository](https://github.com/byrne-saw/team_tbd_sdtm_spr_2024)

## Final Status Report:
### Completed:
We designed and developed an application that performs the first few steps to generating a Jeopardy game board, sourcing it’s clue categories from previous real-world Jeopardy games. The user arrives at a landing page with the option to learn more (About) or start initializing a game (Play).
The former option navigates to a page with a preliminary explanation of the application and its vision, while the latter option navigates to a page that accepts dynamic user input for the user’s chosen name. Once accepted, the application navigates to a page with the classic Jeopardy board. The player’s name from the previous page is used to populate the scoreboard at the bottom of the screen, while a query to our database tables returns the category clues that fill the six clue columns. More information about our SQL database, including the PLAYER, GAME, CATEGORY, CLUE_ANSWER, and GAME_LOG tables as well as the necessary testing can be found in the file 
 [SQL_TESTING.md](https://github.com/byrne-saw/team_tbd_sdtm_spr_2024/blob/main/SQL_TESTING.md).

To source the clues, we were able to complete scripts for downloading and extracting clues and responses from html files on J-archive. Using these scripts, 
we were able to create a database of clues sorted into six different categories: Geography, History, Literature, Pop Culture, Science, and Sports. Our database
includes 10 clues in each category, which is enough for one full game of Jeopardy. These clues are stored in the clues subdirectory, while the correct responses
are in the answers subdirectory. 


### In the middle:
In the ongoing development of our game, a single game file that was sourced from J! Archive was used to extract data (clue IDs, clue text, category name). This file was converted from HTML to a text format and category IDs were added. A ‘Clues’ database table was created in the app.py file. Data was read into each field of the Clues table. The plan was to use this table for a JavaScript function that fetches the clue data based on a player’s selection from the gameboard. This function was to be added after running SQL tests for the new table and relationship. Due to the time constraint, this branch with the revised app.py file wasn’t merged into the main branch.
In addition, we were working on allowing our application to accept more than one player, either dynamically adding additional form inputs or using a static array of input fields to do so. While we queried our database in order to populate the headers for each clue column, we were also working towards developing logic to generate “random” queries into the database. This would allow for games to be played consecutively with a small chance for repeat conditions upon repeated plays.
In addition to the random clue generation logic, we were working on an option to manually select clue categories from the set of all categories. A dropdown menu (or similar) would query all categories and allow the player(s) to select any six categories to form their own custom game.

### Future Plans:
In the future we were planning to tackle the logic behind scoring and interacting with the game board. While it appears fairly straightforward, we found that planning and anticipating for the logic behind the progression of an actual Jeopardy game to be quite complex.
For example, for any given player they would be able to click and open a concealed category’s clue box revealing the clue to be answered. The user would be prompted to input an answer, which would trigger an assert equal (with sufficient wiggle room) and a transition to reveal the answer…rewarding points should the user be correct. On returning to the game board, the chosen tile will have been flipped and would no longer be clickable. The next player in line would be prompted and the process continues.
We would have continued to develop the “Daily Double” hidden tile, as well as the Double Jeopardy and Final Jeopardy game play functionality. Ultimately declaring a winner, presenting the scores and prompting for another game.

### Known Bugs:
As the application stands, we have yet to establish the logic to pull “random” clue categories nor manually selected clue categories to generate the game board. As touched on earlier our application makes valid database queries to pull the data, just in a hard-coded manner that consistently returns the same categories. 
The application does not allow for multiple players at this point, with the logic to dynamically generate additional user fields and/or an array of set player inputs to be created. This hangup will proceed to generate a single player game rather than offering the option for more dynamic play.
Game tiles are not currently clickable making the actual game board a visual representation of the end product, much of this logic has yet to be ironed out and developed. That said, the components of the project that are completed have been vetted and do not exhibit any known bugs.

### Weekly Meetings:
Due to schedule conflicts, we needed to establish our project meetings on a weekly basis. Our team’s full weekly availability would be known every Sunday, at which point we shared a When2Meet on our Discord channel. The team would outline their anticipated availability and the When2Meet interface would illustrate particular times that would maximize our attendance.
Using this approach allowed us to have meetings with all team members in attendance for the vast majority of the semester, while providing the flexibility to meet according to upcoming deadlines and current project hangups. Establishing meetings week to week based on our current availability ensured that we could maximize our team’s attendance. The flexible nature had its benefits, but often made our sprints revolve around major project deadlines rather than general development milestones.
Overall, our team made the most of the changing schedule and were able to maintain fairly consistent weekly meetings. We were still able to hit all our project milestones without the need for late nights or rushed development at the last minute. In a real-world scenario, it would have likely been most effective to have a consistent Agile stand-up to retain pacing throughout the project while supplemental floating meetings could be scheduled independently for more in-depth project collaboration/support.

## Public Deployment Site:
