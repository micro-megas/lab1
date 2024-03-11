echo start server
/home/appveyor/.local/bin/waitress-serve --call 'wsgi:create_app' & APP_PID=$!
echo $APP_PID
sleep 5
echo start client
python3 client.py
sleep 5
kill -TERM $APP_PID
echo process waitress-serve kills
exit 0