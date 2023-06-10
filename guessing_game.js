let secretNumber = Math.floor(Math.random() * 100) + 1;
let guess;
let attempts = 0;

do {
    guess = prompt("Guess a number between 1 and 100:");
attempts++;
    if (guess < secretNumber) {
        alert("Too low, try again.");
    } else if (guess > secretNumber) {
        alert("Too high, try again.");
    }
} while (guess != secretNumber);

alert("Congratulations! You guessed the number in " + attempts + " attempts.");