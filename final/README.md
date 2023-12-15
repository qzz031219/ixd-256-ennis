# FINAL PROJECT: life's silent escape.

## Introduction

This is my initial idea, which is to create an interactive art installation piece. So I want to use the pressure sensor to toggle the videos and use the distance sensor/ultrasonic sensor to control the volume based on the distance between the screen and the audience.

The big concept behind this piece is life. The noise and hustle and bustle of life are everywhere, working and studying, getting up early and going to bed late, all of which take a toll on our minds. Including the seriousness of today's rat race, whether it is society or people around us will bring us a lot of pressure. How do we escape this predicament?

Therefore, I want the viewers to put down their phones, relax and enter a meditative state through this work. That's why I wanted to create an immersive space for this project.

![image](https://github.com/qzz031219/ixd-256-ennis/assets/146476099/710eaf1f-fb2d-42b0-9ee6-d9ad6fd5cafd)

## Implementation

### Hardware - material & wiring

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


### Firmware - hardware

Pressure sensor setup:

```ruby
adc = ADC(Pin(PRESSURE_SENSOR_PIN))
adc.atten(ADC.ATTN_11DB)
```

Define the maximum and minimum distances for the ultrasonic sensor:

```ruby
MAX_DISTANCE_CM = 400
MIN_DISTANCE_CM = 2  
```

Trigger the ultrasonic sensor:

```ruby
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
```

Calculate the distance in cm (speed of sound is 0.0343 cm/µs, so distance = timepassed * 0.0343/2):

```ruby
    while echo.value() == 0:
        signaloff = time.ticks_us()

    while echo.value() == 1:
        signalon = time.ticks_us()

    timepassed = signalon - signaloff
    distance_cm = (timepassed * 0.017)

    if distance_cm < MIN_DISTANCE_CM or distance_cm > MAX_DISTANCE_CM:
        return None
    else:
        return distance_cm
```

Read the value from the pressure sensor; Call the function to read the distance from the ultrasonic sensor; Print the value to monitor the value, if the value is right, if the connection is stable:

```ruby
    while True:
        pressure_val = adc.read()
        distance_val = read_ultrasonic()

        if distance_val is not None:
            print("{},{}".format(distance_val, pressure_val))
        else:
            print("Distance invalid,{}".format(pressure_val))

        time.sleep(0.5)
```


### Firmware - software

Add 2 videos to the software and hide default video elements on screeen:

```ruby
    createCanvas(windowWidth, windowHeight);
    vid1 = createVideo("video1.mp4");
    vid2 = createVideo("video2.mp4");

    vid1.size(windowWidth, windowHeight);
    vid2.size(windowWidth, windowHeight);

    vid1.hide();
    vid2.hide();
```

Use conditional operator to determine which video should play based on pressure sensor value, if value is greater than 4000, play video 1; if value is less than 4000, toggle to video 2; Besides that, check if a transition is not already happening:

```ruby
    let newVideo = (pressure > 4000) ? vid1 : vid2;
    if (newVideo !== currentVideo && !isTransitioning) {
        nextVideo = newVideo;
        isTransitioning = true;
        nextVideo.time(0);
        nextVolume = 0;
    }
```

Volume fade in and out during transition: 

```ruby
        currentVolume = max(0, currentVolume - volumeTransitionSpeed);
        nextVolume = min(1, nextVolume + volumeTransitionSpeed);
```

Video fade in and out during transition:

```ruby
        fade += 2;
```

```ruby
        if (fade >= 255) {
            fade = 0;
            currentVideo.hide();
            currentVideo = nextVideo;
            nextVideo = null;
            isTransitioning = false;
            currentVolume = nextVolume;
            nextVolume = 0;
```

```ruby
    tint(255, 255 - fade);
    image(currentVideo, 0, 0, windowWidth, windowHeight);
    if (nextVideo) {
        tint(255, fade);
        image(nextVideo, 0, 0, windowWidth, windowHeight);
```

Change volume based on the distance (ultrasonic value):

```ruby
        if (distance >= 100) {
            currentVolume = 0;
        } else if (distance <= 50) {
            currentVolume = 1;
        } else {
            currentVolume = map(distance, 50, 100, 1, 0);
        }
```

### Integrations

I am not using software like Adafruit or IFTTT. But I created two motion clips by using after effects in this project and uploaded them locally. So that I can directly call them in the software.

<img width="282" alt="image" src="https://github.com/qzz031219/ixd-256-ennis/assets/146476099/5a07a744-73fb-49fe-b012-cfb8a0ac971d">

<img width="1481" alt="image" src="https://github.com/qzz031219/ixd-256-ennis/assets/146476099/e00529ed-b8f6-4598-b82c-e2bc59c81745">


### Enclosure / Mechanical Design

Laser cutting was used to cut out the base to hold the cell phone:

<img width="1000" alt="image" src="https://github.com/qzz031219/ixd-256-ennis/assets/146476099/8349d190-ad37-4f79-ba3e-93ac0920817e">

Testing the pressure sensor (test how many pieces need to be stacked to have a change in value after putting the phone):

<img width="1038" alt="image" src="https://github.com/qzz031219/ixd-256-ennis/assets/146476099/e17852b3-76e5-4dea-bb23-6a59993d5afb">

Different variations:

<img width="900" alt="image" src="https://github.com/qzz031219/ixd-256-ennis/assets/146476099/eae04477-4e4f-4888-ab53-98141d93a810">

After testing, the best way to detect the distance between screen and the audience:

<img width="754" alt="image" src="https://github.com/qzz031219/ixd-256-ennis/assets/146476099/31c77020-58e1-45fe-b6ca-c8c91af698a5">


## Project outcome

<img width="1235" alt="image" src="https://github.com/qzz031219/ixd-256-ennis/assets/146476099/ccde22a1-aaa6-4262-96ad-b336ae27ba03">

<img width="1478" alt="image" src="https://github.com/qzz031219/ixd-256-ennis/assets/146476099/3daf5e6a-3146-4f2c-8740-3490debd46d5">



## Conclusion

Before I got into ArtCenter, I did play around with some sensors, one of which was an ultrasonic sensor. At that time, when I was using the arduino uno, I felt that the video playback wasn't that smooth and clear, and I didn't know what to do with it. I thought there must be a new hardware or way to fix it. But now, I figured it out.


And in the process of doing this project, I learned more about ultrasonic sensors. It's really hard to make the ultrasonic sensor measure the distance between the screen and the viewer, but measuring the distance from the viewer to the wall would be better. That's why I made the ultrasonic sensor a wearable device.


If I had more time to test and simulate, I think I could have made a better box or laser cut pieces for the wearable.


I also learned that if the object is hard then the pressure sensor will not detect it. So I added a piece of rubber under the base of the phone so that the pressure sensor could detect gravity.


During the coding process, I forgot how to connect the hardware data to javascript and how to visualize it in the browser, or some other testing issues. But Nikita and Micheal really helped me with those issues. I really appreciate that!!


Wish you have a nice winter break!!


## Project references

[Ultrasonic sensor connected to the atom s3 board](https://www.youtube.com/watch?v=DM1Lu8oo-50)

[Trigger ultrasonic sensor to measure and calculate distance](https://github.com/orgs/micropython/discussions/11205)



