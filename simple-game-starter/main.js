/* eslint-disable prefer-const, no-unused-vars */
/* globals requestAnimationFrame, Keyboarder */

class Game {
  constructor () {
    let canvas = document.querySelector('#game-board')
    let context = canvas.getContext('2d')
    let gameSize = { x: canvas.width, y: canvas.height }
    this.player = new Player(gameSize)
    let animate = () => {
      this.update()
      this.drawPlayer(context, gameSize)
      requestAnimationFrame(animate)
    }
    animate()
  }

  drawPlayer (context, gameSize) {
    context.clearRect(0, 0, gameSize.x, gameSize.y)
    console.log('Draw player method called')
    context.fillStyle = '#07BEB8'
    let startingXPosition = this.player.center.x - this.player.size.x / 2
    let startingYPosition = this.player.center.y - this.player.size.y / 2
    let playerWidth = this.player.size.x
    let playerHeight = this.player.size.y
    context.fillRect(startingXPosition, startingYPosition, playerWidth, playerHeight)
  }

  update () {
    // eventually this method will have to update all the objects
    this.player.update()
  }
}

class Player {
  constructor (gameSize) {
    this.size = { x: 30, y: 30 }
    this.center = { x: gameSize.x / 2, y: gameSize.y - this.size.y * 2 }
    this.keyboarder = Keyboarder
  }

  update () {
    if (this.keyboarder.isDown(this.keyboarder.KEYS.RIGHT)) {
      this.center.x += 2
    } else if (this.keyboarder.isDown(this.keyboarder.KEYS.LEFT)) {
      this.center.x -= 2
    }
  }
}

new Game()
