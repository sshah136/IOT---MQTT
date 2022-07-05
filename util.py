import random, time
import uuid

start_id = 111
topic = 'M2MQTT_Unity/test'
allowed_status= ["on-plan", "planning", "avoid-stranger", "teleop", "please-stop", "please-help"]

def generate_data(data):
    global start_id

    # temperature sensors are placed around the world
    new_data = {
        'id': start_id,
        'time': time.asctime(),
        'temperature': round(data, 4),
        'geographical_location': {
            'long': round(random.uniform(-180, 180), 2),
            'lat': round(random.uniform(-90, 90), 2)
        }
    }

    start_id += 1

    return new_data

def fake_robot_data(
    specversion="1.0", 
    type="io.harmony.robot-navigation.status-report.v1",
    source="/edge/fleet/robot/navigation",
    subject="/cloud/dispatch",
    datacontenttype="application/json; charset=utf-8",
    id="90a5c360-fef2-404c-b7ac-d3c0d0c707d6",
    time="2022-04-05T17:31:00Z",
    site="fresh-hq",
    fleet="fresh-robotics-dev",
    robot="velma",
    status="on-plan",
    pose_position=[0,0,0],
    pose_heading=[0,1,0],
    twist_linear=[0,0,0],
    twist_angular=[0,0,0],
    building="crestwood-corporation-plaza",
    floor=1,
    charge_remaining=100):

    global start_id

    # robot status data as per Mikey's status message definition v1
    new_data = {
        "specversion": specversion,
        "type": type,
        "source" : source,
        "subject" : subject,
        "datacontenttype" : datacontenttype,
        "id" : id,
        "time" : time,
        "site": site,
        "fleet": fleet,
        "robot": robot,
        "data": {
            "status": status,
            "pose": {
                "position": pose_position,
                "heading": pose_heading
            },
            "twist": {
                "linear": twist_linear,
                "angular": twist_angular
            },
            "building": building,
            "floor": floor,
            "charge-remaining": charge_remaining
            }
        }

    start_id += 1

    return new_data

def is_valid_uuid(value):
    try:
        uuid.UUID(str(value))
        return True
    except ValueError:
        return False

def print_data(data_dict, indent=0):
    for key, value in data_dict.items():
        if isinstance(value, dict):
            print(str(key) + ': ')
            print_data(value, indent + 1)
        else:
            print('\t' * indent + str(key) + ': ' + str(value))
    print()

# new_data = create_data()
# print_data(new_data)
