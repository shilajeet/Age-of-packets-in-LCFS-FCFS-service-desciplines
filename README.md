# Age of packets in LCFS-FCFS service desciplines

## Simulation Setup
We consider a single queue and a single user generating packets in exponentially distributed intervals with rate $\lambda$ and the service rate of the packets is $\mu$. We run the simulation for time $T=20000$ slots with $\lambda \in [0.2,0.8]$ in steps of $0.1$ and have assumed the service rate to be $\mu=1$. Time averaged age metric has been used evaluated using equations (2) to (5) of paper [*Real-time status: How often should one update?*](https://ieeexplore.ieee.org/document/6195689). Finally we plot the variation of average age wrt server utilisation $(\rho=\lambda/\mu)$. In M/D/1 we have assumed each packet takes time $D=1$ to get served while for D/M/1 each packet is generated after a fixed duration $D=1/\rho$.

In LCFS, the newest arriving packet in the queue is served first. Here we have simulated two possibilities- with preemption and without preemption. Under LCFS without preemption any old packet waiting in the queue is replaced by a new packet while the packet currently being serviced is allowed to finish it's service. Then the newest packet waiting in the queue is allowed to service. While in LCFS with preemption, the packet currently under service is preempted with the newest packet arriving in the queue i.e it's service is halted and the new packet is allowed to finish it's service and thereafter the halted packet can finish it's remaining service duration. 

## References
[1] [*Real-time status: How often should one update?*](https://ieeexplore.ieee.org/document/6195689)

[2] [*Status Updates Through Queues*](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.726.6036&rep=rep1&type=pdf)
