class StringCalculator:
    """
    String calculator base class
    """

    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        num_list = list(map(int, numbers.split(",")))
        return sum(num_list)
