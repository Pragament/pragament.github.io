document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('internshipForm');
    const formMessage = document.getElementById('formMessage');
    

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Basic form validation
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const motivation = document.getElementById('motivation').value.trim();
        
        if (!name || !email || !phone || !motivation) {
            showMessage('Please fill in all required fields.', 'error');
            return;
        }
        
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            showMessage('Please enter a valid email address.', 'error');
            return;
        }
        
        const phoneRegex = /^\d{10,15}$/;
        if (!phoneRegex.test(phone.replace(/[^0-9]/g, ''))) {
            showMessage('Please enter a valid phone number.', 'error');
            return;
        }
        
        simulateFormSubmission();
    });
    
    
    function showMessage(message, type) {
        formMessage.textContent = message;
        formMessage.className = 'form-message ' + type;
        
        // Scroll to the message
        formMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
    
    function simulateFormSubmission() {
        // Show loading state
        const submitBtn = form.querySelector('.submit-btn');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Submitting...';
        submitBtn.disabled = true;
        
       
        setTimeout(function() {
            
            showMessage('Your application has been submitted successfully! We will contact you soon.', 'success');
            
            // Reset form
            form.reset();
            
            // Reset button
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }, 1500);
    }
   
    const mediaQuery = window.matchMedia('(max-width: 768px)');
    
    function handleScreenChange(e) {
        if (e.matches) {
        }
    }
    

    handleScreenChange(mediaQuery);
    

    mediaQuery.addEventListener('change', handleScreenChange);
});