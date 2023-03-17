class Solution:
    def DG(self, yu, id_start):
        global l_ls
        global tup

        for d_k in l_ls[id_start:]:
            if d_k>yu:
                break
            elif d_k==yu:
                tup+=(d_k,)
                L1.append(tup)
                tup=tup[:-1]
            else:
                tup+=(d_k,)
                self.DG(yu-d_k, l_ls.index(d_k))
                tup=tup[:-1]
    '''
    def Mam_Comb(self, Ml):
        Mll=[len(Ml[i]) for i in range(len(Ml))]
        Mmax=max(Mll)
        Mlli=[]
        for i in range(len(Mll)):
            if Mll[i]==Mmax:
                Mlli.append(i)
        
        return Mlli

    def Findmax(self, Ftl, Fl):
        Fs=''
        for fke,fval in Fl:
            while True:
                if fval in Ftl:
                    Fs+=str(fke)
                    Ftl.remove(fval)
                else: break
        return int(Fs)
    '''


    def largestNumber(self, cost: List[int], target: int) -> str:
        #intial cost in hashmap l_hm, simple listl_ls
        '''
        l_hm={}
        for i in range(len(cost)):
            l_hm[i+1]=cost[i]
        '''
        ll1=[9,8,7,6,5,4,3,2,1]
        global l_ls
        l_ls=sorted(list(set(cost)))
        #print(l_hm,l_ls)

        #make a list L1 to stroe all combination of tuples
        global L1
        L1=[]
        global tup
        tup=()
        self.DG(target,0)
        #print(L1)
        if len(L1)==0:
            return '0'
        #nl_l_hm=sorted(l_hm.items(), key=lambda x:x[0], reverse=True)
        #T_max=max(L1,key=len)
        len_max=max(len(x) for x in L1)
        TL2=[t for t in L1 if len(t)==len_max]
        #becasue the count same, the first num decide max
        cost_r=list(reversed(cost))
        Lm='0'
        for T2 in TL2:
            L2=[ll1[cost_r.index(i)] for i in T2]
            L2=''.join(map(str, sorted(L2, reverse=True)))
            if L2>Lm:
                Lm=L2

        return Lm
        '''
        #find the max count comb, transfer into num, add in the list L2
        L2i=[]
        L2=[]
        

        tem_l=sorted(l_hm.items(),key=lambda x:x[0],reverse=True)
        #l_hm_s={ke:valu for ke,valu in tem_l}
        #print(l_hm_s)
        L2i=self.Mam_Comb(L1)
        for n in range(len(L2i)):
            L2.append(self.Findmax(list(L1[L2i[n]]), tem_l))
        return str(max(L2))
        '''