import sys, grader, parse
import collections

def dfs_search(problem):
    #Your p1 code here
    start = problem["start"]
    goal = problem["goal"]
    graph = problem["graph"]

    frontier = collections.deque([[start]]) # format example: [["Ar"]]
    explored = set()

    solution = [] # final output solution
    while frontier:
        node = frontier.pop()
        if node[-1] == (goal):
            solution = " ".join(solution) + "\n" + " ".join(node) # first line is the order record, second line is the solution path
            return solution
        if node[-1] not in explored:
            explored.add(node[-1])
            solution.append(node[-1]) # record the order

            neighbors = graph[node[-1]]
            for i in reversed(neighbors): # reverse the order, to let lowest cost on the rightmost, so that it will be popped first
                frontier.append(node + [i[1]])


if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 1
    grader.grade(problem_id, test_case_id, dfs_search, parse.read_graph_search_problem)