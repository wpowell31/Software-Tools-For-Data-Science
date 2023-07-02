'''Demonstrate recursion.'''
import json


cache: dict[str, list[list[str]]] = dict()

def graph_to_key(dag: dict[str, list[str]], start: str, finish: str) -> str:
    return json.dumps(dag, sort_keys=True) + "," + start + ',' + finish

def find_paths(
    dag: dict[str, list[str]], start: str, finish: str
) -> list[list[str]]:
    '''Find paths through a DAG.'''
    key = graph_to_key(dag, start, finish)

    if key in cache:
        return cache[key]
    
    if start == finish:
        return [[start]]
    paths = []
    for node in dag[start]:
        paths.extend(
            [[start] + path for path in find_paths(dag, node, finish)]
        )

    cache[key] = paths
    return paths

if __name__ == '__main__':
    print('hi')
    print(
        find_paths(
            {'A': ['B', 'C'], 'B': ['D'], 'C': ['D', 'E'], 'D': [], 'E': []},
            'A',
            'E'
        )
    )