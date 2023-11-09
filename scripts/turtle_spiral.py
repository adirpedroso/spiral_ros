#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def turtle_spiral():
    rospy.init_node('turtle_spiral', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    # Velocidade angular inicial
    angular_speed = 1.0

    # Raio inicial e taxa de aumento
    initial_radius = 8.0
    radius_increase_rate = 0.01

    while not rospy.is_shutdown():
        twist = Twist()

        # Velocidade linear  
        twist.linear.x = 1.0

        # Velocidade angular em relação ao raio atual
        twist.angular.z = angular_speed

        pub.publish(twist)
        rate.sleep()

        # Aumento gradualmente o raio para criar a espiral
        initial_radius += radius_increase_rate

        # Velocidade angular para acelerar a espiral 
        angular_speed += 0.01

if __name__ == '__main__':
    try:
        turtle_spiral()
    except rospy.ROSInterruptException:
        pass


#LEMBRAR: Pra iniciar preciso dar catkin_make e principalmente source devel/setup.bash em todos terminais que eu for usar
#Preciso antes de tudo iniciar o ROS com: roscore
#Comando pra executar o ambiente do turtle: rosrun turtlesim turtlesim_node
#E por ultimo iniciar o script com: rosrun turtle_spiral turtle_spiral.py
