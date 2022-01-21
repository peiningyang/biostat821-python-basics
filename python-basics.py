"""Functions to take filepath and calculate summary statistics."""
import math


# Function that turns file into list of lists of integers
def get_data(file: str) -> list[list[int]]:
    """Take filepath and returns list of lists of integers."""
    # Open file and read into list of lists
    with open(file) as dta:
        nums = [line.strip("\n").split(" ") for line in dta]
    num_list = []
    # Create new lists, converting list entries from string to ints
    for lst in nums:
        num_list.append([int(x) for x in lst])
    return num_list


# Function that calculates various summary statistics given lists of lists
def analyze_data(integers: list[list[int]], option: str) -> float:
    """Calculate summary statistics given list of lists and string option."""
    # Create list that is all entries
    all_numbers = [integer for sublist in integers for integer in sublist]
    if option == "average":
        return average(all_numbers)
    elif option == "standard deviation":
        return standard_deviation(all_numbers)
    elif option == "covariance":
        return covariance(integers)
    else:
        return correlation(integers)


# Average function
def average(integers: list[int]) -> float:
    """Calculate average of a list."""
    return sum(integers) / len(integers)


# Standard deviation function
def standard_deviation(integers: list[int]) -> float:
    """Calculate standard deviation given a list."""
    integer_average = average(integers)
    std = 0.0
    for i in integers:
        std += (i - integer_average) ** 2
        pass
    return math.sqrt(std / len(integers))


# Covariance function
def covariance(integers: list[list[int]]) -> float:
    """Calcualte covariance, given a list of two lists of integers."""
    average_0 = average(integers[0])
    average_1 = average(integers[1])
    n = len(integers[0])
    cov = 0.0
    for i in range(n):
        cov += (integers[0][i] - average_0) * (integers[1][i] - average_1)
        pass
    return cov / n


# Correlation function
def correlation(integers):
    """Calculate correlation given a list of two lists of integers."""
    top = covariance(integers)
    bottom = standard_deviation(integers[0]) * standard_deviation(integers[1])
    return top / bottom


if __name__ == "__main__":
    # Test get_data()
    integers = get_data("example.txt")
    print(integers)

    # Test analyze data function
    print(round(analyze_data(integers, "average"), 1))  # ~21.4
    print(round(analyze_data(integers, "standard deviation"), 1))  # ~22.9
    print(round(analyze_data(integers, "covariance"), 1))  # ~-257
    print(round(analyze_data(integers, "correlation"), 3))  # ~-0.594
