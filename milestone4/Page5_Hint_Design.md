
<center>JeoparDIY Web Page Design</center>
<br><br>

Page 5 Title: Hint

Prototype: 

<img src="./Images/page5.png" alt="Page 5" width="300" height="200">

Parameters: 
1) Active player
    - Populate user input box with active player's name and prompt
2) Clue Name/ID
3) Clue Value
4) User response
    - Gather from user input

Data Needed:
1) Correct Question (answer)
2) Clue text/description

Link Destinations: 

1. <u><font color="blue">Home</font></u>: Return to Homepage
2. <u><font color="blue">Submit</font></u>: Navigate to Answer page

Tests for verifying the rendering of the page:
1) Verify that answer text/card and its value rendered matches the button clicked previously
2) Verify that incorrect user input triggers incorrect response (navigate/trigger answer)
3) Verify that correct user input triggers correct response (navigate/trigger answer)
4) Verify that empty user input triggers error message prompting valid input
5) Verify that **/Game{id}/Hint** URL renders page correctly
    - If visited prior to game creation, error message and redirect occurs



