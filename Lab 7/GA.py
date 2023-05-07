from deap import base, creator, tools
import random

# Define the problem parameters
string_length = 30
target_ones = 15
pop_size = 50
max_generations = 1000
mutation_rate = 0.1

# Create the fitness and individual classes using DEAP
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Initialize the toolbox
toolbox = base.Toolbox()

# Define the attributes (i.e., the genes) as binary values
toolbox.register("attr_bool", random.randint, 0, 1)

# Define the individual creation operator
toolbox.register(
    "individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, string_length
)

# Define the population creation operator
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


# Define the evaluation function (i.e., the fitness function)
def evaluate(individual):
    return (sum(individual),)


# Register the evaluation function with the toolbox
toolbox.register("evaluate", evaluate)

# Define the selection operator
toolbox.register("select", tools.selTournament, tournsize=5)

# Define the crossover operator
toolbox.register("mate", tools.cxTwoPoint)

# Define the mutation operator
toolbox.register("mutate", tools.mutFlipBit, indpb=mutation_rate)

# Initialize the population
pop = toolbox.population(n=pop_size)

# Evolution loop
for generation in range(max_generations):
    # Evaluate the fitness of each individual in the population
    fitnesses = map(toolbox.evaluate, pop)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    # Check if a solution has been found
    if target_ones in [ind.fitness.values[0] for ind in pop]:
        solution_index = [ind.fitness.values[0] for ind in pop].index(target_ones)
        print(f"Solution found after {generation} generations: {pop[solution_index]}")
        break

    # Select parents for reproduction
    parents = toolbox.select(pop, 2)

    # Create offspring by crossover
    offspring1, offspring2 = [toolbox.clone(ind) for ind in parents]
    toolbox.mate(offspring1, offspring2)

    # Introduce mutation to the offspring
    toolbox.mutate(offspring1)
    toolbox.mutate(offspring2)

    # Replace the two least fit individuals in the population with the offspring
    offspring_fitnesses = map(toolbox.evaluate, (offspring1, offspring2))
    for ind, fit in zip((offspring1, offspring2), offspring_fitnesses):
        ind.fitness.values = fit

    pop = toolbox.select(pop + [offspring1, offspring2], k=pop_size)

    # Print some status information
    if (generation + 1) % 100 == 0:
        print(
            f"Generation {generation+1}: Max Fitness = {max([ind.fitness.values[0] for ind in pop])}, Mean Fitness = {sum([ind.fitness.values[0] for ind in pop])/pop_size}"
        )
