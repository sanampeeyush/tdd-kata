import re


class StringCalculator:
    """
    String calculator base class
    """

    def __init__(self):
        self.call_count = 0

    def get_called_count(self) -> int:
        return self.call_count

    def add(self, numbers: str) -> int:
        self.call_count += 1

        delimiter = ",|\n"
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]

        num_list = [
            int(num) for num in re.split(delimiter, numbers) if int(num) <= 1000
        ]
        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {negatives}")

        return sum(num_list)
