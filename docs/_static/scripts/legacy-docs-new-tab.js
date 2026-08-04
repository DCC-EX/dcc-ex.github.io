/*
  This list looks for all links to the legacy documentation and ensures they open in a new tab, and have an icon.
*/

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll('a[href^="https://dcc-ex.com/legacy-docs/"]').forEach(link => {
    link.setAttribute("target", "_blank");
    link.setAttribute("rel", "noopener");
    link.classList.add("external-link-icon");
  });
});
