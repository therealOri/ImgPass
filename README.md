# ImgPass
A proof of concept involving using images or files as a "password" to login or register. No more needing to remmber long and complicated passwords. all you need and an image or a file. 

For an image it can be anything you take with your camera. **THAT ISN'T POSTED TO THE INTERNET**. Basically DON'T use public images from the interent. Alternatively, you can digitally alter the image and change the pixels and then voilà, the image will have its own unique hash value that doesn't match any other image on the interent. 

Same can go for files, write whatever you want in said file, have the files name be whatever, etc. It will have a unique hash value that doesn't match anything else. I would personally use a pgp/gpg key file/signature. But anything will be fine.
__ __

<br />
<br />

# About
ImgPass allows you to drag and drop and image or file into the terminal window to then be turned into a blake2b hash value. That hash value then gets encrypted and stored away into a sqlite3 database (along with an email). I have added ways to make it seem more "realistic" to how you would login or register an account.

You will be asked some questions, you can store or write down what you use. Perhaps in a password manager that allows you to make notes. Regardless, it's up to you to decide how you store your information.

<br />
<br />

![image](https://user-images.githubusercontent.com/45724082/157733323-8ed98e8e-382f-443d-b696-79cb6de42054.png)
__ __

<br />
<br />

# Support
> Coming soon.. <3
