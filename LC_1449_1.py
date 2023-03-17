import sys
class Solution:

    def largestNumber(self, cost, target):
        def OPT(ol, od):
            #find the max count
            omax_count=0
            oold=0
            for ot in ol:
                onew=0
                for oi in range(len(ot)//2):
                    onew+=ot[oi*2+1]
                if oold<onew:
                    oold=onew
            #put all max count comb into List
            oL=[]
            for ot in ol:
                onew=0
                for oi in range(len(ot)//2):
                    onew+=ot[oi*2+1]
                if onew==oold:
                    ostr=[]
                    for oi in range(len(ot)//2):
                        thevalue=str(GK(ot[oi*2],od))
                        ostr+=[thevalue for nn in range(ot[oi*2+1])]
                    ostr=''.join(sorted(ostr,reverse=True))
                    oL.append(int(ostr))
            return oL

        def GK(gv, gd):
            for k in gd.keys():
                if gd[k]==gv:
                    return k

        def DG(yu, l1):
            global t_record
            for k in l1:
                if yu%k==0:
                    comb_l.append(t_record+(k,yu//k))
                elif yu//k==0:
                    continue
                else:
                    t_record+=(k,yu//k)
                    DG(yu%k, l1[:l1.index(k)]+l1[l1.index(k)+1:])
                    t_record=t_record[:-2]
        #make hashmap for cost {i:cost}
        hashmap={}
        for i in range(len(cost)):
            hashmap[i+1]=cost[i]
        
        #sort the list and remove repeat
        cost_new=sorted(list(set(cost)))

        #digui by counts
        comb_l=[]
        global t_record
        count_max=target//cost_new[0]

        while count_max:
            for k in cost_new:
                t_record=(k, count_max)
                if k*count_max==target:
                    comb_l.append(t_record)
                elif k*count_max<target:
                    DG(target-k*count_max, cost_new[:cost_new.index(k)]+cost_new[cost_new.index(k)+1:])
            count_max-=1
        #print(comb_l)
        #comb_l: [ (value, count, value2, count2 ...)  ]
        #final L: [combine_num from big to small (int)]
        if len(comb_l)==0:
            print('0')
            sys.exit(0)
        f_L=[]
        #make hashmap form max to mini
        hashl_s=sorted(hashmap.items(),key=lambda x:x[0], reverse=True)
        hashmap_s={h_k:h_v for h_k,h_v in hashl_s}
        
        f_L=OPT(comb_l, hashmap_s)
        
        f_L.sort(reverse=True)
        print(str(f_L[0]))

s=Solution()
s.largestNumber([6,10,15,53,43,53,51,47,43], 89)