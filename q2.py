import sys
import vcount

totalc=0
def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    f=open(filename,"r+")
    f1=f.read()
    print(f1)
    totalc=vcount.vc(f1)
if __name__ == '__main__':
   main()

#a=["a","e","i","o","u"]
    #c=0
    #def vc(t):
     #   global c
     #   for i in t:
      #       if i in a:
       #          c=c+1
        #print(c)


