import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class DuvardanKacanKaplumbaga(Node):

    def __init__(self):
        super().__init__('duvardan_kacan_kaplumbaga')

        self.declare_parameter('linear_speed', 8.0)
        self.declare_parameter('angular_speed', 2.5)
        self.declare_parameter('min_limit', 1.8)
        self.declare_parameter('max_limit', 9.2)

        self.linear_speed = self.get_parameter('linear_speed').value
        self.angular_speed = self.get_parameter('angular_speed').value
        self.min_limit = self.get_parameter('min_limit').value
        self.max_limit = self.get_parameter('max_limit').value

        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

        self.current_pose = None

        # Durumlar: ileri, geri, dön
        self.state = 'ileri'
        self.state_counter = 0

        # Dönüş yönü: 1 veya -1
        self.turn_direction = 1

        self.control_timer = self.create_timer(
            0.1,
            self.control_loop
        )

        self.log_timer = self.create_timer(
            1.0,
            self.log_konum
        )

        self.get_logger().info(
            'Duvardan Kaçan Kaplumbağa başlatıldı!'
        )

    def pose_callback(self, msg: Pose):
        self.current_pose = msg

    def control_loop(self):

        if self.current_pose is None:
            return

        move_msg = Twist()

        x = self.current_pose.x
        y = self.current_pose.y

        duvara_yakin = (
            x < self.min_limit or
            x > self.max_limit or
            y < self.min_limit or
            y > self.max_limit
        )

        # 1. İleri hareket
        if self.state == 'ileri':

            if duvara_yakin:

                self.state = 'geri'
                self.state_counter = 8

                # Her kaçışta dönüş yönünü değiştir
                self.turn_direction *= 1

                self.get_logger().info(
                    'Duvara yaklaşıldı! Geri kaçılıyor.'
                )

                move_msg.linear.x = -1.0
                move_msg.angular.z = 0.0

            else:

                move_msg.linear.x = self.linear_speed
                move_msg.angular.z = 0.0

        # 2. Geri gitme
        elif self.state == 'geri':

            move_msg.linear.x = -1.0
            move_msg.angular.z = 0.0

            self.state_counter -= 1

            if self.state_counter <= 0:
                self.state = 'don'
                self.state_counter = 15

        # 3. Yön değiştirme
        elif self.state == 'don':

            move_msg.linear.x = 0.0
            move_msg.angular.z = (
                self.angular_speed * self.turn_direction
            )

            self.state_counter -= 1

            if self.state_counter <= 0:
                self.state = 'ileri'

        self.publisher_.publish(move_msg)

    def log_konum(self):

        if self.current_pose is not None:

            self.get_logger().info(
                f'Konum -> X: {self.current_pose.x:.2f}, '
                f'Y: {self.current_pose.y:.2f}, '
                f'Theta: {self.current_pose.theta:.2f}, '
                f'Durum: {self.state}'
            )


def main(args=None):

    rclpy.init(args=args)

    node = DuvardanKacanKaplumbaga()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        # Düğüm kapanırken kaplumbağayı durdur
        stop_msg = Twist()
        node.publisher_.publish(stop_msg)

        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
