def bfs(data, start, visited=set()):

    queue = [start]

    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print(current_node, end=" ")
        visited.add(current_node)

        for i in data[current_node] - visited:
            queue.append(i)
    return