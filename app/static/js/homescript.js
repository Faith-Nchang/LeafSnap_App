document.addEventListener("DOMContentLoaded", function() {
    const cards = document.querySelectorAll('.card');
    function showCardsOnScroll() {
        cards.forEach(card => {
            const rect = card.getBoundingClientRect();
            if (rect.top < window.innerHeight - 30) {
                card.classList.add('visible');
            }
        });
    }
    window.addEventListener('scroll', showCardsOnScroll);
    showCardsOnScroll(); // Initial check
});
