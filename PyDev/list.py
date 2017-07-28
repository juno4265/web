orders = ['Park','Moon','Kim','Joo']
orders.append('Jake')
orders.insert(2, 'Nam')
print("",orders[2])

import sys
if len(sys.argv) !=2:
    print ("Please supply a filename")
    raise SystemExit(1)
file = open(sys.argv[1])
lines = file.readlines()
file.close()

# 모든 입력 값을 문자열에서 실수로 변환 합니다 
fvalues = [float(line) for line in lines]

# 최소값과 최대값을 출력합니다
print("Maximum",max(fvalues))
print("Minimum",min(fvalues))
