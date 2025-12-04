"""
memory_extractor.py
Simple rule-based memory extraction from a sequence of chat messages.

Produces JSON list of memory items with:
- category: preference / emotional_pattern / fact
- key: short key
- value: extracted text or normalized value
- source_message: original message
- confidence: heuristic confidence score 0-1
"""

import re
from typing import List, Dict

PREFERENCE_KEYWORDS = {
    "food": ["idli","sambar","buttermilk","vegetarian","rice","dal","dosa","oats","almond"],
    "music": ["lo-fi","jazz","music","song","listen"],
    "language": ["python","c","java","c++","javascript"],
    "editor": ["vs code","vscode","sublime"],
    "movies": ["sci-fi","thriller","movie","movies"],
    "sport": ["football","cricket","gym"]
}

FACT_PATTERNS = {
    "age": r"(\b\d{1,2}\b)\s*(?:years old|yo|y/o|yrs|yrs old)?",
    "cgpa": r"(\b\d\.\d{1,2}\b)\s*(?:cgpa)?",
    "location": r"\bIndia\b|\bUSA\b|\bBangalore\b|\bHyderabad\b",
    "projects": r"(project|completed|finished).{0,60}"
}

EMOTION_WORDS = {
    "anxiety": ["anxious","anxiety","stress","stressed","sweaty","worried"],
    "sadness": ["lonely","sad","down","depressed"],
    "frustration": ["frustrat","annoyed","hate","dislike"],
    "happiness": ["love","like","enjoy","happy","relax"]
}

def extract_memories(messages: List[str]) -> List[Dict]:
    memories = []
    # preferences
    for msg in messages:
        low = msg.lower()
        # preferences by keywords
        for cat, kwlist in PREFERENCE_KEYWORDS.items():
            for kw in kwlist:
                if kw in low:
                    memories.append({
                        "category":"preference",
                        "subtype":cat,
                        "key":f"pref_{cat}_{kw.replace(' ','_')}",
                        "value":kw,
                        "source_message":msg,
                        "confidence":0.9
                    })
        # facts
        for fact, pat in FACT_PATTERNS.items():
            m = re.search(pat, msg, re.IGNORECASE)
            if m:
                val = m.group(0)
                memories.append({
                    "category":"fact",
                    "subtype":fact,
                    "key":f"fact_{fact}",
                    "value":val.strip(),
                    "source_message":msg,
                    "confidence":0.85
                })
        # emotional patterns
        for emo, words in EMOTION_WORDS.items():
            for w in words:
                if w in low:
                    # heuristics for frequency, here we just record occurrence
                    memories.append({
                        "category":"emotional_pattern",
                        "subtype":emo,
                        "key":f"emo_{emo}_{w}",
                        "value":w,
                        "source_message":msg,
                        "confidence":0.7
                    })
    # simple dedup
    unique = {}
    for mem in memories:
        k = (mem['category'], mem['subtype'], mem['value'])
        if k not in unique or mem['confidence'] > unique[k]['confidence']:
            unique[k] = mem
    return list(unique.values())

if __name__ == "__main__":
    import json, sys
    msgs = json.load(open(sys.argv[1]))
    mems = extract_memories(msgs)
    print(json.dumps(mems, indent=2))
