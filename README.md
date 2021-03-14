# RSA-encode-with-FastAPI
As a recruitment task for a certain company, I was supposed to create a message encryption and decryption program that was to be implemented on a FastAPI-based server and authorized with BasicAuth.

## 1. Code
At the very beginning, you need to choose a cipher, which we will later convert to a code. As for the general division of ciphers, they can be divided into symmetric and asymmetric. Symmetric keys are based on the operation of a single key that is used to encrypt and decrypt messages. This solution is simpler and easier to hack. I decided to implement an asymmetric cipher, namely the RSA cipher. It is based on the operation of a one-way function, i.e. it is easy to encrypt a message, while decryption is much more difficult (longer).
more details can be found here (english):
- https://www.youtube.com/watch?v=nXL5FG7u5s4&t=2s 

## 2. FastAPI
First, install the library which contains FastAPI technology. Remember to be in the design directory during installation:

$ pip install virtualenv
$ python -m venv env
$ (optional) source env/Scripts/activate
$ pip install fastapi
$ python -m pip install --upgrade pip
$ pip install uvicorn 
$ uvicorn main:app --reload
