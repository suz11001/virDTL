import sys
import operator
import os
from collections import OrderedDict 
from operator import getitem 

def parse(directory):
    donors={}
    recipients={}
    pairs={}
    samples_path=directory
    for sample in os.listdir(samples_path):
        agg_input=(os.path.join(samples_path, sample))
        lines=[line.rstrip('\n') for line in open(agg_input)]
        for line in lines:
            if "Transfer, Mapping" in line:
                cols=line.split("-->")
                donor=cols[1].split(',')[0].lstrip().rstrip()
                recipient=cols[2].lstrip().rstrip()
                if donor in donors.keys():
                    donors[donor]+=1 
                else:
                    donors[donor]=1
                if recipient in recipients.keys():
                    recipients[recipient]+=1
                else:
                    recipients[recipient]=1
            
                if donor in pairs.keys():
                    if recipient in pairs[donor].keys():
                        pairs[donor][recipient]+=1
                    else:
                        pairs[donor][recipient]=1
                else:
                    pairs[donor]={}
                    pairs[donor][recipient]=1
                
    sorted_donors = sorted(donors.items(), key=operator.itemgetter(1), reverse=True)
    sorted_recipients= sorted(recipients.items(), key=operator.itemgetter(1), reverse=True)

    print("----")
    print "Top 10 donors:"
    for k in sorted_donors[:10]:
         print(k[0]+"\t"+str(k[1]))
    print("----")

    print "Top 10 recipients:"
    for k in sorted_recipients[:10]:
        print(k[0]+"\t"+str(k[1]))
    print("----")


    print "top transfer events"
    res = OrderedDict(sorted(pairs.items(), key=operator.itemgetter(1), reverse=True )) 
    for key in res.keys():
        for k in res.get(key):
            if res.get(key).get(k) > 800:
                print(key+"\t"+k+"\t"+str(res.get(key).get(k)))

    print("----")

    print "symmetric transfer events"
    done=[]
    for key in res.keys():
        for k in res.get(key):
            if res.has_key(k) and res.get(k).has_key(key) and ((res.get(key).get(k)) + (res.get(k).get(key)) > 700) :
                if key not in done and k not in done:
                    print(key+"\t"+k+"\t"+str(res.get(key).get(k))+"\t"+k+"\t"+key+"\t"+str(res.get(k).get(key)))
                    done.append(key)
                    done.append(k)

    print("----")

    print("all pairs of transfer events")
    for key in res.keys():
        for k in res.get(key):
            print(key+"\t"+k+"\t"+str(res.get(key).get(k)))     

    print("----")

    dict_unordered_pairs={}
    print("all pairs of transfer events unsymmetric")
    for key in res.keys():
         for k in res.get(key):
            t=(key,k)
            rev_t=(k,key)
            a=(res.get(key).get(k))
            #print(a)
            if rev_t in dict_unordered_pairs.keys():
                dict_unordered_pairs[rev_t]+=a
            else:
                dict_unordered_pairs[t]=a
    
    res2 = OrderedDict(sorted(dict_unordered_pairs.items(), key=operator.itemgetter(1), reverse=True ))
    for key in res2.keys(): 
        print(','.join(key)+"\t"+str(res2.get(key)))
    
    print("------")
    
    print("top transfer events - unordered")
    for key in res2.keys():
        if res2.get(key) > 700:
            try:
                if res.get(key[0]) is None:
                    print(','.join(key)+"\t"+str(res2.get(key))+"\t"+key[1]+"-"+str(res.get(key[1]).get(key[0])))
                elif res.get(key[1]) is None:
                    print(','.join(key)+"\t"+str(res2.get(key))+"\t"+key[0]+"-"+str(res.get(key[0]).get(key[1])))
                else:
                    print(','.join(key)+"\t"+str(res2.get(key))+"\t"+key[0]+"-"+str(res.get(key[0]).get(key[1]))+"\t"+key[1]+"-"+str(res.get(key[1]).get(key[0])))
            except Exception  as e:
                print('problem: '+ str(e))
                print(','.join(key)+"\t"+str(res2.get(key))) 
                print(res.get(key[0]).get(key[1]))
                print(res.get(key[1]).get(key[0]))
                print("---")

    print("---")
    print("transfer events for calde of interest")
    for key in res2.keys():
        #change interal node name and/or leaf node names to search for transfer events in clade of interest
        if "n46" in key or "n47" in key or "n49" in key or "NC0455122" in key:
                if res.get(key[0]) is None:
                    print(','.join(key)+"\t"+str(res2.get(key))+"\t"+key[1]+"-"+str(res.get(key[1]).get(key[0])))
                elif res.get(key[1]) is None:
                    print(','.join(key)+"\t"+str(res2.get(key))+"\t"+key[0]+"-"+str(res.get(key[0]).get(key[1])))
                else:
                    print(','.join(key)+"\t"+str(res2.get(key))+"\t"+key[0]+"-"+str(res.get(key[0]).get(key[1]))+"\t"+key[1]+"-"+str(res.get(key[1]).get(key[0])))

        
if __name__ == "__main__":
    directory=sys.argv[1]
    parse(directory)

