import os
import gym
import multiprocessing

class Config:
    env_name = 'CartPole-v0'
    mode = 'discrete' #discrete/continuous

    gamma = .99
    num_hidden = 128
    lr = 1e-4
    checkpoints = 3

    save_freq = 250
    max_episode_len = 300
    buffer_len = 30

    load_model = False
    model_path = './model'
    if not os.path.exists(model_path):
        os.makedirs(model_path)

    num_workers = 1 #multiprocessing.cpu_count() 

    game = gym.make(env_name)
    s_size = len(game.reset()) 
    if mode == 'discrete':
        a_size = game.action_space.n
    else:
        a_size = game.action_space.shape[0]
        a_bound = [game.action_space.low, game.action_space.high]
        a_gap = game.action_space.high - game.action_space.low
        max_ep_step = 400