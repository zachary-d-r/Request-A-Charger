
document.getElementById("IDButton").addEventListener("click", ()=>{eel.getStudentID()}, false)

// Get the student ID from the textbox
eel.expose(getStudentIDJS)
function getStudentIDJS() {
    return document.getElementById("studentIDTextBox").value
}
