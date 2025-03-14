import random

emoji_dict = {
    "happy" : "😀",
    "love" : "❤",
    "fire" : "🔥",
    "sad" : "☹",
    "cool" : "😎",
    "food" : "🍔",
    "dog" : "🐶",
    "cat" : "🐱"
}

def emoji_translate(sentence):
    """
    Takes a sentence, and returns the sentence with the words replaced with emojis.
    """
    words = sentence.split()
    return " ".join(emoji_dict.get(word, word) for word in words)

mood_emojis = {
    "happy" : ["😀", "😆", "🤣", "😂", "🥳"],
    "sad" : ["☹", "😧", "😨", "😰", "😢", "😭"],
    "angry" : ["😡", "😠", "🤬", "💢"],
    "excited" : ["🌟", "✨", "🎉", "🤩"]
}

def mood_fill(sentence):
    """
    Returns the sentence with emojis if the user asks for
    filling with the phrase (fill with ... emojis)
    """
    words = sentence.split()
    mood = None

    for key in mood_emojis:
        if f"(fill with {key} emojis)" in sentence:
            mood = key
            to_remove = f"(fill with {key} emojis)"
            words_to_remove = to_remove.split()
            for wtr in words_to_remove:
                words.remove(wtr)
            break
    
    if mood:
        words.append("".join(random.choices(mood_emojis[key], k=3)))

    return " ".join(words)


while True:
    print("Welcome to emoji translator")
    print("1. Emoji Translator")
    print("2. Mood-Fill Emoji Generator")
    print("5. Exit")

    choice = int(input("Choose an option (1-5): "))

    if choice == 1:
        text = input("Enter a sentence to translate: ")
        print("Translated: ", emoji_translate(text))
    elif choice == 2:
        text = input("Enter a sentence with mood: ")
        print("Mood-filled: ", mood_fill(text))
    elif choice == 5:
        print("Goodbye")
        break
    else:
        print("Invalid choice! Try again.")
