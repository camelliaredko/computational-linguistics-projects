# Olga Redko
# CMPU-366
# Palindrome

def getRev(text):
    return text[::-1]

def cleanInput(text):
    return text.lower().replace(' ', '').replace("'", '').replace(',', '').replace(':', '').replace('.', '')

def main():
        exp = input("Give me a palindrome: ")
        exp_clean = cleanInput(exp)
        exp_clean_rev = getRev(exp_clean)
        if exp_clean == exp_clean_rev and len(exp) > 2:
            print('YES, "' + exp + '" is a palindrome.')
            print('Goodbye.')
        elif len(exp) < 3:
            print('Sorry, try something longer.')
            main()
        else:
            print('NO, "' + exp + "\" is not a palindrome. Let's try again.")
            main()

main()