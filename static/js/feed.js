document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.querySelector('.search-bar button');
    const experienceSelect = document.getElementById('experience');
    const locationSelect = document.getElementById('location');
    const searchInput = document.querySelector('.search-bar input');
  
    searchButton.addEventListener('click', function(event) {
      //event.preventDefault(); // Prevent form submission
  
      // Fetch data based on selected filters and search query
      fetchData();
    });
  
    function fetchData() {
      const experienceValue = experienceSelect.value;
      const locationValue = locationSelect.value;
      const searchValue = searchInput.value;
  
      // Construct URL with query parameters
      const url = `/feed?search=${searchValue}&experience=${experienceValue}&location=${locationValue}`;
  
      fetch(url, {
        headers: {
          'X-Requested-With': 'XMLHttpRequest'  // Important to distinguish AJAX request
        }
      })
      .then(response => response.json())
      .then(data => {
        // Update the profile-cards section with new data
        const profileCards = document.querySelector('.profile-cards ul');
        profileCards.innerHTML = ''; // Clear existing cards
  
        if (data.users.length === 0) {
          profileCards.innerHTML = '<li>No users found</li>';
        } else {
          data.users.forEach(user => {
            const card = `
              <div class="profile-card">
                <div class="profile-image"></div>
                <h3>${user.username}</h3>
                <p class="job-title">${user.job_title}</p>
                <p class="freelancer">${user.freelancer}</p>
                <div class="technologies">
                  ${user.technologies.map(tech => `<span class="tech">${tech}</span>`).join('')}
                </div>
                <p class="description">${user.description}</p>
                <button class="view-profile">View Profile</button>
              </div>
            `;
            profileCards.innerHTML += card;
          });
        }
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
    }
  });
  