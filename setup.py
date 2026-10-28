from setuptools import setup

package_name = 'turtle_duvar_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],  # <-- BURASI ÇOK ÖNEMLİ: Paket adını burada liste olarak vermelisin
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kagan',
    maintainer_email='kagan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'duvar_kontrol = turtle_duvar_py.duvar_kontrol:main',
        ],
    },
)
