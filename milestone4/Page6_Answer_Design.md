
<center>JeoparDIY Web Page Design</center>
<br><br>

Page 6 Title: Answer

Prototype: 

<img src="./Images/page6.png" alt="Page 6" width="300" height="200">

Parameters:
1) Active player (depending on UI/UX this likely is not needed)
2) Clue Name/ID
3) Clue Value
4) User Input from Hint Page

Data Needed: 
1) Correct Question (answer)

Link Destinations: 

1) <u><font color="blue">Home</font></u>: Return to Homepage
2) <u><font color="blue">Return</font></u>: Return to Gameplay page

Tests for verifying the rendering of the page:
1) Verify that answer text/card and its value rendered matches previous hint card
2) Verify that incorrect user input triggers visual response (indicate by color or similar)
3) Verify that correct user input triggers visual response (indicate by color or similar)
4) Verify that onClick() of return button, return to game and increment/decrement is registered
5) Verify that **/Game(id)/Hint** URL renders page correctly
    - If visited prior to game creation, error message and redirect occurs




