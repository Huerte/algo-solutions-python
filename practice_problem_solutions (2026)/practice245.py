# Print in Order


from threading import Event
class Foo:
    def __init__(self):
        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst) -> None:
        
        printFirst()
        self.first_done.set()


    def second(self, printSecond) -> None:
        self.first_done.wait()
        printSecond()
        self.second_done.set()


    def third(self, printThird) -> None:

        self.second_done.wait()        
        printThird()