# Word Counter

text = input("Enter a sentence: ")

words = text.split()

word_count = len(words)
character_count = len(text)

print("Word count:", word_count)
print("Character count:", character_count)
