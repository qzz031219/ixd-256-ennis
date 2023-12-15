# ixd-256-ennis

**Project Name: life's silent escape.**

**Introduction**

![image](https://github.com/qzz031219/ixd-256-ennis/assets/146476099/710eaf1f-fb2d-42b0-9ee6-d9ad6fd5cafd)


This is my initial idea, which is to create an interactive art installation piece. So I want to use the pressure sensor to toggle the videos and use the distance sensor/ultrasonic sensor to control the volume based on the distance between the screen and the audience.


The big concept behind this piece is life. The noise and hustle and bustle of life are everywhere, working and studying, getting up early and going to bed late, all of which take a toll on our minds. Including the seriousness of today's rat race, whether it is society or people around us will bring us a lot of pressure. How do we escape this predicament?


So I want to go through this work to let the audience's mood relax and enter into a meditative state. That's why I want to create an immersive space for this project.



**Implementation**
I used:
- 1 Atom s3 lite board
- 1 Ultrasonic sensor
- 1 Pressure sensor

<img width="947" alt="image" src="https://github.com/qzz031219/ixd-256-ennis/assets/146476099/d246a4b8-8b45-4c1a-aeff-b8d49222b411">

<img width="657" alt="image" src="https://github.com/qzz031219/ixd-256-ennis/assets/146476099/8a6b5dec-2fb4-4cd9-92f6-debe69417af4">

<img width="1118" alt="image" src="https://github.com/qzz031219/ixd-256-ennis/assets/146476099/8dfd7fe1-3d33-4077-a177-5f6883a1bdad">

<img width="1076" alt="image" src="https://github.com/qzz031219/ixd-256-ennis/assets/146476099/2499f167-dabe-4098-af8d-03693109d941">

<img width="1223" alt="image" src="https://github.com/qzz031219/ixd-256-ennis/assets/146476099/7dd69982-c7f5-45b5-99a0-8b3fc44aa0fa">

<img width="1128" alt="image" src="https://github.com/qzz031219/ixd-256-ennis/assets/146476099/abc555db-ef31-47a4-89bf-39fbebb4837d">


**Firmware**

**HARDWARE**

Pressure sensor setup:
```ruby
adc = ADC(Pin(PRESSURE_SENSOR_PIN))
adc.atten(ADC.ATTN_11DB)
```

[Define the maximum and minimum distances for the ultrasonic sensor:](https://github.com/qzz031219/ixd-256-ennis/blob/42ff30b4b52e4528044a516af9264c4412e8d17d/final/pressure%20and%20distance.py#L8C1-L9C22)

[Trigger the ultrasonic sensor:](https://github.com/qzz031219/ixd-256-ennis/blob/42ff30b4b52e4528044a516af9264c4412e8d17d/final/pressure%20and%20distance.py#L17C1-L22C18)

[Calculate the distance in cm (speed of sound is 0.0343 cm/µs, so distance = timepassed * 0.0343/2):](https://github.com/qzz031219/ixd-256-ennis/blob/42ff30b4b52e4528044a516af9264c4412e8d17d/final/pressure%20and%20distance.py#L24C1-L36C27)

[Read the value from the pressure sensor:](https://github.com/qzz031219/ixd-256-ennis/blob/42ff30b4b52e4528044a516af9264c4412e8d17d/final/pressure%20and%20distance.py#L40C1-L41C1)

[Call the function to read the distance from the ultrasonic sensor:](https://github.com/qzz031219/ixd-256-ennis/blob/42ff30b4b52e4528044a516af9264c4412e8d17d/final/pressure%20and%20distance.py#L41C4-L41C4)

[Print the value to monitor the value, if the value is right, if the connection is stable:](https://github.com/qzz031219/ixd-256-ennis/blob/42ff30b4b52e4528044a516af9264c4412e8d17d/final/pressure%20and%20distance.py#L43C1-L46C62)

**SOFTWARE**

[Add 2 videos to the software and hide default video elements on screeen:]
(https://github.com/qzz031219/ixd-256-ennis/blob/42ff30b4b52e4528044a516af9264c4412e8d17d/final/sketch.js#L12C1-L20C17)

[Use ternary operator to determine which video should play based on pressure sensor value, if value is greater than 4000, play video 1; if value is less than 4000, toggle to video 2; Besides that, check if a transition is not already happening:](https://github.com/qzz031219/ixd-256-ennis/blob/42ff30b4b52e4528044a516af9264c4412e8d17d/final/sketch.js#L35C1-L41C6)

[Volume fade in and out during transition:](https://github.com/qzz031219/ixd-256-ennis/blob/42ff30b4b52e4528044a516af9264c4412e8d17d/final/sketch.js#L45C1-L46C65)

[Video fade in and out during transition:](https://github.com/qzz031219/ixd-256-ennis/blob/42ff30b4b52e4528044a516af9264c4412e8d17d/final/sketch.js#L44C5-L44C5;https://github.com/qzz031219/ixd-256-ennis/blob/42ff30b4b52e4528044a516af9264c4412e8d17d/final/sketch.js#L48C1-L55C28;https://github.com/qzz031219/ixd-256-ennis/blob/42ff30b4b52e4528044a516af9264c4412e8d17d/final/sketch.js#L70C1-L74C59)

[Change volume based on the distance (ultrasonic value):](https://github.com/qzz031219/ixd-256-ennis/blob/42ff30b4b52e4528044a516af9264c4412e8d17d/final/sketch.js#L57C7-L64C10)


**Project references**

[link text in square brackets] followed by (link URL in parantheses)
[Ultrasonic sensor connected to the atom s3 board](https://www.youtube.com/watch?v=DM1Lu8oo-50)
[Trigger ultrasonic sensor to measure and calculate distance](https://github.com/orgs/micropython/discussions/11205)



