class Worker:
    def __init__(self, name):
        self.name = name

    def work(self):
        return "Worker is working"

class Developer(Worker):
    def work(self):
        return "Developer writes code"

class Designer(Worker):
    def work(self):
        return "Designer created design"

workers = [
    Developer("Alex"),
    Designer("Kate"),
    Worker("Sam")
]
for i in workers:
    print(i.work())
