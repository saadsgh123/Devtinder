
document.getElementById('toggle-more').addEventListener('click', function(event) {
    event.preventDefault();
    const moreOptions = document.getElementById('more-options');
    const moreLink = document.getElementById('toggle-more');

    if (moreOptions.classList.contains('collapsed')) {
        moreOptions.classList.remove('collapsed');
        moreLink.textContent = 'Less';
    } else {
        moreOptions.classList.add('collapsed');
        moreLink.textContent = 'More';
    }
});

function toggleDropdown() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.circle')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}
