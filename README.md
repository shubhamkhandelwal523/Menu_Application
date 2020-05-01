Hello User !!
Here is the file of my docker "TUI" project that name is "dockerproject.py" that make your life simple into the docker world . The program is fully build up and easy to use . A very simple to use this, in the program you have to "PRESS NO : " that you want to do inside the docker.
You don't have to write the all furter command (You have to press and it willl create for you ")
The docker project is you can use it as a remotely and locally. Locally you can use without giving an IPAddress
but If you want to use it remotely you have to write the IP .

** Very Important : For using the any command you have to start the docker first")

** For using the docker compose file the file ("docker-compose.yml")

for starting the docker-compose you have to use ("docker-compose up")
for stop the docker-compose you have to use ("docker compose down/stop") or you can use "ctrl+c".
** IF someone is facing issue while running the docker-compose : use the cmds given below it will work file :
iptables -F
iptables -P FORWARD ACCEPT
firewall-cmd --zone=trusted --change-interface=dockerO --permanent
(If there are any other networks for docker add them too like br -xxxx)
firewall-cmd --zone=trusted --add-masquerade --permanent
firewall-cmd --reload
firewall-cmd --add-port= 3306/tcp
systemctl restart docker
** some cmds of firewalld

systemctl enable firewalld
systemctl disable firewalld or systemctl stop firewalld
{ I would like to Thank The "WORLD RECORD HOLDER :- MR. VIMAL SIR" & " PREETI MAM " for a great initiative .
I created this project under the mendorshhip of Vimal sir }
