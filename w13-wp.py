class University:
    def __init__(self,name):
        self.cps=[]
        self.name=name

class Canpus:
    def __init__(self,name):
        self.dps=[]
        self.name=name

class Department:
    def __init__(self,name):
        self.name=name
dic={"建功校區":["電機系","機械系","化材系","電子系","土木系"],"燕巢校區":["智商系","金資系","會資系","財稅系","觀光系"],"旗津校區":["電工系","輪機系","海資系","海工系","航運系"],"楠梓校區":["海生系","海管系","供管系","水產系","商資系"],"第一校區":["外語系","資管系","資工系","營建系","運籌系"]}

nkust=University("國立高雄科技大學")
a=-1
for key, value in dic.items():
    nkust.cps.append(Canpus(key))
    a=a+1
    for i in value:
        nkust.cps[a].dps.append(Department(i))