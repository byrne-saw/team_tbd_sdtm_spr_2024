// Javascript for JeoparDIY Game Play 


// define the function to redirect to the about page
function redirectToHomePage() {
	// redirect to the about page
	window.location.href = '/';
}



// ************** Categories  ***************

// function to fetch categories from Flask route and populate the gameplay page
function fetchCategories() {
	fetch('/categories')
		.then(response => response.json())
		.then(data => {
			// Update the category headers on the gameplay page
			for (let i = 0; i < data.length; i++) {
				document.getElementById(`categ_${i + 1}`).innerText = data[i].CategName;
			}
		})
		.catch(error => console.error('Error fetching categories:', error));
}

// call fetchCategories() when the window is fully loaded
window.onload = function() {
	fetchCategories();
};


// Function to handle "Random" category button click
/*
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
*/


