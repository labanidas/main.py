$(document).ready(function () {
  // Hide all nav sections and show the "All Students" section by default
  $(".nav-section").hide();
  $("#all-students").show();

  // Function to load students and update the table
  function loadStudents() {
    $.get(
      "http://localhost:8000/cgi-bin/student-crud/read.py",
      function (response) {
        if (response.status === "success") {
          const students = response.data;
          students.forEach(function (student) {
            appendStudentRow(student);
          });
        } else {
          console.error("Error loading student data:", response.message);
        }
      }
    );
  }

  // Function to append a student row to the table
  function appendStudentRow(student) {
    const newRow = `
      <tr id="student${student.id}">
        <td>${student.id}</td>
        <td>${student.name}</td>
        <td>${student.roll}</td>
        <td>${student.marks}</td>
        <td><a href="/templates/student-crud/edit.html?id=${student.id}" class="btn btn-warning btn-sm">Edit</a></td>
        <td>
          <button type="button" class="btn btn-danger delete-btn" data-id="${student.id}">
            Delete
          </button>
        </td>
      </tr>
    `;
  
    $("#students-table tbody").append(newRow);
  }
  

  // Load students when the page loads
  loadStudents();

  // Handle sidebar navigation
  $("#sidebar-items li").click(function () {
    const target = $(this).data("bs-target");
    $(".content-section").hide();
    $("#" + target).show();
  });

  // Handle student creation
  $("form").submit(function (event) {
    event.preventDefault();

    const studentName = $("#studentName").val();
    const rollNumber = $("#rollNumber").val();
    const marks = $("#marks").val();

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
          appendStudentRow(response.student);
          $("#successMessage").text(response.message);
          $("#successModal").modal("show");
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

  // Handle student deletion
  $(document).on('click', '.delete-btn', function () {
    const studentId = $(this).data('id');
    console.log(studentId)
  
    if (confirm('Are you sure you want to delete this student?')) {
      $.ajax({
        url: `http://localhost:8000/cgi-bin/student-crud/delete.py`,
        type: 'POST',
        data: { id: studentId },
        success: function (response) {
          if (response.status === 'success') {
            $(`#student${studentId}`).remove();
            alert('Student deleted successfully.');
          } else {
            alert('Error: ' + response.message);
          }
        },
        error: function () {
          alert('Failed to delete the student.');
        }
      });
    }
  });
  

});
