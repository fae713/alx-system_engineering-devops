# Distributed Web Infrastructure

![1-distributed_web_infrastructure](https://github.com/Astrokojo/alx-system_engineering-devops/assets/60085282/d84054ae-c157-4560-9068-9b245a1bf57d)

https://github.com/fae713/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure

## Description

This is a distributed web infrastructure that uses a load balancer to reduce the traffic to the primary server by distributing some of the load from the master server to a replica server

## Specifics About This Infrastructure

+ The distribution algorithm the load balancer is configured with and how it works.<br/>Theload balancer uses a *Round Robin* distribution algorithm. It evenly distributes requests sequentially in a circular order.

+ The setup enabled by the load-balancer.<br/>The HAProxy load-balancer is setup as *Active-Passive*. It involves one active load balancer handling traffic while the passive one remains on standby, ready to take over in case the active one fails.

+ How a database *Primary-Replica* (*Master-Slave*) cluster works.<br/>The database cluster works as a setup with a Primary node, responsible for handling write operations and maintaining the authoritative database copy, and one or more Replica nodes that primarily serve read queries, provide redundancy, and act as backups.

+ Difference between the Primary node and the Replica node?<br/> Primary node can write and read, Replica can only read

## Issues With This Infrastructure

+ There are multiple SPOF (Single Point Of Failure).<br/>For example, if the Primary MySQL database server is down, the entire site would be unable to make changes to the site (including adding or removing users). The server containing the load balancer and the application server connecting to the primary database server are also SPOFs.

+ Security issues.<br/>The data transmitted over the network isn't encrypted using an SSL certificate so hackers can spy on the network. There is no way of blocking unauthorized IPs since there's no firewall installed on any server.

+ No monitoring.<br/>We have no way of knowing the status of each server since they're not being monitored.
