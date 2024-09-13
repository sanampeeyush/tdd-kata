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

        if numbers == "":
            return 0

        delimiter = ",|\n"

        # Check if custom delimiters are present
        if numbers.startswith("//"):
            delimiter_section, numbers = numbers[2:].split("\n", 1)
            delimiter = "|".join(
                re.escape(delim)
                for delim in re.findall(r"\[([^\]]+)\]", delimiter_section)
            )

        # Split the numbers using the detected delimiters
        num_list = [
            int(num)
            for num in re.split(delimiter, numbers)
            if num != "" and int(num) <= 1000
        ]

        # Detect negative numbers and raise an exception if present
        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {negatives}")

        return sum(num_list)
