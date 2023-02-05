let home = document.querySelector('#home')
let find_similarities = document.querySelector('#find_similarities')
let credits = document.querySelector('#credits')
let faq = document.querySelector('#faq')

function switchPage(id) {
  if (id === 'find_similarities') {
    window.open('./find_similarities.html', EventTarget='_self')
  } else if (id === 'credits') {
    window.open('./credits.html', EventTarget='_self')
  } else if (id === 'faq') {
    window.open('./faq.html', EventTarget='_self')
  } else if (id === 'home') {
    window.open('./index.html', EventTarget='_self')
  }
}