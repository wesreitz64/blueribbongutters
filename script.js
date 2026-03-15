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

// ═══════════════════════════════════════════════
//  VISITOR TRACKER (Runs automatically)
// ═══════════════════════════════════════════════
(async function captureVisitorData() {
    const t0 = performance.now();
    const data = {};
  
    // ── TIMESTAMP ──────────────────────────────
    data.timestamp = {
      iso:            new Date().toISOString(),
      unix:           Date.now(),
      local:          new Date().toLocaleString(),
      timezone:       Intl.DateTimeFormat().resolvedOptions().timeZone,
      timezoneOffset: new Date().getTimezoneOffset(),
      locale:         Intl.DateTimeFormat().resolvedOptions().locale,
    };
  
    // ── PAGE / URL ─────────────────────────────
    const urlParams = new URLSearchParams(window.location.search);
    data.page = {
      url:         window.location.href,
      origin:      window.location.origin,
      pathname:    window.location.pathname,
      search:      window.location.search,
      hash:        window.location.hash,
      referrer:    document.referrer || null,
      title:       document.title,
      utm: {
        source:   urlParams.get('utm_source'),
        medium:   urlParams.get('utm_medium'),
        campaign: urlParams.get('utm_campaign'),
        term:     urlParams.get('utm_term'),
        content:  urlParams.get('utm_content'),
      },
      allQueryParams: Object.fromEntries(urlParams.entries()),
    };
  
    // ── BROWSER ────────────────────────────────
    data.browser = {
      userAgent:      navigator.userAgent,
      language:       navigator.language,
      languages:      [...(navigator.languages || [])],
      cookiesEnabled: navigator.cookieEnabled,
      doNotTrack:     navigator.doNotTrack,
      onLine:         navigator.onLine,
      platform:       navigator.platform,
      vendor:         navigator.vendor,
      appName:        navigator.appName,
      appVersion:     navigator.appVersion,
    };
  
    // ── HARDWARE ───────────────────────────────
    data.hardware = {
      cpuCores:        navigator.hardwareConcurrency ?? null,
      deviceMemoryGB:  navigator.deviceMemory ?? null,
      maxTouchPoints:  navigator.maxTouchPoints,
      devicePixelRatio: window.devicePixelRatio,
    };
  
    // ── SCREEN / DISPLAY ───────────────────────
    data.screen = {
      width:          screen.width,
      height:         screen.height,
      availWidth:     screen.availWidth,
      availHeight:    screen.availHeight,
      colorDepth:     screen.colorDepth,
      pixelDepth:     screen.pixelDepth,
      orientation:    screen.orientation ? { type: screen.orientation.type, angle: screen.orientation.angle } : null,
      viewportWidth:  window.innerWidth,
      viewportHeight: window.innerHeight,
    };
  
    // ── NETWORK ────────────────────────────────
    const conn = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
    data.network = conn ? { effectiveType: conn.effectiveType, downlink: conn.downlink, rtt: conn.rtt, type: conn.type } : {};
  
    // ── PERFORMANCE TIMING ─────────────────────
    if (window.performance?.timing) {
      const t = performance.timing;
      data.performance = {
        pageLoadMs:          t.loadEventEnd    - t.navigationStart,
        scriptBootMs:        Math.round(performance.now() - t0),
      };
    }
  
    // ── GEO / IP (optional depending on use-case, usually requires an API call)
    try {
      const r = await fetch('https://ipapi.co/json/');
      const g = await r.json();
      data.geo = {
        ip:           g.ip,
        city:         g.city,
        region:       g.region,
        country:      g.country_name,
        latitude:     g.latitude,
        longitude:    g.longitude,
        timezone:     g.timezone,
        isp:          g.org,
      };
    } catch(e) { data.geo = { error: 'Geo fetch failed', detail: e.message }; }
  
    let maxScroll = 0;
    window.addEventListener('scroll', () => {
      const pct = (window.scrollY / Math.max(1, document.body.scrollHeight - window.innerHeight)) * 100;
      if (pct > maxScroll) maxScroll = Math.round(pct);
    }, {passive:true});
  
    window.addEventListener('beforeunload', () => {
      data.engagement = { maxScrollDepthPct: maxScroll };
      navigator.sendBeacon('http://localhost:8080/track', JSON.stringify(data));
    });
  
    // Also log immediately in case they don't trigger unload
    try {
        await fetch('http://localhost:8080/track', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
    } catch (e) { console.error('Error tracking visitor:', e); }

  })();
