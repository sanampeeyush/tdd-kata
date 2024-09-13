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

        # Default delimiters are comma and newline
        delimiters = ",|\n"

        # Handle custom delimiters
        if numbers.startswith("//"):
            delimiter_section, numbers = numbers.split("\n", 1)
            delimiters = self.extract_custom_delimiters(delimiter_section)

        # Split the numbers using the detected delimiters
        num_list = re.split(delimiters, numbers)

        # Process the numbers and handle negative numbers and large numbers
        return self.process_numbers(num_list)

    def extract_custom_delimiters(self, delimiter_section: str) -> str:
        # If there are multiple custom delimiters or longer ones
        if delimiter_section.startswith("//["):
            delimiters = re.findall(r"\[(.*?)\]", delimiter_section)
            # Join all delimiters into a single regex pattern (escaping special characters)
            return "|".join(map(re.escape, delimiters))
        else:
            # Single character delimiter
            return re.escape(delimiter_section[2])

    def process_numbers(self, num_list) -> int:
        negatives = []
        total_sum = 0

        for num in num_list:
            if num == "":
                continue
            number = int(num)
            if number < 0:
                negatives.append(number)
            elif number <= 1000:
                total_sum += number

        # Raise exception if there are negative numbers
        if negatives:
            raise ValueError(f"negatives not allowed: {negatives}")

        return total_sum
