
document.getElementById('submit-button').addEventListener("click", ()=>{eel.getStudentEmail()}, false)

// Get the student ID from the textbox
eel.expose(getStudentEmailJS)
function getStudentEmailJS() {
    var email = document.getElementById('email-input').value
    firstAnimation()  // Trigger animations
    return email
}

eel.expose(clearTextBox)
function clearTextBox() {
    document.getElementById('email-input').value = ''
}

eel.expose(getVerificationCodeJS)
function getVerificationCodeJS() {
    return document.getElementById('email-input').value
}


function firstAnimation() {
    document.getElementById('domain').className = 'domain-animate'
    document.getElementById('login-div').className = 'login-div-animate'
    document.getElementById('title').className = 'title-animate'
    document.getElementById('subtitle').className = 'subtitle-animate'
    document.getElementById('email').className = 'email-animate'
    document.getElementById('submit-button').className = 'signin-button-animate'
    document.getElementById('email-input').placeholder = 'Check your email for code'
}