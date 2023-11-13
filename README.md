# Solving Travelling Salesman Problem Using Evolutionary Algorithm (EA)

### Project description
This program implements a Evolutionary Algorithm (EA) to solve the Traveling Salesman Problem (TSP),
a classic problem in combinatorial optimization. The goal is to find the shortest possible route 
that visits a set of cities and returns to the origin city. Our EA approach uses a combination 
of selection, crossover, and mutation strategies to evolve a population of potential solutions 
towards the optimal route.

### Folder Structure
```commandline
.
├── Classes
│   ├── Crossover.py
│   ├── Fitness.py
│   ├── Mutation.py
│   ├── Population.py
│   ├── TournamentSelection.py
│   └── __init__.py
├── README.md
├── data
│   ├── brazil58.xml
│   └── burma14.xml
├── ea.py
├── experiments
│   ├── brazil
│   └── burma
├── main.py
├── requirements.txt
└── utils.py

```

#### Description of the Structure

- **Classes**: Contains the core modules of the EA:
  - `Crossover.py`: Handles the crossover operation in EA.
  - `Fitness.py`: Calculates the fitness of each solution.
  - `Mutation.py`: Manages mutation operations.
  - `Population.py`: Manages the population of solutions.
  - `TournamentSelection.py`: Implements the tournament selection process.
  - `__init__.py`: Marks the directory as a Python package.

- **data**: Stores data files for the TSP instances (`brazil58.xml`, `burma14.xml`).

- **ea.py**: A script related to the evolutionary algorithm components of the EA.

- **experiments**: Contains folders (`brazil`, `burma`) for storing experiment-specific configurations and results.
For each of these folder, there are sub-folders `group-Nth` contains data for 10 trials with a 
specified group of parameters. Each `group-Nth` folder will have:
  - 10 convergence curve `png` files represent 10 trials.
  - 1 `parameters.txt` file contains parameters settings for that trial.
  - 1 `trials_log.csv` file contains the results after 10 trials.

- **main.py**: The entry point of the program.

- **requirements.txt**: Lists the Python package dependencies.

- **utils.py**: Includes utility functions used across the project.

### Features

- **Flexible EA Parameters**: Allows customization of key EA parameters such as population size, mutation rate, crossover rate, and selection mechanism.
- **Selection Mechanism**: Implements a tournament selection method to choose parents for the next generation.
- **Crossover Strategies**: Supports single-point and multi-points crossover, enabling the mixing of parent routes to produce offspring.
- **Mutation Techniques**: Incorporates a swap and multi-swap mutation method, which helps to maintain diversity in the population and explore the solution space effectively.
- **Fitness Evaluation**: Uses a specialized fitness function to evaluate the total distance of a route, guiding the selection of superior solutions.
- **Convergence Tracking**: Monitors the algorithm's progress over generations, tracking improvements in solution quality.

### Setup & Installations

##### Python Version:
- Python 3.xx

You need to activate the virtual environment and install all the necessary packages:

##### To activate the virtual environment:

On Window machines (Command Prompt):
```commandline
venv\Scripts\activate.bat
```
On MacOS machines:
```commandline
source venv/bin/activate
```

##### Install packages:
```commandline
pip install -r requirements.txt
```

### Running the program

To run the EA for solving a TSP instance:
```commandline
python main.py
```

### Author

An Nguyen

