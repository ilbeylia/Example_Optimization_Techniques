import numpy as np

def ant_colony(distances, n_ants, n_best, decay, alpha=1, beta=2, n_iterations=100):
    pheromone = np.ones(distances.shape) / len(distances)
    all_inds = np.arange(len(distances))
    best_route = None
    best_route_length = np.inf

    for i in range(n_iterations):
        all_routes = gen_all_routes(n_ants, all_inds, pheromone, alpha, beta, distances)
        move_ants(all_routes, pheromone, distances, n_best, alpha, beta)
        pheromone *= decay
        deposit_pheromone(all_routes, pheromone, distances)

        total_dist, best_route = update_best(all_routes, distances, best_route)
        if total_dist < best_route_length:
            best_route_length = total_dist

    return best_route

def gen_all_routes(n_ants, all_inds, pheromone, alpha, beta, distances):
    all_routes = []
    for i in range(n_ants):
        route = []
        current = np.random.choice(all_inds)
        route.append(current)

        while len(route) < len(all_inds):
            probs = get_transition_prob(current, pheromone, distances, route, alpha, beta)
            next_ind = pick_next_ind(all_inds, probs)
            route.append(next_ind)
            current = next_ind

        all_routes.append(route)
    return all_routes

def move_ants(all_routes, pheromone, distances, n_best, alpha, beta):
    for route in all_routes:
        pheromone_to_add = 1.0 / len(route)
        for i in range(len(route) - 1):
            pheromone[route[i], route[i+1]] += pheromone_to_add
            pheromone[route[i+1], route[i]] += pheromone_to_add

def get_transition_prob(current, pheromone, distances, route, alpha, beta):
    pheromone_row = np.copy(pheromone[current, :])
    pheromone_row[route] = 0

    distances_row = distances[current, :]
    distances_row[route] = 0

    row_prob = pheromone_row ** alpha * (1.0 / (distances_row + 1e-10)) ** beta

    # Kontrol için ekledim
    if np.any(np.isnan(row_prob)):
        return np.ones(len(row_prob)) / len(row_prob)

    norm_row_prob = row_prob / row_prob.sum()
    return norm_row_prob

def pick_next_ind(all_inds, probs):
    return np.random.choice(all_inds, p=probs)

def deposit_pheromone(all_routes, pheromone, distances):
    for route in all_routes:
        pheromone_to_add = 1.0 / len(route)
        for i in range(len(route) - 1):
            pheromone[route[i], route[i+1]] += pheromone_to_add
            pheromone[route[i+1], route[i]] += pheromone_to_add

def update_best(all_routes, distances, best_route):
    total_dist = total_distance(all_routes[0], distances)
    best_route = all_routes[0]

    for route in all_routes[1:]:
        dist = total_distance(route, distances)
        if dist < total_dist:
            total_dist = dist
            best_route = route

    return total_dist, best_route

def total_distance(route, distances):
    total = 0
    for i in range(len(route) - 1):
        total += distances[route[i], route[i+1]]
    return total