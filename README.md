# CalcReplay
A FastAPI-based service that utilizes a shared C library (`.so`) for basic calculations.  

## Building the shared library(.so)
```
gcc -c -fPIC calc.c -o calc.o  
gcc -shared -o calc.so calc.o  
```
## run without docker
On linux:
```
python3 -m venv .venv  
source .venv/bin/activate  
fastapi installing:  
pip install "fastapi[standard]"  
uvicorn apiserver:app --reload  
```
Go to - http://127.0.0.1:8000  
## run with docker

Under docker server dir:
```  
docker build -t fastapi-server .  
docker run -p 8000:8000 fastapi-server  
```
Go to - http://127.0.0.1:8000  
