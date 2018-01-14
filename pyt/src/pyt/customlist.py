from collections import Sequence

class customlist(Sequence):
    def __init__(self):
        self.data=[]

    def __len__(self):
        return len(self.data)

    def append(self,item):
        self.data.append(item)

    def remove(self,item):
        self.data.remove(item)

    def pop(self):
        if(len(self.data)==0):
            q=raw_input().decode('utf-8')
            try:
                qq=float(q)
                if("." not in q):
                    qq=int(qq)
            except ValueError:
                qq=q
                if(q[0]=='[' and q[-1]==']'):
                    return eval(q)
            else:
                return qq
        return self.data.pop()

    def __repr__(self):
        return str(self.data)

    def __getitem__(self,index):
        if isinstance(index, int):
            if(len(self.data)<abs(index)):
                q=raw_input().decode('utf-8')
                try:
                    qq=float(q)
                    if("." not in q):
                        qq=int(qq)
                except ValueError:
                    qq=q
                if(q[0]=='[' and q[-1]==']'):
                    qq=eval(q)
                self.data.append(qq)
                return qq
            else:
                return self.data[index]
        elif isinstance(index, slice):
            return self.data[index]

    def reverse(self):
        self.data.reverse()