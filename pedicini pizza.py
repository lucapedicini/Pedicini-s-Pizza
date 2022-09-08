from simpful import *

FS = FuzzySystem()

TLV = AutoTriangle(3, terms=['poor', 'average', 'good'], universe_of_discourse=[0,10])
FS.add_linguistic_variable("service", TLV)
FS.add_linguistic_variable("quality", TLV)

O1 = TriangleFuzzySet(0,0,13,   term="low")
O2 = TriangleFuzzySet(0,13,25,  term="medium")
O3 = TriangleFuzzySet(13,25,25, term="high")
FS.add_linguistic_variable("tip", LinguisticVariable([O1, O2, O3], universe_of_discourse=[0,25]))

FS.add_rules([
	"IF (quality IS poor) OR (service IS poor) THEN (tip IS low)",
	"IF (service IS average) THEN (tip IS medium)",
	"IF (quality IS good) OR (quality IS good) THEN (tip IS high)"
	])
i = False
while(i!=True):
    qualita_cibo = input("Vota la qualità del cibo con un numero da 0 a 10: ")
    if(any(c.isalpha() for c in qualita_cibo)==False):
        q = float(qualita_cibo)
        if(q>=0 and q<=10):
            i = True
        else:
            print("Il valore deve essere compreso tra 0 e 10\n")
    else:
        print("Il valore deve essere un numero\n")

u = False
while(u!=True):
    qualita_servizio = input("Vota la qualità del servizio con un numero da 0 a 10: ")
    if(any(c.isalpha() for c in qualita_servizio)==False):
        s = float(qualita_servizio)
        if(s>=0 and s<=10):
            u = True
            print("\n")
        else:
            print("Il valore deve essere compreso tra 0 e 10\n")
    else:
        print("Il valore deve essere un numero\n")        

FS.set_variable("quality", q) 
FS.set_variable("service", s) 

tip = FS.inference()
print("Ecco la mancia da pagare: ",round(tip["tip"],2),"€")
