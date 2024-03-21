import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        """
        Метод для вывода матрицы на печать.
        """
        result = ""
        for row in self.matrix:
            result += " ".join(map(str, row)) + "\n"
        return result

    def __eq__(self, other):
        """
        Метод для сравнения двух матриц.
        """
        return self.matrix == other.matrix

    def __add__(self, other):
        """
        Метод для сложения двух матриц.
        """
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            logging.error(f"Матрицы разных размеров нельзя сложить: {len(self.matrix)}x{len(self.matrix[0])} и {len(other.matrix)}x{len(other.matrix[0])}")
            raise ValueError("Матрицы разных размеров нельзя сложить")

        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        """
        Метод для умножения матриц.
        """
        if len(self.matrix[0]) != len(other.matrix):
            logging.error(f"Нельзя умножить матрицы заданных размеров: {len(self.matrix)}x{len(self.matrix[0])} и {len(other.matrix)}x{len(other.matrix[0])}")
            raise ValueError("Нельзя умножить матрицы заданных размеров")

        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other.matrix[0])):
                element = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                row.append(element)
            result.append(row)
        return Matrix(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Используйте: python matrix.py матрица 1 и матрица 2")
        sys.exit(1)

    try:
        matrix1 = eval(sys.argv[1])
        matrix2 = eval(sys.argv[2])
        m1 = Matrix(matrix1)
        m2 = Matrix(matrix2)
        print("Матрица 1:")
        print(m1)
        print("Матрица 2:")
        print(m2)
        print("Сумма матриц:")
        print(m1 + m2)
        print("Произведение матриц:")
        print(m1 * m2)
    except Exception as e:
        print("Ошибка:", e)
        sys.exit(1)
