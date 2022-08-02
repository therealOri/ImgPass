import hashlib as hsh
import os
from ocryptor import oCrypt
import sqlite3



def clear():
    os.system("clear||cls")


def banner():
    return """
    ██╗███╗   ███╗ ██████╗ ██████╗  █████╗ ███████╗███████╗
    ██║████╗ ████║██╔════╝ ██╔══██╗██╔══██╗██╔════╝██╔════╝
    ██║██╔████╔██║██║  ███╗██████╔╝███████║███████╗███████╗
    ██║██║╚██╔╝██║██║   ██║██╔═══╝ ██╔══██║╚════██║╚════██║
    ██║██║ ╚═╝ ██║╚██████╔╝██║     ██║  ██║███████║███████║
    ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝

            Made By https://github.com/therealOri
    """



def img_to_hash(img):
    isFile = os.path.isfile(img)
    if isFile == True:
        BUF_SIZE = 65536
        with open(img, 'rb') as fh:
            while True:
                data = fh.read(BUF_SIZE)
                if not data or data == '':
                    break
                else:
                    return hsh.blake2b(data, digest_size=32).hexdigest()
        raise Exception("There is no data to hash...[Empty File]") from None
    else:
        ithE = "File that was provided does not exist or isn't a file.."
        raise Exception(ithE) from None




def verify_hash(email, img, enc_key, enc_salt):
    img_result = img_to_hash(img)

    database = sqlite3.connect('accounts.hshes')
    c = database.cursor()
    c.execute(f"SELECT hash FROM logins WHERE email LIKE '{email}'")
    if h := c.fetchone():
        enc_hash = oCrypt().string_decrypt(h[0], enc_key, enc_salt)
        return enc_hash == img_result
    else:
        msg = "No account with the provided email exists."
        raise ValueError(msg) from None



def add_db(email, img_hash, enc_key, enc_salt):
    enc_hash = oCrypt().string_encrypt(img_hash, enc_key, enc_salt)
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

        clear()
        if options == 1:
            img = input(f'{COLORS["cyan"]}Please drag and drop the file/image you want to use into the terminal window.\nThen press "enter" to continue...{COLORS["end"]}\n\n{COLORS["red"]}').replace('\\ ', ' ').strip()
            clear()
            result = img_to_hash(img)
            print(f'{COLORS["green"]}Here is your hash! - (blake2b): {COLORS["end"]}{COLORS["red"]}{result}{COLORS["end"]}\n\n')
            input(f'{COLORS["cyan"]}Press "Enter" to continue...{COLORS["end"]}')
            clear()
        elif options == 2:
            email = input(f'{COLORS["green"]}Please enter your email address:\nEmail: {COLORS["red"]}')
            print(f'{COLORS["end"]}')
            clear()
            img = input(f'{COLORS["cyan"]}Please drag and drop the file/image you want to use into the terminal window.\nThen press "enter" to continue...{COLORS["end"]}\n\n{COLORS["red"]}').replace('\\ ', ' ').strip()
            print(f'{COLORS["end"]}')
            clear()


            enc_key = input(f'{COLORS["green"]}Please provide a key for the encryption: {COLORS["end"]}{COLORS["red"]}')
            print(f'{COLORS["end"]}')

            enc_salt = input(f'{COLORS["green"]}Please provide a salt for the encryption: {COLORS["end"]}{COLORS["red"]}')
            print(f'{COLORS["end"]}')
            clear()
            result = img_to_hash(img)
            add_db(email, result, enc_key, enc_salt)
            print(f'{COLORS["green"]}Values added to the database successfully!{COLORS["end"]}\n\n')
            input(f'{COLORS["cyan"]}Press "Enter" to continue...{COLORS["end"]}')
            clear()

        elif options == 3:
            email = input(f'{COLORS["green"]}Please enter your email address:\nEmail: {COLORS["red"]}')
            print(f'{COLORS["end"]}')
            clear()
            img = input(f'{COLORS["cyan"]}Please drag and drop the file/image you want to use into the terminal window.\nThen press "enter" to continue...{COLORS["end"]}\n\n{COLORS["red"]}').replace('\\ ', ' ').strip()
            print(f'{COLORS["end"]}')
            clear()

            enc_key = input(f'{COLORS["green"]}Please provide a key for the encryption: {COLORS["end"]}{COLORS["red"]}')
            print(f'{COLORS["end"]}')

            enc_salt = input(f'{COLORS["green"]}Please provide a salt for the encryption: {COLORS["end"]}{COLORS["red"]}').replace('\\ ', ' ').strip()
            print(f'{COLORS["end"]}')
            clear()


            if verify_hash(email, img, enc_key, enc_salt) == True:
                print(f"{COLORS['green']}Welcome user! You have now logged in!{COLORS['end']}\n\n")
                input(f'{COLORS["cyan"]}Press "Enter" to continue...{COLORS["end"]}')
            else:
                print(f"{COLORS['red']}Error: Incorrect login credentials have been given..please try again.{COLORS['end']}\n\n")
                input(f'{COLORS["green"]}Press "Enter" to continue...{COLORS["end"]}')
            clear()
        elif options == 4:
            quit()
        else:
            print(f'{COLORS["red"]}That is not a valid menu option...{COLORS["end"]}\n\n')
            input(f'{COLORS["green"]}Press "Enter" to continue...{COLORS["end"]}')
            clear()



if __name__ == '__main__':
    COLORS = {"cyan": '\033[1;36;48m', "green": '\033[1;32;48m', "red": '\033[1;31;48m', "end": '\033[0m'}
    main()
