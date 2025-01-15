$(document).ready(function () {
  $("button[type='submit']").prop("disabled", true);

  $("#password, #confirm-password").on("input", function () {
    var password = $("#password").val();
    var confirmPassword = $("#confirm-password").val();

    if (password === confirmPassword && password !== "") {
      $("button[type='submit']").prop("disabled", false);
    } else {
      $("button[type='submit']").prop("disabled", true);
    }
  });

  $("form").on("submit", function (e) {
    e.preventDefault();

    var formData = {
      username: $("#username").val(),
      password: $("#password").val(),
    };

    // Make the POST request to the backend
    $.ajax({
      url: "http://localhost:8000/cgi-bin/register.py", // Form action URL
      type: "POST",
      data: formData,
      success: function (response) {
        // Show a Bootstrap modal with the response message
        var modalHtml = `
      <div class="modal fade" id="responseModal" tabindex="-1" aria-labelledby="responseModalLabel" aria-hidden="true">
          <div class="modal-dialog">
              <div class="modal-content">
                  <div class="modal-header">
                      <h5 class="modal-title" id="responseModalLabel">Registration Status</h5>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                      ${response.message}
                  </div>
                  <div class="modal-footer">
                      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                  </div>
              </div>
          </div>
      </div>
  `;

        // Append modal HTML to body and show the modal
        $("body").append(modalHtml);
        $("#responseModal").modal("show");

        // Redirect to login page when the modal is closed
        $("#responseModal").on("hidden.bs.modal", function () {
          window.location.href = "/templates/login.html"; // Redirect to login page
        });

        console.log(response.message);
      },
      error: function (xhr, status, error) {
        alert("Registration failed! " + error);
      },
    });

    $("form input").val(""); // Clear input fields
  });
});
