import os
import getpass
os.system("tput setaf 3")
print("***********************************************************************************")
os.system("tput setaf 7")
print("HEY !! Here Is my docker TUI project that make your life simple in the docker world")
os.system("tput setaf 3")
print("***********************************************************************************")
os.system("tput setaf 4")
passwd = getpass.getpass("Enter Your Password :")

apass = "redhat"

if passwd != apass:
    print("Authentication Incorrect")
    exit()

os.system("tput setaf 7")
print("Where You Would Like To Perform Your Job (local/remote) :" , end='')
location = input()
print(location)

if location == "remote":
    remoteIP = input("Enter Your IP :")
os.system("tput setaf 3")
os.system("figlet \t\t DOCKER WORLD !")
os.system("tput setaf 9")
print("IMPORTANT : TO PERFORM ANY TASK YOU HAVE TO START THE DOCKER USING PRESS 4:")
os.system("tput setaf 1")
while True:                                                                                                                                                                                       
            print("Press 1: To Install Docker community edition.")                                                                                                                                 
            print("Press 2: To create gedit file")                                                                                                                                               
            print("Press 3: TO open gedit file and see repo list")                                                                                                                                     
            print("Press 4: To start/stop/restart of  docker/httpd/firewall/")                                                                                                                   
            print("Press 5: To check docker version/running container/repository/images etc. using example just you have to type the name like(version/ps/images).")                             
            print("Press 6: To Pull images from docker i.e. ubuntu,centos,mysql,worpress,php etc. But before pulling the images, you have to start the docker,httpd etc.")                       
            print("Press 7: To create a new container images without giving any name ,only you have to give image name(ubuntu:14.04/mycentos etc.)")                                             
            print("Press 8: To create a new container images with giving any name of the container image eg.(topOS ,pop etc.) ,only you have to give image name (ubuntu:14.04/mycentos etc.)")   
            print("Press 9: To check the list of the container")                                                                                                                                 
            print("Press 10: To install the net-tools/wget etc.using yum.")                                                                                                                      
            print("Press 11: To remove all the containers.")                                                                                                                                     
            print("Press 12: To inspect anything eg.(web,container image,IPAddress,MacAddress etc)")                                                                                             
            print("Press 13: To check free space in memory.")                                                                                                                                    
            print("Press 14: Enable httpd server permanent inside docker")                                                                                                                       
            print("Press 15: To push your container image to docker hub (but should have a docker hub account to post the images there)")                                                     
            print("Press 16: To check the netstat -tnlp")                                                                                                                                        
            print("Press 17: How many images you have (centos/worpress/mysql etc.)")                                                                                                             
            print("Press 18: To curl the IP")                                                                                                                                                    
            print("Press 19: To curl URL using sSL just input URL name")                                                                                                                         
            print("Press 20: To commit the docker image and repository file")                                                                                                                    
            print("Press 21: To check the Gateway of the container")                                                                                                                             
            print("Press 22: To create a new volume inside docker ")                                                                                                                             
            print("Press 23: To check volume list ")                     
            print("Press 24: Exit")                                                                                                                                                                     

            
            print("Press any no. that you want to perform :" , end='') 
            ch = input()
            print(ch)

            if location == "local":
                if int(ch) == 1:
                    os.system("tput setaf 7")
                    os.system("yum install docker-ce --nobest")
                elif int(ch) == 2:
                    print("Give file name only :" ,end='')
                    file_name = input()
                    os.system("tput setaf 7")
                    os.system("gedit {}".format(file_name))
                elif int(ch) == 3:
                    os.system("tput setaf 7")
                    os.system("gedit docker.repo")
                elif int(ch) == 4:
                    print("Enter what you want to do start/stop/restart :" ,end ='')
                    create_name = input()
                    os.system("systemctl {} ".format(create_name))
                    print("Enter your choice docker/httpd/firewall etc. :" , end ='')
                    create_name = input()
                    os.system("tput setaf 7")   
                    os.system("systemctl start {} ".format(create_name))
                elif int(ch) == 5:
                    print("Enter what you want to check :" ,end ='')
                    check_name = input(ch)
                    os.system("tput setaf 6")
                    os.system("docker {} ".format(check_name))
                elif int(ch) == 6:
                    print("Enter image name to pull :" ,end ='')
                    image_name = input(ch)
                    os.system("tput setaf 6")
                    os.system("docker pull {} ".format(image_name))
                elif int(ch) == 7:
                    print("Enter image name to create container :" ,end ='')
                    image_name = input()
                    os.system("tput setaf 6")
                    os.system("docker run -it {}".format(image_name))
                elif int(ch) == 8:
                    print("Give name to the container :",end = '')
                    name = input()
                    os.system("docker container run -it  --name {}".format(name))
                    print("Enter image name to create container :" ,end ='')
                    image_name = input()
                    os.system("docker run -it {}".format(image_name))
                    print("Press :0 To exit")
                    os.system("exit")
                elif int(ch) == 10:
                    print("Enter what yo install :",end='')
                    install_name = input()
                    os.system("tput setaf 6")
                    os.system("yum install {}".format(install_name))
                elif int(ch) == 11:
                    os.system("tput setaf 5")
                    os.system("docker rm -f $(docker ps -a -q)")
                elif int(ch) == 12:
                    print("what you want to inspect :",end='')
                    inspect_name = input()
                    os.system("tput setaf 6")
                    os.system("docker inspect {}".format(inspect_name))
                elif int(ch) == 13:
                    os.system("tput setaf 5")
                    os.system("free -m")
                elif int(ch) == 14:
                    os.system("tput setaf 5")
                    os.system("cd /var/run/httpd/")
                elif int(ch) == 15:
                    print("Enter User ID and image name (eg. shubham523/webserver:v2) :",end='')
                    enter_name = input()
                    os.system("tput setaf 5")
                    os.system("docker push {}".format(enter_name))
                elif int(ch) == 16:
                    os.system("tput setaf 5")
                    os.system("netstat -tnlp")
                elif int(ch) == 17:
                    print("Enter Image name :" ,end='')
                    image_name = input()
                    os.system("tput setaf 5")
                    os.system("docker images | grep {}".format(image_name))
                elif int(ch) == 18:
                    print("Enter IP :",end='')
                    IP_NO = input()
                    os.system("tput setaf 5")
                    os.system("curl {}".format(IP_NO))
                elif int(ch) == 19:
                    print("Enter URL:",end='')
                    URL_name = input()
                    os.system("tput setaf 5")
                    os.system(" curl -sSL {}".format(URL_name))
                elif int(ch) == 20:
                    print("Enter the image name to commit :",end='')
                    Image_name = input()
                    os.system("docker commit {}".format(Image_name))
                    print("Enter Repository file name to commit :",end='')
                    file_name=input()
                    os.system("tput setaf 5")
                    os.system("docker commit {}".format(file_name))
                elif int(ch) == 21:
                    os.system("tput setaf 5")
                    os.system("route -n")
                elif int(ch) == 22:
                    print("Enter volume name :",end='')
                    volume_name = input()
                    os.system("tput setaf 5")
                    os.system("docker volume create {}".format(volume_name))
                elif int(ch) == 23:
                    os.system("tput setaf 5")
                    os.system("docker volume ls")
                elif int(ch) == 24:
                    os.system("tput setaf 2")
                    os.system("exit")
	
                else:
                    print("Option Not Supported")
                input("Enter To Continue......")
                os.system("clear")


