# CalcReplay

make so:
gcc -c -fPIC calc.c -o calc.o
gcc -shared -o calc.so calc.o

enter to venv:
py -m venv .venv
.venv\Scripts\activate