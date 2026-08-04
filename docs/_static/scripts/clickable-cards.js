/*
  This script ensures grid cards are clickable links, rather than having to provide a specific link.
*/
document.addEventListener('DOMContentLoaded', function() {
  // Make grid cards fully clickable
  const cards = document.querySelectorAll('.md-typeset .grid.cards.clickable > ul > li');
  
  cards.forEach(card => {
    const link = card.querySelector('a[href]');
    if (link) {
      card.style.cursor = 'pointer';
      card.addEventListener('click', function(e) {
        // Prevent if clicking on the actual link
        if (e.target.tagName === 'A') return;
        
        // Navigate to the link
        if (link.href.startsWith('#')) {
          window.location.hash = link.href;
        } else {
          window.location.href = link.href;
        }
      });
    }
  });
});
