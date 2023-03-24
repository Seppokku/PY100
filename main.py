place_dist = [["home-work", 15],
              ["work-park", 8],
              ["home-park", 2],
              ["home-store", 1],
              ["work-store", 14],
              ["park-store", 1]]

t = 0.32
for i in range(len(place_dist)):
    print(f'Добраться из по маршруту {place_dist[i][0]} стоит {place_dist[i][1] * t}')

# посчитать сколько стоит добраться из одной точки в другую