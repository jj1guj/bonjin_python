def hantei():
    #行の判定
    #先手番の置き石の判定
    if j<=14 and row[i][j]==1 and row[i][j+1]==1 and row[i][j+2]==1 and \
          row[i][j+3]==1 and row[i][j+4]==1:
              #print("先手番の勝ちです")
              syouhai.append(1)
    #4の判定
    if j<=15 and row[i][j]==1 and row[i][j+1]==1 and row[i][j+2]==1 and row[i][j+3]==1:
        if (j>=1 and j<=14 and row[i][j-1]==2 and row[i][j+4]==0) or (j==0 and row[i][j+4]==0):
            r[i][j+4]=r[i][j+4]+katayon
        elif (j>=1 and j<=14 and row[i][j-1]==0 and row[i][j+4]==2) or (j==15 and row[i][j-4]==0):
            r[i][j-1]=r[i][j-1]+katayon
        elif j>=1 and j<=14 and row[i][j-1]==0 and row[i][j+4]==0:
            #print("先手番の勝ちです")
            syouhai.append(1)
    #飛び四の判定
    if j<=14:
        if  row[i][j]==1 and row[i][j+1]==0 and row[i][j+2]==1 and row[i][j+3]==1 and\
                row[i][j+4]==1:
                    r[i][j+1]=r[i][j+1]+katayon
        elif row[i][j]==1 and row[i][j+1]==1 and row[i][j+2]==0 and row[i][j+3]==1 and\
                 row[i][j+4]==1:
                    r[i][j+2]=r[i][j+2]+katayon
        elif row[i][j]==1 and row[i][j+1]==1 and row[i][j+2]==1 and row[i][j+3]==0 and\
                 row[i][j+4]==1:
                     r[i][j+3]=r[i][j+3]+katayon
    #3の判定
    if j<=16 and row[i][j]==1 and row[i][j+1]==1 and row[i][j+2]==1:
        if j>=1 and j<=14 and row[i][j-1]==0 and row[i][j+3]==0:
            r[i][j-1]=r[i][j-1]+san
            r[i][j+3]=r[i][j+3]+san
        elif (j>=1 and j<=15 and row[i][j-1]==2 and row[i][j+3]==0) or (j==0 and row[i][j+3]==0):
            r[i][j+3]=r[i][j+3]+katasan
        elif (j>=1 and j<=15 and row[i][j-1]==0 and row[i][j+3]==2) or (j==18 and row[i][j+1]==0):
            r[i][j-1]=r[i][j-1]+katasan
    #飛び三の判定
    if j<=15:
        if row[i][j]==1 and row[i][j+1]==0 and row[i][j+2]==1 and row[i][j+3]==1:
            if j>=1 and j<=14 and row[i][j-1]==0 and row[i][j+4]==0:
                if soutesu%2==1:
                    r[i][j-1]=r[i][j-1]+san
                    r[i][j+1]=r[i][j+1]+san
                    r[i][j+4]=r[i][j+4]+san
                else:
                    r[i][j+1]=r[i][j+1]+san
            elif (j>=1 and j<=14 and row[i][j-1]==2 and row[i][j+4]==0) or (j==0 and row[i][j+4]==0):
                r[i][j+1]=r[i][j+1]+katasan
                r[i][j+4]=r[i][j+4]+san
            elif (j>=1 and j<=14 and row[i][j-1]==0 and row[i][j+4]==2) or (j==15 and row[i][j-1]==0):
                r[i][j-1]=r[i][j-1]+san
                r[i][j+1]=r[i][j+1]+katasan
        elif row[i][j]==1 and row[i][j+1]==1 and row[i][j+2]==0 and row[i][j+3]==1:
            if j>=1 and j<=14 and row[i][j-1]==0 and row[i][j+4]==0:
                if soutesu%2==1:
                    r[i][j-1]=r[i][j-1]+san
                    r[i][j+1]=r[i][j+2]+san
                    r[i][j+4]=r[i][j+4]+san
                else:
                    r[i][j+1]=r[i][j+2]+san
            elif (j>=1 and j<=14 and row[i][j-1]==2 and row[i][j+4]==0) or (j==0 and row[i][j+4]==0):
                r[i][j+2]=r[i][j+2]+katasan
                r[i][j+4]=r[i][j+4]+san
            elif (j>=1 and j<=14 and row[i][j-1]==0 and row[i][j+4]==2) or (j==15 and row[i][j-1]==0):
                r[i][j-1]=r[i][j-1]+san
                r[i][j+2]=r[i][j+2]+katasan
    #2の判定
    if j<=17 and row[i][j]==1 and row[i][j+1]==1:
        if j<=14 and row[i][j+2]==0 and row[i][j+3]==0 and row[i][j+4]==0:
            if j==0 or (j>=1 and row[i][j-1]==2):
                r[i][j+2]=r[i][j+2]+katani
                r[i][j+3]=r[i][j+3]+katani
            elif j>=1 and row[i][j-1]==0:
                r[i][j+2]=r[i][j+2]+ni
                r[i][j+3]=r[i][j+3]+ni
                if j>=2 and row[i][j-2]==2:
                    r[i][j-1]=r[i][j-1]+katani
                elif j>=2 and row[i][j-2]==0:
                    r[i][j-1]=r[i][j-1]+ni
        elif j>=1 and j<=15 and row[i][j-1]==0 and row[i][j+2]==0 and row[i][j+3]==0:
            r[i][j+2]=r[i][j+2]+ni
            r[i][j+3]=r[i][j+3]+ni

            if j>=2 and row[i][j-2]==0:
                r[i][j-1]=r[i][j-1]+ni
            elif j==1 or (j>=2 and row[i][j-2]==2):
                r[i][j-1]=r[i][j-1]+katani
        elif j>=2 and j<=16 and row[i][j-2]==0 and row[i][j-1]==0 and row[i][j+2]==0:
            r[i][j-1]=r[i][j-1]+ni
            r[i][j+2]=r[i][j+2]+ni

            if j>=3 and row[i][j-3]==0:
                r[i][j-2]=r[i][j-2]+ni
            elif j==2 or (j>=3 and row[i][j-3]==2):
                r[i][j-2]=r[i][j-2]+ni
        elif j>=3 and j<=17 and row[i][j-3]==0 and row[i][j-2]==0 and row[i][j-1]==0:
            if j<=16 and row[i][j+2]==0:
                r[i][j-2]=r[i][j-2]+ni
                r[i][j-1]=r[i][j-1]+ni
            elif j==17 or (j<=16 and row[i][j+2]==2):
                r[i][j-2]=r[i][j-2]+katani
                r[i][j-1]=r[i][j-1]+katani
    #飛び二の判定
    if j<=16 and row[i][j]==1 and row[i][j+1]==0 and row[i][j+2]==1:
        if j>=1 and j<=15 and row[i][j-1]==0 and row[i][j+3]==0:
            r[i][j-1]=r[i][j-1]+ni
            r[i][j+1]=r[i][j+1]+ni
            r[i][j+3]=r[i][j+3]+ni
        elif (j>=1 and j<=14 and row[i][j-1]==2 and row[i][j+3]==0 and row[i][j+4]==0) or\
             (j==0 and row[i][j+3]==0 and row[i][j+4]==0):
            r[i][j+1]=r[i][j+1]+katani
            r[i][j+3]=r[i][j+3]+katani
        elif (j>=2 and j<=15 and row[i][j-2]==0 and row[i][j-1]==0 and row[i][j+3]==2) or\
             (j==16 and row[i][j-2]==0 and row[i][j-1]==0):
            r[i][j-1]=r[i][j-1]+katani
            r[i][j+1]=r[i][j+1]+katani
    #1の判定
    if j<=18 and row[i][j]==1:
        if j>=1 and j<=14 and row[i][j+1]==0 and row[i][j+2]==0 and\
           row[i][j+3]==0 and row[i][j+4]==0:
            if  row[i][j-1]==0:
                r[i][j+1]=r[i][j+1]+ichi
                r[i][j+2]=r[i][j+2]+ichi
                if j>=2 and row[i][j-2]==0:
                    r[i][j-1]=r[i][j-1]+ichi
                elif j>=2 and row[i][j-2]==2:
                    r[i][j-1]=r[i][j-1]+kataichi
            elif row[i][j-2]==2:
                r[i][j+1]=r[i][j+1]+kataichi
                r[i][j+2]=r[i][j+2]+kataichi
        elif j>=1 and j<=15 and row[i][j-1]==0 and row[i][j+1]==0 and row[i][j+2]==0 and\
             row[i][j+3]==0:
            r[i][j+1]=r[i][j+1]+ichi
            r[i][j+2]=r[i][j+2]+ichi
            if j>=2 and row[i][j-2]==0:
                r[i][j-1]=r[i][j-1]+ichi
            elif j==1 or (j>=2 and row[i][j-2]==2):
                r[i][j-1]=r[i][j-1]+kataichi
        elif j>=2 and j<=16 and row[i][j-2]==0 and row[i][j-1]==0 and row[i][j+1]==0 and\
             row[i][j+2]==0:
            r[i][j-1]=r[i][j-1]+ichi
            r[i][j+1]=r[i][j+1]+ichi

            if j<=15 and row[i][j+3]==0:
                r[i][j+2]=r[i][j+2]+ichi
            elif j==16 or (j<=15 and row[i][j+3]==2):
                r[i][j+2]=r[i][j+2]+kataichi

            if j>=3 and row[i][j-3]==0:
                r[i][j-2]=r[i][j-2]+ichi
            elif j==2 or (j>=3 and row[i][j-3]==2):
                r[i][j-2]=r[i][j-2]+kataichi
        elif j>=3 and j<=17 and row[i][j-3]==0 and row[i][j-2]==0 and row[i][j-1]==0 and\
             row[i][j+1]==0:
            r[i][j-2]=r[i][j-2]+ichi
            r[i][j-1]=r[i][j-1]+ichi

            if j<=16 and row[i][j+2]==0:
                r[i][j+1]=r[i][j+1]+ichi
            elif j==17 or (j<=16 and row[i][j+2]==2):
                r[i][j+1]=r[i][j+1]+kataichi
    
    #後手番の判定
    if j<=14 and row[i][j]==2 and row[i][j+1]==2 and row[i][j+2]==2 and \
          row[i][j+3]==2 and row[i][j+4]==2:
              #print("後手番の勝ちです")
              syouhai.append(2)
    #4の判定
    if j<=15 and row[i][j]==2 and row[i][j+1]==2 and row[i][j+2]==2 and row[i][j+3]==2:
        if (j>=1 and j<=14 and row[i][j-1]==1 and row[i][j+4]==0) or (j==0 and row[i][j+4]==0):
            r[i][j+4]=r[i][j+4]+katayon
        elif (j>=1 and j<=14 and row[i][j-1]==0 and row[i][j+4]==1) or (j==15 and row[i][j-1]==0):
            r[i][j-1]=r[i][j-1]+katayon
        elif j>=1 and j<=14 and row[i][j-1]==0 and row[i][j+4]==0:
            #print("後手番の勝ちです")
            syouhai.append(2)
    #飛び四の判定
    if j<=14:
        if  row[i][j]==2 and row[i][j+1]==0 and row[i][j+2]==2 and row[i][j+3]==2 and\
                row[i][j+4]==2:
                    r[i][j+1]=r[i][j+1]+katayon
        elif row[i][j]==2 and row[i][j+1]==2 and row[i][j+2]==0 and row[i][j+3]==2 and\
                 row[i][j+4]==2:
                    r[i][j+2]=r[i][j+2]+katayon
        elif row[i][j]==2 and row[i][j+1]==2 and row[i][j+2]==2 and row[i][j+3]==0 and\
                 row[i][j+4]==2:
                     r[i][j+3]=r[i][j+3]+katayon
    #3の判定
    if j<=16 and row[i][j]==2 and row[i][j+1]==2 and row[i][j+2]==2:
        if j>=1 and j<=14 and row[i][j-1]==0 and row[i][j+3]==0:
            r[i][j-1]=r[i][j-1]+san
            r[i][j+3]=r[i][j+3]+san
        elif (j>=1 and j<=15 and row[i][j-1]==1 and row[i][j+3]==0) or (j==0 and row[i][j+3]==0):
            r[i][j+3]=r[i][j+3]+katasan
        elif (j>=1 and j<=15 and row[i][j-1]==0 and row[i][j+3]==1) or (j==18 and row[i][j-1]==0):
            r[i][j-1]=r[i][j-1]+katasan
    #飛び三の判定
    if j<=15:
        if row[i][j]==2 and row[i][j+1]==0 and row[i][j+2]==2 and row[i][j+3]==2:
            if j>=1 and j<=14 and row[i][j-1]==0 and row[i][j+4]==0:
                r[i][j-1]=r[i][j-1]+san
                r[i][j+1]=r[i][j+1]+san
                r[i][j+4]=r[i][j+4]+san
            elif (j>=1 and j<=14 and row[i][j-1]==1 and row[i][j+4]==0) or (j==0 and row[i][j+4]==0):
                r[i][j+1]=r[i][j+1]+katasan
                r[i][j+4]=r[i][j+4]+san
            elif (j>=1 and j<=14 and row[i][j-1]==0 and row[i][j+4]==1) or (j==15 and row[i][j-1]==0):
                r[i][j-1]=r[i][j-1]+san
                r[i][j+1]=r[i][j+1]+katasan
        elif row[i][j]==2 and row[i][j+1]==2 and row[i][j+2]==0 and row[i][j+3]==2:
            if j>=1 and j<=14 and row[i][j-1]==0 and row[i][j+4]==0:
                r[i][j-1]=r[i][j-1]+san
                r[i][j+2]=r[i][j+2]+san
                r[i][j+4]=r[i][j+4]+san
            elif (j>=1 and j<=14 and row[i][j-1]==1 and row[i][j+4]==0) or (j==0 and row[i][j+4]==0):
                r[i][j+2]=r[i][j+2]+katasan
                r[i][j+4]=r[i][j+4]+san
            elif (j>=1 and j<=14 and row[i][j-1]==0 and row[i][j+4]==1) or (j==15 and row[i][j-1]==0):
                r[i][j-1]=r[i][j-1]+san
                r[i][j+2]=r[i][j+2]+katasan
    #2の判定
    if j<=17 and row[i][j]==2 and row[i][j+1]==2:
        if j<=14 and row[i][j+2]==0 and row[i][j+3]==0 and row[i][j+4]==0:
            if j==0 or (j>=1 and row[i][j-1]==1):
                r[i][j+2]=r[i][j+2]+katani
                r[i][j+3]=r[i][j+3]+katani
            elif j>=1 and row[i][j-1]==0:
                r[i][j+2]=r[i][j+2]+ni
                r[i][j+3]=r[i][j+3]+ni
                if j>=2 and row[i][j-2]==1:
                    r[i][j-1]=r[i][j-1]+katani
                elif j>=2 and row[i][j-2]==0:
                    r[i][j-1]=r[i][j-1]+ni
        elif j>=1 and j<=15 and row[i][j-1]==0 and row[i][j+2]==0 and row[i][j+3]==0:
            r[i][j+2]=r[i][j+2]+ni
            r[i][j+3]=r[i][j+3]+ni

            if j>=2 and row[i][j-2]==0:
                r[i][j-1]=r[i][j-1]+ni
            elif j==1 or (j>=2 and row[i][j-2]==1):
                r[i][j-1]=r[i][j-1]+katani
        elif j>=2 and j<=16 and row[i][j-2]==0 and row[i][j-1]==0 and row[i][j+2]==0:
            r[i][j-1]=r[i][j-1]+ni
            r[i][j+2]=r[i][j+2]+ni

            if j>=3 and row[i][j-3]==0:
                r[i][j-2]=r[i][j-2]+ni
            elif j==2 or (j>=3 and row[i][j-3]==1):
                r[i][j-2]=r[i][j-2]+ni
        elif j>=3 and j<=17 and row[i][j-3]==0 and row[i][j-2]==0 and row[i][j-1]==0:
            if j<=16 and row[i][j+2]==0:
                r[i][j-2]=r[i][j-2]+ni
                r[i][j-1]=r[i][j-1]+ni
            elif j==17 or (j<=16 and row[i][j+2]==1):
                r[i][j-2]=r[i][j-2]+katani
                r[i][j-1]=r[i][j-1]+katani
    #飛び二の判定
    if j<=16 and row[i][j]==2 and row[i][j+1]==0 and row[i][j+2]==2:
        if j>=1 and j<=15 and row[i][j-1]==0 and row[i][j+3]==0:
            r[i][j-1]=r[i][j-1]+ni
            r[i][j+1]=r[i][j+1]+ni
            r[i][j+3]=r[i][j+3]+ni
        elif (j>=1 and j<=14 and row[i][j-1]==1 and row[i][j+3]==0 and row[i][j+4]==0) or\
             (j==0 and row[i][j+3]==0 and row[i][j+4]==0):
            r[i][j+1]=r[i][j+1]+katani
            r[i][j+3]=r[i][j+3]+katani
        elif (j>=2 and j<=15 and row[i][j-2]==0 and row[i][j-1]==0 and row[i][j+3]==1) or\
             (j==16 and row[i][j-2]==0 and row[i][j-1]==0):
            r[i][j-1]=r[i][j-1]+katani
            r[i][j+1]=r[i][j+1]+katani
    #1の判定
    if j<=18 and row[i][j]==2:
        if j>=1 and j<=14 and row[i][j+1]==0 and row[i][j+2]==0 and\
           row[i][j+3]==0 and row[i][j+4]==0:
            if  row[i][j-1]==0:
                r[i][j+1]=r[i][j+1]+ichi
                r[i][j+2]=r[i][j+2]+ichi
                if j>=2 and row[i][j-2]==0:
                    r[i][j-1]=r[i][j-1]+ichi
                elif j>=2 and row[i][j-2]==1:
                    r[i][j-1]=r[i][j-1]+kataichi
            elif row[i][j-2]==1:
                r[i][j+1]=r[i][j+1]+kataichi
                r[i][j+2]=r[i][j+2]+kataichi
        elif j>=1 and j<=15 and row[i][j-1]==0 and row[i][j+1]==0 and row[i][j+2]==0 and\
             row[i][j+3]==0:
            r[i][j+1]=r[i][j+1]+ichi
            r[i][j+2]=r[i][j+2]+ichi
            if j>=2 and row[i][j-2]==0:
                r[i][j-1]=r[i][j-1]+ichi
            elif j==1 or (j>=2 and row[i][j-2]==1):
                r[i][j-1]=r[i][j-1]+kataichi
        elif j>=2 and j<=16 and row[i][j-2]==0 and row[i][j-1]==0 and row[i][j+1]==0 and\
             row[i][j+2]==0:
            r[i][j-1]=r[i][j-1]+ichi
            r[i][j+1]=r[i][j+1]+ichi

            if j<=15 and row[i][j+3]==0:
                r[i][j+2]=r[i][j+2]+ichi
            elif j==16 or (j<=15 and row[i][j+3]==1):
                r[i][j+2]=r[i][j+2]+kataichi

            if j>=3 and row[i][j-3]==0:
                r[i][j-2]=r[i][j-2]+ichi
            elif j==2 or (j>=3 and row[i][j-3]==1):
                r[i][j-2]=r[i][j-2]+kataichi
        elif j>=3 and j<=17 and row[i][j-3]==0 and row[i][j-2]==0 and row[i][j-1]==0 and\
             row[i][j+1]==0:
            r[i][j-2]=r[i][j-2]+ichi
            r[i][j-1]=r[i][j-1]+ichi

            if j<=16 and row[i][j+2]==0:
                r[i][j+1]=r[i][j+1]+ichi
            elif j==17 or (j<=16 and row[i][j+2]==1):
                r[i][j+1]=r[i][j+1]+kataichi
    
    #列方向の判定
    #先手番の判定
    if j<=14 and clm[i][j]==1 and clm[i][j+1]==1 and clm[i][j+2]==1 and \
          clm[i][j+3]==1 and clm[i][j+4]==1:
              #print("先手番の勝ちです")
              syouhai.append(1)
    #4の判定
    if j<=15 and clm[i][j]==1 and clm[i][j+1]==1 and clm[i][j+2]==1 and clm[i][j+3]==1:
        if (j>=1 and j<=14 and clm[i][j-1]==2 and clm[i][j+4]==0) or (j==0 and clm[i][j+4]==0):
            r[j+4][i]=r[j+4][i]+katayon
        elif (j>=1 and j<=14 and clm[i][j-1]==0 and clm[i][j+4]==2) or (j==15 and clm[i][j-1]==0):
            r[j-1][i]=r[j-1][i]+katayon
        elif j>=1 and j<=14 and clm[i][j-1]==0 and clm[i][j+4]==0:
            #print("先手番の勝ちです")
            syouhai.append(1)
    #飛び四の判定
    if j<=14:
        if  clm[i][j]==1 and clm[i][j+1]==0 and clm[i][j+2]==1 and clm[i][j+3]==1 and\
                clm[i][j+4]==1:
                    r[j+1][i]=r[j+1][i]+katayon
        elif clm[i][j]==1 and clm[i][j+1]==1 and clm[i][j+2]==0 and clm[i][j+3]==1 and\
                 clm[i][j+4]==1:
                    r[j+2][i]=r[j+2][i]+katayon
        elif clm[i][j]==1 and clm[i][j+1]==1 and clm[i][j+2]==1 and clm[i][j+3]==0 and\
                 clm[i][j+4]==1:
                     r[j+3][i]=r[j+3][i]+katayon
    #3の判定
    if j<=16 and clm[i][j]==1 and clm[i][j+1]==1 and clm[i][j+2]==1:
        if j>=1 and j<=14 and clm[i][j-1]==0 and clm[i][j+3]==0:
            r[j-1][i]=r[j-1][i]+san
            r[j+3][i]=r[j+3][i]+san
        elif (j>=1 and j<=15 and clm[i][j-1]==2 and clm[i][j+3]==0) or (j==0 and clm[i][j+3]==0):
            r[j+3][i]=r[j+3][i]+katasan
        elif (j>=1 and j<=15 and clm[i][j-1]==0 and clm[i][j+3]==2) or (j==18 and clm[i][j-1]==0):
            r[j-1][i]=r[j-1][i]+katasan
    #飛び三の判定
    if j<=15:
        if clm[i][j]==1 and clm[i][j+1]==0 and clm[i][j+2]==1 and clm[i][j+3]==1:
            if j>=1 and j<=14 and clm[i][j-1]==0 and clm[i][j+4]==0:
                r[j-1][i]=r[j-1][i]+san
                r[j+1][i]=r[j+1][i]+san
                r[j+4][i]=r[j+4][i]+san
            elif (j>=1 and j<=14 and clm[i][j-1]==2 and clm[i][j+4]==0) or (j==0 and clm[i][j+4]==0):
                r[j+1][i]=r[j+1][i]+katasan
                r[j+4][i]=r[j+4][i]+san
            elif (j>=1 and j<=14 and clm[i][j-1]==0 and clm[i][j+4]==2) or (j==15 and clm[i][j-1]==0):
                r[j-1][i]=r[j-1][i]+san
                r[j+1][i]=r[j+1][i]+katasan
        elif clm[i][j]==1 and clm[i][j+1]==1 and clm[i][j+2]==0 and clm[i][j+3]==1:
            if j>=1 and j<=14 and clm[i][j-1]==0 and clm[i][j+4]==0:
                r[j-1][i]=r[j-1][i]+san
                r[j+2][i]=r[j+2][i]+san
                r[j+4][i]=r[j+4][i]+san
            elif (j>=1 and j<=14 and clm[i][j-1]==2 and clm[i][j+4]==0) or (j==0 and clm[i][j+4]==0):
                r[j+2][i]=r[j+2][i]+katasan
                r[j+4][i]=r[j+4][i]+san
            elif (j>=1 and j<=14 and clm[i][j-1]==0 and clm[i][j+4]==2) or (j==15 and clm[i][j-1]==0):
                r[j-1][i]=r[j-1][i]+san
                r[j+2][i]=r[j+2][i]+katasan
    #2の判定
    if j<=17 and clm[i][j]==1 and clm[i][j+1]==1:
        if j<=14 and clm[i][j+2]==0 and clm[i][j+3]==0 and clm[i][j+4]==0:
            if j==0 or (j>=1 and clm[i][j-1]==2):
                r[j+2][i]=r[j+2][i]+katani
                r[j+3][i]=r[j+3][i]+katani
            elif j>=1 and clm[i][j-1]==0:
                r[j+2][i]=r[j+2][i]+ni
                r[j+3][i]=r[j+3][i]+ni
                if j>=2 and clm[i][j-2]==2:
                    r[j-1][i]=r[j-1][i]+katani
                elif j>=2 and clm[i][j-2]==0:
                    r[j-1][i]=r[j-1][i]+ni
        elif j>=1 and j<=15 and clm[i][j-1]==0 and clm[i][j+2]==0 and clm[i][j+3]==0:
            r[j+2][i]=r[j+2][i]+ni
            r[j+3][i]=r[j+3][i]+ni

            if j>=2 and clm[i][j-2]==0:
                r[j-1][i]=r[j-1][i]+ni
            elif j==1 or (j>=2 and clm[i][j-2]==2):
                r[j-1][i]=r[j-1][i]+katani
        elif j>=2 and j<=16 and clm[i][j-2]==0 and clm[i][j-1]==0 and clm[i][j+2]==0:
            r[j-1][i]=r[j-1][i]+ni
            r[j+2][i]=r[j+2][i]+ni

            if j>=3 and clm[i][j-3]==0:
                r[j-2][i]=r[j-2][i]+ni
            elif j==2 or (j>=3 and clm[i][j-3]==2):
                r[j-2][i]=r[j-2][i]+ni
        elif j>=3 and j<=17 and clm[i][j-3]==0 and clm[i][j-2]==0 and clm[i][j-1]==0:
            if j<=16 and clm[i][j+2]==0:
                r[j-2][i]=r[j-2][i]+ni
                r[j-1][i]=r[j-1][i]+ni
            elif j==17 or (j<=16 and clm[i][j+2]==2):
                r[j-2][i]=r[j-2][i]+katani
                r[j-1][i]=r[j-1][i]+katani
    #飛び二の判定
    if j<=16 and clm[i][j]==1 and clm[i][j+1]==0 and clm[i][j+2]==1:
        if j>=1 and j<=15 and clm[i][j-1]==0 and clm[i][j+3]==0:
            r[j-1][i]=r[j-1][i]+ni
            r[j+1][i]=r[j+1][i]+ni
            r[j+3][i]=r[j+3][i]+ni
        elif (j>=1 and j<=14 and clm[i][j-1]==2 and clm[i][j+3]==0 and clm[i][j+4]==0) or\
             (j==0 and clm[i][j+3]==0 and clm[i][j+4]==0):
            r[j+1][i]=r[j+1][i]+katani
            r[j+3][i]=r[j+3][i]+katani
        elif (j>=2 and j<=15 and clm[i][j-2]==0 and clm[i][j-1]==0 and clm[i][j+3]==2) or\
             (j==16 and clm[i][j-2]==0 and clm[i][j-1]==0):
            r[j-1][i]=r[j-1][i]+katani
            r[j+1][i]=r[j+1][i]+katani
    #1の判定
    if j<=18 and clm[i][j]==1:
        if j>=1 and j<=14 and clm[i][j+1]==0 and clm[i][j+2]==0 and\
           clm[i][j+3]==0 and clm[i][j+4]==0:
            if  clm[i][j-1]==0:
                r[j+1][i]=r[j+1][i]+ichi
                r[j+2][i]=r[j+2][i]+ichi
                if j>=2 and clm[i][j-2]==0:
                    r[j-1][i]=r[j-1][i]+ichi
                elif j>=2 and clm[i][j-2]==2:
                    r[j-1][i]=r[j-1][i]+kataichi
            elif clm[i][j-2]==2:
                r[j+1][i]=r[j+1][i]+kataichi
                r[j+2][i]=r[j+2][i]+kataichi
        elif j>=1 and j<=15 and clm[i][j-1]==0 and clm[i][j+1]==0 and clm[i][j+2]==0 and\
             clm[i][j+3]==0:
            r[j+1][i]=r[j+1][i]+ichi
            r[j+2][i]=r[j+2][i]+ichi
            if j>=2 and clm[i][j-2]==0:
                r[j-1][i]=r[j-1][i]+ichi
            elif j==1 or (j>=2 and clm[i][j-2]==2):
                r[j-1][i]=r[j-1][i]+kataichi
        elif j>=2 and j<=16 and clm[i][j-2]==0 and clm[i][j-1]==0 and clm[i][j+1]==0 and\
             clm[i][j+2]==0:
            r[j-1][i]=r[j-1][i]+ichi
            r[j+1][i]=r[j+1][i]+ichi

            if j<=15 and clm[i][j+3]==0:
                r[j+2][i]=r[j+2][i]+ichi
            elif j==16 or (j<=15 and clm[i][j+3]==2):
                r[j+2][i]=r[j+2][i]+kataichi

            if j>=3 and clm[i][j-3]==0:
                r[j-2][i]=r[j-2][i]+ichi
            elif j==2 or (j>=3 and clm[i][j-3]==2):
                r[j-2][i]=r[j-2][i]+kataichi
        elif j>=3 and j<=17 and clm[i][j-3]==0 and clm[i][j-2]==0 and clm[i][j-1]==0 and\
             clm[i][j+1]==0:
            r[j-2][i]=r[j-2][i]+ichi
            r[j-1][i]=r[j-1][i]+ichi

            if j<=16 and clm[i][j+2]==0:
                r[j+1][i]=r[j+1][i]+ichi
            elif j==17 or (j<=16 and clm[i][j+2]==2):
                r[j+1][i]=r[j+1][i]+kataichi
    
    #後手番の判定
    if j<=14 and clm[i][j]==2 and clm[i][j+1]==2 and clm[i][j+2]==2 and \
          clm[i][j+3]==2 and clm[i][j+4]==2:
              #print("先手番の勝ちです")
              syouhai.append(2)
    #4の判定
    if j<=15 and clm[i][j]==2 and clm[i][j+1]==2 and clm[i][j+2]==2 and clm[i][j+3]==2:
        if (j>=1 and j<=14 and clm[i][j-1]==1 and clm[i][j+4]==0) or (j==0 and clm[i][j+4]==0):
            r[j+4][i]=r[j+4][i]+katayon
        elif (j>=1 and j<=14 and clm[i][j-1]==0 and clm[i][j+4]==1) or (j==15 and clm[i][j-1]==0):
            r[j-1][i]=r[j-1][i]+katayon
        elif j>=1 and j<=14 and clm[i][j-1]==0 and clm[i][j+4]==0:
            #print("先手番の勝ちです")
            syouhai.append(2)
    #飛び四の判定
    if j<=14:
        if  clm[i][j]==2 and clm[i][j+1]==0 and clm[i][j+2]==2 and clm[i][j+3]==2 and\
                clm[i][j+4]==2:
                    r[j+1][i]=r[j+1][i]+katayon
        elif clm[i][j]==2 and clm[i][j+1]==2 and clm[i][j+2]==0 and clm[i][j+3]==2 and\
                 clm[i][j+4]==2:
                    r[j+2][i]=r[j+2][i]+katayon
        elif clm[i][j]==2 and clm[i][j+1]==2 and clm[i][j+2]==2 and clm[i][j+3]==0 and\
                 clm[i][j+4]==2:
                     r[j+3][i]=r[j+3][i]+katayon
    #3の判定
    if j<=16 and clm[i][j]==2 and clm[i][j+1]==2 and clm[i][j+2]==2:
        if j>=1 and j<=14 and clm[i][j-1]==0 and clm[i][j+3]==0:
            r[j-1][i]=r[j-1][i]+san
            r[j+3][i]=r[j+3][i]+san
        elif (j>=1 and j<=15 and clm[i][j-1]==1 and clm[i][j+3]==0) or (j==0 and clm[i][j+3]==0):
            r[j+3][i]=r[j+3][i]+katasan
        elif (j>=1 and j<=15 and clm[i][j-1]==0 and clm[i][j+3]==1) or (j==18 and clm[i][j-1]==0):
            r[j-1][i]=r[j-1][i]+katasan
    #飛び三の判定
    if j<=15:
        if clm[i][j]==2 and clm[i][j+1]==0 and clm[i][j+2]==2 and clm[i][j+3]==2:
            if j>=1 and j<=14 and clm[i][j-1]==0 and clm[i][j+4]==0:
                r[j-1][i]=r[j-1][i]+san
                r[j+1][i]=r[j+1][i]+san
                r[j+4][i]=r[j+4][i]+san
            elif (j>=1 and j<=14 and clm[i][j-1]==1 and clm[i][j+4]==0) or (j==0 and clm[i][j+4]==0):
                r[j+1][i]=r[j+1][i]+katasan
                r[j+4][i]=r[j+4][i]+san
            elif (j>=1 and j<=14 and clm[i][j-1]==0 and clm[i][j+4]==1) or (j==15 and clm[i][j-1]==0):
                r[j-1][i]=r[j-1][i]+san
                r[j+1][i]=r[j+1][i]+katasan
        elif clm[i][j]==2 and clm[i][j+1]==2 and clm[i][j+2]==0 and clm[i][j+3]==2:
            if j>=1 and j<=14 and clm[i][j-1]==0 and clm[i][j+4]==0:
                r[j-1][i]=r[j-1][i]+san
                r[j+2][i]=r[j+2][i]+san
                r[j+4][i]=r[j+4][i]+san
            elif (j>=1 and j<=14 and clm[i][j-1]==1 and clm[i][j+4]==0) or (j==0 and clm[i][j+4]==0):
                r[j+2][i]=r[j+2][i]+katasan
                r[j+4][i]=r[j+4][i]+san
            elif (j>=1 and j<=14 and clm[i][j-1]==0 and clm[i][j+4]==1) or (j==15 and clm[i][j-1]==0):
                r[j-1][i]=r[j-1][i]+san
                r[j+2][i]=r[j+2][i]+katasan
    
    #2の判定
    if j<=17 and clm[i][j]==2 and clm[i][j+1]==2:
        if j<=14 and clm[i][j+2]==0 and clm[i][j+3]==0 and clm[i][j+4]==0:
            if j==0 or (j>=1 and clm[i][j-1]==1):
                r[j+2][i]=r[j+2][i]+katani
                r[j+3][i]=r[j+3][i]+katani
            elif j>=1 and clm[i][j-1]==0:
                r[j+2][i]=r[j+2][i]+ni
                r[j+3][i]=r[j+3][i]+ni
                if j>=2 and clm[i][j-2]==1:
                    r[j-1][i]=r[j-1][i]+katani
                elif j>=2 and clm[i][j-2]==0:
                    r[j-1][i]=r[j-1][i]+ni
        elif j>=1 and j<=15 and clm[i][j-1]==0 and clm[i][j+2]==0 and clm[i][j+3]==0:
            r[j+2][i]=r[j+2][i]+ni
            r[j+3][i]=r[j+3][i]+ni

            if j>=2 and clm[i][j-2]==0:
                r[j-1][i]=r[j-1][i]+ni
            elif j==1 or (j>=2 and clm[i][j-2]==1):
                r[j-1][i]=r[j-1][i]+katani
        elif j>=2 and j<=16 and clm[i][j-2]==0 and clm[i][j-1]==0 and clm[i][j+2]==0:
            r[j-1][i]=r[j-1][i]+ni
            r[j+2][i]=r[j+2][i]+ni

            if j>=3 and clm[i][j-3]==0:
                r[j-2][i]=r[j-2][i]+ni
            elif j==2 or (j>=3 and clm[i][j-3]==1):
                r[j-2][i]=r[j-2][i]+ni
        elif j>=3 and j<=17 and clm[i][j-3]==0 and clm[i][j-2]==0 and clm[i][j-1]==0:
            if j<=16 and clm[i][j+2]==0:
                r[j-2][i]=r[j-2][i]+ni
                r[j-1][i]=r[j-1][i]+ni
            elif j==17 or (j<=16 and clm[i][j+2]==1):
                r[j-2][i]=r[j-2][i]+katani
                r[j-1][i]=r[j-1][i]+katani
    #飛び二の判定
    if j<=16 and clm[i][j]==2 and clm[i][j+1]==0 and clm[i][j+2]==2:
        if j>=1 and j<=15 and clm[i][j-1]==0 and clm[i][j+3]==0:
            r[j-1][i]=r[j-1][i]+ni
            r[j+1][i]=r[j+1][i]+ni
            r[j+3][i]=r[j+3][i]+ni
        elif (j>=1 and j<=14 and clm[i][j-1]==1 and clm[i][j+3]==0 and clm[i][j+4]==0) or\
             (j==0 and clm[i][j+3]==0 and clm[i][j+4]==0):
            r[j+1][i]=r[j+1][i]+katani
            r[j+3][i]=r[j+3][i]+katani
        elif (j>=2 and j<=15 and clm[i][j-2]==0 and clm[i][j-1]==0 and clm[i][j+3]==1) or\
             (j==16 and clm[i][j-2]==0 and clm[i][j-1]==0):
            r[j-1][i]=r[j-1][i]+katani
            r[j+1][i]=r[j+1][i]+katani
    #1の判定
    if j<=18 and clm[i][j]==2:
        if j>=1 and j<=14 and clm[i][j+1]==0 and clm[i][j+2]==0 and\
           clm[i][j+3]==0 and clm[i][j+4]==0:
            if  clm[i][j-1]==0:
                r[j+1][i]=r[j+1][i]+ichi
                r[j+2][i]=r[j+2][i]+ichi
                if j>=2 and clm[i][j-2]==0:
                    r[j-1][i]=r[j-1][i]+ichi
                elif j>=2 and clm[i][j-2]==1:
                    r[j-1][i]=r[j-1][i]+kataichi
            elif clm[i][j-2]==1:
                r[j+1][i]=r[j+1][i]+kataichi
                r[j+2][i]=r[j+2][i]+kataichi
        elif j>=1 and j<=15 and clm[i][j-1]==0 and clm[i][j+1]==0 and clm[i][j+2]==0 and\
             clm[i][j+3]==0:
            r[j+1][i]=r[j+1][i]+ichi
            r[j+2][i]=r[j+2][i]+ichi
            if j>=2 and clm[i][j-2]==0:
                r[j-1][i]=r[j-1][i]+ichi
            elif j==1 or (j>=2 and clm[i][j-2]==1):
                r[j-1][i]=r[j-1][i]+kataichi
        elif j>=2 and j<=16 and clm[i][j-2]==0 and clm[i][j-1]==0 and clm[i][j+1]==0 and\
             clm[i][j+2]==0:
            r[j-1][i]=r[j-1][i]+ichi
            r[j+1][i]=r[j+1][i]+ichi

            if j<=15 and clm[i][j+3]==0:
                r[j+2][i]=r[j+2][i]+ichi
            elif j==16 or (j<=15 and clm[i][j+3]==1):
                r[j+2][i]=r[j+2][i]+kataichi

            if j>=3 and clm[i][j-3]==0:
                r[j-2][i]=r[j-2][i]+ichi
            elif j==2 or (j>=3 and clm[i][j-3]==1):
                r[j-2][i]=r[j-2][i]+kataichi
        elif j>=3 and j<=17 and clm[i][j-3]==0 and clm[i][j-2]==0 and clm[i][j-1]==0 and\
             clm[i][j+1]==0:
            r[j-2][i]=r[j-2][i]+ichi
            r[j-1][i]=r[j-1][i]+ichi

            if j<=16 and clm[i][j+2]==0:
                r[j+1][i]=r[j+1][i]+ichi
            elif j==17 or (j<=16 and clm[i][j+2]==1):
                r[j+1][i]=r[j+1][i]+kataichi
                
    #斜め方向の判定
    if i<=14:
        #盤面上部の判定
        #右斜め方向の判定
        
        #先手番の判定
        #5の判定
        if j<=14-i and miginaname1[i][j]==1 and miginaname1[i][j+1]==1 and miginaname1[i][j+2]==1 and\
                      miginaname1[i][j+3]==1 and miginaname1[i][j+4]==1:
                          #print("先手番の勝ちです")
                          syouhai.append(1)
        #4の判定
        if j<=15-i and miginaname1[i][j]==1 and miginaname1[i][j+1]==1 and miginaname1[i][j+2]==1 and miginaname1[i][j+3]==1:
            if (j>=1 and j<=14-i and miginaname1[i][j-1]==2 and miginaname1[i][j+4]==0) or (j==0 and miginaname1[i][j+4]==0):
                r[j+4][j+4+i]=r[j+4][j+4+i]+katayon
            elif (j>=1 and j<=14-i and miginaname1[i][j-1]==0 and miginaname1[i][j+4]==2) or (j==15-i and miginaname1[i][j-1]==0):
                r[j-1][j-1+i]=r[j-1][j-1+i]+katayon
            elif j>=1 and j<=14-i and miginaname1[i][j-1]==0 and miginaname1[i][j+4]==0:
                #print("先手番の勝ちです")
                syouhai.append(1)
        #飛び四の判定
        if j<=14-i:
            if  miginaname1[i][j]==1 and miginaname1[i][j+1]==0 and miginaname1[i][j+2]==1 and miginaname1[i][j+3]==1 and\
                    miginaname1[i][j+4]==1:
                        r[j+1][j+1+i]=r[j+1][j+1+i]+katayon
            elif miginaname1[i][j]==1 and miginaname1[i][j+1]==1 and miginaname1[i][j+2]==0 and miginaname1[i][j+3]==1 and\
                     miginaname1[i][j+4]==1:
                        r[j+2][j+2+i]=r[j+2][j+2+i]+katayon
            elif miginaname1[i][j]==1 and miginaname1[i][j+1]==1 and miginaname1[i][j+2]==1 and miginaname1[i][j+3]==0 and\
                     miginaname1[i][j+4]==1:
                         r[j+3][j+3+i]=r[j+3][j+3+i]+katayon
        #3の判定
        if j<=16-i and miginaname1[i][j]==1 and miginaname1[i][j+1]==1 and miginaname1[i][j+2]==1:
            if j>=1 and j<=14-i and miginaname1[i][j-1]==0 and miginaname1[i][j+3]==0:
                r[j-1][j-1+i]=r[j-1][j-1+i]+san
                r[j+3][j+3+i]=r[j+3][j+3+i]+san
            elif (j>=1 and j<=15-i and miginaname1[i][j-1]==2 and miginaname1[i][j+3]==0) or (j==0 and miginaname1[i][j+3]==0):
                r[j+3][j+3+i]=r[j+3][j+3+i]+katasan
            elif (j>=1 and j<=15-i and miginaname1[i][j-1]==0 and miginaname1[i][j+3]==2) or (j==18-i and miginaname1[i][j-1]==0):
                r[j-1][j-1+i]=r[j-1][j-1+i]+katasan
        #飛び三の判定
        if j<=15-i:
            if miginaname1[i][j]==1 and miginaname1[i][j+1]==0 and miginaname1[i][j+2]==1 and miginaname1[i][j+3]==1:
                if j>=1 and j<=14-i and miginaname1[i][j-1]==0 and miginaname1[i][j+4]==0:
                    r[j-1][j-1+i]=r[j-1][j-1+i]+san
                    r[j+1][j+1+i]=r[j+1][j+1+i]+san
                    r[j+4][j+4+i]=r[j+4][j+4+i]+san
                elif (j>=1 and j<=14-i and miginaname1[i][j-1]==2 and miginaname1[i][j+4]==0) or (j==0 and miginaname1[i][j+4]==0):
                    r[j+1][j+1+i]=r[j+1][j+1+i]+katasan
                    r[j+4][j+4+i]=r[j+4][j+4+i]+san
                elif (j>=1 and j<=14-i and miginaname1[i][j-1]==0 and miginaname1[i][j+4]==2) or (j==15-i and miginaname1[i][j-1]==0):
                    r[j-1][j-1+i]=r[j-1][j-1+i]+san
                    r[j+1][j+1+i]=r[j+1][j+1+i]+katasan
            elif miginaname1[i][j]==1 and miginaname1[i][j+1]==1 and miginaname1[i][j+2]==0 and miginaname1[i][j+3]==1:
                if j>=1 and j<=14-i and miginaname1[i][j-1]==0 and miginaname1[i][j+4]==0:
                    r[j-1][j-1+i]=r[j-1][j-1+i]+san
                    r[j+2][j+2+i]=r[j+2][j+2+i]+san
                    r[j+4][j+4+i]=r[j+4][j+4+i]+san
                elif (j>=1 and j<=14-i and miginaname1[i][j-1]==2 and miginaname1[i][j+4]==0) or (j==0 and miginaname1[i][j+4]==0):
                    r[j+2][j+2+i]=r[j+2][j+2+i]+katasan
                    r[j+4][j+4+i]=r[j+4][j+4+i]+san
                elif (j>=1 and j<=14-i and miginaname1[i][j-1]==0 and miginaname1[i][j+4]==2) or (j==15-i and miginaname1[i][j-1]==0):
                    r[j-1][j-1+i]=r[j-1][j-1+i]+san
                    r[j+2][j+2+i]=r[j+2][j+2+i]+katasan
        #2の判定
        if j<=17-i and miginaname1[i][j]==1 and miginaname1[i][j+1]==1:
            if j>=1 and j<=16-i and miginaname1[i][j-1]==0 and miginaname1[i][j+2]==0:
                r[j-1][j-1+i]=r[j-1][j-1+i]+ni
                r[j+2][j+2+i]=r[j+2][j+2+i]+ni
            elif (j>=1 and j<=16-i and miginaname1[i][j-1]==2 and miginaname1[i][j+2]==0) or (j==0 and miginaname1[i][j+2]==0):
                r[j+2][j+2+i]=r[j+2][j+2+i]+katani 
            elif (j>=1 and j<=16-i and miginaname1[i][j-1]==0 and miginaname1[i][j+2]==2) or (j==17-i and miginaname1[i][j-1]==0):
                r[j-1][j-1+i]=r[j-1][j-1+i]+katani
        #飛び二の判定
        if j<=16-i and miginaname1[i][j]==1 and miginaname1[i][j+1]==0 and miginaname1[i][j+2]==1:
            if j>=1 and j<=15-i and miginaname1[i][j-1]==0 and miginaname1[i][j+3]==0:
                r[j-1][j-1+i]=r[j-1][j-1+i]+ni
                r[j+1][j+1+i]=r[j+1][j+1+i]+ni
                r[j+3][j+3+i]=r[j+3][j+3+i]+ni
            elif (j>=1 and j<=15-i and miginaname1[i][j-1]==2 and miginaname1[i][j+3]==0) or (j==0 and miginaname1[i][j+3]==0):
                r[j+1][j+1+i]=r[j+1][j+1+i]+katani
                r[j+3][j+3+i]=r[j+3][j+3+i]+ni
            elif (j>=1 and j<=15-i and miginaname1[i][j-1]==0 and miginaname1[i][j+3]==2) or (j==16-i and miginaname1[i][j-1]==0):
                r[j-1][j-1+i]=r[j-1][j-1+i]+ni
                r[j+1][j+1+i]=r[j+1][j+1+i]+katani
        #1の判定
        if j<=18-i and miginaname1[i][j]==1:
            if j>=1 and j<=17-i and miginaname1[i][j-1]==0 and miginaname1[i][j+1]==0:
                r[j-1][j-1+i]=r[j-1][j-1+i]+ichi
                r[j+1][j+1+i]=r[j+1][j+1+i]+ichi
            elif (j>=1 and j<=17-i and miginaname1[i][j-1]==2 and miginaname1[i][j+1]==0) or (j==0 and miginaname1[i][j+1]==0):
                r[j+1][j+1+i]=r[j+1][j+1+i]+kataichi
            elif (j>=1 and j<=17-i and miginaname1[i][j-1]==0 and miginaname1[i][j+1]==2) or (j==18-i and miginaname1[i][j-1]==0):
                r[j-1][j-1+i]=r[j-1][j-1+i]+kataichi
                 
        #後手番の判定
        #5の判定
        if j<=14-i and miginaname1[i][j]==2 and miginaname1[i][j+1]==2 and miginaname1[i][j+2]==2 and\
                      miginaname1[i][j+3]==2 and miginaname1[i][j+4]==2:
                          #print("後手番の勝ちです")
                          syouhai.append(2)
        #4の判定
        if j<=15-i and miginaname1[i][j]==2 and miginaname1[i][j+1]==2 and miginaname1[i][j+2]==2 and miginaname1[i][j+3]==2:
            if (j>=1 and j<=14-i and miginaname1[i][j-1]==1 and miginaname1[i][j+4]==0) or (j==0 and miginaname1[i][j+4]==0):
                r[j+4][j+4+i]=r[j+4][j+4+i]+katayon
            elif (j>=1 and j<=14-i and miginaname1[i][j-1]==0 and miginaname1[i][j+4]==1) or (j==15-i and miginaname1[i][j-1]==0):
                r[j-1][j-1+i]=r[j-1][j-1+i]+katayon
            elif j>=1 and j<=14-i and miginaname1[i][j-1]==0 and miginaname1[i][j+4]==0:
                #print("後手番の勝ちです")
                syouhai.append(2)
        #飛び四の判定
        if j<=14-i:
            if  miginaname1[i][j]==2 and miginaname1[i][j+1]==0 and miginaname1[i][j+2]==2 and miginaname1[i][j+3]==2 and\
                    miginaname1[i][j+4]==2:
                        r[j+1][j+1+i]=r[j+1][j+1+i]+katayon
            elif miginaname1[i][j]==2 and miginaname1[i][j+1]==2 and miginaname1[i][j+2]==0 and miginaname1[i][j+3]==2 and\
                     miginaname1[i][j+4]==2:
                        r[j+2][j+2+i]=r[j+2][j+2+i]+katayon
            elif miginaname1[i][j]==2 and miginaname1[i][j+1]==2 and miginaname1[i][j+2]==2 and miginaname1[i][j+3]==0 and\
                     miginaname1[i][j+4]==2:
                         r[j+3][j+3+i]=r[j+3][j+3+i]+katayon
        #3の判定
        if j<=16-i and miginaname1[i][j]==2 and miginaname1[i][j+1]==2 and miginaname1[i][j+2]==2:
            if j>=1 and j<=14-i and miginaname1[i][j-1]==0 and miginaname1[i][j+3]==0:
                r[j-1][j-1+i]=r[j-1][j-1+i]+san
                r[j+3][j+3+i]=r[j+3][j+3+i]+san
            elif (j>=1 and j<=15-i and miginaname1[i][j-1]==1 and miginaname1[i][j+3]==0) or (j==0 and miginaname1[i][j+3]==0):
                r[j+3][j+3+i]=r[j+3][j+3+i]+katasan
            elif (j>=1 and j<=15-i and miginaname1[i][j-1]==0 and miginaname1[i][j+3]==1) or (j==18-i and miginaname1[i][j-1]==0):
                r[j-1][j-1+i]=r[j-1][j-1+i]+katasan
        #飛び三の判定
        if j<=15-i:
            if miginaname1[i][j]==2 and miginaname1[i][j+1]==0 and miginaname1[i][j+2]==2 and miginaname1[i][j+3]==2:
                if j>=1 and j<=14-i and miginaname1[i][j-1]==0 and miginaname1[i][j+4]==0:
                    r[j-1][j-1+i]=r[j-1][j-1+i]+san
                    r[j+1][j+1+i]=r[j+1][j+1+i]+san
                    r[j+4][j+4+i]=r[j+4][j+4+i]+san
                elif (j>=1 and j<=14-i and miginaname1[i][j-1]==1 and miginaname1[i][j+4]==0) or (j==0 and miginaname1[i][j+4]==0):
                    r[j+1][j+1+i]=r[j+1][j+1+i]+katasan
                    r[j+4][j+4+i]=r[j+4][j+4+i]+san
                elif (j>=1 and j<=14-i and miginaname1[i][j-1]==0 and miginaname1[i][j+4]==1) or (j==15-i and miginaname1[i][j-1]==0):
                    r[j-1][j-1+i]=r[j-1][j-1+i]+san
                    r[j+1][j+1+i]=r[j+1][j+1+i]+katasan
            elif miginaname1[i][j]==2 and miginaname1[i][j+1]==2 and miginaname1[i][j+2]==0 and miginaname1[i][j+3]==2:
                if j>=1 and j<=14-i and miginaname1[i][j-1]==0 and miginaname1[i][j+4]==0:
                    r[j-1][j-1+i]=r[j-1][j-1+i]+san
                    r[j+2][j+2+i]=r[j+2][j+2+i]+san
                    r[j+4][j+4+i]=r[j+4][j+4+i]+san
                elif (j>=1 and j<=14-i and miginaname1[i][j-1]==1 and miginaname1[i][j+4]==0) or (j==0 and miginaname1[i][j+4]==0):
                    r[j+2][j+2+i]=r[j+2][j+2+i]+katasan
                    r[j+4][j+4+i]=r[j+4][j+4+i]+san
                elif (j>=1 and j<=14-i and miginaname1[i][j-1]==0 and miginaname1[i][j+4]==1) or (j==15-i and miginaname1[i][j-1]==0):
                    r[j-1][j-1+i]=r[j-1][j-1+i]+san
                    r[j+2][j+2+i]=r[j+2][j+2+i]+katasan
        #2の判定
        if j<=17-i and miginaname1[i][j]==2 and miginaname1[i][j+1]==2:
            if j>=1 and j<=16-i and miginaname1[i][j-1]==0 and miginaname1[i][j+2]==0:
                r[j-1][j-1+i]=r[j-1][j-1+i]+ni
                r[j+2][j+2+i]=r[j+2][j+2+i]+ni
            elif (j>=1 and j<=16-i and miginaname1[i][j-1]==1 and miginaname1[i][j+2]==0) or (j==0 and miginaname1[i][j+2]==0):
                r[j+2][j+2+i]=r[j+2][j+2+i]+katani 
            elif (j>=1 and j<=16-i and miginaname1[i][j-1]==0 and miginaname1[i][j+2]==1) or (j==17-i and miginaname1[i][j-1]==0):
                r[j-1][j-1+i]=r[j-1][j-1+i]+katani
        #飛び二の判定
        if j<=16-i and miginaname1[i][j]==2 and miginaname1[i][j+1]==0 and miginaname1[i][j+2]==2:
            if j>=1 and j<=15-i and miginaname1[i][j-1]==0 and miginaname1[i][j+3]==0:
                r[j-1][j-1+i]=r[j-1][j-1+i]+ni
                r[j+1][j+1+i]=r[j+1][j+1+i]+ni
                r[j+3][j+3+i]=r[j+3][j+3+i]+ni
            elif (j>=1 and j<=15-i and miginaname1[i][j-1]==1 and miginaname1[i][j+3]==0) or (j==0 and miginaname1[i][j+3]==0):
                r[j+1][j+1+i]=r[j+1][j+1+i]+katani
                r[j+3][j+3+i]=r[j+3][j+3+i]+ni
            elif (j>=1 and j<=15-i and miginaname1[i][j-1]==0 and miginaname1[i][j+3]==1) or (j==16-i and miginaname1[i][j-1]==0):
                r[j-1][j-1+i]=r[j-1][j-1+i]+ni
                r[j+1][j+1+i]=r[j+1][j+1+i]+katani
        #1の判定
        if j<=18-i and miginaname1[i][j]==2:
            if j>=1 and j<=17-i and miginaname1[i][j-1]==0 and miginaname1[i][j+1]==0:
                r[j-1][j-1+i]=r[j-1][j-1+i]+ichi
                r[j+1][j+1+i]=r[j+1][j+1+i]+ichi
            elif (j>=1 and j<=17-i and miginaname1[i][j-1]==1 and miginaname1[i][j+1]==0) or (j==0 and miginaname1[i][j+1]==0):
                r[j+1][j+1+i]=r[j+1][j+1+i]+kataichi
            elif (j>=1 and j<=17-i and miginaname1[i][j-1]==0 and miginaname1[i][j+1]==1) or (j==18-i and miginaname1[i][j-1]==0):
                r[j-1][j-1+i]=r[j-1][j-1+i]+kataichi
        
        #左斜め方向の判定
        #先手番の判定
        #5の判定
        if j<=14-i and hidarinaname1[i][j]==1 and hidarinaname1[i][j+1]==1 and hidarinaname1[i][j+2]==1 and\
                      hidarinaname1[i][j+3]==1 and hidarinaname1[i][j+4]==1:
                          #print("先手番の勝ちです")
                          syouhai.append(1)
        #4の判定
        if j<=15-i and hidarinaname1[i][j]==1 and hidarinaname1[i][j+1]==1 and hidarinaname1[i][j+2]==1 and hidarinaname1[i][j+3]==1:
            if (j>=1 and j<=14-i and hidarinaname1[i][j-1]==2 and hidarinaname1[i][j+4]==0) or (j==0 and hidarinaname1[i][j+4]==0):
                r[j+4][18-(j+4+i)]=r[j+4][18-(j+4+i)]+katayon
            elif (j>=1 and j<=14-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+4]==2) or (j==15-i and hidarinaname1[i][j-1]==0):
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+katayon
            elif j>=1 and j<=14-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+4]==0:
                #print("先手番の勝ちです")
                syouhai.append(1)
        #飛び四の判定
        if j<=14-i:
            if  hidarinaname1[i][j]==1 and hidarinaname1[i][j+1]==0 and hidarinaname1[i][j+2]==1 and hidarinaname1[i][j+3]==1 and\
                    hidarinaname1[i][j+4]==1:
                        r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+katayon
            elif hidarinaname1[i][j]==1 and hidarinaname1[i][j+1]==1 and hidarinaname1[i][j+2]==0 and hidarinaname1[i][j+3]==1 and\
                     hidarinaname1[i][j+4]==1:
                        r[j+2][18-(j+2+i)]=r[j+2][18-(j+2+i)]+katayon
            elif hidarinaname1[i][j]==1 and hidarinaname1[i][j+1]==1 and hidarinaname1[i][j+2]==1 and hidarinaname1[i][j+3]==0 and\
                     hidarinaname1[i][j+4]==1:
                         r[j+3][18-(j+3+i)]=r[j+3][18-(j+3+i)]+katayon
        #3の判定
        if j<=16-i and hidarinaname1[i][j]==1 and hidarinaname1[i][j+1]==1 and hidarinaname1[i][j+2]==1:
            if j>=1 and j<=14-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+3]==0:
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+san
                r[j+3][18-(j+3+i)]=r[j+3][18-(j+3+i)]+san
            elif (j>=1 and j<=15-i and hidarinaname1[i][j-1]==2 and hidarinaname1[i][j+3]==0) or (j==0 and hidarinaname1[i][j+3]==0):
                r[j+3][18-(j+3+i)]=r[j+3][18-(j+3+i)]+katasan
            elif (j>=1 and j<=15-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+3]==2) or (j==18-i and hidarinaname1[i][j-1]==0):
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+katasan
        #飛び三の判定
        if j<=15-i:
            if hidarinaname1[i][j]==1 and hidarinaname1[i][j+1]==0 and hidarinaname1[i][j+2]==1 and hidarinaname1[i][j+3]==1:
                if j>=1 and j<=14-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+4]==0:
                    r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+san
                    r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+san
                    r[j+4][18-(j+4+i)]=r[j+4][18-(j+4+i)]+san
                elif (j>=1 and j<=14-i and hidarinaname1[i][j-1]==2 and hidarinaname1[i][j+4]==0) or (j==0 and hidarinaname1[i][j+4]==0):
                    r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+katasan
                    r[j+4][18-(j+4+i)]=r[j+4][18-(j+4+i)]+san
                elif (j>=1 and j<=14-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+4]==2) or (j==15-i and hidarinaname1[i][j-1]==0):
                    r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+san
                    r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+katasan
            elif hidarinaname1[i][j]==1 and hidarinaname1[i][j+1]==1 and hidarinaname1[i][j+2]==0 and hidarinaname1[i][j+3]==1:
                if j>=1 and j<=14-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+4]==0:
                    r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+san
                    r[j+2][18-(j+2+i)]=r[j+2][18-(j+2+i)]+san
                    r[j+4][18-(j+4+i)]=r[j+4][18-(j+4+i)]+san
                elif (j>=1 and j<=14-i and hidarinaname1[i][j-1]==2 and hidarinaname1[i][j+4]==0) or (j==0 and hidarinaname1[i][j+4]==0):
                    r[j+2][18-(j+2+i)]=r[j+2][18-(j+2+i)]+katasan
                    r[j+4][18-(j+4+i)]=r[j+4][18-(j+4+i)]+san
                elif (j>=1 and j<=14-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+4]==2) or (j==15-i and hidarinaname1[i][j-1]==0):
                    r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+san
                    r[j+2][18-(j+2+i)]=r[j+2][18-(j+2+i)]+katasan
        #2の判定
        if j<=17-i and hidarinaname1[i][j]==1 and hidarinaname1[i][j+1]==1:
            if j>=1 and j<=16-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+2]==0:
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+ni
                r[j+2][18-(j+2+i)]=r[j+2][18-(j+2+i)]+ni
            elif (j>=1 and j<=16-i and hidarinaname1[i][j-1]==2 and hidarinaname1[i][j+2]==0) or (j==0 and hidarinaname1[i][j+3]==0):
                r[j+2][18-(j+2+i)]=r[j+2][18-(j+2+i)]+katani 
            elif (j>=1 and j<=16-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+2]==2) or (j==17-i and hidarinaname1[i][j-1]==0):
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+katani
        #飛び二の判定
        if j<=16-i and hidarinaname1[i][j]==1 and hidarinaname1[i][j+1]==0 and hidarinaname1[i][j+2]==1:
            if j>=1 and j<=15-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+3]==0:
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+ni
                r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+ni
                r[j+3][18-(j+3+i)]=r[j+3][18-(j+3+i)]+ni
            elif (j>=1 and j<=15-i and hidarinaname1[i][j-1]==2 and hidarinaname1[i][j+3]==0) or (j==0 and hidarinaname1[i][j+3]==0):
                r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+katani
                r[j+3][18-(j+3+i)]=r[j+3][18-(j+3+i)]+ni
            elif (j>=1 and j<=15-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+3]==2) or (j==16-i and hidarinaname1[i][j-1]==0):
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+ni
                r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+katani
        #1の判定
        if j<=18-i and hidarinaname1[i][j]==1:
            if j>=1 and j<=17-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+1]==0:
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+ichi
                r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+ichi
            elif (j>=1 and j<=17-i and hidarinaname1[i][j-1]==2 and hidarinaname1[i][j+1]==0) or (j==0 and hidarinaname1[i][j+1]==0):
                r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+kataichi
            elif (j>=1 and j<=17-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+1]==2) or (j==18-i and hidarinaname1[i][j-1]==0):
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+kataichi
        
        #後手番の判定
        #5の判定
        if j<=14-i and hidarinaname1[i][j]==2 and hidarinaname1[i][j+1]==2 and hidarinaname1[i][j+2]==2 and\
                      hidarinaname1[i][j+3]==2 and hidarinaname1[i][j+4]==2:
                          #print("後手番の勝ちです")
                          syouhai.append(2)
        #4の判定
        if j<=15-i and hidarinaname1[i][j]==2 and hidarinaname1[i][j+1]==2 and hidarinaname1[i][j+2]==2 and hidarinaname1[i][j+3]==2:
            if (j>=1 and j<=14-i and hidarinaname1[i][j-1]==1 and hidarinaname1[i][j+4]==0) or (j==0 and hidarinaname1[i][j+4]==0):
                r[j+4][18-(j+4+i)]=r[j+4][18-(j+4+i)]+katayon
            elif (j>=1 and j<=14-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+4]==1) or (j==15-i and hidarinaname1[i][j-1]==0):
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+katayon
            elif j>=1 and j<=14-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+4]==0:
                #print("後手番の勝ちです")
                syouhai.append(2)
        #飛び四の判定
        if j<=14-i:
            if  hidarinaname1[i][j]==2 and hidarinaname1[i][j+1]==0 and hidarinaname1[i][j+2]==2 and hidarinaname1[i][j+3]==2 and\
                    hidarinaname1[i][j+4]==2:
                        r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+katayon
            elif hidarinaname1[i][j]==2 and hidarinaname1[i][j+1]==2 and hidarinaname1[i][j+2]==0 and hidarinaname1[i][j+3]==2 and\
                     hidarinaname1[i][j+4]==2:
                        r[j+2][18-(j+2+i)]=r[j+2][18-(j+2+i)]+katayon
            elif hidarinaname1[i][j]==2 and hidarinaname1[i][j+1]==2 and hidarinaname1[i][j+2]==2 and hidarinaname1[i][j+3]==0 and\
                     hidarinaname1[i][j+4]==2:
                         r[j+3][18-(j+3+i)]=r[j+3][18-(j+3+i)]+katayon
        #3の判定
        if j<=16-i and hidarinaname1[i][j]==2 and hidarinaname1[i][j+1]==2 and hidarinaname1[i][j+2]==2:
            if j>=1 and j<=14-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+3]==0:
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+san
                r[j+3][18-(j+3+i)]=r[j+3][18-(j+3+i)]+san
            elif (j>=1 and j<=15-i and hidarinaname1[i][j-1]==1 and hidarinaname1[i][j+3]==0) or (j==0 and hidarinaname1[i][j+3]==0):
                r[j+3][18-(j+3+i)]=r[j+3][18-(j+3+i)]+katasan
            elif (j>=1 and j<=15-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+3]==1) or (j==18-i and hidarinaname1[i][j-1]==0):
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+katasan
        #飛び三の判定
        if j<=15-i:
            if hidarinaname1[i][j]==2 and hidarinaname1[i][j+1]==0 and hidarinaname1[i][j+2]==2 and hidarinaname1[i][j+3]==2:
                if j>=1 and j<=14-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+4]==0:
                    r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+san
                    r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+san
                    r[j+4][18-(j+4+i)]=r[j+4][18-(j+4+i)]+san
                elif (j>=1 and j<=14-i and hidarinaname1[i][j-1]==1 and hidarinaname1[i][j+4]==0) or (j==0 and hidarinaname1[i][j+4]==0):
                    r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+katasan
                    r[j+4][18-(j+4+i)]=r[j+4][18-(j+4+i)]+san
                elif (j>=1 and j<=14-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+4]==1) or (j==15-i and hidarinaname1[i][j-1]==0):
                    r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+san
                    r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+katasan
            elif hidarinaname1[i][j]==2 and hidarinaname1[i][j+1]==2 and hidarinaname1[i][j+2]==0 and hidarinaname1[i][j+3]==2:
                if j>=1 and j<=14-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+4]==0:
                    r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+san
                    r[j+2][18-(j+2+i)]=r[j+2][18-(j+2+i)]+san
                    r[j+4][18-(j+4+i)]=r[j+4][18-(j+4+i)]+san
                elif (j>=1 and j<=14-i and hidarinaname1[i][j-1]==1 and hidarinaname1[i][j+4]==0) or (j==0 and hidarinaname1[i][j+4]==0):
                    r[j+2][18-(j+2+i)]=r[j+2][18-(j+2+i)]+katasan
                    r[j+4][18-(j+4+i)]=r[j+4][18-(j+4+i)]+san
                elif (j>=1 and j<=14-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+4]==1) or (j==15-i and hidarinaname1[i][j-1]==0):
                    r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+san
                    r[j+2][18-(j+2+i)]=r[j+2][18-(j+2+i)]+katasan
        #2の判定
        if j<=17-i and hidarinaname1[i][j]==2 and hidarinaname1[i][j+1]==2:
            if j>=1 and j<=16-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+2]==0:
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+ni
                r[j+2][18-(j+2+i)]=r[j+2][18-(j+2+i)]+ni
            elif (j>=1 and j<=16-i and hidarinaname1[i][j-1]==1 and hidarinaname1[i][j+2]==0) or (j==0 and hidarinaname1[i][j+2]==0):
                r[j+2][18-(j+2+i)]=r[j+2][18-(j+2+i)]+katani 
            elif (j>=1 and j<=16-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+2]==1) or (j==17-i and hidarinaname1[i][j-1]==0):
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+katani
        #飛び二の判定
        if j<=16-i and hidarinaname1[i][j]==2 and hidarinaname1[i][j+1]==0 and hidarinaname1[i][j+2]==2:
            if j>=1 and j<=15-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+3]==0:
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+ni
                r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+ni
                r[j+3][18-(j+3+i)]=r[j+3][18-(j+3+i)]+ni
            elif (j>=1 and j<=15-i and hidarinaname1[i][j-1]==1 and hidarinaname1[i][j+3]==0) or (j==0 and hidarinaname1[i][j+3]==0):
                r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+katani
                r[j+3][18-(j+3+i)]=r[j+3][18-(j+3+i)]+ni
            elif (j>=1 and j<=15-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+3]==1) or (j==16-i and hidarinaname1[i][j-1]==0):
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+ni
                r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+katani
        #1の判定
        if j<=18-i and hidarinaname1[i][j]==2:
            if j>=1 and j<=17-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+1]==0:
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+ichi
                r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+ichi
            elif (j>=1 and j<=17-i and hidarinaname1[i][j-1]==1 and hidarinaname1[i][j+1]==0) or (j==0 and hidarinaname1[i][j+1]==0):
                r[j+1][18-(j+1+i)]=r[j+1][18-(j+1+i)]+kataichi
            elif (j>=1 and j<=17-i and hidarinaname1[i][j-1]==0 and hidarinaname1[i][j+1]==1) or (j==18-i and hidarinaname1[i][j-1]==0):
                r[j-1][18-(j-1+i)]=r[j-1][18-(j-1+i)]+kataichi
        if i<=13:
            #盤面下部の判定
            
            #右斜め方向の判定
        
            #先手番の判定
            #5の判定
            if j<=13-i and miginaname2[i][j]==1 and miginaname2[i][j+1]==1 and miginaname2[i][j+2]==1 and\
                          miginaname2[i][j+3]==1 and miginaname2[i][j+4]==1:
                              #print("先手番の勝ちです")
                              syouhai.append(1)
            #4の判定
            if j<=14-i and miginaname2[i][j]==1 and miginaname2[i][j+1]==1 and miginaname2[i][j+2]==1 and miginaname2[i][j+3]==1:
                if (j>=1 and j<=13-i and miginaname2[i][j-1]==2 and miginaname2[i][j+4]==0) or (j==0 and miginaname2[i][j+4]==0):
                    r[j+i+5][j+4]=r[j+i+5][j+4]+katayon
                elif (j>=1 and j<=13-i and miginaname2[i][j-1]==0 and miginaname2[i][j+4]==2) or (j==14-i and miginaname2[i][j-1]==0):
                    r[j+i][j-1]=r[j+i][j-1]+katayon
                elif j>=1 and j<=13-i and miginaname2[i][j-1]==0 and miginaname2[i][j+4]==0:
                    #print("先手番の勝ちです")
                    syouhai.append(1)
            #飛び四の判定
            if j<=13-i:
                if  miginaname2[i][j]==1 and miginaname2[i][j+1]==0 and miginaname2[i][j+2]==1 and miginaname2[i][j+3]==1 and\
                        miginaname2[i][j+4]==1:
                            r[j+i+2][j+1]=r[j+i+2][j+1]+katayon
                elif miginaname2[i][j]==1 and miginaname2[i][j+1]==1 and miginaname2[i][j+2]==0 and miginaname2[i][j+3]==1 and\
                         miginaname2[i][j+4]==1:
                            r[j+i+3][j+2]=r[j+i+3][j+2]+katayon
                elif miginaname2[i][j]==1 and miginaname2[i][j+1]==1 and miginaname2[i][j+2]==1 and miginaname2[i][j+3]==0 and\
                         miginaname2[i][j+4]==1:
                             r[j+i+4][j+3]=r[j+i+4][j+3]+katayon
            #3の判定
            if j<=15-i and miginaname2[i][j]==1 and miginaname2[i][j+1]==1 and miginaname2[i][j+2]==1:
                if j>=1 and j<=14-i and miginaname2[i][j-1]==0 and miginaname2[i][j+3]==0:
                    r[j+i][j-1]=r[j+i][j-1]+san
                    r[j+i+4][j+3]=r[j+i+4][j+3]+san
                elif (j>=1 and j<=14-i and miginaname2[i][j-1]==2 and miginaname2[i][j+3]==0) or (j==0 and miginaname2[i][j+3]==0):
                    r[j+i+4][j+3]=r[j+i+4][j+3]+katasan
                elif (j>=1 and j<=14-i and miginaname2[i][j-1]==0 and miginaname2[i][j+3]==2) or (j==15-i and miginaname2[i][j-1]==0):
                    r[j+i][j-1]=r[j+i][j-1]+katasan
            #飛び三の判定
            if j<=14-i:
                if miginaname2[i][j]==1 and miginaname2[i][j+1]==0 and miginaname2[i][j+2]==1 and miginaname2[i][j+3]==1:
                    if j>=1 and j<=13-i and miginaname2[i][j-1]==0 and miginaname2[i][j+4]==0:
                        r[j+i][j-1]=r[j+i][j-1]+san
                        r[j+i+2][j+1]=r[j+i+2][j+1]+san
                        r[j+i+5][j+4]=r[j+i+5][j+4]+san
                    elif (j>=1 and j<=13-i and miginaname2[i][j-1]==2 and miginaname2[i][j+4]==0) or (j==0 and miginaname2[i][j+4]==0):
                        r[j+i+2][j+1]=r[j+i+2][j+1]+katasan
                        r[j+i+5][j+4]=r[j+i+5][j+4]+san
                    elif (j>=1 and j<=13-i and miginaname2[i][j-1]==0 and miginaname2[i][j+4]==2) or (j==15 and miginaname2[i][j-1]==0):
                        r[j+i][j-1]=r[j+i][j-1]+san
                        r[j+i+2][j+1]=r[j+i+2][j+1]+katasan
                elif miginaname2[i][j]==1 and miginaname2[i][j+1]==1 and miginaname2[i][j+2]==0 and miginaname2[i][j+3]==1:
                    if j>=1 and j<=13-i and miginaname2[i][j-1]==0 and miginaname2[i][j+4]==0:
                        r[j+i][j-1]=r[j+i][j-1]+san
                        r[j+i+3][j+2]=r[j+i+3][j+2]+san
                        r[j+i+5][j+4]=r[j+i+5][j+4]+san
                    elif (j>=1 and j<=13-i and miginaname2[i][j-1]==2 and miginaname2[i][j+4]==0) or (j==0 and miginaname2[i][j+4]==0):
                        r[j+i+3][j+2]=r[j+i+3][j+2]+katasan
                        r[j+i+5][j+4]=r[j+i+5][j+4]+san
                    elif (j>=1 and j<=13-i and miginaname2[i][j-1]==0 and miginaname2[i][j+4]==2) or (j==15 and miginaname2[i][j-1]==0):
                        r[j+i][j-1]=r[j+i][j-1]+san
                        r[j+i+3][j+2]=r[j+i+3][j+2]+katasan
            #2の判定
            if j<=16-i and miginaname2[i][j]==1 and miginaname2[i][j+1]==1:
                if j>=1 and j<=15-i and miginaname2[i][j-1]==0 and miginaname2[i][j+2]==0:
                    r[j+i][j-1]=r[j+i][j-1]+ni
                    r[j+i+3][j+2]=r[j+i+3][j+2]+ni
                elif (j>=1 and j<=15-i and miginaname2[i][j-1]==2 and miginaname2[i][j+2]==0) or (j==0 and miginaname2[i][j+2]==0):
                    r[j+3+i][j+2]=r[j+3+i][j+2]+katani 
                elif (j>=1 and j<=15-i and miginaname2[i][j-1]==0 and miginaname2[i][j+2]==2) or (j==16-i and miginaname2[i][j-1]==0):
                    r[j+i][j-1]=r[j+i][j-1]+katani
            #飛び二の判定
            if j<=15-i and miginaname2[i][j]==1 and miginaname2[i][j+1]==0 and miginaname2[i][j+2]==1:
                if j>=1 and j<=14-i and miginaname2[i][j-1]==0 and miginaname2[i][j+3]==0:
                    r[j+i][j-1]=r[j+i][j-1]+ni
                    r[j+i+2][j+1]=r[j+i+2][j+1]+ni
                    r[j+i+4][j+3]=r[j+i+4][j+3]+ni
                elif (j>=1 and j<=14-i and miginaname2[i][j-1]==2 and miginaname2[i][j+3]==0) or (j==0 and miginaname2[i][j+3]==0):
                    r[j+i+2][j+1]=r[j+i+2][j+1]+katani
                    r[j+i+4][j+3]=r[j+i+4][j+3]+ni
                elif (j>=1 and j<=14-i and miginaname2[i][j-1]==0 and miginaname2[i][j+3]==2) or (j==16 and miginaname2[i][j-1]==0):
                    r[j+i][j-1]=r[j+i][j-1]+ni
                    r[j+i+2][j+1]=r[j+i+2][j+1]+katani
            #1の判定
            if j<=17-i and miginaname2[i][j]==1:
                if j>=1 and j<=16-i and miginaname2[i][j-1]==0 and miginaname2[i][j+1]==0:
                    r[j+i][j-1]=r[j+i][j-1]+ichi
                    r[j+2+i][j+1]=r[j+2+i][j+1]+ichi
                elif (j>=1 and j<=16-i and miginaname2[i][j-1]==2 and miginaname2[i][j+1]==0) or (j==0 and miginaname2[i][j+1]==0):
                    r[j+2+i][j+1]=r[j+2+i][j+1]+kataichi
                elif (j>=1 and j<=16-i and miginaname2[i][j-1]==0 and miginaname2[i][j+1]==2) or (j==17-i and miginaname2[i][j-1]==0):
                    r[j+i][j-1]=r[j+i][j-1]+kataichi
                     
            #後手番の判定
            #5の判定
            if j<=13-i and miginaname2[i][j]==2 and miginaname2[i][j+1]==2 and miginaname2[i][j+2]==2 and\
                          miginaname2[i][j+3]==2 and miginaname2[i][j+4]==2:
                              #print("後手番の勝ちです")
                              syouhai.append(2)
            #4の判定
            if j<=14-i and miginaname2[i][j]==2 and miginaname2[i][j+1]==2 and miginaname2[i][j+2]==2 and miginaname2[i][j+3]==2:
                if (j>=1 and j<=13-i and miginaname2[i][j-1]==0 and miginaname2[i][j+4]==1) or (j==0 and miginaname2[i][j+4]==0):
                    r[j+i+5][j+4]=r[j+i+5][j+4]+katayon
                elif (j>=1 and j<=13-i and miginaname2[i][j-1]==1 and miginaname2[i][j+4]==0) or (j==14-i and miginaname2[i][j-1]==0):
                    r[j+i][j-1]=r[j+i][j-1]+katayon
                elif j>=1 and j<=13-i and miginaname2[i][j-1]==0 and miginaname2[i][j+4]==0:
                    #print("後手番の勝ちです")
                    syouhai.append(2)
            #飛び四の判定
            if j<=13-i:
                if  miginaname2[i][j]==2 and miginaname2[i][j+1]==0 and miginaname2[i][j+2]==2 and miginaname2[i][j+3]==2 and\
                        miginaname2[i][j+4]==2:
                            r[j+i+2][j+1]=r[j+i+2][j+1]+katayon
                elif miginaname2[i][j]==2 and miginaname2[i][j+1]==2 and miginaname2[i][j+2]==0 and miginaname2[i][j+3]==2 and\
                         miginaname2[i][j+4]==2:
                            r[j+i+3][j+2]=r[j+i+3][j+2]+katayon
                elif miginaname2[i][j]==2 and miginaname2[i][j+1]==2 and miginaname2[i][j+2]==2 and miginaname2[i][j+3]==0 and\
                         miginaname2[i][j+4]==2:
                             r[j+i+4][j+3]=r[j+i+4][j+3]+katayon
            #3の判定
            if j<=15-i and miginaname2[i][j]==2 and miginaname2[i][j+1]==2 and miginaname2[i][j+2]==2:
                if j>=1 and j<=14-i and miginaname2[i][j-1]==0 and miginaname2[i][j+3]==0:
                    r[j+i][j-1]=r[j+i][j-1]+san
                    r[j+i+4][j+3]=r[j+i+4][j+3]+san
                elif (j>=1 and j<=14-i and miginaname2[i][j-1]==1 and miginaname2[i][j+3]==0) or (j==0 and miginaname2[i][j+3]==0):
                    r[j+i+4][j+3]=r[j+i+4][j+3]+katasan
                elif (j>=1 and j<=14-i and miginaname2[i][j-1]==0 and miginaname2[i][j+3]==1) or (j==15-i and miginaname2[i][j-1]==0):
                    r[j+i][j-1]=r[j+i][j-1]+katasan
            #飛び三の判定
            if j<=14-i:
                if miginaname2[i][j]==2 and miginaname2[i][j+1]==0 and miginaname2[i][j+2]==2 and miginaname2[i][j+3]==2:
                    if j>=1 and j<=13-i and miginaname2[i][j-1]==0 and miginaname2[i][j+4]==0:
                        r[j+i][j-1]=r[j+i][j-1]+san
                        r[j+i+2][j+1]=r[j+i+2][j+1]+san
                        r[j+i+5][j+4]=r[j+i+5][j+4]+san
                    elif (j>=1 and j<=13-i and miginaname2[i][j-1]==1 and miginaname2[i][j+4]==0) or (j==0 and miginaname2[i][j+4]==0):
                        r[j+i+2][j+1]=r[j+i+2][j+1]+katasan
                        r[j+i+5][j+4]=r[j+i+5][j+4]+san
                    elif (j>=1 and j<=13-i and miginaname2[i][j-1]==0 and miginaname2[i][j+4]==1) or (j==15 and miginaname2[i][j-1]==0):
                        r[j+i][j-1]=r[j+i][j-1]+san
                        r[j+i+2][j+1]=r[j+i+2][j+1]+katasan
                elif miginaname2[i][j]==2 and miginaname2[i][j+1]==2 and miginaname2[i][j+2]==0 and miginaname2[i][j+3]==2:
                    if j>=1 and j<=13-i and miginaname2[i][j-1]==0 and miginaname2[i][j+4]==0:
                        r[j+i][j-1]=r[j+i][j-1]+san
                        r[j+i+3][j+2]=r[j+i+3][j+2]+san
                        r[j+i+5][j+4]=r[j+i+5][j+4]+san
                    elif (j>=1 and j<=13-i and miginaname2[i][j-1]==1 and miginaname2[i][j+4]==0) or (j==0 and miginaname2[i][j+4]==0):
                        r[j+i+3][j+2]=r[j+i+3][j+2]+katasan
                        r[j+i+5][j+4]=r[j+i+5][j+4]+san
                    elif (j>=1 and j<=13-i and miginaname2[i][j-1]==0 and miginaname2[i][j+4]==1) or (j==15 and miginaname2[i][j-1]==0):
                        r[j+i][j-1]=r[j+i][j-1]+san
                        r[j+i+3][j+2]=r[j+i+3][j+2]+katasan
            #2の判定
            if j<=16-i and miginaname2[i][j]==2 and miginaname2[i][j+1]==2:
                if j>=1 and j<=15-i and miginaname2[i][j-1]==0 and miginaname2[i][j+2]==0:
                    r[j+i][j-1]=r[j+i][j-1]+ni
                    r[j+i+3][j+2]=r[j+i+3][j+2]+ni
                elif (j>=1 and j<=15-i and miginaname2[i][j-1]==1 and miginaname2[i][j+2]==0) or (j==0 and miginaname2[i][j+2]==0):
                    r[j+3+i][j+2]=r[j+3+i][j+2]+katani 
                elif (j>=1 and j<=15-i and miginaname2[i][j-1]==0 and miginaname2[i][j+2]==1) or (j==16-i and miginaname2[i][j-1]==0):
                    r[j+i][j-1]=r[j+i][j-1]+katani
            #飛び二の判定
            if j<=15-i and miginaname2[i][j]==2 and miginaname2[i][j+1]==0 and miginaname2[i][j+2]==2:
                if j>=1 and j<=14-i and miginaname2[i][j-1]==0 and miginaname2[i][j+3]==0:
                    r[j+i][j-1]=r[j+i][j-1]+ni
                    r[j+i+2][j+1]=r[j+i+2][j+1]+ni
                    r[j+i+4][j+3]=r[j+i+4][j+3]+ni
                elif (j>=1 and j<=14-i and miginaname2[i][j-1]==1 and miginaname2[i][j+3]==0) or (j==0 and miginaname2[i][j+3]==0):
                    r[j+i+2][j+1]=r[j+i+2][j+1]+katani
                    r[j+i+4][j+3]=r[j+i+4][j+3]+ni
                elif (j>=1 and j<=14-i and miginaname2[i][j-1]==0 and miginaname2[i][j+3]==1) or (j==16 and miginaname2[i][j-1]==0):
                    r[j+i][j-1]=r[j+i][j-1]+ni
                    r[j+i+2][j+1]=r[j+i+2][j+1]+katani
            #1の判定
            if j<=17-i and miginaname2[i][j]==2:
                if j>=1 and j<=16-i and miginaname2[i][j-1]==0 and miginaname2[i][j+1]==0:
                    r[j+i][j-1]=r[j+i][j-1]+ichi
                    r[j+2+i][j+1]=r[j+2+i][j+1]+ichi
                elif (j>=1 and j<=16-i and miginaname2[i][j-1]==1 and miginaname2[i][j+1]==0) or (j==0 and miginaname2[i][j+1]==0):
                    r[j+2+i][j+1]=r[j+2+i][j+1]+kataichi
                elif (j>=1 and j<=16-i and miginaname2[i][j-1]==0 and miginaname2[i][j+1]==1) or (j==17-i and miginaname2[i][j-1]==0):
                    r[j+i][j-1]=r[j+i][j-1]+kataichi
            
            #左斜め方向の判定
            #先手番の判定
            #5の判定
            if j<=13-i and hidarinaname2[i][j]==1 and hidarinaname2[i][j+1]==1 and hidarinaname2[i][j+2]==1 and\
                          hidarinaname2[i][j+3]==1 and hidarinaname2[i][j+4]==1:
                              #print("先手番の勝ちです")
                              syouhai.append(1)
            #4の判定
            if j<=14-i and hidarinaname2[i][j]==1 and hidarinaname2[i][j+1]==1 and hidarinaname2[i][j+2]==1 and hidarinaname2[i][j+3]==1:
                if (j>=1 and j<=13-i and hidarinaname2[i][j-1]==2 and hidarinaname2[i][j+4]==0) or (j==0 and hidarinaname2[i][j+4]==0):
                    r[j+i+5][18-(j+4)]=r[j+i+5][18-(j+4)]+katayon
                elif (j>=1 and j<=13-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+4]==2) or (j==14-i and hidarinaname2[i][j-1]==0):
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+katayon
                elif j>=1 and j<=13-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+4]==0:
                    #print("先手番の勝ちです")
                    syouhai.append(1)
            #飛び四の判定
            if j<=13-i:
                if  hidarinaname2[i][j]==1 and hidarinaname2[i][j+1]==0 and hidarinaname2[i][j+2]==1 and hidarinaname2[i][j+3]==1 and\
                        hidarinaname2[i][j+4]==1:
                            r[j+i+2][18-(j+1)]=r[j+i+2][18-(j+1)]+katayon
                elif hidarinaname2[i][j]==1 and hidarinaname2[i][j+1]==1 and hidarinaname2[i][j+2]==0 and hidarinaname2[i][j+3]==1 and\
                         hidarinaname2[i][j+4]==1:
                            r[j+i+3][18-(j+2)]=r[j+i+3][18-(j+2)]+katayon
                elif hidarinaname2[i][j]==1 and hidarinaname2[i][j+1]==1 and hidarinaname2[i][j+2]==1 and hidarinaname2[i][j+3]==0 and\
                         hidarinaname2[i][j+4]==1:
                             r[j+i+4][18-(j+3)]=r[j+i+4][18-(j+3)]+katayon
            #3の判定
            if j<=15-i and hidarinaname2[i][j]==1 and hidarinaname2[i][j+1]==1 and hidarinaname2[i][j+2]==1:
                if j>=1 and j<=14-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+3]==0:
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+san
                    r[j+i+4][18-(j+3)]=r[j+i+4][18-(j+3)]+san
                elif (j>=1 and j<=14-i and hidarinaname2[i][j-1]==2 and hidarinaname2[i][j+3]==0) or (j==0 and hidarinaname2[i][j+3]==0):
                    r[j+i+4][18-(j+3)]=r[j+i+4][18-(j+3)]+katasan
                elif (j>=1 and j<=14-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+3]==2) or (j==15-i and hidarinaname2[i][j-1]==0):
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+katasan
            #飛び三の判定
            if j<=14-i:
                if hidarinaname2[i][j]==1 and hidarinaname2[i][j+1]==0 and hidarinaname2[i][j+2]==1 and hidarinaname2[i][j+3]==1:
                    if j>=1 and j<=13-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+4]==0:
                        r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+san
                        r[j+i+2][18-(j+1)]=r[j+i+2][18-(j+1)]+san
                        r[j+i+5][18-(j+4)]=r[j+i+5][18-(j+4)]+san
                    elif (j>=1 and j<=13-i and hidarinaname2[i][j-1]==2 and hidarinaname2[i][j+4]==0) or (j==0 and hidarinaname2[i][j+4]==0):
                        r[j+i+2][18-(j+1)]=r[j+i+2][18-(j+1)]+katasan
                        r[j+i+5][18-(j+4)]=r[j+i+5][18-(j+4)]+san
                    elif (j>=1 and j<=13-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+4]==2) or (j==15 and hidarinaname2[i][j-1]==0):
                        r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+san
                        r[j+i+2][18-(j+1)]=r[j+i+2][18-(j+1)]+katasan
                elif hidarinaname2[i][j]==1 and hidarinaname2[i][j+1]==1 and hidarinaname2[i][j+2]==0 and hidarinaname2[i][j+3]==1:
                    if j>=1 and j<=13-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+4]==0:
                        r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+san
                        r[j+i+3][18-(j+2)]=r[j+i+3][18-(j+2)]+san
                        r[j+i+5][18-(j+4)]=r[j+i+5][18-(j+4)]+san
                    elif (j>=1 and j<=13-i and hidarinaname2[i][j-1]==2 and hidarinaname2[i][j+4]==0) or (j==0 and hidarinaname2[i][j+4]==0):
                        r[j+i+3][18-(j+2)]=r[j+i+3][18-(j+2)]+katasan
                        r[j+i+5][18-(j+4)]=r[j+i+5][18-(j+4)]+san
                    elif (j>=1 and j<=13-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+4]==2) or (j==15 and hidarinaname2[i][j-1]==0):
                        r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+san
                        r[j+i+3][18-(j+2)]=r[j+i+3][18-(j+2)]+katasan
            #2の判定
            if j<=16-i and hidarinaname2[i][j]==1 and hidarinaname2[i][j+1]==1:
                if j>=1 and j<=15-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+2]==0:
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+ni
                    r[j+i+3][18-(j+2)]=r[j+i+3][18-(j+2)]+ni
                elif (j>=1 and j<=15-i and hidarinaname2[i][j-1]==2 and hidarinaname2[i][j+2]==0) or (j==0 and hidarinaname2[i][j+2]==0):
                    r[j+3+i][18-(j+2)]=r[j+3+i][18-(j+2)]+katani 
                elif (j>=1 and j<=15-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+2]==2) or (j==16-i and hidarinaname2[i][j-1]==0):
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+katani
            #飛び二の判定
            if j<=15-i and hidarinaname2[i][j]==1 and hidarinaname2[i][j+1]==0 and hidarinaname2[i][j+2]==1:
                if j>=1 and j<=14-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+3]==0:
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+ni
                    r[j+i+2][18-(j+1)]=r[j+i+2][18-(j+1)]+ni
                    r[j+i+4][18-(j+3)]=r[j+i+4][18-(j+3)]+ni
                elif (j>=1 and j<=14-i and hidarinaname2[i][j-1]==2 and hidarinaname2[i][j+3]==0) or (j==0 and hidarinaname2[i][j+3]==0):
                    r[j+i+2][18-(j+1)]=r[j+i+2][18-(j+1)]+katani
                    r[j+i+4][18-(j+3)]=r[j+i+4][18-(j+3)]+ni
                elif (j>=1 and j<=14-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+3]==2) or (j==16 and hidarinaname2[i][j-1]==0):
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+ni
                    r[j+i+2][18-(j+1)]=r[j+i+2][18-(j+1)]+katani
            #1の判定
            if j<=17-i and hidarinaname2[i][j]==1:
                if j>=1 and j<=16-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+1]==0:
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+ichi
                    r[j+2+i][18-(j+1)]=r[j+2+i][18-(j+1)]+ichi
                elif (j>=1 and j<=16-i and hidarinaname2[i][j-1]==2 and hidarinaname2[i][j+1]==0) or (j==0 and hidarinaname2[i][j+1]==0):
                    r[j+2+i][18-(j+1)]=r[j+2+i][18-(j+1)]+kataichi
                elif (j>=1 and j<=16-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+1]==2) or (j==17-i and hidarinaname2[i][j-1]==0):
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+kataichi
                     
            #後手番の判定
            #5の判定
            if j<=13-i and hidarinaname2[i][j]==2 and hidarinaname2[i][j+1]==2 and hidarinaname2[i][j+2]==2 and\
                          hidarinaname2[i][j+3]==2 and hidarinaname2[i][j+4]==2:
                              #print("後手番の勝ちです")
                              syouhai.append(2)
            #4の判定
            if j<=14-i and hidarinaname2[i][j]==2 and hidarinaname2[i][j+1]==2 and hidarinaname2[i][j+2]==2 and hidarinaname2[i][j+3]==2:
                if (j>=1 and j<=13-i and hidarinaname2[i][j-1]==1 and hidarinaname2[i][j+4]==0) or (j==0 and hidarinaname2[i][j+4]==0):
                    r[j+i+5][18-(j+4)]=r[j+i+5][18-(j+4)]+katayon
                elif (j>=1 and j<=13-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+4]==1) or (j==14-i and hidarinaname2[i][j-1]==0):
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+katayon
                elif j>=1 and j<=13-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+4]==0:
                    #print("後手番の勝ちです")
                    syouhai.append(2)
            #飛び四の判定
            if j<=13-i:
                if  hidarinaname2[i][j]==2 and hidarinaname2[i][j+1]==0 and hidarinaname2[i][j+2]==2 and hidarinaname2[i][j+3]==2 and\
                        hidarinaname2[i][j+4]==2:
                            r[j+i+2][18-(j+1)]=r[j+i+2][18-(j+1)]+katayon
                elif hidarinaname2[i][j]==2 and hidarinaname2[i][j+1]==2 and hidarinaname2[i][j+2]==0 and hidarinaname2[i][j+3]==2 and\
                         hidarinaname2[i][j+4]==2:
                            r[j+i+3][18-(j+2)]=r[j+i+3][18-(j+2)]+katayon
                elif hidarinaname2[i][j]==2 and hidarinaname2[i][j+1]==2 and hidarinaname2[i][j+2]==2 and hidarinaname2[i][j+3]==0 and\
                         hidarinaname2[i][j+4]==2:
                             r[j+i+4][18-(j+3)]=r[j+i+4][18-(j+3)]+katayon
            #3の判定
            if j<=15-i and hidarinaname2[i][j]==2 and hidarinaname2[i][j+1]==2 and hidarinaname2[i][j+2]==2:
                if j>=1 and j<=14-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+3]==0:
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+san
                    r[j+i+4][18-(j+3)]=r[j+i+4][18-(j+3)]+san
                elif (j>=1 and j<=14-i and hidarinaname2[i][j-1]==1 and hidarinaname2[i][j+3]==0) or (j==0 and hidarinaname2[i][j+3]==0):
                    r[j+i+4][18-(j+3)]=r[j+i+4][18-(j+3)]+katasan
                elif (j>=1 and j<=14-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+3]==1) or (j==15-i and hidarinaname2[i][j-1]==0):
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+katasan
            #飛び三の判定
            if j<=14-i:
                if hidarinaname2[i][j]==2 and hidarinaname2[i][j+1]==0 and hidarinaname2[i][j+2]==2 and hidarinaname2[i][j+3]==2:
                    if j>=1 and j<=13-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+4]==0:
                        r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+san
                        r[j+i+2][18-(j+1)]=r[j+i+2][18-(j+1)]+san
                        r[j+i+5][18-(j+4)]=r[j+i+5][18-(j+4)]+san
                    elif (j>=1 and j<=13-i and hidarinaname2[i][j-1]==1 and hidarinaname2[i][j+4]==0) or (j==0 and hidarinaname2[i][j+4]==0):
                        r[j+i+2][18-(j+1)]=r[j+i+2][18-(j+1)]+katasan
                        r[j+i+5][18-(j+4)]=r[j+i+5][18-(j+4)]+san
                    elif (j>=1 and j<=13-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+4]==1) or (j==15 and hidarinaname2[i][j-1]==0):
                        r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+san
                        r[j+i+2][18-(j+1)]=r[j+i+2][18-(j+1)]+katasan
                elif hidarinaname2[i][j]==1 and hidarinaname2[i][j+1]==2 and hidarinaname2[i][j+2]==0 and hidarinaname2[i][j+3]==2:
                    if j>=1 and j<=13-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+4]==0:
                        r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+san
                        r[j+i+3][18-(j+2)]=r[j+i+3][18-(j+2)]+san
                        r[j+i+5][18-(j+4)]=r[j+i+5][18-(j+4)]+san
                    elif (j>=1 and j<=13-i and hidarinaname2[i][j-1]==1 and hidarinaname2[i][j+4]==0) or (j==0 and hidarinaname2[i][j+4]==0):
                        r[j+i+3][18-(j+2)]=r[j+i+3][18-(j+2)]+katasan
                        r[j+i+5][18-(j+4)]=r[j+i+5][18-(j+4)]+san
                    elif (j>=1 and j<=13-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+4]==1) or (j==15 and hidarinaname2[i][j-1]==0):
                        r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+san
                        r[j+i+3][18-(j+2)]=r[j+i+3][18-(j+2)]+katasan
            #2の判定
            if j<=16-i and hidarinaname2[i][j]==2 and hidarinaname2[i][j+1]==2:
                if j>=1 and j<=15-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+2]==0:
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+ni
                    r[j+i+3][18-(j+2)]=r[j+i+3][18-(j+2)]+ni
                elif (j>=1 and j<=15-i and hidarinaname2[i][j-1]==1 and hidarinaname2[i][j+2]==0) or (j==0 and hidarinaname2[i][j+2]==0):
                    r[j+3+i][18-(j+2)]=r[j+3+i][18-(j+2)]+katani 
                elif (j>=1 and j<=15-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+2]==1) or (j==16-i and hidarinaname2[i][j-1]==0):
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+katani
            #飛び二の判定
            if j<=15-i and hidarinaname2[i][j]==2 and hidarinaname2[i][j+1]==0 and hidarinaname2[i][j+2]==2:
                if j>=1 and j<=14-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+3]==0:
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+ni
                    r[j+i+2][18-(j+1)]=r[j+i+2][18-(j+1)]+ni
                    r[j+i+4][18-(j+3)]=r[j+i+4][18-(j+3)]+ni
                elif (j>=1 and j<=14-i and hidarinaname2[i][j-1]==1 and hidarinaname2[i][j+3]==0) or (j==0 and hidarinaname2[i][j+3]==0):
                    r[j+i+2][18-(j+1)]=r[j+i+2][18-(j+1)]+katani
                    r[j+i+4][18-(j+3)]=r[j+i+4][18-(j+3)]+ni
                elif (j>=1 and j<=14-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+3]==1) or (j==16 and hidarinaname2[i][j-1]==0):
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+ni
                    r[j+i+2][18-(j+1)]=r[j+i+2][18-(j+1)]+katani
            #1の判定
            if j<=17-i and hidarinaname2[i][j]==2:
                if j>=1 and j<=16-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+1]==0:
                    r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+ichi
                    r[j+2+i][18-(j+1)]=r[j+2+i][18-(j+1)]+ichi
                elif (j>=1 and j<=16-i and hidarinaname2[i][j-1]==1 and hidarinaname2[i][j+1]==0) or (j==0 and hidarinaname2[i][j+1]==0):
                    r[j+2+i][18-(j+1)]=r[j+2+i][18-(j+1)]+kataichi
                elif (j>=1 and j<=16-i and hidarinaname2[i][j-1]==0 and hidarinaname2[i][j+1]==1) or (j==17-i and hidarinaname2[i][j-1]==0):
                   r[j+i][18-(j-1)]=r[j+i][18-(j-1)]+kataichi
        if row[i][j]==1 or row[i][j]==2:
            r[i][j]=0