// Animated dark/light mode toggle & fade-ins
document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById('toggleTheme');
    toggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        toggle.textContent = document.body.classList.contains('dark-mode') ? '☀️' : '🌙';
    });

    // Animate on scroll for .fade-in elements
    const faders = document.querySelectorAll('.fade-in');
    const appearOptions = { threshold: 0, rootMargin: "0px 0px -50px 0px" };
    const appearOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add('appear');
            observer.unobserve(entry.target);
        });
    }, appearOptions);
    faders.forEach(fader => { appearOnScroll.observe(fader); });
});
