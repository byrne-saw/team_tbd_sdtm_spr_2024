# Project Milestone 5: SQL Design
The preliminary tables below will comprise the SQL structure to maintain and facilitate JeoparDIY gampeplay.

***
## Category Table
### Table Name: 
Category

### Description: 
Stores information related to our custom categories, which currently include Geography, History, Literature, Pop Culture, Science, and Sports. This table links each category to its corresponding questions and answers.

### Fields:
- CategID (INT, Primary Key)
- CategName (VARCHAR(50))

### Constraints:
- CategID must be unique
- CategName must be unique and not null

### Relationships:
- Links to the Clue_Answer Table through category_id.
- Links to the Game Table through category_id.

### Tests:
Use case name:
- Fetch 5 clue/answers that belong to CategName when CategID is queried

Description:
- Test game generation/customization

Pre-Conditions:
- Game initiation has been started w/ "Lets Play" onClick behavior, player names *may or may not* be established at this point.

Test Steps:
1) Navigate to 'Create Game' page
2) Enter quantity of players and their names
3) Test Random Category selection; click 'Random', start game
4) Test Custom Category selection; click 'Custom', start game

Expected Results:
- Valid game board is generated with 6 categories w/ 5 clue/answer squares each

Actual Results:
- Assert 6 category values are returned, each with a data length of 5 clue/answers

Status:

Notes:

Post-Conditions:
- Game is established and ready to play.

***
## Clue_Answer Table
#### Table Name:
Clue_Answer

### Description:
Contains all questions and clues pulled from past Jeopardy games, associated with categories.

### Fields:
- CluesAnsID INT (PK)
- CategID INT (FK)
- Value INT(5,2)
- Clue VARCHAR(255)
- Answer VARCHAR(255)

### Constraints:
- CluesAnsID must be unique
- CategID must exist in the Category table

### Relationships:
Each ClueAnsID correlates to a specific category

### Tests:

***
## Players Table
### Table Name: 
Players

### Description: 
Contains the current players and their attributed data

### Fields:
- PlayerID INT (PK)
- Name VARCHAR (50)
- Score INT

### Constraints:
- PlayerID is unique

### Relationships:
- PlayerID relates to Player# in Game table
- Score is queried 
### Tests:

***
## Game Table
### Table Name: 
Game

### Description:
Table for tracking/storing current game and board data.

### Fields:
- GameID INT (PK)
- Random BIT
- Player1 INT (nullable)
- Player2 INT (nullable)
- Player3 INT (nullable)
- Player4 INT (nullable)
- Category1 INT (CategoryID)
- Category2 INT (CategoryID)
- Category3 INT (CategoryID)
- Category4 INT (CategoryID)
- Category5 INT (CategoryID)
- Category6 INT (CategoryID)

### Constraints:
### Relationships:
### Tests:

***
## Game_Log Table
### Table Name:
Game_Log

### Description:
Logs the current state of gameplay to retrieve in case of page refresh/navigation

### Fields:
- GameID INT (FK)
- EventId INT (PK)
- CluesAnsID INT (FK)
- CluesAnsID INT (FK)
- Correct BIT

### Constraints:
### Relationships:
- GameID relates to game table for specific game data
- 
### Tests:
