// Modal functionality
function handleApplication(event) {
    if (event) event.preventDefault();
    
    // Show application modal
    const modal = document.getElementById('applicationModal');
    modal.classList.add('show');
}

function closeModal() {
    const modal = document.getElementById('applicationModal');
    modal.classList.remove('show');
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('applicationModal');
    if (event.target === modal) {
        closeModal();
    }
}

function submitApplication(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    
    // Convert FormData to object for display
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });
    
    // Log the submission (in production, this would go to a server)
    console.log('Application submitted:', data);
    
    // Show success message
    const modal = document.getElementById('applicationModal');
    modal.innerHTML = `
        <div class="modal-content success-message">
            <h2>Application Received! 🎉</h2>
            <p>Thank you for your interest in ETH Nexus.</p>
            <p>We'll review your application and contact you within 2-3 business days.</p>
            <button onclick="closeModal()" class="cta-primary">Close</button>
        </div>
    `;
}

// Download whitepaper
function downloadWhitepaper() {
    window.location.href = 'assets/whitepaper.html';
}
