def find_paths(
    dag: dict[str, list[str]], start: str, finish: str
) -> list[list[str]]:
    if start == finish:
        return [[start]]
    paths = []
    for node in dag[start]:
        paths.extend(
            [[start] + path for path in find_paths(dag, node, finish)]
        )
    return paths

if __name__ == '__main__':
    print()