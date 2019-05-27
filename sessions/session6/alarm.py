import pyglet
import datetime
import time
while True:
    current = str(datetime.datetime.now().time())
    timed = "15:22:00.000000"
    if current >= timed:
        music = pyglet.resource.media('tokyo_ghoul.mp3')
        music.play()

        pyglet.app.run()
