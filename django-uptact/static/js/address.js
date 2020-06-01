const addAddressLink = document.querySelector('#add-address-link')
addAddressLink.addEventListener('click', (event) => {
  event.preventDefault()
  const addressForm = document.querySelector('#address-form')
  addressForm.classList.remove('dn')
  addAddressLink.classList.add('dn')
})
