
BEFORE_PID=$(cat sh.pid)

echo "before PID: $BEFORE_PID"

kill -9 $BEFORE_PID


git pull
nohup python setup.py runserver --host=0.0.0.0 &

echo $! > sh.pid

NEW_PID=$(cat sh.pid)
echo "NEW PID: $NEW_PID"

ps -ef | grep runserver
