# RSA-encode-with-FastAPI
As a recruitment task for a certain company, I was supposed to create a message encryption and decryption program that was to be implemented on a FastAPI-based server and authorized with BasicAuth.

## 1. Code
At the very beginning, you need to choose a cipher, which we will later convert to a code. As for the general division of ciphers, they can be divided into symmetric and asymmetric. Symmetric keys are based on the operation of a single key that is used to encrypt and decrypt messages. This solution is simpler and easier to hack. I decided to implement an asymmetric cipher, namely the RSA cipher. It is based on the operation of a one-way function, i.e. it is easy to encrypt a message, while decryption is much more difficult (longer).
more details can be found here (english):
- https://www.youtube.com/watch?v=nXL5FG7u5s4&t=2s 

## 2. FastAPI
First, install the library which contains FastAPI technology. Remember to be in the design directory during installation:

```

$ pip install virtualenv
$ python -m venv env
$ (optional) source env/Scripts/activate
$ pip install fastapi
$ python -m pip install --upgrade pip
$ pip install uvicorn 
$ uvicorn main:app --reload

```

If everything installed and started correctly, we can enter the address http://127.0.0.1:8000 in the browser and our eyes should receive the answer:

```

$ {"Hello":"World"}

```

In the next steps, change the address to http://127.0.0.1:8000/docs. This will make us get to the functions available on the server. In our case, the coding function sends the dictionary to the server in the following form:

```

${
  "contents": "string"
}

```
, where "string" that's our sentence to code.The answer is an array of numbers, where one number corresponds to one character in the sentence.

The second function is decoding, which is used to decode the previously sent message. Here, the body of the transmitted values looks like this:

```

${
  "private_key": 0,
  "coding_sentence": [
    null
  ]
}

```
, where private_key is a previously calculated private key, without which we will not get the correct decoding of the code, while coding_sentence is an array of numbers, returned from the coding function. The result should be the original sentence.

### but earlier..

## 3. BasicAuth
