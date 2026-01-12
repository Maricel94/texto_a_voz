from extractor import extract_text
from tts import text_to_mp3
from cleaner import clean_text

import re


def main():
    url = input("Introduce la URL del artículo: ")

    print("Extrayendo texto del artículo...")
    text = extract_text(url)
    text = clean_text(text)

    print("Convirtiendo texto a audio...")
    output_file = text_to_mp3(text)

    print(f"Audio generado correctamente en: {output_file}")


if __name__ == "__main__":
    main()
