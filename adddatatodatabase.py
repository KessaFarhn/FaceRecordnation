import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://faceattendancerealtime-914d5-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data = {
    "1710623005":
        {
            "name": "Ranty Pratiwi",
            "major": "Bisnis Digital",
            "starting_year": 2023,
            "total_attendance":15,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2027-07-15 00:55:30"
        },
    "1710623300":
        {
            "name": "Murtaza Hassan",
            "major": "Robotic",
            "starting_year": 2017,
            "total_attendance":6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-07-15 00:55:30"
        },
    "1711096009":
        {
            "name": "Elon Musk",
            "major": "Bisnis",
            "starting_year": 2000,
            "total_attendance":15,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2004-07-15 00:55:30"
        },
    "1713456776":
        {
            "name": "Emily Blunt",
            "major": "Fashion",
            "starting_year": 2003,
            "total_attendance":15,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2007-07-15 00:55:30"
        },
    "1710623020":
        {
            "name": "Okta Vinandesh T",
            "major": "Bisnis Digital",
            "starting_year": 2023,
            "total_attendance":15,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2027-07-15 00:55:30"
        },
    "1710623036":
        {
            "name": "Syadin Alivia Yusuf",
            "major": "Bisnis Digital",
            "starting_year": 2023,
            "total_attendance":15,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2027-07-15 00:55:30"
        },
    "1710623097":
        {
            "name": "Khairunnisa Azzahra",
            "major": "Bisnis Digital",
            "starting_year": 2023,
            "total_attendance":15,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2027-07-15 00:55:30"
        },
    "1710623109":
        {
            "name": "Muhammad Farhan Kessa",
            "major": "Bisnis Digital",
            "starting_year": 2023,
            "total_attendance":15,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2027-07-15 00:55:30"
        },
}

for key,value in data.items():
    ref.child(key).set(value)