from collections import Counter
def validate_word(word):
    char_counts = Counter(word.lower())
    unique_counts = set(char_counts.values())
    if len(unique_counts) == 1:
        return True
    else:
        return False
