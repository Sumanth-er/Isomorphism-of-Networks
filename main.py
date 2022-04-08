
class Graph(object):

    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size


    def add_connection(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val)),
            print
    def isomorphic(g,g2):
        count = 0
        for i in g:
            if i == 1:
                count = count + 1
        for j in g2:
            if i == 1:
                if i == 1:
                    count = count - 1
        if count == 0:
            print("the graph is isomorphic")
        else:
            print("the gramph is not isomorphic")

def main():
    g = Graph(5)
    g.add_connection(0, 1)
    g.add_connection(0, 2)
    g.add_connection(1, 2)
    g.add_connection(2, 0)
    g.add_connection(2, 3)

    g.print_matrix()

    g2 = Graph(5)
    g2.add_connection(0, 1)
    g2.add_connection(0, 2)
    g2.add_connection(1, 2)
    g2.add_connection(2, 0)
    g2.add_connection(2, 3)
    print("network 2")
    g2.print_matrix()

    print(type(g))
    print(Graph.isomorphic(g,g2))

if __name__ == '__main__':
    main()