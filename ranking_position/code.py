def ranking(people):
    people = sorted(sorted(people, key=lambda x: x['name']), key=lambda x: x['points'], reverse=True)
    points, position = people[0]['points'] if people else 0, 1
    for i, person in enumerate(people):
        if person['points'] < points:
            position = i + 1
        person['position'] = position
        points = person['points']
    return people
