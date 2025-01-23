document.addEventListener('DOMContentLoaded', function() {
    // Handle booking form submission
    const bookingForm = document.getElementById('booking-form');
    
    bookingForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(bookingForm);
        const data = Object.fromEntries(formData);
        
        try {
            const response = await fetch('/api/book', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
            
            if (response.ok) {
                alert('Booking submitted successfully! We will contact you soon.');
                bookingForm.reset();
            } else {
                alert('There was an error submitting your booking. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('There was an error submitting your booking. Please try again.');
        }
    });

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            target.scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Mobile menu toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }
}); 