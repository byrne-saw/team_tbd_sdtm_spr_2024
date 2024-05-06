# Project Title: JeoparDIY

## Team Members
Andrew Byrnes, Cameron Braatz, Ben Little, Amber Tin, Kori Price

## Project Tracker Link:
[JeoparDIY Trello](https://trello.com/b/H7kuLDWW/teamtbdsdtmspr2024)

## Demo Video:
[JeoparDIY Demo](https://github.com/byrne-saw/team_tbd_sdtm_spr_2024/blob/main/JeoparDIY_demo_video.mp4)

## Repository Link
[JeoparDIY Repository](https://github.com/byrne-saw/team_tbd_sdtm_spr_2024)

## Public Website Link
[Public Website](https://team-tbd-sdtm-spr-2024-p0th.onrender.com)


## Final Status Report:
### Completed:
We designed and developed an application that kickstarts the process of creating a customizable Jeopardy game utilizing clues and categories from past Jeopardy games. Users first arrive on a landing page with the option to learn more (About) or start initializing a game (Play). Opting for the ‘About’ option leads the user to a page with an initial explanation of the app and its vision, while choosing the ‘Play’ option navigates to a page that prompts and accepts dynamic user input for the user’s chosen name. Once accepted, the application builds and displays the iconic Jeopardy board where the user’s name fills the scoreboard, and database queries fill the six clue columns.

To gather clues for the application, we developed scripts to download the raw .HTML data from J-archive and extract relevant clue and answer details. With these scripts, we built a database of clues sorted into six different categories: Geography, History, Literature, Pop Culture, Science, and Sports. Currently, this database includes 10 clues in each category, sufficient for a complete Jeopardy game. However, our developed scripts allow for efficient expansion. The current clues are stored in a dedicated clues subdirectory while the correct answers are stored in the answers subdirectory.  

For further detail about our SQL database design, including the PLAYER, GAME, CATEGORY, CLUE_ANSWER, and GAME_LOG tables, as well as the designed testing, see 
 [SQL_TESTING.md](https://github.com/byrne-saw/team_tbd_sdtm_spr_2024/blob/main/SQL_TESTING.md).


### Ongoing Development:
In our most recent stages of development, we were focusing on a single game file to eliminate confounding variables, ensure our data extraction was accurate, and test if the data could integrate into the application without causing a cascade of issues. To do so, we scraped the .HTML file from J-Archive, isolated the pertinent info such as clue IDs, clue text, and category name, then converted this information into a text format including category IDs. With this, a ‘Clues’ database table was created in the app.py file and data was read into each field of the Clues table. Ultimately, our intention was to use this table with a JavaScript function to fetch clue data based on the player’s selection on the game board, but we wanted to implement SQL tests for the new table and relationship prior to adding this function. Due to time constraints, this branch with the revised app.py file wasn’t merged into the main branch. 

Beyond this, we were working on multiplayer functionality, a random query of the database, and an option to select broad, predefined clue categories for a customizable game. For multiplayer functionality, we were exploring dynamically adding additional form inputs as well as using a static array of input fields to accommodate more than one player. The random query would minimize the chance of repeat conditions over consecutive games, and the category selection would provide a dropdown menu or equivalent option to help the user take advantage of the wealth of Jeopardy categories available while giving more control over the game play.


### Future Plans:
Moving forward, we plan to shift our focus towards implementing scoring and interacting with the game board. While seemingly straightforward, we found that planning for, anticipating, and emulating the logic behind a Jeopardy game’s progression has a unique and unexpected set of challenges. For example, each player needs the ability to reveal and respond to clues within concealed category boxes. Upon clicking a box, the user will be prompted to input an answer, triggering a comparison with appropriate tolerance, and transitioning to reveal the correct answer, rewarding points for correct responses and detracting for incorrect responses. On returning to the game board, the chosen clue must no longer be an option and the game needs to progress to the next question and/or player. But what is an appropriate level of tolerance for an answer given and checked through text and what is the best way of implementing this? Can the buzzing in practice be replicated as well? If not, how should the next player be selected to choose a question? 

After the essential mechanics, we planned to continue to develop the Daily Double hidden tile, as well as the Double Jeopardy and Final Jeopardy game play functionality. Ultimately, functionality would also include declaring a winner, presenting the scores, and prompting for another game. We also discussed saving scores and displaying a leaderboard of top players.

### Known Bugs:
As the application stands, we have yet to establish the logic to pull “random” clue categories nor manually selected clue categories to generate the game board. As touched on earlier our application makes valid database queries to pull the data, just in a hard-coded manner that consistently returns the same categories. 
The application does not allow for multiple players at this point, with the logic to dynamically generate additional user fields and/or an array of set player inputs to be created. This hangup will proceed to generate a single player game rather than offering the option for more dynamic play.
Game tiles are not currently clickable making the actual game board a visual representation of the end product, much of this logic has yet to be ironed out and developed. That said, the components of the project that are completed have been vetted and do not exhibit any known bugs.

### Weekly Meetings:
Due to schedule conflicts, we needed to establish our project meetings on a weekly basis. Our team’s full weekly availability would be known every Sunday, at which point we shared a When2Meet on our Discord channel. The team would outline their anticipated availability and the When2Meet interface would illustrate particular times that would maximize our attendance.
Using this approach allowed us to have meetings with all team members in attendance for the vast majority of the semester, while providing the flexibility to meet according to upcoming deadlines and current project hangups. Establishing meetings week to week based on our current availability ensured that we could maximize our team’s attendance. The flexible nature had its benefits, but often made our sprints revolve around major project deadlines rather than general development milestones.
Overall, our team made the most of the changing schedule and were able to maintain fairly consistent weekly meetings. We were still able to hit all our project milestones without the need for late nights or rushed development at the last minute. In a real-world scenario, it would have likely been most effective to have a consistent Agile stand-up to retain pacing throughout the project while supplemental floating meetings could be scheduled independently for more in-depth project collaboration/support.

## Public Deployment Site:
