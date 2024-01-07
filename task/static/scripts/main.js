function searchTask() {
    var searchInput = document.getElementById('search');
    var searchText = searchInput.value;
    window.location.href = '/search/' + searchText + '/';
}
