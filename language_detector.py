import unicodedata

def detect_script(char):
    """Identify script of a character"""
    try:
        return unicodedata.name(char).split()[0]
    except ValueError:
        return "UNKNOWN"

def analyse_text_file(filename):
    """
    Analyse script distribution in a text file
    """
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    
    script_counts = {}

    for char in text:
        if char.isalpha():
            script = detect_script(char)
            script_counts[script] = script_counts.get(script, 0) + 1
    return script_counts

print(analyse_text_file('language_file.txt'))