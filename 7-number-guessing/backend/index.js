import cors from "cors";
import express from "express";
import rateLimit from "express-rate-limit";

const app = express();
app.use(express.json());
app.use(cors());
app.set("trust proxy", 1);
const port = 3333;

let number = 0;
// Default maxNumber to 100 if not specified
let maxNumber = parseInt(process.argv[2]) || 100;

const generateNumber = () => {
  number = Math.floor(Math.random() * maxNumber);
};

generateNumber();

// Define the rate limit rule
const guessLimit = rateLimit({
  windowMs: 10 * 1000, // 10 seconds
  max: 10, // Limit each IP to 100 requests per windowMs
  message: "Too many guesses from this IP, please try again after 10 seconds",
});

app.post("/guess", guessLimit, (req, res) => {
  const { guess } = req.body;
  console.log(`The guess was ${guess}`);
  console.log(`The correct number was ${number}`);
  if (guess === number) {
    res.json({ message: "You are correct! Generating new number..." });
    generateNumber();
  } else if (guess < number) {
    res.json({ message: "Your guess is too low!" });
  } else if (guess > number) {
    res.json({ message: "Your guess is too high!" });
  } else {
    res.json({ message: "Invalid guess" });
  }
});

app.listen(port, () => {
  console.log(
    `Number guessing app listening on port ${port}, setup your ngrok tunnel with `
  );
  console.log(`ngrok http ${port}`);
});
