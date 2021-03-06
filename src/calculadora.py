"""Módulo principal"""


class Calculadora():
    """Representa uma calculadora com operações básicas"""

    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def soma(self):
        """Calcula a soma de dois números

        Args:
            num_1 (int): O primeiro número
            num_2 (int): O segundo número

        Returns:
            int: A soma dos dois números
        """
        return self.num_1 + self.num_2

    def subtracao(self):
        """Calcula a subtração de dois números

        Args:
            num_1 (int): O primeiro número
            num_2 (int): O segundo número

        Returns:
            int: A subtração dos dois números
        """
        return self.num_1 - self.num_2

    def multiplicacao(self):
        """Calcula a multiplicação de dois números

        Args:
            num_1 (int): O primeiro número
            num_2 (int): O segundo número

        Returns:
            int: A multiplicação dos dois números
        """
        return self.num_1 * self.num_2

    def divisao(self):
        """Calcula a divisão de dois números

        Args:
            num_1 (int): O primeiro número
            num_2 (int): O segundo número

        Returns:
            int: A divisão dos dois números
        """

        if self.num_1 == 0 or self.num_2 == 0:
            return "Divisão por Zero"

        return self.num_1 / self.num_2


if __name__ == '__main__':
    num1 = int(input('1st number: '))
    num2 = int(input('2nd number: '))

    calc = Calculadora(num1, num2)
    print('Sum: ', calc.soma())
