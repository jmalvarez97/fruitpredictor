
const p = document.querySelector('p')
window.addEventListener('scroll', () => {
    const current = window.scrollY
    console.log(current)
    p.style.color =  `rgb(255,255,255,clamp(0.2, ${current}, 0.7))`

})
