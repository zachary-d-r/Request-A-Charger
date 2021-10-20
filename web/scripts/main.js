
document.getElementById('submit-button').addEventListener("click", ()=>{eel.getStudentEmail()}, false)
document.getElementById('button-1').addEventListener("click", ()=>{chargerSelected(1)}, false)
document.getElementById('button-2').addEventListener("click", ()=>{chargerSelected(2)}, false)
document.getElementById('button-3').addEventListener("click", ()=>{chargerSelected(3)}, false)
document.getElementById('button-4').addEventListener("click", ()=>{chargerSelected(4)}, false)

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

// Animation from verification to what charger select screen
eel.expose(secondAnimation)
function secondAnimation() {
    document.getElementById('login-div').className = 'login-div-animate-2'
    document.getElementById('submit-button').className = 'signin-button-animate-2'
    document.getElementById('email-input').placeholder = ''
    document.getElementById('email-input').style.visibility = 'hidden'
    document.getElementById('email').className = 'number-box-2'
    document.getElementById('title').innerHTML = 'Select a Charger'
    document.getElementById('subtitle').innerHTML = 'TO USE FOR YOUR COMPUTER'
    document.getElementById('buttons').className = 'show-button'
}

// Animation from verification to what locker number you take out
eel.expose(thirdAnimation)
function thirdAnimation() {
    document.getElementById('login-div').className = 'login-div-animate-3'
    document.getElementById('buttons').className = 'show-button-animate-3'
    document.getElementById('title').className = 'title-animate-3'
    document.getElementById('title').innerHTML = 'Your Charger is In'
    document.getElementById('subtitle').innerHTML = 'LOCKER NUMBER'
    document.getElementById('submit-button').className = 'signin-button-animate-3'
    document.getElementById('submit-button').innerHTML = 'Done'
    document.getElementById('email').className = 'number-box-3'
    eel.stall()

}

eel.expose(numberAnimate)
function numberAnimate(num) {
    document.getElementById('locker-number').className = 'locker-number-show'
    document.getElementById('locker-number').innerHTML = num
}

// Animation from email screen to verification
function firstAnimation() {
    document.getElementById('domain').className = 'domain-animate'
    document.getElementById('login-div').className = 'login-div-animate'
    document.getElementById('title').className = 'title-animate'
    document.getElementById('subtitle').className = 'subtitle-animate'
    document.getElementById('email').className = 'email-animate'
    document.getElementById('submit-button').className = 'signin-button-animate'
    document.getElementById('subtitle').innerHTML = 'FOR VERIFICATION CODE'
    document.getElementById('title').innerHTML = 'Check Your Email'
    document.getElementById('email-input').style.textTransform = 'uppercase'
    document.getElementById('email-input').placeholder = 'Verification Code'
}

function chargerSelected(num) {
    thirdAnimation()
    eel.setChargerType(num)
}

eel.expose(newVerificationCode) 
function newVerificationCode() {
    document.getElementById('title').innerHTML = 'Verification Failed'
    document.getElementById('subtitle').innerHTML = 'Resending Code'
    document.getElementById('email-input').placeholder = 'Check email for new code'

    document.getElementById('title').className = 'validation-title'
    document.getElementById('subtitle').className = 'validation-subtitle'
    document.getElementById('login-div').className = 'validation-login-div'
    document.getElementById('submit-button').className = 'validation-signin-button'
    document.getElementById('email').className = 'validation-email'
    document.getElementById('domain').className = 'validation-domain'

    document.getElementById('email-input').style.textTransform = 'none'
}

eel.expose(lastAnimation)
function lastAnimation() {
    document.getElementById('title').className = 'title'
    document.getElementById('subtitle').className = 'subtitle'
    document.getElementById('submit-button').className = 'signin-button'
    document.getElementById('login-div').className = 'login-div'
    document.getElementById('email').className = 'email'
    document.getElementById('domain').className = 'domain'
    document.getElementById('email-input').style.visibility = 'visible'
    document.getElementById('email-input').placeholder = 'email'
    document.getElementById('locker-number').className = 'locker-number-hidden'
    document.getElementById('subtitle').innerHTML = 'PRE-PRE-ALPHA'
    document.getElementById('title').innerHTML = 'Request a Charger'
    document.getElementById('submit-button').innerHTML = 'Submit'

    document.getElementById('email-input').style.textTransform = 'none'
}

eel.expose(backAnimation)
function backAnimation() {
    document.getElementById('login-div').className = 'login-div-animate-back'
    document.getElementById('buttons').className = 'show-button-animate-back'
    document.getElementById('title').innerHTML = 'Please Put Your Charger In'
    document.getElementById('subtitle').innerHTML = 'LOCKER NUMBER'
    document.getElementById('submit-button').className = 'signin-button-animate-back'
    document.getElementById('submit-button').innerHTML = 'Done'
    document.getElementById('email').className = 'number-box-back'
    document.getElementById('email-input').style.visibility = 'hidden'
    eel.stall()
}