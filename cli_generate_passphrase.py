from passphrase_generator.io import read_phrases
from passphrase_generator.passphrase import generate_passphrase

def main() -> None:

    phrases = read_phrases("Please input atleast 3 phrases (words) to create passphrase (password) out of.")
    password = generate_passphrase(phrases)
    print(f"Password is: {password}")

if __name__ == "__main__":
    main()
