class SilvaRouter:
    def __init__(self):
        self.routes = {}

    def add_route(self, path, handler):
        self.routes[path] = handler

    def get(self, path):
        return self.routes.get(path, None)
 





