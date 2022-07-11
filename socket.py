from socket import *
import numpy as np
import os
HOST = "127.0.0.1"
PORT = 9001
s = socket(AF_INET, SOCK_STREAM)
print ('Socket created')
s.bind((HOST, PORT))
print ('Socket bind complete')
s.listen(1)
print ('Socket now listening')
#print(s)

while True:

   #접속 승인
    conn, addr = s.accept()
    print("Connected by ", addr)
    # 글자수 세기
    idx = 0
    idx2 = 0
   #데이터 수신
    rc = conn.recv(1024)
    rc = rc.decode("utf8").strip()
    if not rc: break
    for i in range(len(rc)):
        if rc[i]=="+":
            idx = i
        if rc[i]=="/":
            idx2 = i
    rc1 = rc[0:idx]
    rc2 = rc[idx+1:idx2]
    rc3 = rc[idx2+1:]
        
    #print("rc1:",rc1)
    #print("rc2:",rc2)
    #print("rc3:",rc3)
    

    print('출발지:',rc1)
    print('경유지:',rc2)
    print('도착지:',rc3)

    #클라이언트에게 답을 보냄
    #res = "AIcenter"
    #conn.sendall(res.encode("utf-8"))
    #연결 닫기
    #conn.close()
    #break


#파일보내기
data_transferred = 0


file_size = os.path.getsize(r'C:\Users\USER\Desktop\2021-2\해커톤\그린지도.png')
print('File Size:', file_size, 'bytes')


conn.send(str(file_size).encode())


with open(r'C:\Users\USER\Desktop\2021-2\해커톤\그린지도.png', 'rb') as f:#현재dir에 filename으로 파일을 받는다     
    
    data = f.read(1) #1024바이트 읽는다
    while data: #데이터가 없을 때까지
        conn.send(data) #1024바이트 보내고 크기 저장
        data_transferred += 1
        data = f.read(1) #1024바이트 읽는다
            


print("전송완료 ,전송량 %d" %(data_transferred))


s.close()

