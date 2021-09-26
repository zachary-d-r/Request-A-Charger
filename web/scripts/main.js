
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
    secondAnimation()
    return document.getElementById('email-input').value
}

// Animation from verification to what locker number you take out
eel.expose(secondAnimation)
function secondAnimation() {
    document.getElementById('login-div').className = 'login-div-animate-2'
    document.getElementById('title').className = 'title-animate-2'
    document.getElementById('title').innerHTML = 'Your Charger is In'
    document.getElementById('subtitle').innerHTML = 'LOCKER NUMBER'
    document.getElementById('submit-button').className = 'signin-button-animate-2'
    document.getElementById('submit-button').innerHTML = 'Done'
    document.getElementById('email-input').placeholder = ''
    document.getElementById('email-input').style.visibility = 'hidden'
    document.getElementById('email').className = 'number-box-2'

}

// Animation from email screen to verification
function firstAnimation() {
    document.getElementById('domain').className = 'domain-animate'
    document.getElementById('login-div').className = 'login-div-animate'
    document.getElementById('title').className = 'title-animate'
    document.getElementById('subtitle').className = 'subtitle-animate'
    document.getElementById('email').className = 'email-animate'
    document.getElementById('submit-button').className = 'signin-button-animate'
    document.getElementById('email-input').placeholder = 'Check your email for code'
}