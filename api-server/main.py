# main.py -- put your code here!
print("API Server with Microdot here")

from microdot import Microdot
import uasyncio
from microdot_asyncio import Microdot


from dotstar import lights
from dotstar import fillstrip

app = Microdot()
current_task = None


htmldoc = '''<!DOCTYPE html>
<html>
    <head>
        <title>Microdot Example Page</title>
        <meta charset="UTF-8">
    </head>
    <body>
        <div>
            <h1>Microdot Example Page</h1>
            <p>Hello from Microdot!</p>
            <p><a href="/shutdown">Click to shutdown the server</a></p>
        </div>
    </body>
</html>
'''


@app.route('/')
async def hello(request):
    return htmldoc, 200, {'Content-Type': 'text/html'}


@app.route('/lights')
async def hello(request):
    lights()
    print("lights")

    global current_task
    current_task = uasyncio.create_task(lights())
    return htmldoc, 200, {'Content-Type': 'text/html'}


@app.route('/fill')
async def fill(request):
    """Takes URL arguments: fill?r=50&g=20&b=20 """

    args_dict = {}
    for key in request.args.keys():
        args_dict[key] = int(request.args[key])

    print(args_dict)
    global current_task
    current_task = uasyncio.create_task(fillstrip(**args_dict))
    return 'Set Props: {}'.format(args_dict)


@app.route('/shutdown')
async def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'


@app.before_request
async def pre_request_handler(request):
    if current_task:
        current_task.cancel()


def start_server():
    print('Starting microdot app')
    try:
        app.run(port=80, debug=True)
    except:
        app.shutdown()


# Start the server right away
start_server()