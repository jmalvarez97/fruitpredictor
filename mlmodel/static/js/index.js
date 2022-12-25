const p = document.querySelector('p')
window.addEventListener('scroll', () => {
    const current = window.scrollY
    p.style.color =  `rgb(255,255,255,clamp(0.7, ${current}, 0.9))`
})

