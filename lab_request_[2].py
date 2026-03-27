import requests
import random

url = "http://127.0.0.1:5000/number/"

# GET 
param = random.randint(1, 10)
response = requests.get(url, params={"param": param})
number1 = response.json()["result"]
operation1 = response.json()["operation"]
random_num1 = response.json()["random_number"]
print(f"GET: param={param}, random_num={random_num1}, result={number1}, operation={operation1}")

# POST 
json_param = random.randint(1, 10)
response = requests.post(
    url,
    headers={"Content-Type": "application/json"},
    json={"jsonParam": json_param}
)
number2 = response.json()["result"]
operation2 = response.json()["operation"]
random_num2 = response.json()["random_number"]
print(f"POST: jsonParam={json_param}, random_num={random_num2}, result={number2}, operation={operation2}")

# DELETE 
response = requests.delete(url)
number3 = response.json()["number"]
operation3 = response.json()["operation"]
print(f"DELETE: number={number3}, operation={operation3}")


result = number1

# Операция GET
if operation1 == "sum":
    result = result + number1
elif operation1 == "sub":
    result = result - number1
elif operation1 == "mul":
    result = result * number1
elif operation1 == "div":
    result = result / number1

# Операция POST
if operation2 == "sum":
    result = result + number2
elif operation2 == "sub":
    result = result - number2
elif operation2 == "mul":
    result = result * number2
elif operation2 == "div":
    result = result / number2

# Операция DELETE
if operation3 == "sum":
    result = result + number3
elif operation3 == "sub":
    result = result - number3
elif operation3 == "mul":
    result = result * number3
elif operation3 == "div":
    result = result / number3

print(f"Ответ: {int(result)}")