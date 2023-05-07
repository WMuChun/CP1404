"""
Word Occurrences
Estimate: 30 minutes
Actual:   69 minutes
"""

user_input = input("Enter a string: ")
words = user_input.lower().split()
words_counts = {}

max_width = 0
for word in words:
    if len(word) > max_width:
        max_width = len(word)

for word in words:
    if word in words_counts:
        words_counts[word]+= 1
    else:
        words_counts[word] = 1

print(f"Text: {user_input}")
for word, count in words_counts.items():
    print(f"{word: {max_width}}: {str(count)} ")