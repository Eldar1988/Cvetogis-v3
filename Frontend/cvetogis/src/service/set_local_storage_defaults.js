export default function setLocalStorageDefaults(city) {
  // cart
  if (localStorage.getItem('cart') === null) {
    let cart = []
    localStorage.setItem('cart', JSON.stringify(cart))
  }

  // wishList
  if (localStorage.getItem('wishList') === null) {
    let wishList = []
    localStorage.setItem('wishList', JSON.stringify(wishList))
  }

  // setDefaultCity
  if(!city) {
    if(localStorage.getItem('city') === null) {
      localStorage.setItem('city', 'karaganda')
    }
  } else {
    localStorage.setItem('city', city)
  }
}
