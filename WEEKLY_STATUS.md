# JeoparDIY Weekly Updates

## Week 3 Status:

Five different categories have been created: Geography, History, Pop Culture, Literature, and Sports. In each category, there are 10 possible clues taken fron three different Jeopardy games. The game ids used are 3942, 6885, and 8212. These clues and categories will serve as a basis to test populating our data base, choosing the categories, and randomizing the clues. As we get this working, more clues and categories can be added to allow the user extra customization.

Very rough first pass at a user interface has been created and shared to the repository for review. Team members will review and provide initial feedback for continued refinement prior to developing our front end pages design and explanations for next week. Development/refinement of this outline will be used for streamlined development of database, frontend development and Flask routing.

A Flask project directory was created with a basic Python script to define our Flask application and initial 
routes. A framework was set up to render HTML templates dynamically from a list of game categories. The next steps will involve meeting with the team in order to define additional routes and functions for our application, and to ensure alignment between the frontend and backend components of our website.

Flask Files in Shared Directory: 
```
flask_proj/
├── images
│   └── ...
├── static
│   ├── css
│   │   └── prefix.css
│   └── images
│       └── test.jpg
├── templates
│   └── categories.html
├── venv
│   └── ...
├── jeop_app.py
├── prefix.py
├── setup.cmds
```


## Week 4 Status:

Now that we have an initial sketch of the web pages, the routes in Flask are being extended to handle redirection and the flow of the website. All of the web pages currently have at least one button to allow a user to change pages. The POST method is being used to handle button clicks and to perform redirection. The backend will be developed further, especially when the web page design phase is complete. 

We are continuing to refine our web page prototypes this week. By the end of next week, we will finalize the parameters, links, data, and testing requirements for each page (this is not an actual implementation, but a detailed plan for each web page). We have a strong initial design of the user interface, gameplay/board layout, and web page flow.  

## Week 5 Status:

Milestone 4 has been completed and turned in. A team meeting was held to go over the PAGE_TESTING.md file and disucss any necessary changes. After the meeting, the appropriate changes were made and the milestone was submitted to Moodle. In the meeting, we also discussed the next steps for each team member and made plans for our next weekly meeting. 

## Week 6 Status:

The database of clues has been expanded to include 6 categories with 10 clues each. This way, we have the data for one complete game of Jeopardy to work with as we work on the SQL milestone. The category added was Science, with clues taken from game ids 8831 and 8833. Also, a script to extract the answers from the game html files was written and added to the bin directory. This script was then used to extract the correct responses for the clues that are included in our database. The answers are all located in the newly created answers directory. This has the same layout as the clues directory, with each category having its own folder and text file, and all of the answers are in the same order that the clues are in in their respective text files. Further, the html files for all of the games used have been added to the repository in the game_files directory. 


