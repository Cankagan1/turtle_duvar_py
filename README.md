🐢 Duvardan Kaçan Kaplumbağa (ROS 2 Humble & Turtlesim)

Bu proje, ROS 2 Humble mimarisi ve `rclpy` (Python istemci kütüphanesi) kullanılarak geliştirilmiş otonom bir engel kaçınma (obstacle avoidance) simülasyonudur. Popüler `turtlesim` simülatöründeki kaplumbağanın konumunu anlık olarak takip eden, sınır ihlallerini algılayan ve dinamik olarak yön değiştiren bir ROS 2 düğümü (node) barındırır.

---

## 📋 Proje Mimarisi ve İstekler

Ödev kapsamında karşılanan temel gereksinimler şunlardır:
1. **Paket Yapısı:** `rclpy`, `geometry_msgs` ve `turtlesim` bağımlılıklarını içeren ament_python tabanlı `turtle_duvar_py` paketi.
2. **Abone (Subscriber):** `/turtle1/pose` konusuna (topic) abone olunarak kaplumbağanın $(x, y)$ koordinatlarının anlık takibi.
3. **Yayıncı (Publisher):** `/turtle1/cmd_vel` konusuna hız komutları (`Twist`) yayınlanarak kaplumbağanın sürülmesi.
4. **Loglama (Logging):** `rclpy`'nin yerleşik `get_logger().info()` fonksiyonu kullanılarak kaplumbağanın güncel konumunun saniyede bir konsola yazdırılması.
5. **Bonus (Parametre Desteği):** Hareket hızlarının (`linear_speed`, `angular_speed`) ve çalışma sınırlarının (`min_limit`, `max_limit`) ROS 2 parametreleri üzerinden dinamik olarak ayarlanabilmesi.

---

## ⚙️ Sistem Gereksinimleri

* Ubuntu 22.04 LTS
* ROS 2 Humble Hawksbill
* Python 3.10+

---

## 🚀 Kurulum ve Derleme Adımları

Eğer projenizi henüz workspace'inize kurduysanız, sırasıyla şu adımları izleyin:

1. **Çalışma Alanınıza (Workspace) gidin ve paketinizin `src` altında olduğundan emin olun:**
   ```bash
   cd ~/ros2_ws
