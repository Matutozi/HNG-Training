from fastapi import FastAPI
import httpx
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"] 
)

def is_prime(n):
    """method that checks if n is prime"""

    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Method to check if a number is perfect"""
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i

    return sum == n

def is_armstrong(n):
    """Method to check if a number is amstrong"""

    if n < 0:
        return False
    
    digits = [int(d) for d in str(abs(n))]
    power = len(digits)
    return sum(d ** power for d in digits) == abs(n) #return boolean value

def digit_sum(n):
    """Return the sum of the digits of a number."""
    return sum(int(digit) for digit in str(abs(n)))

def get_fun_facts(n):
    """method that reads an api based on the value n and returns a response"""
    response = httpx.get(f"http://numbersapi.com/{n}")
    if response.status_code == 200:
        return response.text
    else:
        return "No fun fact Available"

@app.get("/api/classify-number")
def classify_number(number : str):
    try:
        num = int(number)
    except ValueError:
        return JSONResponse (
            status_code = 400,
            content ={
            "number": number,
            "error": True
            }
        )

    properties = []

    if is_armstrong(num):
        properties.append("armstrong")
    
    if num % 2 == 0:
        properties.append("even")

    else:
        properties.append("odd")

    
    
    return {
    "number": num,
    "is_prime": is_prime(num),
    "is_perfect": is_perfect(num),
    "properties": properties,
    "digit_sum": digit_sum(num),
    "fun_fact": get_fun_facts(num)
    }
