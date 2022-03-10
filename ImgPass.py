import hashlib as hsh
import os
from ocryptor import oCrypt
import sqlite3



def clear():
    os.system("clear||cls")


def banner():
    banner = """
    ██╗███╗   ███╗ ██████╗ ██████╗  █████╗ ███████╗███████╗
    ██║████╗ ████║██╔════╝ ██╔══██╗██╔══██╗██╔════╝██╔════╝
    ██║██╔████╔██║██║  ███╗██████╔╝███████║███████╗███████╗
    ██║██║╚██╔╝██║██║   ██║██╔═══╝ ██╔══██║╚════██║╚════██║
    ██║██║ ╚═╝ ██║╚██████╔╝██║     ██║  ██║███████║███████║
    ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝

            Made By https://github.com/therealOri
    """
    return banner



def img_to_hash(img):
    isFile = os.path.isfile(img)
    BUF_SIZE = 65536
    if isFile == True:
        with open(img, 'rb') as fh:
            while True:
                data = fh.read(BUF_SIZE)
                if not data:
                    break
                elif data == '':
                    break
                else:
                    nhash = hsh.blake2b(data, digest_size=32).hexdigest()
                    return nhash
        raise Exception("There is no data to hash...[Empty File]") from None
    else:
        ithE = "File that was provided does not exist or isn't a file.."
        raise Exception(ithE) from None




def verify_hash(email, img, key, key_salt, enc_salt):
    img_result = img_to_hash(img)

    database = sqlite3.connect('accounts.hshes')
    c = database.cursor()
    c.execute(f"SELECT hash FROM logins WHERE email LIKE '{email}'")
    h = c.fetchone()[0]
    if not h:
        raise Exception("Oof..nothing here but us foxos...") from None
    else:
        enc_hash = oCrypt().string_decrypt(key, key_salt, h, enc_salt)
        if enc_hash == img_result:
            return True
        else:
            return False



def add_db(email, img_hash, key, key_salt, enc_salt):
    enc_hash = oCrypt().string_encrypt(key, key_salt, img_hash, enc_salt)
    database = sqlite3.connect('accounts.hshes')
    c = database.cursor()

    c.execute(f"INSERT INTO logins VALUES ('{email}', '{enc_hash}')")
    database.commit()
    database.close()
        



def main():
    while True:
        try:
            clear()
            options = int(input(f'{COLORS["cyan"]}{banner()}\n\n\n\nWhat do you want to do today?\n\n1. Check the hash of a file?\n2. Register?\n3. Login?\n4. Quit?\n\nEnter: {COLORS["end"]}{COLORS["green"]}'))
            print(f'{COLORS["end"]}')
        except Exception as e:
            clear()
            print(f'{COLORS["red"]}Oops, the value given is not an integer/number.{COLORS["end"]}\n\n')
            input(f'{COLORS["green"]}Press "Enter" to continue...{COLORS["end"]}')
            clear()
            continue

        if options == 1:
            clear()
            img = input(f'{COLORS["cyan"]}Please drag and drop the file/image you want to use into the terminal window.\nThen press "enter" to continue...{COLORS["end"]}\n\n{COLORS["red"]}').replace('\\ ', ' ').strip()
            clear()
            result = img_to_hash(img)
            print(f'{COLORS["green"]}Here is your hash! - (blake2b): {COLORS["end"]}{COLORS["red"]}{result}{COLORS["end"]}\n\n')
            input(f'{COLORS["cyan"]}Press "Enter" to continue...{COLORS["end"]}')
            clear()
        elif options == 2:
            clear()
            email = input(f'{COLORS["green"]}Please enter your email address:\nEmail: {COLORS["red"]}')
            print(f'{COLORS["end"]}')
            clear()
            img = input(f'{COLORS["cyan"]}Please drag and drop the file/image you want to use into the terminal window.\nThen press "enter" to continue...{COLORS["end"]}\n\n{COLORS["red"]}').replace('\\ ', ' ').strip()
            print(f'{COLORS["end"]}')
            clear()
            

            key = input(f'{COLORS["green"]}Please provide a key for hashing: {COLORS["end"]}{COLORS["red"]}')
            print(f'{COLORS["end"]}')

            key_salt = input(f'{COLORS["green"]}Please provide a salt for the hasing key: {COLORS["end"]}{COLORS["red"]}')
            print(f'{COLORS["end"]}')

            enc_salt = input(f'{COLORS["green"]}Please provide a salt for the encryption: {COLORS["end"]}{COLORS["red"]}')
            print(f'{COLORS["end"]}')
            clear()
            result = img_to_hash(img)
            add_db(email, result, key, key_salt, enc_salt)
            print(f'{COLORS["green"]}Values added to the database successfully!{COLORS["end"]}\n\n')
            input(f'{COLORS["cyan"]}Press "Enter" to continue...{COLORS["end"]}')
            clear()
            
        elif options == 3:
            clear()
            email = input(f'{COLORS["green"]}Please enter your email address:\nEmail: {COLORS["red"]}')
            print(f'{COLORS["end"]}')
            clear()
            img = input(f'{COLORS["cyan"]}Please drag and drop the file/image you want to use into the terminal window.\nThen press "enter" to continue...{COLORS["end"]}\n\n{COLORS["red"]}').replace('\\ ', ' ').strip()
            print(f'{COLORS["end"]}')
            clear()

            key = input(f'{COLORS["green"]}Please provide a key for hashing: {COLORS["end"]}{COLORS["red"]}')
            print(f'{COLORS["end"]}')

            key_salt = input(f'{COLORS["green"]}Please provide a salt for the hasing key: {COLORS["end"]}{COLORS["red"]}')
            print(f'{COLORS["end"]}')

            enc_salt = input(f'{COLORS["green"]}Please provide a salt for the encryption: {COLORS["end"]}{COLORS["red"]}').replace('\\ ', ' ').strip()
            print(f'{COLORS["end"]}')
            clear()


            if verify_hash(email, img, key, key_salt, enc_salt) == True:
                print(f"{COLORS['green']}Welcome user! You have now logged in!{COLORS['end']}\n\n")
                input(f'{COLORS["cyan"]}Press "Enter" to continue...{COLORS["end"]}')
                clear()
            else:
                print(f"{COLORS['red']}Error: Incorrect login credentials has been given..try again.{COLORS['end']}\n\n")
                input(f'{COLORS["green"]}Press "Enter" to continue...{COLORS["end"]}')
                clear()
        elif options == 4:
            clear()
            quit()
        else:
            clear()
            print(f'{COLORS["red"]}That is not a valid menu option...{COLORS["end"]}\n\n')
            input(f'{COLORS["green"]}Press "Enter" to continue...{COLORS["end"]}')
            clear()



if __name__ == '__main__':
    COLORS = {"cyan": '\033[1;36;48m', "green": '\033[1;32;48m', "red": '\033[1;31;48m', "end": '\033[0m'}
    main()