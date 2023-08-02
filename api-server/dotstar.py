from micropython_dotstar import DotStar
from machine import SPI, Pin, sleep
import uasyncio
import time

async def fillstrip(r, g, b):
    spi = SPI(sck=Pin(12), mosi=Pin(13), miso=Pin(18)) # Configure SPI - see note below
    dotstar = DotStar(spi, 10) # Just one DotStar

    while True:
        dotstar.fill((r, g, b))
        await uasyncio.sleep_ms(10)

async def lights():

    spi = SPI(sck=Pin(12), mosi=Pin(13), miso=Pin(18)) # Configure SPI - see note below
    dotstar = DotStar(spi, 10) # Just one DotStar
    # dotstar[0] = (128, 0, 0) # Red
    # dotstar[1] = (128, 0, 0, 0.5) # Red, half brightness

    t = 0

    while True:
        t += 1
        for i in range(10):
            dotstar[i]=((t+10*i)%128, (t+20*i)%128, (t+30*i)%128, 1)
            print("dotstar {} {}".format(dotstar[i], i))
            # print("bloopy {} {}".format(t, i))
        await uasyncio.sleep_ms(10)

        # time.sleep(1)

        # dotstar._set_item(5,(0,0,128))
        # dotstar.fill((0,0,128)) # Blue
        # dotstar[0]=(128,0,0)
        # sleep(10)
        # dotstar.fill((128,0,0)) # Blue
        # sleep(1000)
        # dotstar.fill((0,128,0)) # Blue
        # sleep(1000)
        # print("bloopy {} {}".format(t, i))

