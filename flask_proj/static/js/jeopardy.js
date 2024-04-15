// Javascript for JeoparDIY Game functions

// handle ‘Play’ and ‘About’ Buttons
// Function to handle "Play" button click
document.getElementById('play-button').addEventListener('click', () => {
	// Redirect to the player names page
	window.location.href = '/player-names';
});
// Function to handle "About" button click
document.getElementById('about-button').addEventListener('click', () => {
	// Redirect to the about page
	window.location.href = '/about';
});


// Function to handle "Random" category button click
document.getElementById('random-button').addEventListener('click', () => {
	// Send an AJAX request to fetch random categories from the server
	// Display the fetched categories in the 'categories' div
	fetch('/random-categories')
		.then(response => response.json())
		.then(data => {
			const categoriesDiv = document.getElementById('categories');
			categoriesDiv.innerHTML = ''; // Clear previous categories

			// Display the fetched categories
			data.categories.forEach(category => {
				const categoryElement = document.createElement('div');
				categoryElement.textContent = category;
				categoriesDiv.appendChild(categoryElement);
			});
		})
		.catch(error => console.error('Error fetching random categories:', error));
});


// Function to add player name slots dynamically
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
