/* eslint-disable no-unused-vars, prefer-const */
/* globals fetch, moment */

let todoForm = document.querySelector('#todo-form')
let todoList = document.querySelector('.todos')

// 1. Add event listener for form submission
todoForm.addEventListener('submit', function (event) {
  event.preventDefault()
  let todoTextInput = document.querySelector('#todo-text')
  let todoText = todoTextInput.value
  // create the new todo item on the list (by sending a POST request so that it is added to the database)
  todoTextInput.value = ''
  createNewTodo(todoText)
})

// 2. write the fetch request to post data, in its own function
function createNewTodo (todoText) {
  fetch('http://localhost:3000/todos', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ item: todoText, done: false, created: moment().format() })
  })
    .then(() => renderTodos())
  // Instead of making another request to GET the data in renderTodos(),
  //   you could just use the response data to append the new item to the list.
  // A successful POST response from this server contains the newly created data,
  //   so you could use that to insert each created item individually.
}

// 3. render the todoList using the data that is now on the server
function renderTodos () {
  todoList.innerHTML = ''
  fetch('http://localhost:3000/todos', {
    method: 'GET'
  })
    .then(response => response.json())
    .then(function (data) {
      // add the content to the DOM
      // create the ul
      // create an li for each item
      let list = document.createElement('ul')
      list.id = 'item-list'
      for (let item of data) {
        let listItem = document.createElement('li')
        listItem.dataset.id = item.id
        listItem.innerText = item.item
        // this is just one idea; you don't need to use an icon. You could just use a button or a link!
        let deleteIcon = document.createElement('span')
        deleteIcon.id = 'delete'
        deleteIcon.classList.add('fa', 'fa-trash', 'mar-l-xs')
        listItem.appendChild(deleteIcon)
        list.appendChild(listItem)
      }
      todoList.appendChild(list)
    })
}

// 4. Delete todo items
todoList.addEventListener('click', function (event) {
  let targetEl = event.target
  if (targetEl.matches('#delete')) {
    console.log('DELETE')
    deleteTodoItem(targetEl.parentElement.dataset.id)
  }
})

function deleteTodoItem (itemId) {
  let itemToDelete = document.querySelector(`li[data-id='${itemId}']`)
  fetch(`http://localhost:3000/todos/${itemId}`, {
    method: 'DELETE'
  })
    .then(function () {
      // Remove the item from the list
      document.querySelector('#item-list').removeChild(itemToDelete)
    })
}

renderTodos()
