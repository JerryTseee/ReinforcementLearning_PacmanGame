import sys, parse, grader
from heapq import heappush, heappop

def greedy_search(problem):
    #Your p4 code here
    start = problem["start"]
    goal = problem["goal"]
    graph = problem["graph"]
    h = problem["heuristic_value"]
    frontier = []
    heappush(frontier, (h[start], [start]))

    exploredSet = set()
    solution = []

    while frontier:
        node = heappop(frontier)
        if node[1][-1] == goal:
            solution = " ".join(solution) + "\n" + " ".join(node[1])
            return solution
        if node[1][-1] not in exploredSet:
            exploredSet.add(node[1][-1])
            solution.append(node[1][-1])
            for i in graph[node[1][-1]]:
                heappush(frontier, (h[i[1]], node[1] + [i[1]]))

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 3
    grader.grade(problem_id, test_case_id, greedy_search, parse.read_graph_search_problem)