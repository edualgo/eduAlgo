from itertools import permutations  
from collections import defaultdict 
from edualgo import print_msg_box

class tsp:
    
    def __init__(self, graph, start = 0):
        self.adj_mat = graph
        self.start = start
        self.size = len( graph )
        self.memo = defaultdict( lambda: defaultdict( lambda:float('inf') ) )
        self.__min_cost_value = self.__path = None

        # initializing table with optimal answer for every sub__paths of length 1
        for i in range(self.size):
            if i != self.start:
                # optimal distance when i is the end node and start and i are visited
                self.memo[i][ 1<<self.start | 1<<i ] = self.adj_mat[self.start][i]

        for r in range(3, self.size+1):

            for subset in self.__get_combinations(r):
                if self.__not_in(self.start, subset): 
                    continue

                # this next will be the current sub__path's end
                for next in range(self.size):
                    if next==self.start or self.__not_in(next, subset):
                        continue

                    # state will be used to get the sub__paths not including next
                    state = subset^(1<<next)
                    min_dist = float('inf')

                    # this end is going to be the previous end
                    for end in range(self.size):

                        if end is self.start or end is next or self.__not_in(end, subset):
                            continue

                        new_distance = self.memo[end][state] + self.adj_mat[end][next]
                        if new_distance< min_dist:
                            min_dist = new_distance
                        self.memo[next][subset] = min_dist


    def __not_in(self, i, subset):
        return ((subset>>i)&1)==0

    def __get_combinations(self, r):
        num = '0'*(self.size-r) + '1'*r 
        for perm in set(permutations(num)):
            yield  int(''.join(perm), 2)

    @property
    def minimum_cost(self):
        if self.__min_cost_value: return self.__min_cost_value

        end_state = (1<<self.size) - 1
        min_cost = float('inf')
        for end in range(self.size):

            if end == self.start: continue
            curr_cost = self.memo[end][end_state] + self.adj_mat[end][self.start]
            min_cost = min(min_cost, curr_cost)

        self.__min_cost_value = min_cost
        return self.__min_cost_value 

    @property
    def optimal_tour(self):

        if self.__path: return  self.__path

        last = self.start
        state = (1<<self.size) - 1
        tour = [None]*(self.size+1)
        tour[0] = tour[-1] = self.start

        for i in range(self.size-1, 0, -1):
            index = -1
            for j in range(self.size):
                if j==self.start or self.__not_in(j, state):
                    continue
                if index==-1: index = j 
                prev_dist = self.memo[index][state] + self.adj_mat[index][last]
                new_dist = self.memo[j][state] + self.adj_mat[j][last]
                if new_dist<prev_dist: index = j 

            tour[i] = index
            state^=(1<<index)
            last = index
        
        self.__path = tour
        return self.__path 

    @property
    def hint(self):
        message = """
                                                    ______________TRAVELLING SALESMAN PROBLEM______________
        given a complete graph, the task is to find the Hamiltonian cycle (path which visits all nodes exactly once and comes back to source) with the minimum weight.

        solution
        --------
        The possible way to find a solution is to try all Hamiltonian cycles and find one with minimum total weight.

        but we can improve.

        we can use dynamic programming to calculate the minimum cost for all possible sub-paths and then combine those results to get our ans.

        we define our dp state as the minimum cost when ending node is E and we have visited VISITED_SET of nodes.

        starting at our source, we calculate the answers for all subpaths with our base case as all paths of length 1(or two nodes).

        since there can be 2^n sub paths ending at any node, the extra space required is of order O(N.2^N).

        A> lets understand how we will calculate the answer for all subpaths.
            i> we have answer to all subpaths of length 1.
            ii> starting from 2, we generate all possible subpaths of length 2 to N which also includes the start node.
                i> we remove any node (except SOURCE) say NEXT from this set.
                ii> form the remaining nodes we will select any node except SOURCE, say END, this end will be the end node for all subpaths of length 1 less than current subpath length.
                    i> we then attach our NEXT to this subpath.
                    ii> if this end is giving reduced cost with END ,we keep it.

        B> finding the minimum cost.
            we iterate through all the costs of subpaths containing all nodes, the subpath which gives minimum cost value on connecting END to SOURCE is the answer.

        C> finding the actual path.
            i> we initialise LAST as SOURCE and VISITED containing all nodes.
                do untill we get all nodes:
                    i> we find a node with min cost to connect to LAST.
                    ii> set LAST to this node and remove it from VISITED.

                in this way we keep reducing the size of tour getting an optimal node in each step.

        The overall time complexity is O(N^2 * 2^N) and space complexity is O(N* 2^N).

        USAGE
        -----

        tsp_obj = tsp(adjacency_matrix, source_node) 
        # node numbering is expected to start from 0.
        # a complete graph is expected.
        # adjacency_matrix must be (N*N) where N is the number of nodes.

        minimum_cost = tsp_obj.minimum_cost
        # returns an integer, the minimum_cost of tour.

        optimal_tour = tsp_obj.optimal_tour
        # returns a list of integers of size N+1, the optimal path.

        """
        print_msg_box(message)