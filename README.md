# Simulation of Schelling’s Model of Segregation on Two Agents System

Python simulation of Tomas Schelling's agent-based model that suggested inadvertent behaviour might also contribute to racial and economic segregation. The program enables users to modify different parameters, like factor of tolerance, and to observe state of the matrix after each step of segregation until all agents are satisfied.

## Problem Descriptions

### Task: Simulate Schelling's Model of Segregation

#### Components

- **City Initialization**: Randomly populate the city with two types of agents and empty spaces.
- **Dissatisfaction Check**: Identify dissatisfied agents based on their neighborhood composition.
- **Relocation**: Move dissatisfied agents to available empty spaces.
- **Satisfaction Calculation**: Calculate the overall satisfaction of agents in the city.

### Functions

#### City Initialization (`popuni_grad`)
- **Function**: Initialize the city with agents and empty spaces based on given parameters.
- **Parameters**:
  - `dimenzija_matrice`: Dimension of the city grid.
  - `odnos`: Ratio of the two types of agents.
  - `nenaseljenost`: Proportion of empty spaces.
  - `grad`: The city grid.

#### Dissatisfaction Check (`nadji_selice`)
- **Function**: Identify dissatisfied agents and empty spaces.
- **Parameters**:
  - `matrica`: The city grid.
  - `dimenzija`: Dimension of the city grid.
  - `vidno_polje`: Neighborhood radius.
  - `tolerancija`: Tolerance level of agents.

#### Relocation (`preseli`)
- **Function**: Relocate dissatisfied agents to empty spaces.
- **Parameters**:
  - `matrica`: The city grid.
  - `slobodno`: List of empty spaces.
  - `selice`: List of dissatisfied agents.

#### Iterations (`iteracije`)
- **Function**: Perform multiple iterations of the relocation process and display the city state periodically.
- **Parameters**:
  - `matrica`: The city grid.
  - `broj_generacija`: Number of iterations.
  - `dimenzija`: Dimension of the city grid.
  - `vidno_polje`: Neighborhood radius.
  - `tolerancija`: Tolerance level of agents.

#### Satisfaction Calculation (`zadovoljstvo`)
- **Function**: Calculate the overall satisfaction of agents.
- **Parameters**:
  - `selice`: Number of dissatisfied agents.
  - `dimenzija`: Dimension of the city grid.
  - `prazno`: Number of empty spaces.

## Running the Project
1. Ensure you have the required dependencies installed.
2. Adjust parameters in the script as needed.
3. Run `Schellings_Model_of_Segregation.py` to start the simulation and visualize the results.

## Dependencies
- Python 3.x
- Required libraries: `numpy`, `random`, `matplotlib`, `os`, `statistics`

## Notes
- The model allows varying parameters such as city size, agent ratio, tolerance level, and neighborhood radius.
- The script generates visualizations of the city grid at different stages of the simulation.
- Additional statistical analysis is performed using the `Statistics.py` script.
