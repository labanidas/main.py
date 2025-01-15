$(document).ready(function () {
  function getQueryStringParameter(name) {
    var urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
  }

  var studentId = getQueryStringParameter("id"); // Get 'id' from the query string

  if (studentId) {
    var formData = { id: studentId };

    $.ajax({
      url: "http://localhost:8000/cgi-bin/student-crud/read_one.py", // Endpoint URL
      method: "POST",
      data: formData,
      success: function (response) {
        if (response.status === "success") {
          // Populate the form with the student data
          $("#studentName").val(response.message.name);
          $("#rollNumber").val(response.message.roll);
          $("#marks").val(response.message.marks);
        } else {
          alert("Error: " + response.message);
        }
      },
      error: function () {
        alert("Failed to fetch student details.");
      },
    });
  } else {
    alert("No student ID provided in the query string.");
  }

  $("form").on("submit", function (e) {
    e.preventDefault();

    var formData = {
        name: $("#studentName").val(),
        roll: $("#rollNumber").val(),
        marks: $("#marks").val(),
    };
    $.ajax({
      url: "http://localhost:8000/cgi-bin/student-crud/edit.py",
      type: "POST",
      data: formData,
      success: function (response) {
        if (response.status === "success") {
            window.location.href = "/index.html";
        }else{
        $("#errorMessage").text(response.message);
          $("#errorModal").modal("show");
        }
      },
      error: function (xhr, status, error) {
        alert(error);
      },

    });
  });
});
