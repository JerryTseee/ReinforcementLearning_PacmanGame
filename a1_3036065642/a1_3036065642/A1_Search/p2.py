import sys, grader, parse
import collections

def bfs_search(problem):
    #Your p2 code here
    start = problem["start"]
    goal = problem["goal"]
    graph = problem["graph"]
    solution = []
    explored_set = set()
    frontier = collections.deque([[start]])

    while frontier:
        node = frontier.popleft()
        if node[-1] == goal:
            solution = " ".join(solution) + "\n" + " ".join(node)
            return solution
        if node[-1] not in explored_set:
            explored_set.add(node[-1])
            solution.append(node[-1])

            neighbors = graph[node[-1]]
            for i in neighbors: # no need to reverse this time! (get the minimum cost first)
                frontier.append(node + [i[1]])


if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 2
    grader.grade(problem_id, test_case_id, bfs_search, parse.read_graph_search_problem)