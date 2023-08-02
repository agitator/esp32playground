# boot.py -- run on boot-up
ENV = False

try:
    import os
    from mpy_env import load_env, get_env

    if "env.json" in os.listdir():
        load_env(verbose=True)
        ENV = True
        print("env.json found and loaded")
    else:
        print("No env.json found for network setup")
except Exception as e:
    print("Could not setup env: {}".format(e))

if ENV:
    from utils import do_connect

    if get_env("HOSTNAME"):
        import network

        network.hostname(get_env("HOSTNAME"))
        print(network.hostname())
    do_connect(get_env("WIFI_SSID"), get_env("WIFI_PASSWD"))
