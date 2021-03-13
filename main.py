import secrets
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

first_prime_number = 397
second_prime_number = 401
multiplication_of_prime_numbers = first_prime_number * second_prime_number
breakability_of_number = (first_prime_number-1) * (second_prime_number - 1)
e = 7  # Low public index e, which has to be odd number, hasn't got common divisor with breakability_of_number
k = 5  # number which makes if private key will be integer
#       private_key = (((k*breakability_of_number)+1)/e) ; In our case private key equal 113143

app = FastAPI()

security = HTTPBasic()


class Word(BaseModel):
    contents: str


class Code(BaseModel):
    private_key: int
    coding_sentense: list


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "zadanie")
    correct_password = secrets.compare_digest(credentials.password, "domowe")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    # return credentials.username


@app.get('/')
async def hello_world():
    return {"Hello":"World"}


@app.post('/coding')
async def words_coding_post(word: Word, secure: str = Depends(get_current_username)):
    array_for_code = []
    for character in word.contents:
        array_for_code.append((ord(character) ** e) % multiplication_of_prime_numbers)
    return array_for_code


@app.post('/decoding')
async def words_decoding_post(code: Code, secure: str = Depends(get_current_username)):
    decoding_word = ''
    array = code.coding_sentense
    for value in array:
        decoding_word = decoding_word + chr((int(value) ** code.private_key) % multiplication_of_prime_numbers)
    return decoding_word

