# CalcReplay

make so:
gcc -c -fPIC calc.c -o calc.o
gcc -shared -o calc.so calc.o

enter to venv
-------------
windows:
py -m venv .venv
.venv\Scripts\activate
linux:
python3 -m venv .venv
source .venv/bin/activate
