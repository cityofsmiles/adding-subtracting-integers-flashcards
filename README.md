# Integer Flashcards App

This project is a **flashcards web app** for practicing integer addition
and subtraction.\
It uses a **Python backend** to generate all flashcards (math rules,
expressions, and answers)\
and a **React frontend** to display them interactively with animations.

------------------------------------------------------------------------

## Features

-   Covers **four key cases** of integer operations:
    1.  **Adding like signs**\
        Examples: `3 + 5 = 8`, `-2 + (-4) = -6`
    2.  **Adding unlike signs**\
        Examples: `-3 + 5 = 2`, `2 + (-4) = -2`
    3.  **Subtracting like signs**\
        Examples: `3 - 5 = -2`, `-2 - (-4) = 2`
    4.  **Subtracting unlike signs**\
        Examples: `-3 - 5 = -8`, `2 - (-4) = 6`
-   Python (`sympy` + `random`) generates **200 flashcards** (50 per
    case).\
-   Output stored in **`public/flashcards.json`**.\
-   React frontend loads JSON and randomly selects **10 flashcards per
    session**.\
-   Interactive UI with:
    -   Input box for user answer\
    -   Instant feedback (Correct / Incorrect)\
    -   Scoreboard and answer key\
    -   Smooth animations for better UX

------------------------------------------------------------------------

## Tech Stack

-   **Backend (Flashcard Generator):** Python 3, Sympy\
-   **Frontend (UI):** React + TailwindCSS + Framer Motion\
-   **Data Exchange:** Pre-generated JSON file (`flashcards.json`)

------------------------------------------------------------------------

## Getting Started

### 1. Clone the repository

``` bash
git clone https://github.com/your-username/integer-flashcards.git
cd integer-flashcards
```

### 2. Generate Flashcards (Python)

Make sure you have Python 3 installed.

``` bash
pip install sympy
python generate_flashcards.py
```

This will create:

    public/flashcards.json

### 3. Run React Frontend

Install dependencies and start the dev server:

``` bash
npm install
npm start
```

Open <http://localhost:3000> to view the app.

------------------------------------------------------------------------

## Project Structure

    .
    â”œâ”€â”€ generate_flashcards.py   # Python script for generating flashcards
    â”œâ”€â”€ public/
    â”‚   â””â”€â”€ flashcards.json      # Generated flashcards (200 total)
    â”œâ”€â”€ src/
    â”‚   â”œâ”€â”€ components/
    â”‚   â”‚   â””â”€â”€ Flashcard.js     # React flashcard component
    â”‚   â””â”€â”€ App.js               # Main React app
    â”œâ”€â”€ package.json
    â””â”€â”€ README.md

------------------------------------------------------------------------

## Example Flashcard JSON

``` json
{
  "question": "2 - (-4)",
  "answer": "6"
}
```

------------------------------------------------------------------------

## Future Improvements

-   Add difficulty levels (easy, medium, hard)\
-   Track progress across sessions\
-   Allow custom flashcard generation from the UI

------------------------------------------------------------------------

## License

This project is licensed under the MIT License.