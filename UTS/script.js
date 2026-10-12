const destinationCards = document.querySelectorAll(".destination-card");
const filterButtons = document.querySelectorAll(".filter-button");
const searchInput = document.querySelector("#destination-search");
const resultCount = document.querySelector("#result-count");
const emptyState = document.querySelector("#empty-state");
let activeFilter = "semua";

function showDestinations() {
    const searchText = searchInput.value.toLowerCase().trim();
    let visibleCount = 0;

    destinationCards.forEach(function (card) {
        const categories = card.dataset.category.split(" ");
        const matchesCategory =
            activeFilter === "semua" || categories.includes(activeFilter);
        const matchesSearch = card.dataset.search.includes(searchText);

        if (matchesCategory && matchesSearch) {
            card.hidden = false;
            visibleCount = visibleCount + 1;
        } else {
            card.hidden = true;
        }
    });

    resultCount.textContent =
        "Menampilkan " +
        visibleCount +
        " dari " +
        destinationCards.length +
        " destinasi";
    emptyState.hidden = visibleCount > 0;
}

if (searchInput) {
    filterButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            activeFilter = button.dataset.filter;

            filterButtons.forEach(function (otherButton) {
                const isSelected = otherButton === button;
                otherButton.classList.toggle("active", isSelected);
                otherButton.setAttribute("aria-pressed", isSelected);
            });

            showDestinations();
        });
    });

    searchInput.addEventListener("input", showDestinations);
}

const favoriteButtons = document.querySelectorAll(".favorite-button");

favoriteButtons.forEach(function (button) {
    button.addEventListener("click", function () {
        const isSaved = button.getAttribute("aria-pressed") === "true";
        button.setAttribute("aria-pressed", !isSaved);
        button.classList.toggle("saved", !isSaved);
        button.textContent = isSaved ? "♡" : "♥";
    });
});

const contactForm = document.querySelector("#contact-form");

if (contactForm) {
    contactForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const name = document.querySelector("#name").value.trim();
        const feedback = document.querySelector("#form-feedback");
        feedback.textContent =
            "Terima kasih, " +
            name +
            "! Pesanmu sudah tercatat di halaman ini.";
        contactForm.reset();
    });
}
