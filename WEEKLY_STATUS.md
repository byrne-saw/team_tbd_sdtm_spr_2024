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





