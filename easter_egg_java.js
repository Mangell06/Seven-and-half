const typingArea = document.getElementById('typingArea');
const textToType = "La pantalla brilla tenue...\n¿Qué decisión tomará el jugador?";
const typingSpeed = 100; // Velocidad de escritura en ms

// Reproducir sonido del teclado
const typeSound = new Audio('https://freesound.org/data/previews/553/553844_11013409-lq.mp3');

let currentIndex = 0;

function typeText() {
    if (currentIndex < textToType.length) {
        const char = textToType[currentIndex];
        typingArea.textContent += char;
        currentIndex++;
        
        if (char !== ' ' && char !== '\n') {
            typeSound.currentTime = 0; // Reinicia el sonido
            typeSound.play();
        }
        
        setTimeout(typeText, typingSpeed);
    }
}

// Navegación de opciones
function navigate(page) {
    window.location.href = page;
}

// Mostrar texto en las opciones
function revealText(element) {
    const hiddenText = element.querySelector('.hidden-text');
    hiddenText.style.opacity = 1;
}

// Ocultar texto en las opciones
function hideText(element) {
    const hiddenText = element.querySelector('.hidden-text');
    hiddenText.style.opacity = 0;
}

// Iniciar escritura
typeText();
