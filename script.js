// Sticky header shadow on scroll
const header = document.getElementById('header');
window.addEventListener('scroll', () => {
    header.style.boxShadow = window.scrollY > 10
        ? '0 4px 20px rgba(0,0,0,0.12)' : '0 2px 8px rgba(0,0,0,0.06)';
});

// Mobile nav toggle
const hamburger = document.getElementById('hamburger');
const mobileNav = document.getElementById('mobileNav');
hamburger.addEventListener('click', () => {
    mobileNav.classList.toggle('open');
});
function closeMobileNav() {
    mobileNav.classList.remove('open');
}

// Smooth close mobile nav on link click
mobileNav.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', closeMobileNav);
});

// Form success feedback
const form = document.querySelector('.contact__form');
if (form) {
    form.addEventListener('submit', function (e) {
        const btn = form.querySelector('button[type="submit"]');
        btn.textContent = '✅ Request Sent! We\'ll be in touch shortly.';
        btn.disabled = true;
        btn.style.background = '#16a34a';
        btn.style.color = '#fff';
    });
}

// Animate cards on scroll
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.card, .testimonial-card, .stat-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    observer.observe(el);
});
