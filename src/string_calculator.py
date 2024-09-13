import re


class StringCalculator:
    """
    String calculator base class
    """

    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        delimiter = ",|\n"
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]

        num_list = list(map(int, re.split(delimiter, numbers)))
        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {negatives}")

        return sum(num_list)
