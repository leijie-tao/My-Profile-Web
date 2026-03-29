// Portfolio — Full-page Slide Navigation

const API_BASE_URL = 'http://localhost:8000/api';

document.addEventListener('DOMContentLoaded', function() {
    initFullPage();
    initBackgroundOrbs();
    setupJourneyTabs();
    setupFormListener();
});

// ===== Full-page Slide Controller =====
function initFullPage() {
    const sections = document.querySelectorAll('.fp-section');
    const dots = document.querySelectorAll('.fp-dot');
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    const navbar = document.getElementById('mainNav');
    let currentSection = 0;
    let isAnimating = false;

    // --- Go to a specific section ---
    function goToSection(index) {
        if (index < 0 || index >= sections.length || index === currentSection || isAnimating) return;
        isAnimating = true;

        const goingDown = index > currentSection;

        // Prepare incoming section position
        sections[index].style.transition = 'none';
        sections[index].classList.remove('exit-up', 'exit-down', 'active');
        sections[index].style.transform = goingDown ? 'translateY(100%)' : 'translateY(-100%)';
        sections[index].style.opacity = '0';

        // Force reflow
        void sections[index].offsetHeight;

        // Re-enable transition
        sections[index].style.transition = '';

        // Exit current
        sections[currentSection].classList.remove('active');
        sections[currentSection].classList.add(goingDown ? 'exit-up' : 'exit-down');

        // Enter new
        sections[index].style.transform = '';
        sections[index].style.opacity = '';
        sections[index].classList.add('active');

        const prevIndex = currentSection;

        setTimeout(() => {
            sections[prevIndex].classList.remove('exit-up', 'exit-down');
            currentSection = index;
            isAnimating = false;
            updateUI();
            triggerAnimations(index);
        }, 700);
    }

    // --- Update dots, nav, navbar ---
    function updateUI() {
        dots.forEach(d => d.classList.toggle('active', parseInt(d.dataset.index) === currentSection));
        navLinks.forEach(l => l.classList.toggle('active', parseInt(l.dataset.index) === currentSection));
        navbar.classList.toggle('scrolled', currentSection > 0);
    }

    // --- Trigger entrance animations ---
    function triggerAnimations(index) {
        const items = sections[index].querySelectorAll('.anim-item:not(.animated)');
        items.forEach((item, i) => {
            setTimeout(() => item.classList.add('animated'), i * 120);
        });
    }

    // --- Click handlers ---
    // Dots
    dots.forEach(dot => {
        dot.addEventListener('click', () => goToSection(parseInt(dot.dataset.index)));
    });

    // Nav links
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            goToSection(parseInt(link.dataset.index));
        });
    });

    // Scroll indicators + back-to-top + any data-goto
    document.querySelectorAll('[data-goto]').forEach(el => {
        el.addEventListener('click', (e) => {
            e.preventDefault();
            goToSection(parseInt(el.dataset.goto));
        });
    });

    // --- Mouse wheel: internal scroll only, no page navigation ---
    // (no handler needed — natural scroll behavior within sections)

    // --- Keyboard navigation ---
    document.addEventListener('keydown', function(e) {
        if (['ArrowDown', 'PageDown'].includes(e.key)) {
            e.preventDefault();
            goToSection(currentSection + 1);
        }
        if (['ArrowUp', 'PageUp'].includes(e.key)) {
            e.preventDefault();
            goToSection(currentSection - 1);
        }
    });

    // --- Initial state ---
    updateUI();
    triggerAnimations(0);
}

// ===== Background Orbs =====
function initBackgroundOrbs() {
    const container = document.getElementById('bgOrbs');
    if (!container) return;

    const orbs = [
        { width: 700, height: 700, top: '-15%', left: '-10%', right: 'auto', animation: 'orbFloat1 30s ease-in-out infinite' },
        { width: 450, height: 450, top: '40%', left: '30%', right: 'auto', animation: 'orbFloat2 35s ease-in-out infinite' },
        { width: 280, height: 280, top: '25%', right: '5%', left: 'auto', animation: 'orbFloat1 25s ease-in-out infinite reverse' },
        { width: 650, height: 650, bottom: '-10%', right: '-10%', top: 'auto', left: 'auto', animation: 'orbFloat2 32s ease-in-out infinite' },
    ];

    const colors = [
        'radial-gradient(circle, rgba(140, 80, 220, 0.3) 0%, transparent 70%)',
        'radial-gradient(circle, rgba(0, 200, 170, 0.25) 0%, transparent 70%)',
        'radial-gradient(circle, rgba(0, 200, 170, 0.2) 0%, transparent 70%)',
        'radial-gradient(circle, rgba(70, 120, 235, 0.3) 0%, transparent 70%)',
    ];

    orbs.forEach((orb, i) => {
        const el = document.createElement('div');
        el.className = 'bg-orb';
        el.style.width = orb.width + 'px';
        el.style.height = orb.height + 'px';
        el.style.background = colors[i];
        el.style.animation = orb.animation;
        if (orb.top !== 'auto') el.style.top = orb.top;
        if (orb.bottom) el.style.bottom = orb.bottom;
        if (orb.left !== 'auto') el.style.left = orb.left;
        if (orb.right !== 'auto') el.style.right = orb.right;
        container.appendChild(el);
    });
}

// ===== Journey Tab Switching =====
function setupJourneyTabs() {
    const expPanel = document.getElementById('jnExperience');
    const eduPanel = document.getElementById('jnEducation');
    if (!expPanel || !eduPanel) return;
    document.querySelectorAll('.jn-tab').forEach(tab => {
        tab.addEventListener('click', function() {
            document.querySelectorAll('.jn-tab').forEach(t => t.classList.remove('active'));
            this.classList.add('active');
            expPanel.style.display = this.dataset.target === 'experience' ? '' : 'none';
            eduPanel.style.display = this.dataset.target === 'education' ? '' : 'none';
            // Reset scroll position on tab switch
            const wrapper = document.querySelector('#sec-timeline .fp-scroll-wrap');
            if (wrapper) wrapper.scrollTop = 0;
        });
    });
}

// ===== Contact Form =====
function setupFormListener() {
    const form = document.getElementById('contactForm');
    const msg = document.getElementById('formMessage');
    if (!form) return;

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        const data = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            subject: document.getElementById('subject').value,
            message: document.getElementById('message').value
        };
        try {
            const res = await fetch(`${API_BASE_URL}/contacts/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            if (res.ok) {
                msg.className = 'form-message success';
                msg.textContent = 'Message sent successfully!';
                form.reset();
                setTimeout(() => { msg.textContent = ''; }, 5000);
            } else throw new Error();
        } catch {
            msg.className = 'form-message error';
            msg.textContent = 'Error sending message. Please try again.';
        }
    });
}
