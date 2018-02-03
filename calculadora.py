#!/usr/bin/python3

import sys

"""
____________________________ Calculadora.py ____________________________

   Make a Python script that works as a calculator and computes simple
   operations (sum, substraction, multiplication and division).

   The program must be able to execute as:
      python calculadora.py <operation> <operand1> <operand2>

   Don't forget to catch all possible exceptions
________________________________________________________________________

Author: Ainhoa Garcia-Ruiz Fuentes.       Date: 24/01/2018
Course: Servicios y Aplicaciones en Redes de Ordenadores.

"""

sumList = ["suma", "mas", "sum", "add", "+"]
subList = ["resta", "menos", "minus", "sub", "-"]
mulList = ["mul", "multiplica", "multiply", "*"]
divList = ["div", "divide", "/"]


# Get the parameters.
if (len(sys.argv) == 4):
   op = sys.argv[1]
   try:
      op1 = float(sys.argv[2])
      op2 = float(sys.argv[3])
   except ValueError:
      print("[ERROR: ] Operands must be numbers.")
      exit()

else:
   print("[USAGE: ] python calculadora.py <operation> <operand1> <operand2>")
   exit()

# Compute the operation.
if op in sumList:
   result = op1 + op2
   opSym = "+"
elif op in subList:
   result = op1 - op2
   opSym = "-"
elif op in mulList:
   result = op1 * op2
   opSym = "*"
elif op in divList:
   result = op1 / op2
   opSym = "/"
else:
   print("[ERROR: ] Operation not included.")
   exit()

# Display result.
print('[RESULT: ] ' + str(op1) + ' ' + opSym + ' ' + str(op2) + ' = ' + str(result))
exit()

