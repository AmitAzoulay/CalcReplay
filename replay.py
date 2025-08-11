from fastapi import FastAPI
import random
import ctypes

app = FastAPI()




@app.get("/")
async def root():
    my_library = ctypes.CDLL(r"C:\clones\CalcReplay\calc.so")
    my_library.main()
    return {"message": "Hello World"}

@app.get("/add")
async def add_numbers(num1: float, num2: float):
    return {"operation": "addition", "result": num1 + num2}