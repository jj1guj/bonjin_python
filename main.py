import time
import random
import copy
from hantei import hantei

row=[[0]*19]*19
clm=[[row[i][j] for i in range(19)] for j in range(19)]
miginaname1=[[row[j][j+k] for j in range(19-k)] for k in range(11)]
miginaname2=[[row[j+k][j] for j in range(19-k)] for k in range(11)]
miginaname2.pop(0)

hidarinaname1=[[row[j][14-j-k] for j in range(19-k)] for k in range(11)]
hidarinaname2=[[row[j+k][14-j] for j in range(19-k)] for k in range(11)]
hidarinaname2.pop(0)

r=[[0 for j in range(19) if row[i][j]==0] for i in range(19)]
sente=[[0 for j in range(19) if row[i][j]==0] for i in range(19)]
gote=[[0 for j in range(19) if row[i][j]==0] for i in range(19)]

r1=row

basyo=[]
maxindex=[]

syouhai=[]

soutesu=0

katayon=1000000
san=50000
katasan=500
ni=200
katani=100
ichi=50
kataichi=20

def init():
    row=[[0]*19]*19
    clm=[[row[i][j] for i in range(19)] for j in range(19)]
    miginaname1=[[row[j][j+k] for j in range(19-k)] for k in range(11)]
    miginaname2=[[row[j+k][j] for j in range(19-k)] for k in range(11)]
    miginaname2.pop(0)

    hidarinaname1=[[row[j][14-j-k] for j in range(19-k)] for k in range(11)]
    hidarinaname2=[[row[j+k][14-j] for j in range(19-k)] for k in range(11)]
    hidarinaname2.pop(0)

    r=[[0 for j in range(19) if row[i][j]==0] for i in range(19)]
    sente=[[0 for j in range(19) if row[i][j]==0] for i in range(19)]
    gote=[[0 for j in range(19) if row[i][j]==0] for i in range(19)]
    return row,clm,miginaname1,miginaname2,hidarinaname1,hidarinaname2,r,sente,gote

def nyuryoku():
    gyou,retu=map(int,input("指し手を行、列の順に空白で区切って入力してください：").split())
    #row[19*(gyou-1)+retu-1]=1
    gyou=gyou-1
    retu=retu-1
    if soutesu%2==1:
        a=1
    else:
        a=2
    row[gyou][retu]=a

def hyouji():
    r1=copy.deepcopy(row)
    
    i=0
    j=0
    
    while i<19:
        while j<19:
            if r1[i][j]=="*":
                r1[i][j]="＊"
            elif r1[i][j]==1:
                r1[i][j]="●"
            elif r1[i][j]==2:
                r1[i][j]="○"
            
            if j<14:
                print(str(r1[i][j]),end="")
            else:
                print(str(r1[i][j]))
            j=j+1
        j=0
        i=i+1
    print("")

def utu():
    i=0
    basyo=[]
    saidai=[]
    while i<=14:
        saidai.append(max(r[i]))
        i=i+1
    #print(saidai)
    i=0
    while i<=14:
        j=0
        maxindex=[k for k, x in enumerate(r[i]) if x==max(saidai)]
        while j<len(maxindex):
            basyo.append([i,maxindex[j]])
            j=j+1
        i=i+1
    #print(basyo)
    
    a=random.randint(0,len(basyo)-1)
    #if soutesu<=225:
        #print("["+str(basyo[a][0]+1)+","+str(basyo[a][1]+1)+"]")
    
    gyou=basyo[a][0]
    retu=basyo[a][1]
    
    if soutesu%2==1:
        a=1
    else:
        a=2
    row[gyou][retu]=a

yotei=int(input("何局実行しますか？："))
starttime=time.time()
soutesu=1
taikyokusu=0

while taikyokusu<yotei:
    taikyokusu=taikyokusu+1
    #print(str(taikyokusu)+"局目")
    soutesu=1
    row,clm,miginaname1,miginaname2,hidarinaname1,hidarinaname2,r,sente,gote=init()
    while soutesu<226:
        if soutesu==1:
            #print(str(soutesu)+"手目")
            row[7][7]=1
        
        clm=[[row[i][j] for i in range(19)] for j in range(19)]
        miginaname1=[[row[j][j+k] for j in range(19-k)] for k in range(11)]
        miginaname2=[[row[j+k][j] for j in range(19-k)] for k in range(11)]
        miginaname2.pop(0)
        
        hidarinaname1=[[row[j][14-j-k] for j in range(19-k)] for k in range(11)]
        hidarinaname2=[[row[j+k][14-j] for j in range(19-k)] for k in range(11)]
        hidarinaname2.pop(0)
        
        r=[[0 for j in range(19)] for i in range(19)]
        sente_kougeki=[[0 for j in range(19) if row[i][j]==0] for i in range(19)]
        sente_bougyo=[[0 for j in range(19) if row[i][j]==0] for i in range(19)]
        gote_kougeki=[[0 for j in range(19) if row[i][j]==0] for i in range(19)]
        gote_bougyo=[[0 for j in range(19) if row[i][j]==0] for i in range(19)]
        for i in range(19):
            for j in range(19):
                if soutesu%2==1:
                    hantei()
                else:
                    hantei()
                if row[i][j]==1 or row[i][j]==2:
                    r[i][j]=0
                if len(syouhai)>=taikyokusu and (syouhai[len(syouhai)-1]==1 or syouhai[len(syouhai)-1]==2):
                    break
            if len(syouhai)>=taikyokusu and (syouhai[len(syouhai)-1]==1 or syouhai[len(syouhai)-1]==2):
                break
        #hyouji_r()
        soutesu=soutesu+1
        utu()
        #print("")
        if len(syouhai)>=taikyokusu and (syouhai[len(syouhai)-1]==1 or syouhai[len(syouhai)-1]==2):
            #print(str(soutesu-1)+"手")
            #print("syouhai=",end="")
            #print(syouhai)
            #hyouji()
            break
        #if soutesu<=225:
            #print(str(soutesu)+"手目")
        if soutesu>225:
            syouhai.append(3)
            #print(syouhai)
            #print("引き分けです")
            #print("225手")
            #hyouji()
    if taikyokusu%100==0:
        if taikyokusu==100:
            keika1=starttime
        keika=time.time()
        print(str(taikyokusu)+"局目"+" 先手勝率:"+str(syouhai.count(1)/taikyokusu*100)+"%",end="")
        print("  後手勝率:"+str(syouhai.count(2)/taikyokusu*100)+"%"+" 引き分け:"+str(syouhai.count(3)/taikyokusu*100)+"%",end="")
        print("     "+str(keika-starttime)+"sec",end="")
        print("     "+str(100/(keika-keika1)*3600)+"局/h")
        keika1=keika
#hyouji()
#print("syouhai=",end="")
#print(syouhai)
#print("先手勝ち："+str(syouhai.count(1)))
#print("後手勝ち："+str(syouhai.count(2)))
#print("引き分け："+str(syouhai.count(3)))
endtime=time.time()
interval=endtime-starttime
print(str(interval)+"sec")
print("100局あたり："+str((100*interval)/yotei)+"sec")