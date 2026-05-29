# tuto_clock_python

A tutorial project for teaching Python and programming to adults

## Contents


## Structure

## How to install this project on your machine ?

Firstly, clone this project in the folder of your choice by executing this command in your terminal :

```bash
git clone https://github.com/Vicken-Ghoubiguian/tuto_clock_python
```

Secondly, go to the cloned repository by executing this command in your terminal :

```bash
cd tuto_clock_python
```

Thirdly, install all of the requirements by executing this command in your terminal :

```bash
pip install -r requirements.txt
```
Now, you're ready to use this project.

## How to test each file ?

To test all of the files, you have to go to the 'modules' folder.

For the dt_management module (in the [dt_management](https://github.com/Vicken-Ghoubiguian/tuto_clock_python/blob/main/tuto_clock_python/dt_management.py) file) :

```bash
python dt_management.py --timezone="<timezone>" --dt_format="<datetime_format>" --zoom_map="<zoom_map>"
```
For the Clock class (in the [clock](https://github.com/Vicken-Ghoubiguian/tuto_clock_python/blob/main/tuto_clock_python/Clock.py) file) :

```bash
python clock.py --timezone="<timezone>" --dt_format="<datetime_format>" --zoom_map="<zoom_map>" --width="<width>" --height="<height>" --title="<title>" --weatherbit_api_key="<weatherbit_api_key>"
```
