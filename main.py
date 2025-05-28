def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    correct_count = 0
    for english,spanish in translations.items():
        user = input(f"What is the Spanish translation for {english}? ").strip().lower()
    
        if user == spanish:
            print("That is correct!")
            correct_count += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english} is {spanish}.")

        print()
    print(f"You got {correct_count}/{len(translations)} words correct, come study again soon!")

    


if __name__ == '__main__':
    main()