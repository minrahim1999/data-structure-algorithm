def dfs(data, start, visited=set()):

    # if not visited print it
    if start not in visited:
        print(start, end=" ")

    visited.add(start)

    for i in data[start] - visited:

        # if not visited gi in depth of it
        dfs(data, i, visited)
    return