/home/appveyor/.local/bin/waitress-serve --call 'flaskr:create_app' & APP_PID=$!
sleep 5
echo $APP_PID
kill -TERM $APP_PID
echo process waitress-serve kills
exit 0