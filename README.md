# navigation_2d
2d navigation gym environment implemented by pyBox2d 

![alt text](./images/display.png?raw=true)

## Installation
~~~~
pip install navigation_2d
~~~~


## Start
~~~~
'''
observation: ['position', 'distance', 'lidar', 'energy', 'obstacle_speed', 'obstacle_position']
Action: velocity
'''
gym.make('Navi-Vel-Full-Obs-Task{task}_{difficulty}-v0')
gym.make('Navi-Vel-Full-Obs-Random-Init-Task{task}_{difficulty}-v0')
~~~~

~~~~
'''
observation: ['position', 'distance', 'lidar', 'energy', 'obstacle_speed', 'obstacle_position', 'velocity']
Action: accleration
'''
gym.make('Navi-Acc-Full-Obs-Task{task}_{difficulty}-v0')
~~~~

~~~~
'''
observation: ['position', 'distance', 'lidar', 'energy', 'velocity']
Action: accleration
'''
gym.make('Navi-Acc-Lidar-Obs-Task{task}_{difficulty}-v0')
~~~~

~~~~
'''
observation: ['position', 'distance', 'lidar', 'energy', 'velocity']
Action: accleration
Non stationary Environment
difficulty: easy, task: non-stationary
'''
gym.make('Non-Stationary-Navigation_dyn_{dynamics}_unc_{uncertainty}-v0')
~~~~

## Info
|Difficulty|Obstacles|
|------|------|
|easy|3 circular obstacles|
|normal|2 circular obstacle, 2 horizontal obstacles|
|hard|3 circular obstacle, 2 vertical obstacles|
|very_hard|3 circular obstacle, 2 horizontal obstacles, 2 vertical obstacles|

|Task|Goal position (If not random-init, Start Position=(0.5, 0.5))|
|-----|-----|
|0|(0.2, 0.2) (position is normalized)|
|1|(0.2, 0.8)|
|2|(0.8, 0.8)|
|3|(0.8, 0.2)|
|4|(0.0756, 0.5)|
|5|(0.5, 0.0756)|
|6|(0.924, 0.5)|
|7|(0.5, 0.924)|

|Option|Description|methods|default|
|-----|-----|-----|-----|
|random_init|make initialize points random.|env.set_random_init(bool)|False|
|collision_done|if it collides with an obstacle, the episode ends.|env.set_collision_done(bool)|True|