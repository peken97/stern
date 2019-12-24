from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import json
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2
import numpy as np
import StarkLego.environments.env_low_height as environments
import threading



@api_view(['POST'])
def train(request):

    x = request.data['x']
    y = request.data['y']
    z = request.data['z']
    steps = request.data['steps']
    numberOfBlocks = request.data['numberOfBlocks']
    
    trainingThread = threading.Thread(target=runTrainingSession, args=(steps, x, y, z, numberOfBlocks))
    trainingThread.start()
    return HttpResponse("Damn")

def runTrainingSession(steps=0, x=0, y=0, z=0, numberOfBlocks=0):
    print("Started Thread")
    env = DummyVecEnv([lambda: environments.LegoEnv(x, y, z, numberOfBlocks+2)])

    model = PPO2(MlpPolicy, env, verbose=1)
    obs = env.reset()
    model.set_env(env)
    model.learn(total_timesteps=steps)
    obs = env.reset()
    
    info = None
    for i in range(numberOfBlocks):
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)

    print(info[0]['content'])
    return info[0]['content']

