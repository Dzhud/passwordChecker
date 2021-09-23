# Small program to determine the strength of Users Password

__author__ = 'Dzhud' #on Github

def checkPasswordStrength(password=''):
    SPECIAL_CHARACTERS = '!@#$%^&*()'
    strength = [0, 0, 0, 0, 0]
    messages = ('Ah! At least a lowercase letter must be included.',
            'Oops! Forgot an uppercase letter?',
            'Missing at least a number',
            'A minimum of one special character must be added.',
            'Password must be minimum 7 characters')
    for letter in password:
        if letter.islower():
            strength[0] = 1
        elif letter.isupper():
            strength[1] = 1
        elif letter.isdigit():
            strength[2] = 1
        elif letter in SPECIAL_CHARACTERS:
            strength[3] = 1
        elif ' ' in password:
            print('Nope! Sorry. Cannot add space to password')
            return False
    if len(password) > 6: 
        strength [4] = 1
    print()
    for count in range(len(strength)):
        if strength[count] == 0:
            print (messages[count])
    if 0 in strength:
        return False
    
    else:
        print ("Now that's a strong password mate!")
        return True


if __name__ == "__main__":
    checkPasswordStrength('Br34!dkkmms ')
        
    
    

