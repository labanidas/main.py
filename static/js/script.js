var sendButton = document.getElementById("sendButton");

sendButton.addEventListener("click", () => {
    que_input = document.getElementById("questionInput");
    que = que_input.value;
    que_input.value = "";
    document.querySelector(".right1").style.display = 'none';
    document.querySelector(".right2").style.display = 'block';

    document.querySelector("#question").innerHTML = que;

})