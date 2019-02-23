'''
Created by Ming Li at 2019-02-22

Feature: 

Description: 
https://leetcode.com/problems/all-paths-from-source-to-target/
Contact: ming.li2@columbia.edu
'''


class Solution:
    def allPathsSourceTarget(self, graph: 'List[List[int]]') -> 'List[List[int]]':
        self.graph = graph
        self.N = len(graph)
        self.visited = [False] * self.N
        self.paths = []
        self.gen_paths(curr_node=0, curr_path=[0],dest_node=N-1)
        return self.paths

    def gen_paths(self, curr_node, curr_path, dest_node):
        # using DFS, if the end of curr_path is our desired dest, then
        # we will add it to our res, else no.
        # So we get all the options using DFS.
        if curr_path[-1] == dest_node:
            self.paths.append(list(curr_path))
        else:
            for neighbor in self.graph[curr_node]:
                if not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    curr_path.append(neighbor)
                    self.gen_paths(curr_node=neighbor,curr_path=curr_path,dest_node=dest_node)
                    curr_path.pop()
                    self.visited[neighbor] = False
            
    

class Solution2:
    # using BFS
    def allPathsSourceTarget(self, graph):
        paths, results = [[0]], []      # initial partial path of [0]

        while paths:

            new_paths = []

            for path in paths:
                for next_node in graph[path[-1]]:
                    destination = results if next_node == len(graph) - 1 else new_paths
                    destination.append(path[:] + [next_node])

            paths = new_paths

        return results


if __name__ == '__main__':
    res = Solution()
    print(res)