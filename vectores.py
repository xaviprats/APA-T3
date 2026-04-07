"""
Tercera tarea de APA: Multiplicación de vectores y ortogonalidad

Nombre y apellidos: Xavi Prats Castillo

Tests unitarios
===============

>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2, 4, 6])
>>> v1 * v2
Vector([4, 10, 18])
>>> 2 * v1
Vector([2, 4, 6])
>>> v1 @ v2
32

>>> v1 = Vector([2, 1, 2])
>>> v2 = Vector([0.5, 1, 0.5])
>>> v1 // v2
Vector([1.0, 2.0, 1.0])
>>> v1 % v2
Vector([1.0, -1.0, 1.0])
>>> v1 // v2 + v1 % v2
Vector([2.0, 1.0, 2.0])
"""

import doctest


class Vector:
    """
    Representa un vector y permite realizar operaciones básicas entre vectores.
    """

    def __init__(self, componentes):
        """
        Construye un vector a partir de una secuencia de componentes.

        Argumentos:
            componentes (iterable): Secuencia de números.

        Salida:
            Vector: Nuevo vector con las componentes indicadas.
        """
        self.componentes = list(componentes)

    def __repr__(self):
        """
        Devuelve la representación formal del vector.

        Argumentos:
            Ninguno.

        Salida:
            str: Cadena con formato Vector([...]).
        """
        return f"Vector({self.componentes})"

    def __eq__(self, other):
        """
        Comprueba si dos vectores son iguales componente a componente.

        Argumentos:
            other (Vector): Vector con el que comparar.

        Salida:
            bool: True si ambos vectores son iguales y False en caso contrario.
        """
        if not isinstance(other, Vector):
            return False
        return self.componentes == other.componentes

    def __len__(self):
        """
        Devuelve la dimensión del vector.

        Argumentos:
            Ninguno.

        Salida:
            int: Número de componentes del vector.
        """
        return len(self.componentes)

    def __add__(self, other):
        """
        Suma dos vectores componente a componente.

        Argumentos:
            other (Vector): Vector que se desea sumar.

        Salida:
            Vector: Vector suma.

        Excepciones:
            TypeError: Si other no es un Vector.
            ValueError: Si los vectores no tienen la misma dimensión.
        """
        if not isinstance(other, Vector):
            raise TypeError("La suma solo puede realizarse entre vectores.")
        if len(self) != len(other):
            raise ValueError("Los vectores deben tener la misma dimensión.")
        return Vector(
            [a + b for a, b in zip(self.componentes, other.componentes)]
        )

    def __sub__(self, other):
        """
        Resta dos vectores componente a componente.

        Argumentos:
            other (Vector): Vector que se desea restar.

        Salida:
            Vector: Vector diferencia.

        Excepciones:
            TypeError: Si other no es un Vector.
            ValueError: Si los vectores no tienen la misma dimensión.
        """
        if not isinstance(other, Vector):
            raise TypeError("La resta solo puede realizarse entre vectores.")
        if len(self) != len(other):
            raise ValueError("Los vectores deben tener la misma dimensión.")
        return Vector(
            [a - b for a, b in zip(self.componentes, other.componentes)]
        )

    def __mul__(self, other):
        """
        Multiplica un vector por un escalar o calcula el producto de Hadamard.

        Argumentos:
            other (int, float o Vector): Escalar o vector.

        Salida:
            Vector: Resultado de la multiplicación.

        Excepciones:
            TypeError: Si other no es un número ni un Vector.
            ValueError: Si other es un Vector de distinta dimensión.
        """
        if isinstance(other, (int, float)):
            return Vector([x * other for x in self.componentes])

        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Los vectores deben tener la misma dimensión.")
            return Vector(
                [a * b for a, b in zip(self.componentes, other.componentes)]
            )

        raise TypeError(
            "La multiplicación requiere un escalar o un vector compatible."
        )

    def __rmul__(self, other):
        """
        Permite multiplicar un escalar por un vector.

        Argumentos:
            other (int o float): Escalar.

        Salida:
            Vector: Resultado de la multiplicación.
        """
        return self * other

    def __matmul__(self, other):
        """
        Calcula el producto escalar de dos vectores.

        Argumentos:
            other (Vector): Vector con el que realizar el producto escalar.

        Salida:
            int o float: Producto escalar.

        Excepciones:
            TypeError: Si other no es un Vector.
            ValueError: Si los vectores no tienen la misma dimensión.
        """
        if not isinstance(other, Vector):
            raise TypeError("El producto escalar solo puede realizarse entre vectores.")
        if len(self) != len(other):
            raise ValueError("Los vectores deben tener la misma dimensión.")
        return sum(a * b for a, b in zip(self.componentes, other.componentes))

    def __rmatmul__(self, other):
        """
        Permite calcular el producto escalar en el caso reflejado.

        Argumentos:
            other (Vector): Vector situado a la izquierda del operador.

        Salida:
            int o float: Producto escalar.
        """
        return other @ self

    def __floordiv__(self, other):
        """
        Devuelve la componente paralela de un vector respecto a otro.

        Argumentos:
            other (Vector): Vector respecto al cual se proyecta.

        Salida:
            Vector: Componente tangencial o paralela.

        Excepciones:
            TypeError: Si other no es un Vector.
            ValueError: Si los vectores no tienen la misma dimensión o si other
            es el vector nulo.
        """
        if not isinstance(other, Vector):
            raise TypeError("La proyección paralela requiere otro vector.")
        if len(self) != len(other):
            raise ValueError("Los vectores deben tener la misma dimensión.")

        norma_cuadrada = other @ other
        if norma_cuadrada == 0:
            raise ValueError("No se puede proyectar sobre el vector nulo.")

        escalar = (self @ other) / norma_cuadrada
        return other * escalar

    def __mod__(self, other):
        """
        Devuelve la componente perpendicular de un vector respecto a otro.

        Argumentos:
            other (Vector): Vector respecto al cual se descompone.

        Salida:
            Vector: Componente normal o perpendicular.

        Excepciones:
            TypeError: Si other no es un Vector.
            ValueError: Si los vectores no tienen la misma dimensión o si other
            es el vector nulo.
        """
        return self - (self // other)


if __name__ == "__main__":
    doctest.testmod(verbose=True)