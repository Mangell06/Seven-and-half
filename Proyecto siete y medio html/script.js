document.addEventListener("DOMContentLoaded", () => {
    console.log("Documento cargado y DOM listo");

    // Cargar la cabecera desde cabecera.html
    fetch('cabecera.html')
        .then(response => response.text())
        .then(data => {
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = data;

            // Agregar elementos al <head>
            const headElements = tempDiv.querySelectorAll('meta, link, script');
            headElements.forEach(el => document.head.appendChild(el));

            // Agregar el <header> al contenedor de la cabecera
            const header = tempDiv.querySelector('header');
            if (header) {
                document.getElementById('cabecera').appendChild(header);

                // Evento para cambiar colores en el header
                header.addEventListener("click", () => {
                    header.classList.toggle("alt-color");
                });

                // --- Aquí empieza la lógica para la clase 'active' ---
                const navLinks = header.querySelectorAll('nav ul li a'); // Obtener enlaces dentro del header cargado
                const currentPage = window.location.pathname.split('/').pop(); // Página actual

                navLinks.forEach(link => {
                    if (link.getAttribute('href') === currentPage) {
                        link.classList.add('active'); // Añade la clase 'active' al enlace actual
                    }
                });
                // --- Aquí termina la lógica para la clase 'active' ---
            }
        })
        .catch(error => console.error('Error al cargar la cabecera:', error));
});
