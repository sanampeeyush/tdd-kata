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

        num_list = re.split(delimiter, numbers)
        return sum(map(int, num_list))
