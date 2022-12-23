import paho.mqtt.client as mqtt
from sentence import sentence
from sorter import sorter
import time


# Taking the variables for the methods
client      =   mqtt.Client()
topicName   =   "aman/cdac/test"
QOS_val        =   2
sorterAlmacen = sorter()



# --------------- Defining call backs---------------------------------------------------------------
def on_connect(pvtClient,userdata,flags,rc):
    if(rc == 0):  # on successful connection
        print("Connected to client! Return Code:"+str(rc)) 

        result = client.subscribe(topicName, QOS_val) 

    elif(rc ==5): # in case of authentication error
        print("Authentication Error! Return Code: "+str(rc))  # printing the data on the screen
        client.disconnect()

def on_message(pvtClient, userdata, msg):
    
    print(f"\n esta fue la palabra que me llegó, Camilo    : {str(msg.payload.decode())}")

    variableMensaje = str(msg.payload.decode())
    print (variableMensaje)
    print("------------")
    
    for i in range(0, sentence(str(msg.payload.decode())).getTamaño(), 1 ):
        print (variableMensaje)
        sorterAlmacen.agregarSentence(sentence(variableMensaje))
        print (variableMensaje)
        variableMensaje = sorterAlmacen.getElemento(-1).getSentenceString()
        print (variableMensaje)
    sorterAlmacen.imprimirS()


    if(msg.payload.decode() == "exit(0)" ):
        client.disconnect()




def on_log(topic, userdata, level, buf):
    print("Logs: "+str(buf))
# -------------------------------------------------------------------------------------------------------------

# ======== Associating the methods with the given callbacks of the MQTT ======
client.on_connect   =   on_connect
client.on_message   =   on_message
client.on_log       =   on_log
#client.will_set     =   will_set
# ============================================================================

host        = "localhost"
port        = 1883
keepAlive   = 60

client.connect(host,port,keepAlive) # establishing the connection

time.sleep(2)            

client.loop_forever()


    