# Simple Web Stack

![0-simple_web_stack](https://github.com/fae713/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/293570121-90dbb7f9-3d55-401e-92a0-a3f803548f76.png)
https://github.com/fae713/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack
## Description

This is a simple web infrastructure with a single server that hosts a website that is reachable via `www.foobar.com`.
## Specifics About This Infrastructure

+ What a server is?<br/>A server is a computer hardware or software that provides data, resources, or services to other computers or devices on a network.

+ The role of the domain name.<br/>The role of a domain name is to provide a human-readable address for accessing resources on the internet. www.foobar.com is human-readable but numbers like 8.8.8.8 is not

+ The type of DNS record `www` is in `www.foobar.com`.<br/>`www.foobar.com` uses a CNAME. This can be checked by running `dig www.foobar.com`.<br/>The record then matches `www.foobar.com` to `foobar.com` which is used to find the A record
<i>Address Mapping record (A Record)—also known as a DNS host record, stores a hostname and its corresponding IPv4 address.</i>

+ The role of the web server.<br/>The web server is a software/hardware that accepts requests via HTTP or secure HTTP (HTTPS) and responds with the content of the requested resource or an error messsage.

+ The role of the application server.<br/>To install, operate and host applications and associated services for end users, IT services and organizations and facilitates the hosting and delivery of high-end consumer or business applications

+ The role of the database.<br/>To maintain a collection of organized information that can easily be accessed, managed and updated

+ What the server uses to communicate with the client (computer of the user requesting the website).<br/>Communication between the client and the server occurs over the internet network through the TCP/IP protocol suite.

## Issues With This Infrastructure

+ There are multiple SPOF (Single Point Of Failure) in this infrastructure.<br/>For example, if the MySQL database server is down, the entire site would be down. Same goes for everyother component.

+ Downtime For Maintenance.<br/>Maintenance checks will be needed at some point in the future. Any component being checked will result in the component to be put down or the server to be turned off. Since there's only one server, the website would be experiencing a significant amount of downtime until its turned back on.

+ Scalability.<br/>Increasing the scale of this infrastructure would be very difficult becauses it uses only one server. The server can and will run out of available resources when traffic increases past a certain point.
