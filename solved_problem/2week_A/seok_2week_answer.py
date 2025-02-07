king,rock=print(input("Place by entered: ").split())                #enter king and rock position
count=0
king=[ord(king[0])-ord("A")+1,int(king[1])]                         #ex) (col: ord(king[0])=ord("A")  ord(king[0])-ord("A")==0 =>init alpha position,row)
rock=[ord(rock[0])-ord("A")+1,int(rock[1])]

move_types=["R","L","B","T","RT","LT","RB","LB"]                    #move_direction
move_col=[1,-1,0,0,1,-1,1,-1]                                       #move_position
move_row=[0,0,-1,1,1,-1,1,-1]

move=print(int(input("Move by the number entered: ")))
move_move=move_types.index(move)
