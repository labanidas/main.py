var sendButton = document.getElementById("sendButton");

sendButton.addEventListener("click", () => {
    que_input = document.getElementById("question");
    question = que_input.value;
    console.log(question)
    que_input.value = "";

    // alert("hi")
})