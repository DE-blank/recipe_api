// Funktion zum Erhalt von Daten von der API
async function fetchData() {
  const searchButton = document.querySelector('button');
  const resultsContainer = document.getElementById('results');
  const input = document.getElementById('input').value.toLowerCase().replace(/\s+/g, '');

  // Eingabe Sperren
  searchButton.disabled = true;
  searchButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Searching...';

  try {
    const response = await fetch(`http://127.0.0.1:5000/search?ingredients=${input}`);
    
    // Ausgabe des Antwortstatus
    console.log('Response status:', response.status);

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const data = await response.json();


    // Vorherige Suchergebnisse löschen
    resultsContainer.innerHTML = '';
    // Neue Suchergebnisse anzeigen
    if (data.recipes && Array.isArray(data.recipes) && data.recipes.length > 0) {
      data.recipes.forEach(recipe => {
        const recipeElement = document.createElement('div');
        recipeElement.classList.add('recipe');

        const titleElement = document.createElement('h3');
        titleElement.textContent = recipe.title;
        recipeElement.appendChild(titleElement);

        const ingredientsTitle = document.createElement('h4');
        ingredientsTitle.textContent = 'Ingredients:';
        recipeElement.appendChild(ingredientsTitle);

        const ingredientsList = document.createElement('ul');
        JSON.parse(recipe.ingredients).forEach(ingredient => {
          const listItem = document.createElement('li');
          listItem.textContent = ingredient;
          ingredientsList.appendChild(listItem);
        });
        recipeElement.appendChild(ingredientsList);

        const directionsTitle = document.createElement('h4');
        directionsTitle.textContent = 'Directions:';
        recipeElement.appendChild(directionsTitle);

        const directionsElement = document.createElement('p');
        directionsElement.textContent = JSON.parse(recipe.directions).join(' ');
        recipeElement.appendChild(directionsElement);

        resultsContainer.appendChild(recipeElement);
      });
    } else {
      resultsContainer.innerHTML = '<p>No recipes found.</p>';
    }
  } catch (error) {
    console.error('Error fetching data:', error);
    // Animation verlängern bei Fehler Meldung
    searchButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Searching...';
    await new Promise(resolve => setTimeout(resolve, 2500));
    resultsContainer.innerHTML = '<p>Error fetching data. Please try again later.</p>';
  } finally {
    // Wieder Aktivieren des Suchbuttons
    searchButton.disabled = false;
    searchButton.innerHTML = '<i class="fas fa-search"></i> Search';
  }
}

// Event Listener für Enter Taste
document.getElementById('input').addEventListener('keypress', function(event) {
  if (event.key === 'Enter') {
    fetchData();
  }
});

// Event Listener für Suchbutton
document.querySelector('button').addEventListener('click', fetchData);