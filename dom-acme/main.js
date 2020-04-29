// 1. When the page is loaded, append an <h1> element to the "user-greeting" div
// This heading should say "Welcome, <userName>"!

const userName = "Oakley"

// The following is code we wrote together in class! #teamwork
window.addEventListener('load', function () {
  // select the element that you'll append this element to
  let parentEl = document.querySelector('#user-greeting')
  console.log(parentEl)
  // create the empty h1 element
  let greetingEl = document.createElement("h1")
  console.log(greetingEl)
  //create text to put into h1
  let text = document.createTextNode("Hello " + userName)
  // let text = document.createTextNode(`Hello ${userName}`)
  console.log(text)
  // attach the text to the h1 element
  greetingEl.appendChild(text)
  // attach an element to user-greeting element to say welcome user name
  parentEl.appendChild(greetingEl)
})


// 2. Write some javascript to display the navigation menu options
// when the navigation elelent is clicked.
// To get started, look at the HTML first.
// You'll need an event listener!

// Select the element and store it in a variable. This is your event target element.


// Write an event listener that will be triggered when the click event happens.
// See MDN's documentation if you want to see an example: https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener


// Your event listener will need a callback function that manipulates the DOM to show the nav menu.
// There are several ways this can be accomplished, but check out the html and css
// Can you see how it is already set up?

