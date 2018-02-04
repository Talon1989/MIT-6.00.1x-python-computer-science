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


def findNum (num: int, arr, startNum: int, endNum: int):
    mid = (startNum+endNum) // 2;
    print("start: "+str(startNum)+" / end: "+str(endNum));
    print("mid: "+str(mid)+" / number at mid: "+str(arr[mid])+" / number to find: "+str(num));
    if num == arr[mid]:
        print("should yes")
        return "yes";
    elif startNum == endNum or startNum == endNum-1 or startNum == endNum+1:
        print("should exit");
        return "no";
    elif num < arr[mid]:
        print("LESS : current "+str(arr[mid])+" / want: "+str(num));
        findNum(num, arr, startNum, mid);
    elif num > arr[mid]:
        print("MORE : current "+str(arr[mid])+" / want: "+str(num));
        findNum(num, arr, mid, endNum);
    print("noff");
    return "no";


# a = np.arange(15).reshape(3, 5);
# javaDifferences();
arr = [0,2,4,6,8,10,12,14,16];
print(findNum(12, arr, 0, len(arr)));