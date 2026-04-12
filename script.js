document.addEventListener("scroll", () => {
    const header = document.querySelector("header");
    const scrollTrigger = document.querySelector(".scroll-trigger");

    if (scrollTrigger.getBoundingClientRect().top < -100) {
        header.style.display = "block";
    } else {
        header.style.display = "none";
    }
});
document.addEventListener("DOMContentLoaded", () => {
    const scrollUpButton = document.getElementById("scroll-up");
    const scrollDownButton = document.getElementById("scroll-down");

    // Fel görgetés
    scrollUpButton.addEventListener("click", () => {
        window.scrollBy({
            top: -window.innerHeight, // Egy nézetablaknyi magassággal feljebb
            behavior: "smooth" // Simított görgetés
        });
    });

    // Le görgetés
    scrollDownButton.addEventListener("click", () => {
        window.scrollBy({
            top: window.innerHeight, // Egy nézetablaknyi magassággal lejjebb
            behavior: "smooth" // Simított görgetés
        });
    });
});