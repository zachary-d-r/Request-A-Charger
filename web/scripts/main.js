
document.getElementById('submit-button').addEventListener("click", ()=>{eel.getStudentEmail()}, false)

// Get the student ID from the textbox
eel.expose(getStudentEmailJS)
function getStudentEmailJS() {
    firstAnimation()  // Trigger animations
    var email = document.getElementById('email-input').value
    var nEmail = email
    document.getElementById('email-input').clear
    return nEmail
}


function firstAnimation() {
    document.getElementById('domain').className = 'domain-animate'
    document.getElementById('login-div').className = 'login-div-animate'
    document.getElementById('title').className = 'title-animate'
    document.getElementById('subtitle').className = 'subtitle-animate'
    document.getElementById('email').className = 'email-animate'
    document.getElementById('submit-button').className = 'signin-button-animate'
    document.getElementById('email-input').placeholder = 'Verification'
}