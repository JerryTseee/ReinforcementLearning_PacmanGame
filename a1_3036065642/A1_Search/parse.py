import os, sys
def read_graph_search_problem(file_path):
    #Your p1 code here
    with open(file_path) as f:
        lines = f.read().split("\n")

    start = lines[0].split(" ")[1] # get the start state
    goal = lines[1].split(" ")[1] # get the goal state

    # use dictionary type for graph and heuristic value
    graph = {}
    heuristic_value = {}

    for i in range(2, len(lines)):
        line = lines[i].split(" ")
        if len(line) == 2: # for state and heuristic value pair
            char = line[0]
            heuristic_value[char] = float(line[1])
        elif len(line) == 3: # for the path cost
            temp_start = line[0]
            temp_end = line[1]
            cost = float(line[2])
            if temp_start not in graph:
                graph[temp_start] = [(cost, temp_end)] # format example: {"A": [(1, "B")]}
            elif temp_start in graph:
                graph[temp_start].append((cost, temp_end)) # format example: {"A": [(1, "B"), (2, "C")]}
            
            # evey time update the graph, also sort the graph by the cost
            graph[temp_start] = sorted(graph[temp_start], key=lambda x: x[0])


    for i in heuristic_value:
        if i not in graph:
            graph[i] = [] # this is the goal state !
    
    # also use dictionary to store the problem
    problem = {
        "graph" : graph,
        "start" : start,
        "goal" : goal,
        "heuristic_value" : heuristic_value
    }

    return problem

def read_8queens_search_problem(file_path):
    #Your p6 code here
    problem = ''
    return problem

if __name__ == "__main__":
    if len(sys.argv) == 3:
        problem_id, test_case_id = sys.argv[1], sys.argv[2]
        if int(problem_id) <= 5:
            problem = read_graph_search_problem(os.path.join('test_cases','p'+problem_id, test_case_id+'.prob'))
        else:
            problem = read_8queens_search_problem(os.path.join('test_cases','p'+problem_id, test_case_id+'.prob'))
        print(problem)
    else:
        print('Error: I need exactly 2 arguments!')