from spell_checker import load_dictionary, suggest

def main():
    dictionary = load_dictionary("dictionary.txt")
    while True:
        typo = input("Introduce una palabra (o 'salir'): ").strip().lower()
        if typo == "salir":
            break
        suggestions = suggest(typo, dictionary)
        print("Sugerencias:")
        for i, word in enumerate(suggestions, 1):
            print(f"{i}. {word}")
        print()

if __name__ == "__main__":
    main()
