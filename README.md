# ImgPass
A proof of concept involving using images or files as a "password" to login or register. No more needing to remember long and complicated passwords. all you need is an image or a file.

For an image it can be anything you take with your camera. **THAT ISN'T POSTED TO THE INTERNET**. Basically DON'T use public images from the internet. Alternatively, you can digitally alter the image and change the pixels and then voilà, the image will have its own unique hash value that doesn't match any other image on the interent. 

Same can go for files, write whatever you want in said file, have the files name be whatever, etc. It will have a unique hash value that doesn't match anything else. I would personally use a pgp/gpg key file/signature. But anything will be fine.
__ __

<br />
<br />

# About
ImgPass allows you to drag and drop an image or file into the terminal window to then be turned into a blake2b hash value. That hash value then gets encrypted and stored away into a sqlite3 database (along with an email). I have added ways to make it seem more "realistic" to how you would login or register an account.

You will be asked some questions, you can store or write down what you use. Perhaps in a password manager that allows you to make notes. Regardless, it's up to you to decide how you store your information.

Basically the same way you'd take the data of a password/string of text and hash it and then encrypt and store it is being done with an image instead. We take the data/bytes of the image or file, hash that instead and then encrypt and store. We then would have some way to compare and verify the hashes made and stored. (whatever method you so choose) and go from there.
__ __

<br />
<br />

![main_menu](https://user-images.githubusercontent.com/45724082/201742745-1fb448b1-3d97-44ab-acd2-920ad84dda77.png)

Links & Resources
* [Genter](https://github.com/therealOri/Genter)
> For password generation to be used in Keys for the encryption.
__ __

<br />
<br />


# Support  |  Buy me a coffee <3
Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)
