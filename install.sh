#!/bin/sh

checkPython3(){
   

    if ! command -v python3 &> /dev/null 
    then    
        echo "python3 not installed!"
        echo "installing python3..."   
        apt install software-properties-common  
        add-apt-repository ppa:deadsnakes/ppa 
        apt update
        apt-get -yq python3.8  
        echo "python3 installed! "      
    else
        echo "python3 ok!"
    fi
}

checkPip3(){
    if  ! command -v pip3 &> /dev/null 
    then   
        echo "pip3 not installed!"
        echo "installing pip3..."
        apt-get -yq install python3-pip 
        echo "pip installed! "       
    else
        echo "pip3 ok!"
    fi
}

installPackage(){
    pip3 install -r requirements.txt 
    chmod a+x app.py 
}

configureCron(){
    crontab -l > machine-monitor 
    echo "* * * * * /usr/bin/python3 $PWD/app.py > /tmp/machine-monitor.log 2>1" >> machine-monitor 
    crontab machine-monitor 
    exit 0 
}


checkPython3 && checkPip3 && installPackage && configureCron

