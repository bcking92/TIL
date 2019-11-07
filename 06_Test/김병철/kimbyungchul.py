import socket
import time
import math

# User and Game Server Information
NICKNAME = 'Python Player'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0    
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData):
    # 1. 타겟에서 가장 가까운 홀 순으로 탐색
    sorted_holes = []
    my_ball = gameData.balls[0]
    target_hole = HOLES[0]
        #1.1 타겟 선정
    for i in range(1, len(gameData.balls)):
        ball = gameData.balls[i]
        if ball[0] or ball[1]:
        #1.2 거리 계산
            for j in range(6):
                dist = (HOLES[j][0] - ball[0]) ** 2 + (HOLES[j][1] - ball[1]) ** 2
                sorted_holes.append([dist, j])
            sorted_holes.sort()
    # 2. 득점할 수 있는지 확인
            if (my_ball[0] - ball[0]):
                incline = (my_ball[1] - ball[1])/(my_ball[0] - ball[0])
            else:
                incline = 99999999
            if incline < 99999999:
                if incline:
                    vertical = -1/incline
                else:
                    vertical = 99999999
            else:
                vertical = 0.000001
            a = ball[1] - vertical * ball[0]
            direction = [ball[0]-my_ball[0], ball[1]-my_ball[1]]
            for hole in sorted_holes:
                print(f'hole={hole}')
                print(f'sorted_holes={sorted_holes}')
                if direction[0] >= 0:
                    if direction[1] >= 0:
                        if HOLES[hole[1]][0] > ((HOLES[hole[1]][1] - a) / vertical) and HOLES[hole[1]][1] > (HOLES[hole[1]][0] * vertical + a):
                            target_hole = HOLES[hole[1]]
                            break
                        else:
                            continue
                    else:
                        if HOLES[hole[1]][0] > ((HOLES[hole[1]][1] - a) / vertical) and HOLES[hole[1]][1] < (HOLES[hole[1]][0] * vertical + a):
                            target_hole = HOLES[hole[1]]
                            break
                        else:
                            continue
                else:
                    if direction[1] >= 0:
                        if HOLES[hole[1]][0] < ((HOLES[hole[1]][1] - a) / vertical) and HOLES[hole[1]][1] > (HOLES[hole[1]][0] * vertical + a):
                            target_hole = HOLES[hole[1]]
                            break
                        else:
                            continue
                    else:
                        if HOLES[hole[1]][0] < ((HOLES[hole[1]][1] - a) / vertical) and HOLES[hole[1]][1] < (HOLES[hole[1]][0] * vertical + a):
                            target_hole = HOLES[hole[1]]
                            break
                        else:
                            continue
    # 3. 파울이 나는가?
    # 4. 각도 계산
            
            direction_to_hole = [target_hole[0] - ball[0], target_hole[1] - ball[1]]
            target_xy = [ball[0] + (direction_to_hole[0] * (-math.sqrt(8))/math.sqrt(direction_to_hole[0]**2 + direction_to_hole[1] ** 2)), ball[1] + (direction_to_hole[1] * (-math.sqrt(8))/math.sqrt(direction_to_hole[0]**2 + direction_to_hole[1] ** 2))]
            break
    print(f'direction_to_hole = {direction_to_hole}')
    print(f'target_xy = {target_xy}')
    print(f'my_ball = {my_ball}')
    print(f'ball = {ball}')
    print(f'sorted_holes = {sorted_holes}')
    print(f'target_hole = {target_hole}')
    ######################################################################################
    # 주어진 정보를 바탕으로 샷을 할 방향과 세기를 결정해서 angle, power 값으로 지정 #
    ######################################################################################
    dx = target_xy[0] - my_ball[0]
    dy = target_xy[1] - my_ball[1]
    gakdo = (target_xy[1] - my_ball[1])/(target_xy[0] - my_ball[0])
    print(f'gakdo = {gakdo}')
    angle_radian = math.atan(gakdo)
    angle_temp = math.degrees(angle_radian)
    print(f'angle_temp = {angle_temp}')
    print(f'dx = {dx}, dy = {dy}')
    if dx < 0 and dy > 0:
        angle_temp += 180
    elif dx < 0 and dy < 0:
        angle_temp += 180
    if angle_temp <= 90:
        angle = 90 - angle_temp
    else:
        angle = 450 - angle_temp
    print(f'angle = {angle}')
    power = 30 + math.sqrt(hole[1])/math.sqrt(84500) * 180 + (abs(target_xy[0] - my_ball[0]) + abs(target_xy[1] - my_ball[1]))/390 * 180
    conn.send(angle, power)
def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        if gameData.balls[0][0] == 9909:
            break
        play(conn, gameData)        
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()
