# Project Milestone 5: SQL Design
The preliminary tables below will comprise the SQL structure to maintain and facilitate JeoparDIY gampeplay.

***
## Category Table
#### Table Name: 
Category

#### Description: 
Stores information related to our custom categories, which currently include Geography, History, Literature, Pop Culture, Science, and Sports. This table links each category to its corresponding questions and answers.

#### Fields:
- CategID (INT, Primary Key)
- CategName (VARCHAR(50))

#### Constraints:
- CategID must be unique
- CategName must be unique and not null

#### Relationships:
- Links to the Clue_Answer Table through category_id.
- Links to the Game Table through category_id.

#### Tests:

***
## Clue_Answer Table
#### Table Name:
Clue_Answer

#### Description:
Contains all questions and clues pulled from past Jeopardy games, associated with categories.

#### Fields:
- CluesAnsID INT (PK)
- CategID INT (FK)
- Value INT(5,2)
- Clue VARCHAR(255)
- Answer VARCHAR(255)

#### Constraints:
- CluesAnsID must be unique
- CategID must exist in the Category table

#### Relationships:
Each ClueAnsID correlates to a specific category

#### Tests:

***
## Players Table
#### Table Name: 
Players

#### Description: 
Contains the current players and their attributed data

#### Fields:
- PlayerID INT (PK)
- Name VARCHAR (50)
- Score INT

#### Constraints:
- PlayerID is unique

#### Relationships:
- PlayerID relates to Player# in Game table
- Score is queried 
#### Tests:

***
## Game Table
#### Table Name: 
Game

#### Description:
Table for tracking/storing current game and board data.

#### Fields:
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

#### Constraints:
#### Relationships:
#### Tests:

***
## Game_Log Table
#### Table Name:
Game_Log

#### Description:
Logs the current state of gameplay to retrieve in case of page refresh/navigation

#### Fields:
- GameID INT (FK)
- EventId INT (PK)
- CluesAnsID INT (FK)
- CluesAnsID INT (FK)
- Correct BIT

#### Constraints:
#### Relationships:
- GameID relates to game table for specific game data
- 
#### Tests:
