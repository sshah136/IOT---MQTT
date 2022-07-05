import numpy as np
import random
import uuid
import strict_rfc3339
import time
import math
import matplotlib.pyplot as plt
import json
import dictfier
import util


query = [
    "specversion",
    "type",
    "source",
    "subject",
    "datacontenttype",
    "id",
    "time",
    "site",
    "fleet",
    "robot",    
    {
        "data": [
        "status",
        {
            "pose": [
                "position",
                "heading"
            ]
        },
        {
            "twist": [
                "linear",
                "angular"
            ]
        },
        "building",
        "floor",
        "charge_remaining"
        ]
    }
]


class Pose:

    def __init__(self, 
        position:list=[0,0,0], 
        heading:list=[0,1,0]):
        self.position = position
        self.heading = heading

    def set(self, 
        position:list=[0,0,0], 
        heading:list=[0,1,0]):
        self.position=position
        self.heading=heading

    def set_position(self, position=[0,0,0]):
        self.position = position    

    def set_heading(self, heading=[0,0,0]):
        self.heading = heading    

    def get_position(self):
        return self.position

    def get_heading(self):
        return self.heading



class Twist:

    def __init__(self, 
        linear:list=[0,0,0], 
        angular:list=[0,0,0]):
        self.linear = linear
        self.angular = angular

    def set(self, 
        linear:list=[0,0,0], 
        angular:list=[0,0,0]):
        self.linear=linear
        self.angular=angular

    def set_linear(self, linear=[0,0,0]):
        self.linear = linear    

    def set_angular(self, angular=[0,0,0]):
        self.angular = angular

    def get_linear(self):
        return self.linear

    def get_angular(self):
        return self.angular



class Data:

    def __init__(self, 
        status:str='on-plan',
        pose_position:list=[0,0,0], pose_heading:list=[0,1,0],
        twist_linear:list=[0,0,0], twist_angular:list=[0,0,0],
        building:str='crestwood-corporation-plaza', 
        floor:int=1,
        charge_remaining:int=100):

        self.status = status
        self.pose = Pose(pose_position, pose_heading)
        self.twist = Twist(twist_linear, twist_angular)
        self.building=building
        self.floor=floor
        self.charge_remaining=charge_remaining

    def set_status(self, status):    
        if status == any(util.allowed_status):
            self.status = status 
        else:
            self.status = util.allowed_status[random.randint(0, len(util.allowed_status)-1)]

    def get_status(self):
        return self.status

    def set_pose(self, pose_position=[0,0,0], pose_heading=[0,1,0]):
        self.pose.set_position(pose_position)
        self.pose.set_heading(pose_heading)

    def get_pose(self):
        return self.pose

    def set_twist(self, linear=[0,0,0], angular=[0,0,0]):
        self.twist.set_linear(linear)
        self.twist.set_angular(angular)

    def get_twist(self):
        return self.twist

    def set_building(self, building):
        self.building=building

    def get_building(self):
        return self.building

    def set_floor(self, floor):
        self.floor=floor

    def get_floor(self):
        return self.floor

    def set_charge_remaining(self, charge_remaining):
        self.charge_remaining = charge_remaining if charge_remaining >= 0 else 0

    def get_charge_remaining(self):
        return self.charge_remaining



class botNavData:

    def __init__(self, 
        specversion:str='1.0', 
        type:str='io.harmony.robot-navigation.status-report.v1',
        source:str='/edge/fleet/robot/navigation',
        subject:str='/cloud/dispatch',
        datacontenttype:str='application/json; charset=utf-8',
        id:str=str(uuid.uuid4()), 
        time:str=strict_rfc3339.now_to_rfc3339_utcoffset(),
        site:str='fresh-hq',
        fleet:str='fresh-robotics-dev',
        robot:str='velma',
        status:str='on-plan',
        pose_position:list=[0,0,0], pose_heading:list=[0,1,0],
        twist_linear:list=[0,0,0], twist_angular:list=[0,0,0],
        building:str='crestwood-corporation-plaza',
        floor:int=1,
        charge_remaining:int=100):

        self.specversion=specversion 
        self.type=type
        self.source=source
        self.subject=subject
        self.datacontenttype=datacontenttype
        self.id=id if util.is_valid_uuid(id) else str(uuid.uuid4())
        self.time=time if strict_rfc3339.validate_rfc3339(time) else strict_rfc3339.now_to_rfc3339_utcoffset()
        self.site=site
        self.fleet=fleet
        self.robot=robot
        self.data = Data(status, pose_position, pose_heading, twist_linear, twist_angular, building, floor, charge_remaining)

    def set_id(self, id):
        self.id = id if util.is_valid_uuid(id) else uuid.uuid4()

    def set_time(self, time):
        self.time = time if strict_rfc3339.validate_rfc3339(time) else strict_rfc3339.now_to_rfc3339_utcoffset()

    def set_site(self, site):
        self.site = site

    def set_fleet(self, fleet):
        self.fleet=fleet

    def set_robot(self, robot):
        self.robot=robot

    def set_data(self, status=util.allowed_status[0], 
        pose_position=[0,0,0], pose_heading=[0,1,0], 
        twist_linear=[0,0,0], twist_angular=[0,0,0], 
        building='crestwood-corporation-plaza', floor=1, 
        charge_remaining=100):
        self.data.set_status(status)
        self.data.pose.set(pose_position, pose_heading)
        self.data.twist.set(twist_linear, twist_angular)
        self.data.set_building(building)        
        self.data.set_floor(floor)        
        self.data.set_charge_remaining(charge_remaining)        


# Plot to show pattern
if __name__ == '__main__':
    dg = botNavData(
        specversion='1.0',
        type='io.harmony.robot-navigation.status-report.v1',
        source='/edge/fleet/robot/navigation',
        subject='/cloud/dispatch',
        datacontenttype='application/json; charset=utf-8',
        id=str(uuid.uuid4()), 
        time=strict_rfc3339.now_to_rfc3339_utcoffset(),
        site='fresh-hq',
        fleet='fresh-robotics-dev',
        robot='velma',
        status='on-plan',
        pose_position=[0,0,0], pose_heading=[0,1,0],
        twist_linear=[0,0,0], twist_angular=[0,0,0],
        building='crestwood-corporation-plaza',
        floor=1,
        charge_remaining=100)

    x = [_ for _ in range(10)]
    y = [_ for _ in x]
    z = [0 for _ in x]
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y)
    plt.show()

    for jj in range(len(x)):
        dg.set_id(str(uuid.uuid4()))
        dg.set_time(strict_rfc3339.now_to_rfc3339_utcoffset())
        dg.set_data(
            pose_position=[x[jj],y[jj],z[jj]], pose_heading=[0,1,0], 
            twist_linear=[0,0,0], twist_angular=[0,0,0], 
            charge_remaining=100-jj*5)

        dg_info = dictfier.dictfy(dg, query)
        #print(dg_info)
        dg_json = json.dumps(dg_info, indent=4)
        print(dg_json)
        time.sleep(1) # Delay for 1 seconds        


'''
{
  "specversion": "1.0",
  "type": "io.harmony.robot-navigation.status-report.v1",
  "source" : "/edge/fleet/robot/navigation",
  "subject" : "/cloud/dispatch",
  "datacontenttype" : "application/json; charset=utf-8",
  "id" : "90a5c360-fef2-404c-b7ac-d3c0d0c707d6",
  "time" : "2022-04-05T17:31:00Z",
  "site": "fresh-hq",
  "fleet": "fresh-robotics-dev",
  "robot": "velma",
  "data": {
    "status": "on-plan",
    "pose": {
      "position": [ 32.5, 43.9, 12.5 ],
      "heading": [ 0, 0, 0.400, 0.916 ]
    },
    "twist": {
      "linear": [ 1.3, -0.6, 0 ],
      "angular": [ 0, 0, 0 ]
    },
    "building": "crestwood-corporation-plaza",
    "floor": 1,
    "charge-remaining": 10500
  }
}

          "enum": [
            "on-plan",
            "planning",
            "avoid-stranger",
            "teleop",
            "please-stop",
            "please-help"
          ]

'''
