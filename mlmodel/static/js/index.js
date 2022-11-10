const text = document.querySelector('h2')
window.addEventListener('scroll' , () => {
const current = window.scrollY;
if (window.screen.width > 520){
    text.style.fontSize = `clamp(4rem, ${current}px , 5rem)`
}
})
const p = document.querySelector('p')
window.addEventListener('scroll', () => {
    const current = window.scrollY
    p.style.color =  `rgb(255,255,255,clamp(0.2, ${current}, 0.7))`
})

