from fastapi import FastAPI
import httpx

app = FastAPI()

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
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n #return boolean value

def digit_sum(n):
    """Return the sum of the digits of a number."""
    return sum(int(digit) for digit in str(n))

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
        return {
            "number": number,
            "error": True
        }

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
