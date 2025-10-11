def main():
    print("Hello from pr!")


if __name__ == "__main__":
    main()

from math_utils import *
import os
from dotenv import load_dotenv
load_dotenv()
import requests

a = 3
b = 4

result = add(a, b)
result2 = multiply(a, b)

print(f"{a} + {b} = {result}")
print(f"{a} * {b} = {result2}")

api = os.getenv("API_URL")

response = requests.get(api)
print(response.json())
