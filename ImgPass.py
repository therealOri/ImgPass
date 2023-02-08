import hashlib as hsh
import os
import sys
import base64 as b64
import sqlite3
import json
import beaupy
import gcm







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




def verify_hash(email, img, enc_key):
    img_result = img_to_hash(img)

    database = sqlite3.connect('accounts.hshes')
    c = database.cursor()
    c.execute(f"SELECT hash FROM logins WHERE email LIKE '{email}'")
    if h := c.fetchone():
        enc_hash = gcm.stringD(dcr_data=h[0], key=enc_key)
        return enc_hash == img_result
    else:
        clear()
        msg = "No account with the provided email exists."
        raise ValueError(msg) from None



def add_db(email, img_hash, enc_key):
    enc_hash = gcm.stringE(enc_data=img_hash, key=enc_key)
    database = sqlite3.connect('accounts.hshes')
    c = database.cursor()

    c.execute(f"INSERT INTO logins VALUES ('{email}', '{enc_hash}')")
    database.commit()
    database.close()
        



def main():
    while True:
        clear()
        options = ['Generate a key?', 'Check hash of a file?', 'Register?', 'Login?', 'Quit?']
        print(f'{COLORS["cyan"]}{banner()}\n\n\n\nWhat do you want to do today?\n')
        print(f'{COLORS["end"]}')
        option = beaupy.select(options, cursor_style="#ffa533")

        if not option:
            clear()
            sys.exit("Keyboard Interuption Detected!\nGoodbye <3")


        if options[0] in option:
            clear()
            m_gen = beaupy.prompt('(It is reccomended to use genter (my password generator) to make the password)\nPress "q" or "ctrl+c" to go back/exit.\n\nPassword to generate master_key - (100+ characters long.): ', secure=True)
            if not m_gen or m_gen.lower() == 'q':
                clear()
            else:
                m_gen = bytes(m_gen, 'unicode-escape')
                m_key = gcm.keygen(m_gen)
                if not m_key:
                    clear()
                    continue
                b64_mKey = b64.b64encode(m_key)
                print(f'If you have made this key to encrypt your data...DO NOT LOSE THIS KEY. If you lose this key, you can not recover your passwords or change encrypted data.\nThis key will be used when encrypting & decrypting passwords.\n\n\nKey: {b64_mKey.decode()}\n\n')
                input('Press "enter" to continue...')
                clear()


        clear()
        if options[1] in option:
            img = input(f'{COLORS["cyan"]}Please drag and drop the file/image you want to use into the terminal window.\nThen press "enter" to continue...{COLORS["end"]}\n\n{COLORS["red"]}').replace('\\ ', ' ').strip()
            clear()
            result = img_to_hash(img)
            print(f'{COLORS["green"]}Here is your hash! - (blake2b): {COLORS["end"]}{COLORS["red"]}{result}{COLORS["end"]}\n\n')
            input(f'{COLORS["cyan"]}Press "Enter" to continue...{COLORS["end"]}')
            clear()



        if options[2] in option:
            email = input(f'{COLORS["green"]}Please enter your email address:\nEmail: {COLORS["red"]}')
            print(f'{COLORS["end"]}')
            clear()
            img = input(f'{COLORS["cyan"]}Please drag and drop the file/image you want to use into the terminal window.\nThen press "enter" to continue...{COLORS["end"]}\n\n{COLORS["red"]}').replace('\\ ', ' ').strip()
            print(f'{COLORS["end"]}')
            clear()

            enc_key = input(f'{COLORS["green"]}Please provide a key for the encryption: {COLORS["end"]}{COLORS["red"]}')
            print(f'{COLORS["end"]}')

            clear()
            result = img_to_hash(img)
            result = bytes(result, 'utf-8')
            try:
                enc_key = b64.b64decode(enc_key)
            except Exception as e:
                print("Provided key isn't base64 encoded...\n\n")
                input('Press "enter" to continue...')
                clear()
                continue
            if len(enc_key) < 32 or len(enc_key) > 32:
                clear()
                input(f'Key needs to be 32 characters/bytes long. Current key length: {len(enc_key)}\n\nPress "enter" to continue...')
                clear()
                continue
            else:
                add_db(email, result, enc_key)
                print(f'{COLORS["green"]}Values added to the database successfully!{COLORS["end"]}\n\n')
                input(f'{COLORS["cyan"]}Press "Enter" to continue...{COLORS["end"]}')
                clear()



        if options[3] in option:
            email = input(f'{COLORS["green"]}Please enter your email address:\nEmail: {COLORS["red"]}')
            print(f'{COLORS["end"]}')
            clear()
            img = input(f'{COLORS["cyan"]}Please drag and drop the file/image you want to use into the terminal window.\nThen press "enter" to continue...{COLORS["end"]}\n\n{COLORS["red"]}').replace('\\ ', ' ').strip()
            print(f'{COLORS["end"]}')
            clear()

            enc_key = input(f'{COLORS["green"]}Please provide a key for the encryption: {COLORS["end"]}{COLORS["red"]}')
            print(f'{COLORS["end"]}')

            try:
                enc_key = b64.b64decode(enc_key)
            except Exception as e:
                print("Provided key isn't base64 encoded...\n\n")
                input('Press "enter" to continue...')
                clear()
                continue
            if len(enc_key) < 32 or len(enc_key) > 32:
                clear()
                input(f'Key needs to be 32 characters/bytes long. Current key length: {len(enc_key)}\n\nPress "enter" to continue...')
                clear()
                continue
            else:
                if verify_hash(email, img, enc_key) == True:
                    print(f"{COLORS['green']}Welcome user! You have now logged in!{COLORS['end']}\n\n")
                    input(f'{COLORS["cyan"]}Press "Enter" to continue...{COLORS["end"]}')
                else:
                    print(f"{COLORS['red']}Error: Incorrect login credentials have been given..please try again.{COLORS['end']}\n\n")
                    input(f'{COLORS["green"]}Press "Enter" to continue...{COLORS["end"]}')
                clear()
                continue



        if options[4] in option:
            sys.exit("Goodbye! <3")



if __name__ == '__main__':
    COLORS = {"cyan": '\033[1;36;48m', "green": '\033[1;32;48m', "red": '\033[1;31;48m', "end": '\033[0m'}
    main()



