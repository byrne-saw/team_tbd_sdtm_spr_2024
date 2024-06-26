// Javascript for JeoparDIY Game functions


// define the function to redirect to the about page
function redirectToAboutPage() {
	// redirect to the about page
	window.location.href = '/about';
}

// define the function to redirect to the about page
function redirectToPlayPage() {
	// redirect to the about page
	window.location.href = '/player-names';
}

// define the function to redirect to the about page
function redirectToHomePage() {
	// redirect to the about page
	window.location.href = '/';
}



// ************** Player Name ***************

// add player name slots dynamically
window.onload = () => {
	const playerNamesDiv = document.getElementById('player-names');
	const numPlayers = 4; // Number of player name slots

	for (let i = 1; i <= numPlayers; i++) {
		const input = document.createElement('input');
		input.type = 'text';
		input.placeholder = `Player ${i} Name`;
		playerNamesDiv.appendChild(input);
	}
};


// define variables to store player names
let playerName = "";

// function to handle the submission of player name
function submitPlayerName() {
	// get the input values
	playerName = document.getElementById('player-input').value.trim();
	
	// check if both input field is filled
	if (playerName) {
		// store the player name in localStorage to pass it to the gameplay.html page
		localStorage.setItem('playerName', playerName);
        
		// redirect to the gameplay.html page
		window.location.href = '/gameplay';
	} else {
		alert("Please enter player name.");
	}
}

// add event listener to the submit button
document.getElementById('submit-name-button').addEventListener('click', submitPlayerName);







