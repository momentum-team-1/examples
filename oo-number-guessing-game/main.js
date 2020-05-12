/* eslint-disable prefer-const, no-unused-vars */
/* globals document */

let playButton = document.querySelector('#play-btn')
playButton.addEventListener('click', function () {
  console.log('PLAY')
  new GuessTheNumberGame(Math.floor(Math.random() * 100 + 1)).play()
})

class GuessTheNumberGame {
  constructor (numberToGuess) {
    this.numberToGuess = numberToGuess
    this.tries = []
    this.feedback = ''
    this.youWon = false
  }

  play () {
    document.querySelector('#game').classList.remove('hidden')
    let guessButton = document.querySelector('#guess-btn')
    guessButton.addEventListener('click', () => this.getUserGuess())
  }

  getUserGuess (feedback) {
    let userGuess = document.querySelector('#user-guess').value
    this.guess(userGuess)
  }

  setFeedbackMessage (feedback) {
    let feedbackDiv = document.querySelector('#feedback')
    if (this.youWon) {
      feedbackDiv.classList.remove('alert-danger')
      feedbackDiv.classList.add('alert-success')
    }
    feedbackDiv.innerText = feedback
  }

  guess (guessedNumber) {
    if (!guessedNumber) { return }
    let inputField = document.querySelector('#user-guess')
    this.tries.push(guessedNumber)
    if (guessedNumber < this.numberToGuess) {
      console.log('Too low')
      this.setFeedbackMessage(`${guessedNumber} is too low. Guess again.`)
      inputField.value = ''
      inputField.focus()
    } else if (guessedNumber > this.numberToGuess) {
      console.log('Too high')
      this.setFeedbackMessage(`${guessedNumber} is too high. Guess again.`)
      inputField.value = ''
      inputField.focus()
      document.querySelector('#user-guess').focus()
    } else {
      this.youWon = true
      this.setFeedbackMessage(`${guessedNumber} is RIGHT! It took you ` + this.tries.length + ' tries!')
      this.reset()
    }
  }

  reset () {
    // TODO: implement reset
  }
}

