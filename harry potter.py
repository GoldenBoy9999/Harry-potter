#!/usr/bin/env python3
"""
Harry‑Potter Quote Quiz

Author:   <your name>
Date:     2026-01-11
"""

import random
from pathlib import Path
import sys

# ----------------------------------------------------------------------
# 1.  The data – a list of (quote, speaker) tuples.
#    Feel free to add more quotes or move them into an external file.
# ----------------------------------------------------------------------
QUOTES = [
    ("It does not do to dwell on dreams and forget to live.", "Albus Dumbledore"),
    ("I am what I am… that is all you ever need know", "Rubeus Hagrid"),
    ("You are a great little person, Harry Potter. Very good at fighting Death Eaters.", "Lord Voldemort (in memory)"),
    ("We’ve all got the right to be afraid of someone we love.", "Hermione Granger"),
    ("The ones that love us never really leave us", "Remus Lupin"),
    ("I will not let you, Potter. I have a duty to my house and its honour.", "Lord Voldemort (at the Dursleys)"),
    ("There is no good or evil in the wizarding world – only those who choose to be so.", "Albus Dumbledore"),
    ("Do not pity the dead; you must not do it, but if you do wish to look after them, please remember them as you would a friend of yours", "Harry Potter (in The Goblet of Fire)"),
    ("A wand is just a tool. A good wizard uses his mind.", "Minerva McGonagall"),
    ("It takes a great deal of courage to be what we are", "Sirius Black")
]

# ----------------------------------------------------------------------
# 2.  Helper: pick a random quote
# ----------------------------------------------------------------------
def choose_random_quote():
    return random.choice(QUOTES)

# ----------------------------------------------------------------------
# 3.  Main quiz logic
# ----------------------------------------------------------------------
def run_quiz():
    print("\n=== Harry‑Potter Quote Quiz ===")
    quote, speaker = choose_random_quote()
    print(f"\nGuess who said this:\n\n  \"{quote}\"\n")

    answer = input("Your guess: ").strip()

    # Normalise the comparison (case insensitive, strip whitespace)
    if answer.lower() == speaker.lower():
        print("\n✅ Correct! Great job.\n")
    else:
        print(f"\n❌ Wrong. The correct answer was: {speaker}\n")

# ----------------------------------------------------------------------
# 4.  Entry point
# ----------------------------------------------------------------------
if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        sys.exit("\n\nQuiz aborted by user.\n")
