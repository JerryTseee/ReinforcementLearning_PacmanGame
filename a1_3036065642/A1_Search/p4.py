import sys, parse, grader
from heapq import heappush, heappop

def astar_search(problem):
    #Your p5 code here
    start = problem["start"]
    goal = problem["goal"]
    graph = problem["graph"]
    h = problem["heuristic_value"]
    solution = []
    frontier = []
    heappush(frontier, (h[start], [start])) # at the beginnig, only heuristic value
    explored_set = set()
    
    while frontier:
        node = heappop(frontier)
        if node[1][-1] == goal:
            solution = " ".join(solution) + "\n" + " ".join(node[1])
            return solution
        if node[1][-1] not in explored_set:
            explored_set.add(node[1][-1])
            solution.append(node[1][-1])
            for i in graph[node[1][-1]]:
                heappush(frontier, (node[0] + i[0] + h[i[1]] - h[node[1][-1]], node[1] + [i[1]]))


if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 4
    grader.grade(problem_id, test_case_id, astar_search, parse.read_graph_search_problem)