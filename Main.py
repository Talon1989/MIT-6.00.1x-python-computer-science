import numpy as np;
import math as math
import matplotlib as mm;

def javaDifferences ():
    num = 1;
    # can't use num++, ** for Math.pow(),
    num += 1; # 2
    num **= 3; # 8
    num = math.sqrt(num+1);
    print(num);
    return;


# a = np.arange(15).reshape(3, 5);
javaDifferences();