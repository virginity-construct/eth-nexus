function handleApplication(event) {
    event.preventDefault();
    
    // Show application modal
    const modal = document.getElementById('applicationModal');
    modal.style.display = 'block';
}

function closeModal() {
    const modal = document.getElementById('applicationModal');
    modal.style.display = 'none';
}

function submitApplication(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    
    // For now, just show a success message
    // In production, this would send data to a server
    const modal = document.getElementById('applicationModal');
    modal.innerHTML = `
        <div class="modal-content">
            <h2>Application Received! 🎉</h2>
            <p>Thank you for your interest in ETH Nexus.</p>
            <p>We'll review your application and contact you within 2-3 business days.</p>
            <button onclick="closeModal()" class="cta-secondary">Close</button>
        </div>
    `;
}

// Download whitepaper
function downloadWhitepaper() {
    // Create a simple PDF with project details
    const link = document.createElement('a');
    link.href = 'assets/ETH_Nexus_Whitepaper.pdf';
    link.download = 'ETH_Nexus_Whitepaper.pdf';
    link.click();
}
