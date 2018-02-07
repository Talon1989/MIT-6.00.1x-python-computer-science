import numpy as np;
import math as math
import matplotlib as mm;

import CourseAlgorithms


def javaDifferences():
    num = 1;
    # can't use num++, ** for Math.pow(),
    num += 1;  # 2
    num **= 3;  # 8
    num = math.sqrt(num + 1);
    print(num);

    # PRINT
    print("hello" + "world");
    print("hello", "world");  # ',' means +' '+

    # ARRAY
    potato = "potato";
    potato[:2];  # 'po'
    potato[1:3];  # 'ot'
    potato[::2];  # skips 2 start from 0 'ptt'
    potato[1::2];  # skips 2 start from 1 'oao'
    print(potato[1:])  # 'otato'

    # CASTING
    x = 1;  # int
    x_str = str(x);  # equivalent of (String) x
    print(type(x_str));

    # INPUT
    while True:
        try:
            my_variable = input("Type anything...");  # input = new Scanner(System.in).nextLine();
            my_int_variable = int(input("Type a number"));  # casts into an int, Integer.parseInt();
            print(my_int_variable);
            break;
        except ValueError:
            print("Count not convert data to integer");

    # FOR LOOP
    for i in range(5): # 0 1 2 3 4
        print(i);
    print();
    for i in range(0, 6, 2): # from 0 to 5, increments by 2
        print(i);



def findNum(num: int, arr, startNum: int, endNum: int):
    mid = (startNum + endNum) // 2;
    print("start: " + str(startNum) + " / end: " + str(endNum));
    print("mid: " + str(mid) + " / number at mid: " + str(arr[mid]) + " / number to find: " + str(num));
    if num == arr[mid]:
        print("should yes")
        return True;
    elif startNum == endNum or startNum == endNum - 1 or startNum == endNum + 1:
        print("should exit");
        return False;
    elif num < arr[mid]:
        print("LESS : current " + str(arr[mid]) + " / want: " + str(num));
        findNum(num, arr, startNum, mid);
    elif num > arr[mid]:
        print("MORE : current " + str(arr[mid]) + " / want: " + str(num));
        findNum(num, arr, mid, endNum);
    print("noff");
    return;


def alpha (s):
    temp_count = 0; total_count = 0; last_position = 0;
    for i in range(len(s)-1):
        if s[i] <= s[i+1]:
            if temp_count > total_count:
                total_count = temp_count;
                last_position = i+1;
            temp_count += 1;
        else:
            temp_count = 0;
    start_postion = last_position-total_count;
    print("longest alphabetical word :", s[start_postion:last_position+1])

# arr = [0,2,4,6,8,10,12,14,16];
# print(findNum(12, arr, 0, len(arr)));
a = np.arange(15).reshape(3, 5);
alpha_string = "abcdaacdefghabd";
alpha(alpha_string);
print("iterating ...");
CourseAlgorithms.approximationCubeRoot(29);