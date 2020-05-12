/* eslint-disable prefer-const, no-unused-vars */
/* globals requestAnimationFrame */

class Game {
  constructor () {
    let canvas = document.querySelector("#game-board")
    let context = canvas.getContext('2d')
    let gameSize = { x: canvas.width, y: canvas.height }
    this.player = new Player(gameSize)
    let animate = () => {
      this.drawPlayer(context)
      requestAnimationFrame(animate)
    }
    animate()
  }

  drawPlayer (context) {
    console.log('Draw player method called')
    context.fillStyle = '#07BEB8'
    let startingXPosition = this.player.center.x - this.player.size.x / 2
    let startingYPosition = this.player.center.y - this.player.size.y / 2
    let playerWidth = this.player.size.x
    let playerHeight = this.player.size.y
    context.fillRect(startingXPosition, startingYPosition, playerWidth, playerHeight)
  }
}

class Player {
  constructor (gameSize) {
    this.size = { x: 30, y: 30 }
    this.center = { x: gameSize.x / 2, y: gameSize.y - this.size.y * 2 }
  }
}
