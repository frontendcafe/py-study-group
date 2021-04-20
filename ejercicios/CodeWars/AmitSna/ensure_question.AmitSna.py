ensure_question = lambda word: [f"{word}?", word][len(word) >= 1 and word[-1] == "?"]

def ensure_question(word):
  if len(word) >= 1 and word[-1] == "?":
    return word
  else:
    return f"{word}?"
