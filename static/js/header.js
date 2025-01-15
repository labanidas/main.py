$(document).ready(function() {
    var currentUser = localStorage.getItem("username");

    if (currentUser) {
        $('#loginBtn').hide();
        $('#signupBtn').hide();
        $('#logoutBtn').show();

        $('#logoutBtn').click(function(event) {
            event.preventDefault();
            destroySessionAndRedirect();
        });
    } else {
        $('#loginBtn').show();
        $('#signupBtn').show();
        $('#logoutBtn').hide();
    }
});

function destroySessionAndRedirect() {
    localStorage.removeItem("username");
    window.location.href = window.location.href;
}
