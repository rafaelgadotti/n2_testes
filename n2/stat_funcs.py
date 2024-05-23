import statistics
import numpy as np
from collections import Counter
import scipy
import pytest

class StatsN2:

    @staticmethod
    def media(lista) -> float:
        """
        Calcula a média aritmética de uma lista de números.

        Args:
            lista (list): Uma lista de números.

        Returns:
            float: A média aritmética dos números na lista.
        """
        if not lista:
            return 0
        return sum(lista) / len(lista)

    @staticmethod
    def media_ponderada(lista, pesos) -> float:
        """
        Calcula a média ponderada de uma lista de números.

        Args:
            lista (list): Uma lista de números.
            pesos (list): Uma lista de pesos correspondentes aos números.

        Returns:
            float: A média ponderada dos números na lista.
        """
        return np.average(lista, weights=pesos)

    @staticmethod
    def mediana(lista) -> float:
        """
        Calcula a mediana de uma lista de números.

        Args:
            lista (list): Uma lista de números.

        Returns:
            float: A mediana dos números na lista.
        """
        n = len(lista)
        if n == 0:
            return 0
        if n % 2:
            median_ = sorted(lista)[round(0.5*(n - 1))]
        else:
            x_ord, index = sorted(lista), round(0.5 * n)
            median_ = 0.5 * (x_ord[index - 1] + x_ord[index])
        return median_

    @staticmethod
    def unimodal(lista):
        """
        Verifica se uma lista de números é unimodal.

        Args:
            lista (list): Uma lista de números.

        Returns:
            str: "Não é unimodal" se a lista não é unimodal, caso contrário, retorna a moda.
        """
        counts = Counter(lista)
        max_count = max(counts.values())
        modas = [num for num, count in counts.items() if count == max_count]
        if len(modas) == 1:
            return modas[0]
        else:
            return "Não é unimodal"

    @staticmethod
    def multimodal(lista):
        """
        Verifica se uma lista de números é multimodal.

        Args:
            lista (list): Uma lista de números.

        Returns:
            str: "Não é multimodal" se a lista não é multimodal, caso contrário, retorna as modas.
        """
        counts = Counter(lista)
        max_count = max(counts.values())
        modas = [num for num, count in counts.items() if count == max_count]
        if len(modas) > 1:
            return modas
        else:
            return "Não é multimodal"

    @staticmethod
    def amodal(lista):
        """
        Verifica se uma lista de números é amodal.

        Args:
            lista (list): Uma lista de números.

        Returns:
            str: "Não existe moda" se a lista não possui moda, caso contrário, retorna "Existe moda".
        """
        counts = Counter(lista)
        if all(count == 1 for count in counts.values()):
            return "Não existe moda"
        else:
            return "Existe moda"

    @staticmethod
    def variancia(lista) -> float:
        """
        Calcula a variância de uma lista de números.

        Args:
            lista (list): Uma lista de números.

        Returns:
            float: A variância dos números na lista.
        """
        n = len(lista)
        media_ = sum(lista) / n
        var_ = sum((item - media_)**2 for item in lista) / (n - 1)
        return var_

    @staticmethod
    def dpadrao(var) -> float:
        """
        Calcula o desvio padrão a partir da variância.

        Args:
            var (float): A variância dos números.

        Returns:
            float: O desvio padrão dos números.
        """
        return var ** 0.5

    @staticmethod
    def skew(lista) -> float:
        """
        Calcula a assimetria de uma lista de números.

        Args:
            lista (list): Uma lista de números.

        Returns:
            float: A assimetria dos números na lista.
        """
        y = np.array(lista)
        skewness = scipy.stats.skew(y, bias=False)
        return skewness
