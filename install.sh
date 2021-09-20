#!/bin/sh

checkPython3(){
    command -v python3 > /dev/null 

    if [ $? -eq 1 ]
    then
        read -r -p "oops, python3 not installed! Do you want install? [Y/n] " input
    
        case $input in
            [yY][eE][sS]|[yY])
        echo "installing python3..."
        apt install software-properties-common  
        add-apt-repository ppa:deadsnakes/ppa 
        apt update
        apt-get -yq python3.8 
        echo "python3 installed! "
        ;;
            [nN][oO]|[nN])
        echo "ok, no problem"
        exit 1
            ;;
            *)   
        echo "invalid option" 
        exit 1
        ;;
        esac
    fi

}

checkPip3(){
    command -v pip3 > /dev/null 

    if [ $? -eq 1 ]
    then
        read -r -p "oops, pip not installed! Do you want install? [Y/n] " input
    
        case $input in
            [yY][eE][sS]|[yY])
        echo "installing pip..."
        apt-get -yq install python3-pip 
        echo "pip installed! "
        ;;
            [nN][oO]|[nN])
        echo "ok, no problem"
        exit 1
            ;;
            *)   
        echo "invalid option" 
        exit 1
        ;;
        esac
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


checkPython3 &&
checkPip3 &&
installPackage &&
configureCron

