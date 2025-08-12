from fastapi import FastAPI
import random
import ctypes

app = FastAPI()
my_library = ctypes.CDLL(r"./calc.so")
my_library.perform_operation.argtypes = [ctypes.c_char]
my_library.perform_operation.restype = ctypes.c_int

@app.get("/initial")
async def add_numbers(number: int):
    res = my_library.init_number(number)
    return {"current number": res}

@app.get("/perform/{operation}")   
async def perform_operation(operation: str):
    if len(operation) == 1 and "r" not in operation:
        res = my_library.perform_operation(operation.encode())
        return {"current number": res}
    elif len(operation) == 1 and "r" in operation:
        res = my_library.perform_operation(operation.encode())
        return {"last operation": chr(res)}
    else:
        return {"Invalid operation - try again"}





