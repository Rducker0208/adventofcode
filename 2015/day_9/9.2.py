raw_routes = open('main.txt').readlines()

longest_distance = 0
longest_route = None

destinations = {}
routes = []


for line in raw_routes:
    origin, _, destination, _, length = line.strip().split()

    if origin not in destinations.keys():
        destinations[origin] = {}

    if destination not in destinations.keys():
        destinations[destination] = {}

    if destination not in destinations[origin].keys():
        destinations[origin][destination] = length

    if origin not in destinations[destination].keys():
        destinations[destination][origin] = length

routes.extend(destinations.keys())

for i in range(len(destinations.keys()) - 1):
    new_routes = []

    for route in routes:
        current_location = route.split()[-1]

        for destination in destinations[current_location].keys():
            if destination not in route.split():
                new_routes.append(f'{route} -> {destination}')

    routes = new_routes

for route in routes:
    total_distance = 0
    path = route.split(' -> ')

    for index, city in enumerate(path[:-1]):
        total_distance += int(destinations[city][path[index + 1]])

    if total_distance > longest_distance:
        longest_route = route
        longest_distance = total_distance

print(f'longest route: {longest_route}\n'
      f'longest distance: {longest_distance}')

