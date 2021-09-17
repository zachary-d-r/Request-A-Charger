
document.getElementById("emailButton").addEventListener("click", ()=>{eel.getStudentEmail()}, false)

// Get the student ID from the textbox
eel.expose(getStudentEmailJS)
function getStudentEmailJS() {
    return document.getElementById("studentEmailTextBox").value
}
