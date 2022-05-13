class villagemap:
    def __init__(self,vmap,lbound,rbound,dbound,ubound,curbuild,curbuildhp,basehp):
        self.vmap=vmap
        self.lbound=lbound
        self.rbound=rbound
        self.dbound=dbound
        self.ubound=ubound
        self.curbuild=curbuild
        self.curbuildhp=curbuildhp
        self.basehp=basehp
    
    def get_health(self):
        return (float(self.curbuildhp)/float(self.basehp))*100