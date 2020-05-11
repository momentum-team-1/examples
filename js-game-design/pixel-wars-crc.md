# CRC Model for Pixel Wars

**Note: this is a DRAFT version of this model. It needs more work and possibly changes to what is written here. This is meant as an example of a structure for creating your own CRC model.**

[Class Responsibility Collaborator Model](http://agilemodeling.com/artifacts/crcModel.htm)

- Play the game over and over till you know what it does.
- Describe the game in a sentence or two.
  - Look for the nouns in your sentences: these are possible classes in your game design.
  - The verbs in your sentences are the methods that those classes might have.
- You might find that you need more or fewer classes as you do this exercise -- it is a tool to help you think as well as to design.

## Game class

### Responsibilities (what does it need to do or know)

- know the boundary of the screen
- collision detection -> player hits target or bomb hits player
- Track score
- Ending the game / knowing when it is over
- Start the game

### Collaborators (for more information or to do something)

- Player
- Target
- Bomb


## Player class

### Responsibilites (what does it need to do or know)

- move back and forth (based on a cue)
- has to shoot (bullets)

### Collaborators (for more information or to do something)

- something to handle click or keypress (Keyboarder)
- Bullet


## Target class

### Responsibilities (what does it need to do or know)

- fall down from the top

## Bomb class

## Bullet class
