/* eslint-disable prefer-const, no-unused-vars */
/* globals fetch */

// I am putting this in global scope so I can reference it in multiple functions
let dataSection = document.querySelector("#github-data")

fetch('https://api.github.com/orgs/momentum-team-1')
  // fetch will return a JS promise as a response
  // to access the data returned when the promise resolves, we use the .then method
  // to transform the data to json, we have to call the .json method
  .then(function (response) {
  // we chain another .then because this one above here returns a promise
  // we do this so we can access the data from the response
    console.log(response)
    return response.json()
  })
  .then(function (data) {
    // huzzah now we can do something with this real data
    console.log(data)
    // let's put an h2 on the page using the name from this first data set
    const h2El = document.createElement('h2')
    h2El.innerText = data.name
    dataSection.appendChild(h2El)
    // This next line may seem a little hard to follow. I want the url to get the repos for this org
    // So I'm using data from this JSON response in order to construct another fetch request
    // Here I am only returning the url I need for that request
    return data.repos_url
  })
  // The argument to the next .then method is the repos_url
  // I immediately use that to make the next fetch request
  // I can return the value of calling the fetch method (remember, arrow syntax has an implicit return)
  .then(reposUrl => fetch(reposUrl))
  // because that return value is a promise, I can chain another .then on top of that
  // now I'm doing the same thing as above, making sure I have json to work with
  .then(response => response.json())
  // then chaining another .then to get the json data so I can use it.
  .then(function (reposData) {
    // Give yourself a console.log to confirm you have what you need here
    console.log(reposData)
    // now that I have the data to use for values, I can construct my DOM elements
    // I could do this in a separate function, but it's fine to just do it here.
    const repoList = document.createElement('ul')
    // These classes are coming from Tachyons CSS
    repoList.classList.add(
      'list',
      'pl0',
      'ml0',
      'center',
      'mw6',
      'ba',
      'b--light-silver',
      'br3'
    )
    dataSection.appendChild(repoList)
    // Loop over the list of repos in that json data
    for (let repo of reposData) {
      console.log(repo.full_name)
      const listItem = document.createElement('li')
      listItem.textContent = repo.full_name
      listItem.classList.add('ph3', 'pv2', 'bb', 'b--light-silver')
      repoList.appendChild(listItem)
    }
  })
