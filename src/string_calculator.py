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
            delimiter_section, numbers = numbers[2:].split("\n", 1)
            delimiter = "|".join(
                re.escape(delim)
                for delim in re.findall(r"\[([^\]]+)\]", delimiter_section)
            )

        num_list = [
            int(num) for num in re.split(delimiter, numbers) if int(num) <= 1000
        ]
        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {negatives}")

        return sum(num_list)
