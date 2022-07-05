## IOT---MQTT
Data transmission from MQTT broker which is generated from simulated temperature sensors from random coordinates and realtime data is displayed on Tkinter GUI as chart

## Further extention to Harmony Hub use cases
1. Modified the Publisher.py and DataGenerator.py to botPublisher.py and botNavData.py to conform with Mikey's robot navigation message definition. See example.json for the definition.
1. Publish the robot navigation message as a json packet at 1 Hz rate
1. The publisher side keeps the original publishing error situation to simulate unreliable transmission, more details can be found in botPublisher.py
2. Another Unity code is prepared for showing the robot navigation message can be received in Unity. See that Unity repo for details.

## Use pip install [dependency name] under python envoironment to install necessary prerequisites (add more dependencies as screen complains), and run the python code
```
paho-mqtt
numpy
matplotlib
uuid
strict-rfc3339        
colorama              
```
Then run the following command to test if the nav data has been generated properly:
```
python botNavData.py
```
Eventually, it the MQTT broker is properly setup, run the following command to start publishing the nav data:
```
python botPublisher.py
```
Ignore Publisher.py and Subscriber.py as they have nothing to do with the extended version of this repo. They were made for the fake temperature massages, and for our starting point.

## Prepare a local MQTT broker
Install mosquitto broker[https://mosquitto.org/] in your computer. If it is a Windows machine, it will be a CMD line console executible file in the broker destination folder.

## Prepare a local MQTT Explorer
Install MQTT explorer[http://mqtt-explorer.com/] in your computer. When using the MQTT explorer, create a new connection, with protocol mqtt://, Host 127.0.0.1, port 1883. It is not a encrypted connection yet so no need to input username and password.

This explorer serves as a tool to visualize all the messages in and out of the local MQTT broker.

## Test in Unity with botPublisher.py
1. Run the mosquitto broker.
2. Run the MQTT explorer, as a side way to see the broker activities. This is just optional.
3. Launch the Unity scene, connect to 127.0.0.1, the main screen should show the broker is connected. Try Test Publishing, the main screen should have an echo response, and the MQTT explorer should see an incoming message.
4. Launch the botPublisher.py under python environment. The event publishing will keep running unless using CTRL-C to stop it in python environment.

## What's next for Unity side?
1. Parse received MQTT json packet, will need to define the data structure as classes using a 
C# script, then use either of these tools to do the job. The second tool seems to be a bit loose in parsing the data structure. But we can start from the easy-to-implement tool for now.
```
https://docs.unity3d.com/ScriptReference/JsonUtility.FromJson.html
https://www.newtonsoft.com/json
```
1. Extract parematers such as pose_linear, twist_linear and chargeremaining to show on the robot agent