function confirmDelete(event) {
    event.preventDefault();
    if (confirm("Delete Task?")) {
        window.location.href = event.target.href;
    }
}

var deleteButtons = document.querySelectorAll(".btn-delete");

deleteButtons.forEach(function(button) {
    button.addEventListener("click", confirmDelete);
});
