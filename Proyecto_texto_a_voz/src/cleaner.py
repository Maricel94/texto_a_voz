import re


def clean_text(text):
    text = re.sub(r"@\w+", "", text)  # elimina @usuarios
    text = re.sub(r"#\w+", "", text)  # elimina hashtags
    text = re.sub(r"http\S+", "", text)  # elimina URLs
    return text