from pieces.piece import Piece

class Rook(Piece):

    alliance = None
    position = None

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position
