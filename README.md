# QuizLock
###### _script by [Florent Loock](https://github.com/liardnos) & [Maxime Deroulou](https://github.com/mderoulou)_

# Step by step tutorial:
#### 1. Clone repository
Clone a repository using https or ssh :
```Shell
https://github.com/mderoulou/QuizLock.git
```
or
```Shell
git@github.com:mderoulou/QuizLock.git
```
#### 2. Edit current pool day
Edit script.py at line 10 pick the pool day number,
all day before this day will be used for the random question pick
#### 3. Run autorun
Run autorun a root of repository :
```Shell
./autorun.sh
```
### To add script on usb device:
Please make sure you're usb device is correctly formatted and doesn't contain an already an autorun.sh
#### 1. Clone/Copy the repository
Clone or Copy the repository to the root of the usb device.
The usb device is often on "/media/${USER}/USB" or "/run/media/${USER}/USB"

#### 2. Execute ./init.sh
At the root of the repository execute ./init.sh

#### 3. Unplug USB
Now you can unplug the USB device,
make sure to use a safe unplug otherwise the content could be erased.

#### 4. Plug USB
Plug USB device on the target !
On some OS a small window will ask if you want to execute
the program, click on run, wait the small black screen and then you can unplug the device.

If the small window doesn't appear, open file system go to the usb device and run ./autorun.sh