def safe_pawns(pawns):
    return sum(chr(ord(pawn[0])-1) + str(int(pawn[1])-1)in pawns or chr(ord(pawn[0])+1) + str(int(pawn[1])-1)in pawns for pawn in pawns)