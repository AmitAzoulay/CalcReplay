# CalcReplay

A FastAPI-based service that utilizes a shared C library (`.so`) for basic calculations.
---

## Building the shared library(.so)

gcc -c -fPIC calc.c -o calc.o
gcc -shared -o calc.so calc.o

## run without docker
py -m venv .venv
.venv\Scripts\activate
fastapi installing:
pip install "fastapi[standard]"
univcorn replay:app --reload

## run with docker
Under docker server dir:\n
docker build -t fastapi-server .
docker run -p 8000:8000 fastapi-server
Go to - http://127.0.0.1:8000