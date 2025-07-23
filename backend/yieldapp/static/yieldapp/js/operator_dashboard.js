document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('formModal');
    const modalContent = document.getElementById('modalContent');
    const closeModalButton = document.querySelector('.close-button');

    function openModal() { modal.style.display = 'block'; }
    function closeModal() { modal.style.display = 'none'; modalContent.innerHTML = ''; }

    if (closeModalButton) {
        closeModalButton.addEventListener('click', closeModal);
    }

    window.addEventListener('click', function(event) {
        if (event.target == modal) {
            closeModal();
        }
    });

    document.querySelectorAll('.process-card.active').forEach(card => {
        card.addEventListener('click', function(event) {
            event.preventDefault();
            const formUrl = this.dataset.url; // Gunakan data-url
            
            modalContent.innerHTML = '<p>Loading form...</p>';
            openModal();

            fetch(formUrl)
                .then(response => {
                    if (!response.ok) { throw new Error('Network response was not ok'); }
                    return response.text();
                })
                .then(html => {
                    modalContent.innerHTML = html;
                })
                .catch(error => {
                    console.error('Error fetching the form:', error);
                    modalContent.innerHTML = '<p>Gagal memuat form. Coba muat ulang halaman.</p>';
                });
        });
    });
});