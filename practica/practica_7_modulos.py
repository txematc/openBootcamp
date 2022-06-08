import operaciones as o
import math
import pprint

def main():
    res = o.suma(3,7)
    resResta =o.resta(7,5)
    print("Hola, soy el main()", res, resResta)
    pprint.pprint(dir(math))
    
if __name__   == '__main__':
    main()