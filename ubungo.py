import math

class Card:
    
    def __init__(self):
        self.shape = []

    def try_put_together(self, pieces):
        pass

    def assign_piece(self, shape, piece):
        """
        assign somehow and return empty rest shape
        """

class Piece:
    """ """
    
    def draw(self):
        pass

class Cell:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, cell):
        return self.x == cell.x and self.y == cell.y

    def has_touch(self, cell):
        return (self.x == cell.x and int(math.fabs(self.y - cell.y))==1) or \
               (self.y == cell.y and  int(math.fabs(self.x - cell.x))==1)
    

class Block:
    
    def __init__(self, start=(0,0), end=(0,0)):
        self.start_x = start[0]
        self.start_y = start[1]
        self.end_x = end[0]
        self.end_y = end[1]
        self.cells = []

    def draw(self):
        """"""

    def __add__(self, block):
        """
        if blocks doent touch each other throw ValueError
        otherwise return their sum block
        """
        # 1.prunik
        if not self._intersection(block.cells) and not self._touch(block.cells):
            raise ValueError("No touch, no intersection among blocks.")
        

    def _intersection(self, other_cells):
        results = [x == y for x in self.cells for y in other_cells]
        return any(results)

    def _touch(self, other_cells):
        results = [x.has_touch(y) for x in self.cells for y in other_cells]
        return any(results)
                
    
