
<center>JeoparDIY Web Page Design</center>
<br><br>

Page 3 Title: Create Your Game

Prototype: 

<img src="./Images/page3.png" alt="Page 3" width="300" height="200">

Parameters:  

1) Number of players, collected via radio button (or similar)
2) Names of players, collected via user input
3) If **CUSTOM**, categories (6) (updates page based on user selections of categories such as Geography, History, Literature, Pop Culture, Sports)
4) If **RANDOM**, categories (6) at random...see Data Needed)

Data Needed: 

1) Categories, either custom selected from list OR randomly selected from database
    - Will need selected categories; their respective clues AND the clues corresponding point values
    - If **CUSTOM**, fetch list of all categories and render as the dropdown list, series of radio buttons, etc.

Link Destinations: 
1) <u><font color="blue">Home</font></u>: Return to Homepage (not shown in prototype)

Tests for verifying the rendering of the page:
1) Verify that 1, 2, 3 and 4 player games initiate correctly
2) Verify that **RANDOM** reliably generates a full six category game onClick() (repeat selections with each click)
    - onClick() of submit/play button initiate gameplay and navigate to **/gameplay**
4) Verify that **CUSTOM** reliably generates a full six category game on
    - onClick() of submit/play button initiate gameplay and navigate to **/gameplay**
5) Visiting **/CreateGame** (or similar) URL of website returns HTML for rendering create game page



