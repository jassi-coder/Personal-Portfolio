document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('contact-form').addEventListener('submit', function (e) {
  e.preventDefault();

  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const message = document.getElementById('message').value.trim();
  const response = document.getElementById('form-response');

  if (!name || !email || !message) {
    response.textContent = "Please fill all the fields.";
    response.style.color = "red";
    return;
  }

  response.textContent = "Message sent successfully!";
  response.style.color = "green";

  e.target.reset();
});

    const hamburger = document.getElementById("hamburger");
  const navMenu = document.getElementById("navLinks");

  hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
  });
  document.addEventListener("click", (e) => {
  if (!navMenu.contains(e.target) && !hamburger.contains(e.target)) {
    navMenu.classList.remove("active");
  }
});
  const backToTopBtn = document.getElementById("backToTopBtn");
  const header = document.querySelector(".header");
  let lastScrollY = window.scrollY;

  window.addEventListener("scroll", () => {
    // Show/hide Back to Top button
    if (window.scrollY > 200) {
      backToTopBtn.style.display = "block";
    } else {
      backToTopBtn.style.display = "none";
    }

    // Header hide/show on scroll
    if (window.scrollY > lastScrollY) {
      header.style.top = "-80px"; // hide header when scrolling down
    } else {
      header.style.top = "0"; // show header when scrolling up
    }

    lastScrollY = window.scrollY;
  });

  backToTopBtn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
    header.style.top = "0"; // ensure header visible when back at top
  });
});
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("contact-form");
    if (!form) return;

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const formData = new FormData(form);

        const response = await fetch("", {
            method: "POST",
            headers: {
                "X-CSRFToken": csrfToken,
                "X-Requested-With": "XMLHttpRequest",
            },
            body: formData,
        });

        const result = await response.json();

        let messageDiv = document.getElementById("form-response");
        if (!messageDiv) {
            messageDiv = document.createElement("div");
            messageDiv.id = "form-response";
            form.prepend(messageDiv);
        }
        messageDiv.innerText = result.message;
        messageDiv.style.color = result.status === "success" ? "green" : "red";

        if (result.status === "success") form.reset();
    });
});
