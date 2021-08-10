class Number:

    num = int(0)
    iterations = int(0)
    visits = []

    def __init__(self, n):
        self.num = int(n)
        self.iterations = int(0)
        self.visits = []

    def set_num(self, n):
        self.num = int(n)

    def get_num(self):
        return self.num

    def append_iteration(self):
        self.iterations += int(1)

    def get_iterations(self):
        return self.iterations

    def add_visit(self, n):
        self.visits.append(int(n))

    def get_visits(self):
        return self.visits

    def __str__(self):
        return ("Number: " + str(self.num) + "\nIterations: " + str(self.iterations) + "\nVisits: " + str(self.visits))
