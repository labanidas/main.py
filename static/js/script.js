$(document).ready(function () {
  $(".nav-section").hide();

  $("#sidebar-items li").click(function () {
    var target = $(this).data("bs-target");

    $(".content-section").hide();

    $("#" + target).show();
  });

  $("#all-students").show();

  $.get(
    "http://localhost:8000/cgi-bin/student-crud/read.py",
    function (response) {
      if (response.status === "success") {
        const students = response.data;

        // Iterate over students and append rows to the table
        students.forEach(function (student) {
          const row = `
              <tr>
                <td>${student.id}</td>
                <td>${student.name}</td>
                <td>${student.roll}</td>
                <td>${student.marks}</td>
              </tr>
            `;
          $("#students-table tbody").append(row);
        });
      } else {
        console.error("Error loading student data:", response.message);
      }
    }
  );

  // ------------- create student form -------------
  $("form").submit(function (event) {
    event.preventDefault();

    var studentName = $("#studentName").val();
    var rollNumber = $("#rollNumber").val();
    var marks = $("#marks").val();

    $.ajax({
      url: "http://localhost:8000/cgi-bin/student-crud/add.py",
      type: "POST",
      data: {
        name: studentName,
        roll: rollNumber,
        marks: marks,
      },
      success: function (response) {
        if (response.status === "success") {
          // Add a new row to the table
          var newRow = `
          <tr>
            <td>${response.student.id}</td>
            <td>${response.student.name}</td>
            <td>${response.student.roll}</td>
            <td>${response.student.marks}</td>
          </tr>
        `;
          $("#students-table tbody").append(newRow);

          // Show modal with the response message
          $("#successMessage").text(response.message);
          $("#successModal").modal("show");
        } else {
          // Show error modal
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

    // Clear input fields
    $("form input").val("");
  });
});
