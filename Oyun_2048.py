import random
import os
import msvcrt
global puan
puan=0
####################################################################################
def matris_olustur(mx,my):
    matris=[[0]*my for i in range(mx)]
    return matris
def yazdir(matris):
    global puan
    for i in range(len(matris)):
        for j in range(len(matris[0])):
            print matris[i][j],
        print
    print "\nPuaniniz:", puan
def sayi_koy(matris):
    toplam=0
    for i in range(len(matris)):
        for j in range(len(matris[0])):
            toplam+=matris[i][j]
    if toplam==0:
        for i in range(2):
            while 1:
                ky=random.randint(0,len(matris)-1)
                kx=random.randint(0,len(matris)-1)
                if matris[ky][kx]==0:
                    matris[ky][kx]=2
                    break
    else:
        while 1:
            ky = random.randint(0, len(matris) - 1)
            kx = random.randint(0, len(matris) - 1)
            if matris[ky][kx] == 0:
                matris[ky][kx] = 2
                break
    return matris
def kaydir_ust(matris):
    for k in range(len(matris)):
        for i in range(len(matris)-1):
            for j in range(len(matris)):
                if matris[i][j]==0:
                    matris[i][j],matris[i+1][j]=matris[i+1][j],matris[i][j]
    return matris
def toplat_ust(matris):
    global puan
    matris=kaydir_ust(matris)
    for i in range(len(matris)-1):
        for j in range(len(matris)):
            if matris[i][j]==matris[i+1][j]:
                matris[i][j]*=2
                matris[i+1][j]=0
                puan+=matris[i][j]
    matris=kaydir_ust(matris)
    return matris
def kaydir_sag(matris):
    for k in range(len(matris)):
        for i in range(len(matris)-1,-1,-1):
            for j in range(len(matris)-1,0,-1):
                if matris[i][j]==0:
                    matris[i][j],matris[i][j-1]=matris[i][j-1],matris[i][j]
    return matris
def toplat_sag(matris):
    global puan
    matris=kaydir_sag(matris)
    for i in range(len(matris)-1,-1,-1):
        for j in range(len(matris[0])-1,0,-1):
            if matris[i][j]==matris[i][j-1]:
                matris[i][j]*=2
                matris[i][j-1]=0
                puan+=matris[i][j]
    matris=kaydir_sag(matris)
    return matris
def kaydir_sol(matris):
    for k in range(len(matris)):
        for i in range(len(matris)):
            for j in range(len(matris[0])-1):
                if matris[i][j]==0:
                    matris[i][j],matris[i][j+1]=matris[i][j+1],matris[i][j]
    return matris
def toplat_sol(matris):
    global puan
    matris=kaydir_sol(matris)
    for i in range(len(matris)):
        for j in range(len(matris[0])-1):
            if matris[i][j]==matris[i][j+1]:
                matris[i][j]*=2
                matris[i][j+1]=0
                puan+=matris[i][j]
    matris=kaydir_sol(matris)
    return matris
def kaydir_alt(matris):
    for k in range(len(matris)):
        for i in range(len(matris)-1,0,-1):
            for j in range(len(matris)-1,-1,-1):
                if matris[i][j]==0:
                    matris[i][j],matris[i-1][j]=matris[i-1][j],matris[i][j]
    return matris
def toplat_alt(matris):
    global puan
    matris=kaydir_alt(matris)
    for i in range(len(matris)-1,0,-1):
        for j in range(len(matris)-1,-1,-1):
            if matris[i][j]==matris[i-1][j]:
                matris[i][j]*=2
                matris[i-1][j]=0
                puan+=matris[i][j]
    matris=kaydir_alt(matris)
    return matris
def oynat(yon,matris):
    global puan
    if yon=='w':
        matris=toplat_ust(matris)
        yazdir(matris)
    elif yon=='s':
        matris=toplat_alt(matris)
        yazdir(matris)
    elif yon=='d':
        matris=toplat_sag(matris)
        yazdir(matris)
    elif yon=='a':
        matris=toplat_sol(matris)
        yazdir(matris)
def kontrol(matris):
    drm=False
    for i in range(len(matris)-1):
        for j in range(len(matris[0])-1):
            if matris[i][j]==matris[i][j+1] or matris[i][j]==matris[i+1][j]:
                drm=True
    return drm
#################################################################################
matris=matris_olustur(4,4)
while 1:
    matris=sayi_koy(matris)
    yazdir(matris)
    if kontrol(matris)==True:
        yon=msvcrt.getche()
        oynat(yon,matris)
        os.system("cls")
    else:
        print"O Y U N  B I T T I"

