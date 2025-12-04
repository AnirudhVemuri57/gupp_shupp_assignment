"""
personality_engine.py
Provide functions to transform a base reply into different tones:
- calm_mentor
- witty_friend
- therapist_style

This is rule-based for demonstration purposes. In production, you'd use a controllable LLM or seq2seq model.
"""

import random
import textwrap

def calm_mentor(reply: str) -> str:
    # make more formal, add short step suggestions
    lines = []
    lines.append("Here's a calm mentor-style answer:")
    lines.append(reply.strip().capitalize())
    lines.append("\nSteps you can take:")
    steps = [
        "Break the task into small subtasks and schedule them.",
        "Practice with small, focused exercises for 25-45 minutes.",
        "Use code snippets and replicate them rather than memorizing."
    ]
    lines.extend([f"- {s}" for s in steps])
    return "\\n".join(lines)

def witty_friend(reply: str) -> str:
    # add casual tone and a light joke
    jokey = ["Trust me, you'll ace it — unless your coffee spills.", 
             "TL;DR: You're closer than you think!"]
    base = reply.strip()
    if not base.endswith('.'):
        base = base + '.'
    transformed = f"Yo! {base} {random.choice(jokey)}"
    return transformed

def therapist_style(reply: str) -> str:
    # reflective, validating style
    base = reply.strip()
    lines = []
    lines.append("I hear you. It sounds like this is important to you.")
    lines.append(base)
    lines.append("Can you tell me what part of this feels most difficult right now?")
    return "\\n".join(lines)

# a wrapper to pick tone
def rewrite(reply: str, tone: str) -> str:
    tone = tone.lower()
    if tone == "calm_mentor" or tone == "mentor":
        return calm_mentor(reply)
    if tone == "witty_friend" or tone == "witty":
        return witty_friend(reply)
    if tone == "therapist" or tone == "therapist_style":
        return therapist_style(reply)
    # default: return original
    return reply

if __name__ == "__main__":
    import sys, json
    sample = "Practice problem solving every day and review fundamentals."
    print("Original:", sample)
    print("Mentor:", calm_mentor(sample))
    print("Witty:", witty_friend(sample))
    print("Therapist:", therapist_style(sample))
