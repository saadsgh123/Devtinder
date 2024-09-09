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
