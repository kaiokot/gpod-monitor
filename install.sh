# /bin/sh

command -v pip > /dev/null

if [ $? -eq 1 ]
then
    read -r -p "oops, pip not installed! Do you want install? [Y/n] " input
 
    case $input in
        [yY][eE][sS]|[yY])
    echo "installing pip..."
    apt -yq install python3-pip &
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

pip install -r requirements.txt

crontab -l > machine-monitor
echo "* * * * * python3 $PWD/app.py > /tmp/machine-monitor.log 2>&1" >> machine-monitor
crontab machine-monitor