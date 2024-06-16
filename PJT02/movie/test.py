import sys
sys.stdin = open('API_KEY.txt')
API_KEYs = []
for i in sys.stdin.readlines():
    API_KEYs.append(i)
print(API_KEYs[0].rstrip(),API_KEYs[1])