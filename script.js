/* ===========================================
   ARCHITECTURE 2.0 WORKSHOP - SCRIPTS
   =========================================== */

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const navHeight = document.querySelector('.navbar').offsetHeight;
            const targetPosition = target.offsetTop - navHeight - 20;
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// Navbar background on scroll
const navbar = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.boxShadow = 'none';
    }
});

// Add animation on scroll (optional enhancement)
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe sections for fade-in animation
document.querySelectorAll('.section').forEach(section => {
    section.style.opacity = '0';
    section.style.transform = 'translateY(20px)';
    section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(section);
});

// Schedule expand/collapse controls
const schedule = document.querySelector('#schedule');
if (schedule) {
    const sessionDetails = Array.from(schedule.querySelectorAll('details.schedule-session'));
    const expandAllBtn = schedule.querySelector('#schedule-expand-all');
    const collapseAllBtn = schedule.querySelector('#schedule-collapse-all');

    // Ensure default expanded even if HTML is edited later
    sessionDetails.forEach(d => { d.open = true; });

    if (expandAllBtn) {
        expandAllBtn.addEventListener('click', () => {
            sessionDetails.forEach(d => { d.open = true; });
        });
    }

    if (collapseAllBtn) {
        collapseAllBtn.addEventListener('click', () => {
            sessionDetails.forEach(d => { d.open = false; });
        });
    }
}

