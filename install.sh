# /bin/sh

command -v pip > /dev/null

if [ $? -eq 1 ]
then
    echo "oops, pip not installed!";
    exit 1
fi

pip install -r requirements.txt

crontab -l > machine-monitor
echo "* * * * * python3 $PWD/monitor.py > /tmp/machine-monitor.log 2>&1" >> machine-monitor
crontab machine-monitor