import nltk
from nltk.corpus import words

nltk.download("punkt")
nltk.download("words")

def generate_key(n: int) -> dict:
    # Generate a dictionary-based encryption key
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for letter in letters:
        key[letter] = letters[(cnt + n) % len(letters)]
        cnt += 1
    return key

def generate_decryption_key(key: dict) -> dict:
    # Generate the decryption key based on the encryption key
    dkey = {}
    for k, v in key.items():
        dkey[v] = k
    return dkey

def encrypt(key: dict, message: str) -> str:
    # Encrypt the given message using the encryption key
    message = message.upper()
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

def decrypt(key: dict, cipher:str) -> str:
    # Decrypt the given cipher using the encryption key
    message = ""
    for c in cipher:
        if c in key.values():
            for k, v in key.items():
                if v == c:
                    message += k
                    break
        else:
            message += c
    return message

def is_valid_english(sentence):
    # Tokenize the sentence into words
    tokens = nltk.word_tokenize(sentence)

    # Count valid english words
    valid_word_count = sum(token.lower() in words.words() for token in tokens)

    # Return true if the majority of words are english
    return valid_word_count / len(tokens) >= 0.5

def find_correct_phrase(brut):
    for phrase in brut:
        if is_valid_english(phrase):
            return phrase
    return None

if __name__ == "__main__":
    # Generate key
    key = generate_key(3)
    
    for k, v in key.items():
        print("key: "+ k + " value: " + v)
        
    message = "A message encrypted the cypher way"
    
    # Encryption
    encrypted_message = encrypt(key, message)
    print(encrypted_message)
    
    # Decryption
    decrypted_cipher = decrypt(key, encrypted_message)
    print(decrypted_cipher)

    # Generate a reverse key by subtracting 3 from the length of the key
    reverse_key = generate_key(len(key)-3)
    reverse_encrypted = encrypt(reverse_key, encrypted_message)
    print(reverse_encrypted)

    # Generate a decryption key based on the original encryption key    
    dkey = generate_decryption_key(key)
    decrypted_by_dkey = encrypt(dkey, encrypted_message)
    print(decrypted_by_dkey + "\n")

    # Brut force approach
    brut = []
    for i in range(len(dkey)):
        deckey = generate_key(i)
        forced_message = encrypt(deckey, encrypted_message)
        brut.append(forced_message)
        print(forced_message)
        
    correct_phrase = find_correct_phrase(brut)
    if correct_phrase:
        print("Correct phrase found:", correct_phrase)
    else:
        print("No correct phrase found.")