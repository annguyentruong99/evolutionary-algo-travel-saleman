import os
import xmltodict
import numpy as np


def read_xml(country: str) -> list:
    """
    Function to read the XML file
    :param country: str
    :return: data: list
    """
    if country == 'brazil':
        with open('data/brazil58.xml') as brazil_file:
            data = xmltodict.parse(brazil_file.read())
    else:
        with open('data/burma14.xml') as burma_file:
            data = xmltodict.parse(burma_file.read())
    return data['travellingSalesmanProblemInstance']['graph']['vertex']


def prompt_input(options: list, input_message: str) -> str:
    """
    Function to prompt user to give input based on given options
    :param options: list
    :param input_message: str
    :return: user_input: str
    """
    # Display the main prompt and options
    print(input_message)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Get user's choice
    while True:
        try:
            choice = int(input("Enter your choice (number): "))
            if 1 <= choice <= len(options):
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Please enter a number.")

    chosen_option = options[choice - 1]

    return chosen_option


def prompt_multi_input(options: list, input_message: str, additional_input=None):
    """
        General utility function to get user input with specified options.
        If additional_input is provided, it will prompt for more input based on the user's choice.

        :param input_message: str
        :param options: list
        :param additional_input: dict
        :return: tuple
        """

    # Display the main prompt and options
    print(input_message)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Get user's choice
    while True:
        try:
            choice = int(input("Enter your choice (number): "))
            if 1 <= choice <= len(options):
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Please enter a number.")

    chosen_option = options[choice - 1]

    # Check if additional input is required for the chosen option
    if additional_input and chosen_option in additional_input:
        additional_prompt = additional_input[chosen_option]
        additional_value = input(additional_prompt)
        return chosen_option, additional_value

    return chosen_option, None


def append_text(filename: str, content: str) -> None:
    """
    Appends content to a file, creating the file's directory path if necessary.

    Parameters:
    - filename: Path to the file for appending content.
    - content: Text to be appended.
    """
    # Ensure the directory exists
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Append the content to the file
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(content + '\n')


def contains_duplicates(array: np.ndarray) -> bool:
    """
    Check if a numpy array contains any duplicates.

    :param array: Numpy array to check for duplicates.
    :return: True if there are duplicates, False otherwise.
    """
    # Convert the array to a set and compare its length to the array's length
    return len(np.unique(array)) != len(array)


def find_duplicate_indexes(array: np.ndarray):
    """
    Find the indexes of a duplicated number in a numpy array.

    :param array: Numpy array to check for a duplicated number.
    :return: The indexes of the duplicated number as two separate numbers.
    """
    seen = {}
    for index, element in enumerate(array):
        if element in seen:
            return seen[element], index
        seen[element] = index
    return None, None
