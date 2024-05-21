from scipy.linalg import pascal


class PascalService():
    def get_matrix(self, size: int):
        return pascal(size, kind='lower')

    def get_line(self, number: int):
        return pascal(number, kind='lower')[-1]
