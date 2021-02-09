from navigation_env import NavigationEnvDefault, NavigationEnvAcc, NavigationEnvAccLidarObs
#
from gym.envs import register
from config import *

custom_envs = {}
for idx, obs_conf in enumerate(config_set):
    custom_envs['Navi-Vel-Full-Obs-Task%d-v0'.format(idx)] = dict(
                 path='navigation_2d:NavigationEnvDefault',
                 max_episode_steps=1000,
                 kwargs=dict(obstacles_args=obs_conf))
    custom_envs['Navi-Acc-Full-Obs-Task%d-v0'.format(idx)] = dict(
                 path='navigation_2d:NavigationEnvAcc',
                 max_episode_steps=1000,
                 kwargs=dict(obstacles_args=obs_conf))
    custom_envs['Navi-Acc-Lidar-Obs-Task%d-v0'.format(idx)] = dict(
                 path='navigation_2d:NavigationEnvAccLidarObs',
                 max_episode_steps=1000,
                 kwargs=dict(obstacles_args=obs_conf))

# register each env into
def register_custom_envs():
    for key, value in custom_envs.items():
        arg_dict = dict(id=key,
                        entry_point=value['path'],
                        max_episode_steps=value['max_episode_steps'],
                        kwargs=value['kwargs'])
        if 'reward_threshold' in value.keys():
            arg_dict['reward_threshold'] = value['reward_threshold']
        register(**arg_dict)

register_custom_envs()