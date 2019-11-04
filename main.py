import time

# input idea: I have a reoccuring appointment every [nD] [xDay] every [nM] Month every [nY] year for [ys] Years, starting this [sM].

# sM starting Month (jan, feb, ...)
# xDays [monday = 0, tuesday = 1, wednesday = 2, thursday = 3, friday = 4, saturday = 5, sunday = 6,]
# nD every nth xDay of nM
# nM every nth month of nY
# nY every nth Year for ys Years
#ys amount of years
def isSJ(y): #prüft ob y ein schaltjahr ist
    if y in range(2020, y+1, 4):
        return True
    else:
        return False

def getWeekday(d,y):
    return time.strftime('%A', time.strptime(d+str(y),'%j%Y')) #nimmt tag im jahr von 001 bis 366 und jahr, gibt name des wochentages

def isNthWeekdayOfMonth(n,m,d,y): # m -> '01' - '12'
    mA = [] #array von allen tagen des monats nach der struktur [[Monday, 001],[Tuesday, 002]]
    if m in ['01','03','05','07','08','10','12']:
        for i in range(1,32):
                mA.append([time.strftime('%A', time.strptime(str(i).zfill(2)+m+str(y),'%d%m%Y')),time.strftime('%j', time.strptime(str(i).zfill(2)+m+str(y),'%d%m%Y'))])
    elif m == '02':
        if isSJ(y):
            for i in range(1,30):
                mA.append([time.strftime('%A', time.strptime(str(i).zfill(2)+m+str(y),'%d%m%Y')),time.strftime('%j', time.strptime(str(i).zfill(2)+m+str(y),'%d%m%Y'))])
        else:
            for i in range(1,29):
                mA.append([time.strftime('%A', time.strptime(str(i).zfill(2)+m+str(y),'%d%m%Y')),time.strftime('%j', time.strptime(str(i).zfill(2)+m+str(y),'%d%m%Y'))])
    else:
        for i in range(1,31):
            mA.append([time.strftime('%A', time.strptime(str(i).zfill(2)+m+str(y),'%d%m%Y')),time.strftime('%j', time.strptime(str(i).zfill(2)+m+str(y),'%d%m%Y'))])

    wD = getWeekday(str(d).zfill(3),y) #zfill füllt eine nummer die durch einen string repräsentiert wird mit nullen auf '1'.zfill(2) -> '01'
    wDC = 0 #zähler
    for i in range(len(mA)):
        if mA[i][0] == wD: #wenn
            wDC += 1
            if wDC == n and mA[i][1] == str(d).zfill(3):
                return True




def isNMonth(s,n,d,y): #s -> starting Month
    m = int(time.strftime('%m', time.strptime(str(d).zfill(3)+str(y),'%j%Y')))
    if m in range(s,12+1,n):
        return True
    else:
        return False

def getDates(sM,  nD,  xDay,         nM,  nY,  ys):
    #        int, int, weekday name, int, int, int
    cY = int(time.strftime('%Y', time.localtime())) #aktuelles Jahr als int
    dates_out = []
    for i in range (cY, cY+ys+1, nY):
        if isSJ(i):
            for b in range(1,367):
                if isNMonth(sM, nM, b, i):
                    sM = 1
                    if getWeekday(str(b).zfill(3),i) == xDay:
                        if isNthWeekdayOfMonth(nD,time.strftime('%m', time.strptime(str(b)+str(i),'%j%Y')),b,i):
                            dates_out.append(time.strftime('%a, %d.%m.%Y', time.strptime(str(b)+str(i),'%j%Y')))
        else:
            for b in range(1,366):
                if isNMonth(sM, nM, b, i):
                    sM = 1
                    if getWeekday(str(b).zfill(3),i) == xDay:
                        if isNthWeekdayOfMonth(nD,time.strftime('%m', time.strptime(str(b)+str(i),'%j%Y')),b,i):
                            dates_out.append(time.strftime('%a, %d.%m.%Y', time.strptime(str(b)+str(i),'%j%Y')))
    return dates_out

print(getDates(3, 3, 'Tuesday', 2,2,3))
