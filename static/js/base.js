const text = document.querySelector('h1')
console.log(text)
window.addEventListener('scroll' , () => {
const current = window.scrollY
text.style.fontSize = `clamp(6rem, ${current}px , 8rem)`
console.log(current)
})