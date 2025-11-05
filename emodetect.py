# emotion_simple.py
# Simple offline keyword-based emotion detector (no external libraries)

EMOTION_KEYWORDS = {
    "happy": ["happy", "joy", "glad", "excited", "pleased", "delighted", "yay", "smile"],
    "sad": ["sad", "unhappy", "depressed", "upset", "sorrow", "cry", "tears"],
    "angry": ["angry", "mad", "furious", "irritat", "annoy", "hate"],
    "fear": ["scared", "afraid", "fear", "terrified", "panic", "anxious", "nervous"],
    "surprise": ["surprised", "wow", "shocked", "amazed", "astonish"],
    "neutral": []
}

def detect_emotion(text):
    text_l = text.lower()
    scores = {k: 0 for k in EMOTION_KEYWORDS.keys()}

    # count keyword matches
    for emo, words in EMOTION_KEYWORDS.items():
        for w in words:
            if w in text_l:
                scores[emo] += text_l.count(w)

    # fallback: if no keyword matched, call neutral
    total = sum(scores.values())
    if total == 0:
        return "neutral", scores

    # choose highest score
    best = max(scores.items(), key=lambda item: item[1])
    return best[0], scores

def main():
    print("Simple Emotion Detector (type 'exit' to quit)\n")
    while True:
        s = input("Enter text: ").strip()
        if s.lower() in ("exit", "quit"):
            break
        emotion, scores = detect_emotion(s)
        print("\nDetected emotion:", emotion)
        print("Scores breakdown:", scores)
        print()

if __name__ == "__main__":
    main()
