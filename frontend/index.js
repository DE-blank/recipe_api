async function fetchData(){
  try{
    const input = document.getElementById('input').value.toLowerCase().replace(/\s+/g, '');
    const response = await fetch(`http://127.0.0.1:5000/search?ingredients=${input}`);
    const data = await response.json();
    
    console.log('Fetched data:', data); // Log the data to see its structure

    // Display data on the screen
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = ''; // Clear previous results

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
    } 
    else {
      const itemElement = document.createElement('div');
      itemElement.textContent = 'No results found';
      resultsContainer.appendChild(itemElement);
    }
  }
  catch(error){
    console.error('Error fetching data:', error);
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = 'An error occurred while fetching data';
  }
}