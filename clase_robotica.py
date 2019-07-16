from random import randint
import rodi
import time
robot= rodi.RoDI()
#Movimiento para adelante
# robot.move_forward()
# time.sleep(1)
# robot.move_stop()
# #Movimiento para la izquierda
# robot.move_left()
# time.sleep(0.5)
# robot.move_stop()

# robot.move_right()
# time.sleep(0.6)
# robot.move_stop()
# robot.move_backward()
# time.sleep(0.6)
# robot.move_stop()
# ##############
# robot=rodi.RoDI()
# robot.move_left()
# time.sleep(0.40)
# robot.move_stop()
# robot.move.move_right()
# time.sleep(0.20)
# robot.move_stop()
# #sensor de distancia
# print(robot.see(), "centimetros")

'''
variable = 3

try:
    while True:
        print(robot.see(),"centimetros")
        
        if robot.see() <= 10:
            print(robot.see(),"variable")
            robot.move_stop()
        else:
            robot.move_forward()
except KeyboardInterrupt:
    print("finalizado")
    robot.move_stop()
'''
#########
'''
try:
    while True:
        cm=robot.see()
        if cm<=20:
            robot.move_forward()
        else:
            robot.move_stop()
            robot.move_right()
            time.sleep(0.5)
        robot.pixel(randint(0,100),randint(0,100),randint(0,100))
        time.sleep(0.5)
except KeyboardInterrupt:
    print("finalizado")
    robot.move_stop()
#robot.move(100.100)
# '''
# while True:
#     print(robot.light())
#     time.sleep(0.5)
# robot.sing(120,2000)

#seguidor de linea
while True:
    linea = robot.sense()
    print(linea)
    print(linea[0])
    print(linea[1])
    time.sleep(0.5)