document.addEventListener('DOMContentLoaded', (event) => {
    const dropZone = document.getElementById('drop-zone');

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });

    dropZone.addEventListener('dragleave', (e) => {
        dropZone.classList.remove('dragover');
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');

        const animalId = e.dataTransfer.getData('animalId');
        const username = e.dataTransfer.getData('username');

        if (animalId && username) {
            fetch('/remove_discovery', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username: username, animal_id: animalId })
            }).then(response => response.json()).then(data => {
                if (data.success) {
                    location.reload();
                } else {
                    alert('Error al eliminar el descubrimiento');
                }
            });
        }
    });

    const images = document.querySelectorAll('.discovery-img');
    images.forEach(img => {
        img.addEventListener('dragstart', (e) => {
            e.dataTransfer.setData('animalId', e.target.getAttribute('data-animal-id'));
            e.dataTransfer.setData('username', e.target.getAttribute('data-username'));
        });
    });

    const deleteUserButtons = document.querySelectorAll('.boton-eliminar-usuario');
    deleteUserButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            const username = e.target.getAttribute('data-username');
            if (confirm(`¿Seguro que quieres eliminar al usuario ${username}?`)) {
                fetch('/delete_user', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ username: username })
                }).then(response => response.json()).then(data => {
                    if (data.success) {
                        document.getElementById(`row-${username}`).remove();
                    } else {
                        alert('Error al eliminar el usuario');
                    }
                });
            }
        });
    });
});
