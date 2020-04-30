let form = document.querySelector('#register-form')

form.addEventListener('submit', function (event) {
  event.preventDefault()

  let emailInput = document.querySelector('#email-input')
  let emailAddress = emailInput.value
  let parentEl = emailInput.parentElement

  if (emailAddress) {
    //do something if it is valid
    console.log("email address is valid")
    parentEl.classList.remove("input-invalid")
    parentEl.classList.add("input-valid")
  } else {
    // do something else if it is invalid
    console.log("email address is invalid")
    parentEl.classList.remove("input-valid")
    parentEl.classList.add("input-invalid")
  }
})

