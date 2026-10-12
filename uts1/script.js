const contactForm = document.querySelector("#contact-form");
const formFeedback = document.querySelector("#form-feedback");

if (contactForm && formFeedback) {
	const departureDate = contactForm.elements.departure;
	const returnDate = contactForm.elements.return;

	function validateDates() {
		returnDate.min = departureDate.value;

		if (departureDate.value && returnDate.value < departureDate.value) {
			returnDate.setCustomValidity(
				"Return date must be on or after the departure date.",
			);
		} else {
			returnDate.setCustomValidity("");
		}
	}

	departureDate.addEventListener("change", validateDates);
	returnDate.addEventListener("change", validateDates);
	contactForm.addEventListener("input", () => {
		formFeedback.textContent = "";
	});

	contactForm.addEventListener("submit", (event) => {
		event.preventDefault();
		validateDates();

		if (!contactForm.reportValidity()) {
			return;
		}

		formFeedback.textContent =
			"Your enquiry is complete in this demo, but it has not been sent.";
	});
}
