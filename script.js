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

// ---- Reviews Carousel ----
const carousel = document.getElementById('reviewsCarousel');
const prevBtn = document.getElementById('reviewPrev');
const nextBtn = document.getElementById('reviewNext');
const dotsWrap = document.getElementById('reviewDots');

if (carousel && prevBtn && nextBtn && dotsWrap) {
    const slides = Array.from(carousel.querySelectorAll('.carousel-slide'));

    function perView() { return window.innerWidth >= 900 ? 3 : 1; }
    function slideWidth() {
        return slides[0].offsetWidth + parseInt(getComputedStyle(carousel).gap || 16);
    }
    function totalPages() { return Math.ceil(slides.length / perView()); }
    function currentPage() {
        return Math.round(carousel.scrollLeft / (perView() * slideWidth()));
    }

    // Build dots
    function buildDots() {
        dotsWrap.innerHTML = '';
        for (let i = 0; i < totalPages(); i++) {
            const d = document.createElement('button');
            d.className = 'carousel-dot' + (i === 0 ? ' active' : '');
            d.setAttribute('aria-label', 'Go to slide ' + (i + 1));
            d.addEventListener('click', () => {
                carousel.scrollTo({ left: i * perView() * slideWidth(), behavior: 'smooth' });
            });
            dotsWrap.appendChild(d);
        }
    }

    function updateDots() {
        const dots = dotsWrap.querySelectorAll('.carousel-dot');
        dots.forEach((d, i) => d.classList.toggle('active', i === currentPage()));
    }

    buildDots();
    carousel.addEventListener('scroll', updateDots, { passive: true });
    window.addEventListener('resize', buildDots);

    prevBtn.addEventListener('click', () => {
        carousel.scrollBy({ left: -(perView() * slideWidth()), behavior: 'smooth' });
    });
    nextBtn.addEventListener('click', () => {
        carousel.scrollBy({ left: perView() * slideWidth(), behavior: 'smooth' });
    });
}

// ---- Color Carousel ----
const colorCarousel = document.getElementById('colorsCarousel');
const colorPrev = document.getElementById('colorPrev');
const colorNext = document.getElementById('colorNext');
const colorDotsWrap = document.getElementById('colorDots');

if (colorCarousel && colorPrev && colorNext && colorDotsWrap) {
    const colorSlides = Array.from(colorCarousel.querySelectorAll('.color-slide'));

    function colorSlideWidth() {
        return colorSlides[0].offsetWidth + parseInt(getComputedStyle(colorCarousel).gap || 16);
    }
    function colorCurrentPage() {
        return Math.round(colorCarousel.scrollLeft / colorSlideWidth());
    }

    function buildColorDots() {
        colorDotsWrap.innerHTML = '';
        for (let i = 0; i < colorSlides.length; i++) {
            const d = document.createElement('button');
            d.className = 'carousel-dot' + (i === 0 ? ' active' : '');
            d.setAttribute('aria-label', 'Go to color group ' + (i + 1));
            d.addEventListener('click', () => {
                colorCarousel.scrollTo({ left: i * colorSlideWidth(), behavior: 'smooth' });
            });
            colorDotsWrap.appendChild(d);
        }
    }

    function updateColorDots() {
        const dots = colorDotsWrap.querySelectorAll('.carousel-dot');
        dots.forEach((d, i) => d.classList.toggle('active', i === colorCurrentPage()));
    }

    buildColorDots();
    colorCarousel.addEventListener('scroll', updateColorDots, { passive: true });
    window.addEventListener('resize', buildColorDots);

    colorPrev.addEventListener('click', () => {
        colorCarousel.scrollBy({ left: -colorSlideWidth(), behavior: 'smooth' });
    });
    colorNext.addEventListener('click', () => {
        colorCarousel.scrollBy({ left: colorSlideWidth(), behavior: 'smooth' });
    });
}
