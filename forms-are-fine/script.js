let form = document.querySelector('#register-form')
let formIsValid

form.addEventListener('submit', function (event) {
  event.preventDefault()

  // Think of these two initial steps as clearing everything
  // to give us a "clean slate" to start from
  removeErrorMessage()
  formIsValid = true

  validateEmail()
  confirmPasswordMatch()
  // TODO: Add more validations here!
  showValidMessage()
})

function validateEmail () {
  let emailInput = document.querySelector('#email-input')
  let emailAddress = emailInput.value
  let parentEl = emailInput.parentElement

  if (emailAddress) {
    //do something if it is valid
    console.log('email address is valid')
    parentEl.classList.remove('input-invalid')
    parentEl.classList.add('input-valid')
  } else {
    // do something else if it is invalid
    console.log('email address is invalid')
    parentEl.classList.remove('input-valid')
    parentEl.classList.add('input-invalid')
    formIsValid = false
  }
}

function confirmPasswordMatch () {
  // grab the value of the password input
  let password = document.querySelector('#password-input').value
  // grab the value of the confirm password input
  let confirmPwd = document.querySelector('#confirm-password').value
  // compare to see if they match

  if (password !== confirmPwd) {
    // show an error message on the page
    let errorDiv = document.querySelector('#error-msg')
    errorDiv.innerHTML = 'Your passwords must match'
    formIsValid = false
  }
}

function removeErrorMessage () {
  let errorDiv = document.querySelector('#error-msg')
  errorDiv.innerHTML = ''
}

function showValidMessage () {
  if (formIsValid) {
    let validDiv = document.querySelector('#valid-message')
    let validMsgEl = document.createElement('h2')
    let validMsgText = document.createTextNode('This form is valid!')
    validMsgEl.appendChild(validMsgText)
    document.querySelector('main').appendChild(validMsgEl)
  }
}
