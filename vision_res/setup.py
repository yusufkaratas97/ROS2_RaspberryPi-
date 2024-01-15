from setuptools import find_packages, setup

package_name = 'vision_res'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='reeng',
    maintainer_email='yusufmasri231998@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_node = vision_res.simple_publisher:main',
            'subscriber_node = vision_res.simple_subscriber:main',
        ],
    },
)
