# coding=utf-8
import math


class Calculadora:
    def sumar(self, num1, num2):
        if self.validar_tipo_datos(num1, num2):
            return num1 + num2
        else:
            return 'Datos inválidos'

    def restar(self, num1, num2):
        if self.validar_tipo_datos(num1, num2):
            return num1 - num2
        else:
            return 'Datos inválidos'

    def multiplicar(self, num1, num2):
        if self.validar_tipo_datos(num1, num2):
            return num1 * num2
        else:
            return 'Datos inválidos'

    def dividir(self, num1, num2):
        if self.validar_tipo_datos(num1, num2):
            try:
                return num1 / num2
            except ZeroDivisionError:
                return 'No se permiten divisiones entre 0'
        else:
            return 'Datos inválidos'

    def raiz(self, num):
        if self.validar_tipo_datos(num):
            try:
                return math.sqrt(num)
            except ValueError:
                return 'No se permiten números negativos'
        else:
            return 'Datos inválidos'

    def potencia(self, num1, potencia):
        if self.validar_tipo_datos(num1, potencia):
            return num1 ** potencia
        else:
            return 'Datos inválidos'

    def validar_tipo_datos(self, num1, num2=0):
        return isinstance(num1, (int, float)) and isinstance(num2, (int, float))
