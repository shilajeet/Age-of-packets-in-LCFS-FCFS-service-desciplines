import numpy as np
import matplotlib.pyplot as plt 
import math

#Server utilisation vector(\rho=\lambda/\mu is the server utilisation vector)
rho=[0.2,0.3,0.4,0.5,0.6,0.7,0.8];

#Total number of Monte Carlo iterations
Monte_Carlo=5;

#Length of time horizon
T=10000;

#List to store the final AoI
age_final=[];

for utilisation in range(0,len(rho)):
     
     #Variable to store age corresponding to each rho 
     age_2=0;
     
     for iterate in range(0,Monte_Carlo):
          
          #Variable to store the age for each Monte_carlo iteration
          age_1=0;
          
          #List to store arrival epochs of each packets
          arrival=[];
          
          #List to store the interarrival times
          arrival_duration=[];
          
          #initializing the arrival list with a random variable
          arrival.append(np.random.exponential(1/rho[utilisation]));
          arrival_duration.append(arrival[0]);
          
          #list to store the service time for each packet
          service_duration=[];
          
          #initializing the service time list with a random variable
          service_duration.append(np.random.exponential(1));
          
          while (arrival[-1]<=T):
               service_duration.append(np.random.exponential(1));
               arrival_duration.append(np.random.exponential(1/rho[utilisation]));
               arrival.append(arrival[-1]+arrival_duration[-1]);
               
          #List to store the time at which each packet leaves the queue
          leaving_time=[];
          
          #initializing the list leaving_time
          leaving_time.append(arrival[0]+service_duration[0]);
          
          #List to store the index of packets that left the queue
          pack_left_index=[];
          pack_left_index.append(0);
          
          #List to store the duration packets that complete the entire service process spend in the queue
          packet_time=[];
          
          index=0;
          
          while(leaving_time[-1]<arrival[-1]):
               
               counter=0;
               
               while(arrival[counter]<leaving_time[-1]):
                    counter=counter+1;
                    
               if(index==counter-1):
                    leaving_time.append(arrival[counter]+service_duration[counter]);
                    index=counter;
                    
               else:
                    leaving_time.append(leaving_time[-1]+service_duration[counter-1]);
                    index=counter-1;
                    
               pack_left_index.append(index);
               
          for i in range(0,len(pack_left_index)):
               
               packet_time.append(leaving_time[i]-arrival[pack_left_index[i]]);
               
          #Arrival delay of packets that left the queue
          pack_arr_delay=[];
          
          for i in range(0,len(pack_left_index)):
               pack_arr_delay.append(arrival[pack_left_index[i]]-arrival[pack_left_index[i-1]]);
               
          for i in range(0,len(pack_left_index)-1):
               age_1=age_1+(pack_arr_delay[i+1]*packet_time[i]+math.pow(pack_arr_delay[i+1],2)/2);
               
          age_1=age_1+((packet_time[-1])**2)/2;
          
          age_1=age_1/T;
          
          age_2=age_2+age_1;
          
     age_final.append(age_2/Monte_Carlo); 
               
#Generate plots     
plt.plot(rho,age_final,linestyle='dashed',color='orange',linewidth=2);
plt.xlabel(r"server utilisation $\rho$",color='blue');
plt.ylabel(r"Age $\Delta$",color='blue');
plt.title("Variation of age for FCFS M/M/1 queue for various arrival rates",color='magenta');
plt.grid(True,alpha=0.8);
plt.show();          
                    
                    
               
               