# coding=utf-8

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

    def validar_tipo_datos(self, num1, num2):
        return isinstance(num1, (int, float)) and isinstance(num2, (int, float))
