document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".cart-item").forEach((item) => {
        const daysInput = item.querySelector(".days-input");
        const phoneNumberInput = item.querySelector(".phone-number");
        const priceDisplay = item.querySelector(".total-price");
        const bookButton = item.querySelector(".book-button");

        // Update total price dynamically
        daysInput.addEventListener("input", () => {
            const pricePerDay = parseInt(item.dataset.price, 10);
            const days = parseInt(daysInput.value, 10) || 1;
            priceDisplay.textContent = `Total Price: ₹${pricePerDay * days}`;
        });

        // Booking logic
        bookButton.addEventListener("click", () => {
            const carName = item.querySelector("h3").textContent;
            const pricePerDay = parseInt(item.dataset.price, 10);
            const days = parseInt(daysInput.value, 10) || 1;
            const phoneNumber = phoneNumberInput.value.trim();

            if (!phoneNumber) {
                alert("Please enter your phone number.");
                return;
            }

            const bookingData = {
                car_name: carName,
                price: pricePerDay,
                days: days,
                phone_number: phoneNumber,
            };

            fetch("/history/book/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                body: JSON.stringify(bookingData),
            })
                .then((response) => response.json())
                .then((data) => {
                    alert(data.message || "Booking successful!");
                    item.querySelector(".status").textContent = "Status: Booked!";
                })
                .catch((error) => console.error("Error:", error));
        });
    });
});

// CSRF Token function
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
