# CalcReplay

make .so:
gcc -c -fPIC calc.c -o calc.o
gcc -shared -o calc.so calc.o

run without docker:
py -m venv .venv
.venv\Scripts\activate
fastapi installing:
pip install "fastapi[standard]"
univcorn replay:app --reload

run with docker:
under docker server dir:\n
docker build -t fastapi-server .
docker run -p 8000:8000 fastapi-server
http://127.0.0.1:8000