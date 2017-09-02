# Calculadora Doctest

Este repositorio es un primer ejemplo de testing automatizado en python con la
ayuda de 'Doctest'

### Ejecución individual de las pruebas

```
python3 -m doctest -v pruebas_calculadora_suma.txt calculadora.py
python3 -m doctest -v pruebas_calculadora_resta.txt calculadora.py
python3 -m doctest -v pruebas_calculadora_multiplicacion.txt calculadora.py
python3 -m doctest -v pruebas_calculadora_division.txt calculadora.py
python3 -m doctest -v pruebas_calculadora_raiz.txt calculadora.py
python3 -m doctest -v pruebas_calculadora_potencia.txt calculadora.py
```

### Ejecución de todas las pruebas

```
python3 -m doctest -v pruebas_calculadora_*.txt calculadora.py 
```