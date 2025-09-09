import sympy as sp
import random
import json
import os


flashcards = []


def format_int(n: int) -> str:
    """Format integer for display, enclosing negatives in parentheses."""
    return f"({n})" if n < 0 else str(n)


def generate_case(case_type: int) -> dict:
    """
    Generate a flashcard for one of four cases:
      1. Adding like signs
      2. Adding unlike signs
      3. Subtracting like signs
      4. Subtracting unlike signs
    """
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

    # Ensure valid "case" generation rules
    if case_type == 1:  # Adding like signs
        # Both positive OR both negative
        sign = random.choice([1, -1])
        a = random.randint(1, 10) * sign
        b = random.randint(1, 10) * sign
        question = f"{format_int(a)} + {format_int(b)}"
        answer = a + b

    elif case_type == 2:  # Adding unlike signs
        # One positive, one negative
        a = random.randint(1, 10)
        b = -random.randint(1, 10)
        if random.choice([True, False]):
            a, b = b, a
        question = f"{format_int(a)} + {format_int(b)}"
        answer = a + b

    elif case_type == 3:  # Subtracting like signs
        # Both positive OR both negative
        sign = random.choice([1, -1])
        a = random.randint(1, 10) * sign
        b = random.randint(1, 10) * sign
        question = f"{format_int(a)} - {format_int(b)}"
        answer = a - b

    else:  # case_type == 4 → Subtracting unlike signs
        a = random.randint(1, 10)
        b = -random.randint(1, 10)
        if random.choice([True, False]):
            a, b = b, a
        question = f"{format_int(a)} - {format_int(b)}"
        answer = a - b

    return {"question": question, "answer": str(answer)}


# Generate 200 flashcards (50 per case)
for case_type in range(1, 5):
    for _ in range(50):
        flashcards.append(generate_case(case_type))

# Save to ./public/flashcards.json
output_dir = os.path.join(os.getcwd(), "public")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "flashcards.json")

with open(output_path, "w") as f:
    json.dump(flashcards, f, indent=2)

print(f"✅ flashcards.json generated with {len(flashcards)} flashcards at {output_path}")