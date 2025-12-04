"""
examples.py - shows the full flow: load messages, extract memories, and show personality rewrites.
"""
import json
from memory_extractor import extract_memories
from personality_engine import rewrite

msgs = json.load(open("messages_30.json"))
print("Sample messages (first 6):")
for m in msgs[:6]:
    print("-", m)
print("\n--- Extracted memories ---")
mems = extract_memories(msgs)
import pprint
pprint.pprint(mems[:20])

# Before/After personality examples
print("\n--- Before/After personality rewrites ---")
base_replies = [
    "Practice problem solving every day and review fundamentals.",
    "Try breaking your work into smaller parts and follow a schedule.",
    "It's okay to feel anxious, try breathing exercises before the test."
]

for br in base_replies:
    print("\nBase reply:\n", br)
    for tone in ["mentor","witty","therapist"]:
        print(f"\nTone: {tone}\n", rewrite(br, tone))
