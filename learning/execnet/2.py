import execnet
gw = execnet.makegateway("popen//python=C:\jython2.7.0")
channel = gw.remote_exec("""
    from java.util import Vector
    v = Vector()
    v.add('aaa')
    v.add('bbb')
    for val in v:
        channel.send(val)
""")

for item in channel:
    print (item)

# import java.util
