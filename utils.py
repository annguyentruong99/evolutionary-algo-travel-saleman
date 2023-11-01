import xmltodict

"""
Function to read the XML file

    Parameters:
        country (str): a string that associates with data file
    Return:
        data (list): a list containing all the vertexes from the data file
"""


def read_xml(country: str) -> list:
    if country == 'brazil':
        with open('data/brazil58.xml') as brazil_file:
            data = xmltodict.parse(brazil_file.read())
    else:
        with open('data/burma14.xml') as burma_file:
            data = xmltodict.parse(burma_file.read())
    return data['travellingSalesmanProblemInstance']['graph']['vertex']


"""
Function to prompt user to give input based on given options

    Parameters:
        options (list): list of option strings
        input_message (str): a string to display to prompt user to input an option
    Return:
         user_input (str): an option from the list of options
"""


def prompt_input(options: list, input_message: str) -> str:
    user_input = ''

    for index, item in enumerate(options):
        input_message += f'{index + 1}) {item.capitalize()}\n'

    input_message += 'Your choice: '

    while user_input.lower() not in options:
        user_input = input(input_message)

    return user_input.lower()


def append_text(filename: str, content: str) -> None:
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(content + '\n')
