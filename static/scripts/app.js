let input = document.querySelector('#input_text')

let results = document.querySelector('#results')

function switchPage(id) {
  if (id === 'find_similarities') {
    window.open('./find_similarities.html', EventTarget='_self')
  } else if (id === 'credits') {
    window.open('./credits.html', EventTarget='_self')
  } else if (id === 'faq') {
    window.open('./faq.html', EventTarget='_self')
  } else if (id === 'home') {
    window.open('./', EventTarget='_self')
  }
}

// input.addEventListener("keypress", function(event) {
//   if (event.key === "Enter") {
//     findSimilarities(value=input.value)
//   }
// });

// function findSimilarities(value) {
//   first_word = 'a'
//   second_word = 'b'
//   third_word = 'c'

//   return results.innerHTML = `<div><img width=40 src='./assets/img/1st.png' /><p>&nbsp;&nbsp;${value}</p></div><div><img width=40 src='./assets/img/2nd.png' /><p>&nbsp;&nbsp;${second_word}</p></div><div><img width=40 src='./assets/img/3rd.png' /><p>&nbsp;&nbsp;${third_word}</p></div>`
// }