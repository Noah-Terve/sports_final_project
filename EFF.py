
# (PTS + REB + AST + STL + BLK − Missed FG − Missed FT - TO) / GP [1]

def EFF(PTS:int, REB:int, AST:int, STL:int, BLK:int, FGA, FG:int, FT:int, FTA:int, TO:int, Games:int):
    # print("Hello World")
    MissedFG = FGA - FG
    MissedFT = FTA - FT
    # print(MissedFG)
    # print(MissedFT)
    EFF = (PTS + REB + AST + STL + BLK - MissedFG - MissedFT - TO) / Games
    return EFF


if __name__ == "__main__":
    print("Hello World")
    NewEFF = EFF(1,2,3,4,5,6,7,8,9,10,11)
    print(NewEFF)
