# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:08:48 2024

@author: MPenella
"""
import time
from random import randint
from random import choice
from tabulate import tabulate

def roll(steps, dim=1):         #this is the function that runs the trials
    start_time = time.time()
    count = 0
    origin = [0,0,0]            #create universal timer, origin, and counter
    for cycle in range(100):
        particle = origin.copy()    
        #create particle at origin and repeat the following process 100 times
        for movement in range(steps):
            sign = choice([-1,1])    #decide step forward or backward      
            step = randint(0,dim-1)  #decide axis/direction to move on
            particle[step] += sign
            if particle == origin:  #check if particle returned to origin
                count +=1
                break               #if yes break from steps and add to count
    end_time = time.time()
    ttime = str(round(end_time-start_time, 3))
    return [f'{ttime}s', f'{count}%'] #return percentage and time elapsed

def main():
    raw_data = [                #create data from different options
        [roll(20,1), roll(200,1), roll(2000,1),
         roll(20000,1), roll(200000,1), roll(2000000,1) ],
        [roll(20,2), roll(200,2), roll(2000,2),
         roll(20000,2), roll(200000,2), roll(2000000,2) ],
        [roll(20,3), roll(200,3), roll(2000,3),
         roll(20000,3), roll(200000,3), roll(2000000,3) ]]
    
    #strip percentages and add to respective axis list
    stat_data= [['1D'],['2D'],['3D'],['Runtime:'],['3D']]
    for i in range(len(raw_data)):
        for j in range(len(raw_data[i])):
            stat_data[i].append(raw_data[i][j].pop())
    #strip times for 3D runs and add to runtime for 3D list
    for i in raw_data[2]:
        stat_data[4].append(i[0])
    
    #present data on table
    headers = ['number of steps:', '20', '200', '2,000', 
               '20,000', '200,000','2,000,000']
    print('Percentages of time particle returned to origin:')
    table = tabulate(stat_data, headers, tablefmt="grid")
    print(table)
    
main()#run
