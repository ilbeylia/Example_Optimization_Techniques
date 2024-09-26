import numpy as np

def fitness(solution, distances):
    total_distance = 0
    for i in range(len(solution) - 1):
        total_distance += distances[solution[i], solution[i+1]]
    total_distance += distances[solution[-1], solution[0]]  # Başlangıç noktasına dönme için bu ekledim 
    return total_distance

# Simulated Annealing
def simulated_annealing(distances, initial_solution, initial_temperature, cooling_rate):
    current_solution = initial_solution.copy()
    best_solution = current_solution.copy()

    current_temperature = initial_temperature

    while current_temperature > 1:

        new_solution = current_solution.copy()
        swap_indices = np.random.choice(len(new_solution), size=2, replace=False)
        new_solution[swap_indices[0]], new_solution[swap_indices[1]] = new_solution[swap_indices[1]], new_solution[swap_indices[0]]

        current_fitness = fitness(current_solution, distances)
        new_fitness = fitness(new_solution, distances)

        acceptance_probability = min(1, np.exp((current_fitness - new_fitness) / current_temperature))

        if np.random.rand() < acceptance_probability:
            current_solution = new_solution.copy()

        if new_fitness < fitness(best_solution, distances):
            best_solution = new_solution.copy()

        current_temperature *= cooling_rate

    return best_solution