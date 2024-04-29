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



// ************** Categories  ***************

// function to fetch categories from Flask route and populate the gameplay page
function fetchCategories() {
	fetch('/categories')
		.then(response => response.json())
		.then(data => {
			// Update the category headers on the gameplay page
			for (let i = 0; i < data.length; i++) {
				document.getElementById(`header_${i + 1}`).textContent = data[i].CategName;
			}
		})
		.catch(error => console.error('Error fetching categories:', error));
}


window.onload = () => {
	// add player name slots dynamically
	const playerNamesDiv = document.getElementById('player-names');
	const numPlayers = 4; // Number of player name slots

	for (let i = 1; i <= numPlayers; i++) {
		const input = document.createElement('input');
		input.type = 'text';
		input.placeholder = `Player ${i} Name`;
		playerNamesDiv.appendChild(input);
	}


	// add event listener to the submit button for player names
	document.getElementById('submit-name-button').addEventListener('click', submitPlayerName);
	
	// fetch categories from Flask route and populate the gameplay page
	fetchCategories();

	// add event listener to the "Random" category button
	document.getElementById('random-button').addEventListener('click', () => {
		// send an AJAX request to fetch random categories from the server
		// display the fetched categories in the 'categories' div
		fetch('/random-categories')
			.then(response => response.json())
			.then(data => {
				const categoriesDiv = document.getElementById('categories');
				categoriesDiv.innerHTML = ''; // Clear previous categories

				// display the fetched categories
				data.categories.forEach(category => {
					const categoryElement = document.createElement('div');
					categoryElement.textContent = category;
					categoriesDiv.appendChild(categoryElement);
				});
			})
			.catch(error => console.error('Error fetching random categories:', error));
	});

};