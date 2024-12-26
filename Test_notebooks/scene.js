const canvas = document.getElementById("scene"); 
const ctx = canvas.getContext("2d");

// Dopasowanie wielkości canvas do okna
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Kolory tła
const backgroundColor = "#121212";

// Tablica do przechowywania kul
let stones = [];

// Funkcja generująca losową liczbę w zakresie
function getRandom(min, max) {
    return Math.random() * (max - min) + min;
}

// Inicjalizacja kul
const numberOfStones = 10; // Liczba kul
for (let i = 0; i < numberOfStones; i++) {
    stones.push({
        x: getRandom(50, canvas.width - 50),
        y: getRandom(50, canvas.height - 50),
        radius: 20,
        dx: getRandom(-5, 5), // Losowa prędkość w osi X
        dy: getRandom(-5, 5), // Losowa prędkość w osi Y
        color: `hsl(${Math.random() * 360}, 100%, 50%)` // Losowy kolor
    });
}

// Zmienna kontrolująca pauzę
let isPaused = false;

// Funkcja rysująca tło
function drawBackground() {
    ctx.fillStyle = backgroundColor;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
}

// Funkcja rysująca kulę
function drawStone(stone) {
    ctx.beginPath();
    ctx.arc(stone.x, stone.y, stone.radius, 0, Math.PI * 2);
    ctx.fillStyle = stone.color;
    ctx.fill();
    ctx.closePath();
}

// Funkcja rysująca strzałkę dla wektora prędkości
function drawVelocityVector(stone) {
    const vectorScale = 20; // Skala wektora (długość)
    const arrowHeadLength = 18; // Długość główki strzałki
    const angle = Math.atan2(stone.dy, stone.dx); // Kąt wektora

    // Koniec strzałki
    const endX = stone.x + stone.dx * vectorScale;
    const endY = stone.y + stone.dy * vectorScale;

    // Rysowanie linii głównej
    ctx.beginPath();
    ctx.moveTo(stone.x, stone.y);
    ctx.lineTo(endX, endY);
    ctx.strokeStyle = "#ffffff"; // Kolor strzałki
    ctx.lineWidth = 5;
    ctx.stroke();

    // Rysowanie główki strzałki (trójkąt)
    ctx.beginPath();
    ctx.moveTo(endX, endY); // Wierzchołek główki
    ctx.lineTo(
        endX - arrowHeadLength * Math.cos(angle - Math.PI / 6), // Lewa krawędź główki
        endY - arrowHeadLength * Math.sin(angle - Math.PI / 6)
    );
    ctx.lineTo(
        endX - arrowHeadLength * Math.cos(angle + Math.PI / 6), // Prawa krawędź główki
        endY - arrowHeadLength * Math.sin(angle + Math.PI / 6)
    );
    ctx.closePath();
    ctx.fillStyle = "#ffffff";
    ctx.fill();
}

// Aktualizacja pozycji kul
function updateStones() {
    stones.forEach(stone => {
        stone.x += stone.dx;
        stone.y += stone.dy;

        // Odbicie od ścian
        if (stone.x + stone.radius > canvas.width || stone.x - stone.radius < 0) {
            stone.dx *= -1;
        }
        if (stone.y + stone.radius > canvas.height || stone.y - stone.radius < 0) {
            stone.dy *= -1;
        }
    });

    // Sprawdzenie kolizji między wszystkimi kulami
    for (let i = 0; i < stones.length; i++) {
        for (let j = i + 1; j < stones.length; j++) {
            handleCollision(stones[i], stones[j]);
        }
    }
}

// Funkcja obsługująca kolizję
function handleCollision(stone1, stone2) {
    const dx = stone2.x - stone1.x;
    const dy = stone2.y - stone1.y;
    const distance = Math.sqrt(dx * dx + dy * dy);

    if (distance < stone1.radius + stone2.radius) {
        // Odbij prędkości w przeciwnym kierunku
        [stone1.dx, stone2.dx] = [stone2.dx, stone1.dx];
        [stone1.dy, stone2.dy] = [stone2.dy, stone1.dy];
    }
}

// Animacja
function animate() {
    if (!isPaused) {
        drawBackground(); // Tło
        stones.forEach(stone => {
            drawStone(stone); // Kula
            drawVelocityVector(stone); // Strzałka prędkości
        });
        updateStones(); // Aktualizuj pozycje kul
    }
    requestAnimationFrame(animate); // Powtórz animację
}

// Obsługa kliknięcia przycisku pauzy
const pauseButton = document.getElementById("pauseButton");
pauseButton.addEventListener("click", () => {
    isPaused = !isPaused; // Zmień stan pauzy
    pauseButton.textContent = isPaused ? "Wznów" : "Pauza"; // Zmień tekst na przycisku
});

// Rozpocznij animację
animate();
