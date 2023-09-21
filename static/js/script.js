

// var sendButton = document.getElementById("sendButton");

// sendButton.addEventListener("click", () => {
//     que_input = document.getElementById("questionInput");
//     que = que_input.value;
//     que_input.value = "";
//     document.querySelector(".right1").style.display = 'none';
//     document.querySelector(".right2").style.display = 'block';

//     document.querySelector("#question").innerHTML = que;
// })

// document.getElementById("askQuestion").addEventListener('click', () => {
//     alert("hi")
// })

function render_user_message(userPrompt) {
    let user_msg_box = `
    <div class="box user box1 flex justify-start w-[70%] space-x-4 p-7 m-auto">
    <img
      class="w-9 h-9"
      src="https://chat.openai.com/_next/image?url=https%3A%2F%2Flh3.googleusercontent.com%2Fa%2FAAcHTtf-3pmhALVSb-1WbSusjdPg_2UhrsZ-k88Nr8nRNUWOvZ0%3Ds96-c&w=48&q=75"
      alt="user"
    />
    <div id="question">
      ${userPrompt}
    </div>
  </div>
    `

    // Append the user message box to the div with id "right2"
    document.querySelector(".allchats").innerHTML += user_msg_box;
}

function render_system_message(sysdata) {
    let sys_msg_box = `
    <div class="bg-gray-600 w-full bg chatgpt">
          <div class="box box2 flex justify-start w-[70%] space-x-4 p-7 m-auto">
            <img
              class="w-9 h-9"
              src="https://chat.openai.com/favicon.ico"
              alt="ChatGPT"
            />
            <div class="flex flex-col">
              <div>
                ${sysdata}
              </div>
            </div>
          </div>
        </div>
    `
    // Append the user message box to the div with id "right2"
    document.querySelector(".allchats").innerHTML += sys_msg_box;
}


// function to add scroll animation
function scrollToBottom() {
    var $allChats = $(".allchats");
    $allChats.animate({ scrollTop: $allChats.prop("scrollHeight") }, 500);
  }

$("#askQuestion").click(function () {
    // Get the user's input
    var userPrompt = $("#questionInput2").val();
    // render user message
    render_user_message(userPrompt);
    scrollToBottom();
    $("#questionInput2").val('');

    // Send an asynchronous request to your Flask server
    $.ajax({
        type: "POST", // Use POST or GET based on your server route
        url: "/api",
        data: { prompt: userPrompt },
        success: function (response) {
            // Update the UI with the response
            render_system_message(response.data);
            scrollToBottom();
            // $("#right2").text(response.data);
        },
        error: function (error) {
            console.log(error);
        }
    });
});