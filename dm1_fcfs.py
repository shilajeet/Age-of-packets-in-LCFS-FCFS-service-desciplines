"""
implementation of S.Kaul and Roy Yates paper for FCFS D/M/1 queue

Algorithm:
     In a FCFS queue, the arrivals to the queue are status updates generated by a single user according to a Poisson process of rate lambda=0.2,0.4,0.6 and 0.8 respectively. Since the queue is D/M/1 which is deterministic arrivals, the arrivals are like 1/0.2; 1/0.4 etc. The service times are exponentially distributed with rate mu=1.
     
"""

import numpy as np
import matplotlib.pyplot as plt 
import math

#Server utilisation vector(\rho=\lambda/\mu is the server utilisation vector)
rho=[0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9];

#Total number of Monte Carlo iterations
Monte_Carlo=10;

#Length of time horizon
T=20000;

#List to store the final AoI
age_final=[];

for utilisation in range(0,len(rho)):
     
     #Variable to store age corresponding to each rho 
     age_2=0;
     
     for iterate in range(0,Monte_Carlo):
          
          #Variable to store the age for each Monte_carlo iteration
          age_1=0;
          
          #List to store the arrivals epochs of packets
          arrival=[];
          
          #List to store the interarrival times
          arrival_duration=[];
          
          #initializing the arrival list with a random variable
          arrival.append(1/rho[utilisation]);
          
          #list to store the service time for each packet
          service_duration=[];
          
          #initializing the service time list with a random variable
          service_duration.append(np.random.exponential(1));
          
          #List to store leaving time for each packet
          leaving_time=[];
          
          #initializing the leaving_time list with a random variable
          leaving_time.append(arrival[0]+service_duration[0]);
          
          #Variable to store the total number of updates made
          count=1;
          
          #List to store service time + waiting time for each of the packets which is the time packet spends in the queue
          packet_time=[];
          
          while(leaving_time[-1]<=T):
               
               arrival_duration.append(1/rho[utilisation]);
               
               arrival.append(arrival[-1]+arrival_duration[-1]);
               
               service_duration.append(np.random.exponential(1));
               
               count=count+1;
               
               if(leaving_time[-1]<arrival[-1]):
                    
                    leaving_time.append(arrival[-1]+service_duration[-1]);
                    
               elif(leaving_time[-1]>=arrival[-1]):
                    
                    leaving_time.append(leaving_time[-1]+service_duration[-1]);
               
          for i in range(0,count):
               packet_time.append(leaving_time[i]-arrival[i]);
          
          #Calculation of age refer equation (2)-(4) of paper
          for i in range(0,count-2):
               age_1=age_1+(arrival_duration[i+1]*packet_time[i]+math.pow(arrival_duration[i+1],2)/2);
          
          age_1=age_1+((packet_time[-1])**2)/2;
                   
          age_1=age_1/T;
          
          age_2=age_2+age_1;
          
     age_final.append(age_2/Monte_Carlo);
          
#Generate plots     
plt.plot(rho,age_final,linestyle='dashed',color='orange',linewidth=2);
plt.xlabel(r"server utilisation $\rho$",color='blue');
plt.ylabel(r"Age $\Delta$",color='blue');
plt.title("Variation of age for FCFS D/M/1 queue for various arrival rates",color='magenta');
plt.grid(True,alpha=0.8);
plt.show();        
          
          
               
               
               
               
               
               
               
          
               
               
          
          
     
     
     
    
     
     

     
     