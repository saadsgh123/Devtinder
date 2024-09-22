// Fetch countries using REST Countries API
    async function fetchCountries() {
        try {
            const response = await fetch('https://restcountries.com/v3.1/all');
            const countries = await response.json();

            // Sort countries alphabetically by their common name
            countries.sort((a, b) => {
                return a.name.common.localeCompare(b.name.common);
            });

            const countrySelect = document.getElementById('country');
            countrySelect.innerHTML = '';  // Clear initial options

            // Populate the select input with sorted countries
            countries.forEach(country => {
                const option = document.createElement('option');
                option.value = country.cca2;  // Use country code as value
                option.textContent = country.name.common;  // Use country name
                countrySelect.appendChild(option);
            });

        } catch (error) {
            console.error('Error fetching countries:', error);
        }
    }

    // Call the function to load and sort countries when the page loads
    document.addEventListener('DOMContentLoaded', fetchCountries);

  const selectElement = document.getElementById('techSelect');
  const addButton = document.getElementById('addButton');
  const techList = document.getElementById('techList');
  const sendListButton = document.getElementById('sendListButton');

  let selectedTechnologies = [];

  // Add selected value to list and display on the page
  addButton.addEventListener('click', function() {
    const selectedValue = selectElement.value;

    if (!selectedTechnologies.includes(selectedValue)) {
      selectedTechnologies.push(selectedValue);

      const listItem = document.createElement('li');
      listItem.textContent = selectedValue;

      const deleteButton = document.createElement('button');
      deleteButton.textContent = 'Delete';
      deleteButton.classList.add('delete-btn');

      // Add delete functionality
      deleteButton.addEventListener('click', function() {
        const index = selectedTechnologies.indexOf(selectedValue);
        if (index > -1) {
          selectedTechnologies.splice(index, 1); // Remove from array
        }
        techList.removeChild(listItem); // Remove from the UI
      });

      listItem.appendChild(deleteButton);
      techList.appendChild(listItem);
    }
  });

  // Send the list to the Flask server via AJAX
  sendListButton.addEventListener('submitBtn', function() {
    fetch('/update_profile', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ techList: selectedTechnologies })
    })
        .then(response => response.json())
        .then(data => {
          alert('List sent to the server: ' + data.message);
        })
        .catch(error => {
          console.error('Error:', error);
        });
  });