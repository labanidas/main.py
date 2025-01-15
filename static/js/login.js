$(document).ready(function () {
  $("form").submit(function (event) {
    event.preventDefault();

    var username = $("#username").val();
    var password = $("#password").val();

    $.ajax({
      url: "http://localhost:8000/cgi-bin/login.py",
      type: "POST",
      data: {
        username: username,
        password: password,
      },
      success: function (response) {
        if (response.status === "success") {
          localStorage.setItem("username", username);
          window.location.href = "/templates/dashboard.html";
        } else {
          $("#errorMessage").text(response.message);
          $("#errorModal").modal("show");
        }
      },
      error: function () {
        alert(
          "Error occurred while processing your request. Please try again."
        );
      },
    });

    $("form input").val(""); // Clear input fields
  });
});
