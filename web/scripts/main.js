
document.getElementById('submit-button').addEventListener("click", ()=>{eel.getStudentEmail()}, false)

// Get the student ID from the textbox
eel.expose(getStudentEmailJS)
function getStudentEmailJS() {
    return document.getElementById('email-input').value
}
