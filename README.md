# Pixy SIW :robot::camera:
Lego robot with a PixyCam which exhibits different behaviours according to the recognized colors. 

### Context
Project developed during Critical Software's Summer Innovation Week

### Description
We used a **PixyCam**, which can be taught to recognize colors, to build a robot which would react to the different inputs. We implemented ways for it to move, rotate, dance, play songs and move a mechanical arm. We also build a system with LEDs which would react to the frequency and tempos of the songs' notes.

A **Raspberry PI** was included in the robot so that it was independent. The camera would send the information to the PI, which had a C program running that communicated with a Python script using a FIFO. This script used the modules we developed to interact with the robot and the LEDs.

The code used to interact with the NXT brick is inside 'brick_control'. The module used for the LEDs is the file 'ledsControl.py'.

The folder 'daemon' holds 2 .system files that were included in the Raspberry so that it would start the C program and python script automatically.

### Programming Languages
* C
* C++
* Java
* Python

### Hardware
* NXT Lego Brick
* PixyCam
* Raspberry PI

### Team
* [Beatriz Abreu](https://github.com/BeatrizAbreu "BeatrizAbreu")
* [Frederico Vicente](https://github.com/Mr-Vicente "Mr-Vicente")
* [Mário Gil](https://github.com/GambuzX "GambuzX")
* [Ricardo Pereira](https://github.com/RicardoPereira99 "RicardoPereira99")
* [Rodolfo Gaspar](https://github.com/rodolfogaspar98 "rodolfogaspar98")
