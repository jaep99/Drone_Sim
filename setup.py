from setuptools import setup, find_packages

setup(
    name='GT_Campus_Nav_Drone',  
    version='0.1.0',             
    packages=find_packages(),    
    install_requires=[           
        'dronekit>=2.9.2',       
        'pymavlink>=2.4.41',     
        'mavproxy>=1.8.71',      
        'numpy>=1.20.0',         
        # 'wxPython>=4.1.1',     # Optional for visualizing
    ],
    entry_points={
        'console_scripts': [
            'start-sitl=scripts.start_sitl:main',
            'start-mavproxy=scripts.start_mavproxy:main',
        ],
    },
    python_requires='>=3.8',     
    author='Hyeonjae Park',      
    author_email='hyeonjae.park990813@gmail.com',  
    description='Campus navigation drone project using ArduPilot and MAVProxy.',
    url='https://github.com/jaep99/GT_Campus_Nav_Drone',
)
