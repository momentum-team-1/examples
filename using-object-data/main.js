/* eslint-disable prefer-const */

/* DATA */
const menuItems = [
  {
    title: 'Noodles',
    imgUrl: 'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60'
  },
  {
    title: 'Burgers',
    imgUrl: 'https://images.unsplash.com/photo-1550950158-d0d960dff51b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1100&q=80'
  },
  {
    title: 'Breakfast',
    imgUrl: 'https://images.unsplash.com/photo-1459789034005-ba29c5783491?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1450&q=80'
  },
  {
    title: 'Dessert',
    imgUrl: 'https://images.unsplash.com/photo-1514849302-984523450cf4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1100&q=80'
  },
  {
    title: 'Abomination Margarita',
    imgUrl: 'https://images.unsplash.com/photo-1586968193505-208fd23ffd33?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1400&q=80'
  }
]

function renderPageContent () {
  let targetElement = document.querySelector(".menu-items")

  for (let item of menuItems) {
    let listItemElement = document.createElement("li")
    listItemElement.innerHTML = `<img src=${item.imgUrl}>`
    targetElement.appendChild(listItemElement)
  }
}



renderPageContent()
