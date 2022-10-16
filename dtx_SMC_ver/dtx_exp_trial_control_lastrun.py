#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on 10월 16, 2022, at 15:50
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.4')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'Main'  # from the Builder filename that created this script
expInfo = {
    'id*': '999',
    '만 나이': '',
    '성별': ["여자", "남자"],
    'weather': ["yes", "no"],
    'boat': ["yes", "no"],
    'parachute': ["yes", "no"],
    'fish': ["yes", "no"],
    'test_mode': ["no", "yes"],
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['id*'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Minu Kim\\Documents\\GitHub\\tonghap_exp_samsung_hospital\\dtx_SMC_ver\\dtx_exp_trial_control_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='hsv',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Total_control" ---
# Run 'Begin Experiment' code from time_control
### WEATHER TIME CONTROL

# 자유연상시간 연습
stimulus_interval_prac = 5
# 자유연상시간 실제
stimulus_interval = 30 #original 30
# 전환시간 2초
transition_duration = 2
# Run 'Begin Experiment' code from total_code

tot_order = int(expInfo['id*'])%6 + 1

if tot_order == 1:
    exp_order1 = [1,0,0] #flanker, parachute, fish.
    exp_order2 = [0,1,0]
    exp_order3 = [0,0,1]
elif tot_order == 2:
    exp_order1 = [1,0,0]
    exp_order2 = [0,0,1]
    exp_order3 = [0,1,0]
elif tot_order == 3:
    exp_order1 = [0,1,0]
    exp_order2 = [1,0,0]
    exp_order3 = [0,0,1]
elif tot_order == 4:
    exp_order1 = [0,1,0]
    exp_order2 = [0,0,1]
    exp_order3 = [1,0,0]
elif tot_order == 5:
    exp_order1 = [0,0,1]
    exp_order2 = [1,0,0]
    exp_order3 = [0,1,0]
elif tot_order == 6:
    exp_order1 = [0,0,1]
    exp_order2 = [0,1,0]
    exp_order3 = [1,0,0]

exp_loop = 1
# Run 'Begin Experiment' code from trial_numbers_2

skip_weather = 1
skip_boat = 0
skip_para = 0
skip_fish = 0
test_mode = 0

activate_weather = expInfo['weather']
activate_boat = expInfo['boat']
activate_para = expInfo['parachute']
activate_fish = expInfo['fish']
activate_test_mode = expInfo['test_mode']


if activate_weather == 'no':
    skip_weather = 0
    
if activate_boat == 'no':
    skip_boat = 1
if activate_para == 'no':
    skip_para = 1
if activate_fish == 'no':
    skip_fish = 1
if activate_test_mode == 'yes':
    test_mode = 1


# you can change trial numbers for test

# weather
wth_repeat_prac_n = 99 # default 99 
wth_trials_n = 4; # 마음날씨 시행반복횟수, 기본 4회 (삼성병원실험)

# flanker (boat)
fprac = 2 #default 2
fmain = 8 #default (삼성병원 8) /  일반 15)

# parachute
para_prac = 2 #default 2 (practice loop)
para_main = 1 #default 1 (main loop)

# fish 
fis_round_tot = 3; # default 5 trial control 3
fish_practice_reps = 3

#############TEST MODE###############
if test_mode == 1:
    wth_trials_n = 1
    # 자유연상시간 연습
    stimulus_interval_prac = 3
    # 자유연상시간 실제
    stimulus_interval = 5 #original 30
    # 사회적 민감성
    fish_practice_reps = 1




# --- Initialize components for Routine "general_instruction" ---
wth_inst_image = visual.ImageStim(
    win=win,
    name='wth_inst_image', units='pix', 
    image='fis_artwork/general_instruction.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[1920, 1080],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
gen_inst_resp = keyboard.Keyboard()

# --- Initialize components for Routine "wth_inst" ---
wth_movie = visual.MovieStim3(
    win=win, name='wth_movie', units='pix',
    noAudio = False,
    filename='ins/weather_intro.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False, anchor='center',
    size=[1920, 1080],
    depth=0.0,
    )
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "wth_begin_prac" ---
wth_background_inst = visual.ImageStim(
    win=win,
    name='wth_background_inst', units='pix', 
    image='Mood Weather Module Artwork/weather input/background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
wth_text = visual.TextStim(win=win, name='wth_text',
    text='단어연상 연습이 시작됩니다.\n\n준비되셨으면 스페이스로 넘어가세요.',
    font='Malgun Gothic',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
wth_next_next = keyboard.Keyboard()

# --- Initialize components for Routine "wth_think_prac" ---
wth_background_6 = visual.ImageStim(
    win=win,
    name='wth_background_6', units='pix', 
    image='Mood Weather Module Artwork/weather input/background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
wth_think_instr_2 = visual.TextStim(win=win, name='wth_think_instr_2',
    text='자유롭게 생각하세요.',
    font='Malgun Gothic',
    pos=(0, .2), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
wth_think_cross_2 = visual.ShapeStim(
    win=win, name='wth_think_cross_2', vertices='cross',
    size=(0.07, 0.07),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-3.0, interpolate=True)

# --- Initialize components for Routine "wth_word_prac" ---
wth_word_back = visual.ImageStim(
    win=win,
    name='wth_word_back', units='pix', 
    image='Mood Weather Module Artwork/weather input/background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
wth_word_instr_4 = visual.TextStim(win=win, name='wth_word_instr_4',
    text='지금 무슨 생각을 하고 있는지\n단어나 구로 입력해주세요.',
    font='Malgun Gothic',
    pos=(0, 0.25), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
# Run 'Begin Experiment' code from wth_code_2
from tkinter import *
end_rt = 0
inputValue = ""

# --- Initialize components for Routine "wth_rating_prac" ---
wth_background_7 = visual.ImageStim(
    win=win,
    name='wth_background_7', units='pix', 
    image='Mood Weather Module Artwork/weather input/background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
wth_word_typed_2 = visual.TextStim(win=win, name='wth_word_typed_2',
    text='',
    font='Malgun Gothic',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
wth_valence_rating_2 = visual.Slider(win=win, name='wth_valence_rating_2',
    startValue=None, size=(0.45, 0.05), pos=(-0.5, -.1), units=None,
    labels=("부정", "중립", "긍정"), ticks=(-1, 0, 1), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='red', lineColor='black', colorSpace='rgb',
    font='Malgun Gothic', labelHeight=0.03,
    flip=False, ori=0.0, depth=-2, readOnly=False)
wth_valence_txt_2 = visual.TextStim(win=win, name='wth_valence_txt_2',
    text='단어에서 느껴지는 감정',
    font='Malgun Gothic',
    pos=(-.5, -0.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
wth_self_txt_2 = visual.TextStim(win=win, name='wth_self_txt_2',
    text='단어가 자신과 관련이 있는 정도',
    font='Malgun Gothic',
    pos=(0.5, -.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
wth_self_rating_2 = visual.Slider(win=win, name='wth_self_rating_2',
    startValue=None, size=(.45, 0.05), pos=(0.5, -.1), units=None,
    labels=("전혀 나와 관련 없음","나와 관련 매우 많음"), ticks=(0, 1), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='red', lineColor='black', colorSpace='rgb',
    font='Malgun Gothic', labelHeight=0.03,
    flip=False, ori=0.0, depth=-5, readOnly=False)
wth_rating_end_2 = visual.TextBox2(
     win, text='클릭해 주세요', font='Malgun Gothic',
     pos=(-.02, -.42),     letterHeight=0.03,
     size=(0.19, 0.06), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='white', borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='wth_rating_end_2',
     autoLog=False,
)
wth_mouse_5 = event.Mouse(win=win)
x, y = [None, None]
wth_mouse_5.mouseClock = core.Clock()

# --- Initialize components for Routine "wth_end_inst" ---
wth_image_2 = visual.ImageStim(
    win=win,
    name='wth_image_2', units='pix', 
    image='Mood Weather Module Artwork/weather input/background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
wth_text_4 = visual.TextStim(win=win, name='wth_text_4',
    text='넘어가시겠습니까?\n\n넘어가기 : Y\n다시연습 : N\n',
    font='Malgun Gothic',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
wth_key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "wth_start" ---
wth_background_inst_2 = visual.ImageStim(
    win=win,
    name='wth_background_inst_2', units='pix', 
    image='Mood Weather Module Artwork/weather input/background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
wth_text_2 = visual.TextStim(win=win, name='wth_text_2',
    text='단어연상을 시작합니다\n\n연상시간은 30초이며\n총 4회 반복됩니다\n\n스페이스로 넘어가세요',
    font='Malgun Gothic',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
wth_key_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "wth_begin_main" ---
wth_begin_background = visual.ImageStim(
    win=win,
    name='wth_begin_background', units='pix', 
    image='Mood Weather Module Artwork/weather input/background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
wth_begin_text = visual.TextStim(win=win, name='wth_begin_text',
    text='시작',
    font='Malgun Gothic',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "wth_think" ---
wth_background = visual.ImageStim(
    win=win,
    name='wth_background', units='pix', 
    image='Mood Weather Module Artwork/weather input/background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
wth_think_instr = visual.TextStim(win=win, name='wth_think_instr',
    text='자유롭게 생각하세요.',
    font='Malgun Gothic',
    pos=(0, .2), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
wth_think_cross = visual.ShapeStim(
    win=win, name='wth_think_cross', vertices='cross',
    size=(0.07, 0.07),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-3.0, interpolate=True)

# --- Initialize components for Routine "wth_word" ---
wth_background_2 = visual.ImageStim(
    win=win,
    name='wth_background_2', units='pix', 
    image='Mood Weather Module Artwork/weather input/background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
wth_word_instr = visual.TextStim(win=win, name='wth_word_instr',
    text='지금 무슨 생각을 하고 있는지\n단어나 구로 입력해주세요.',
    font='Arial',
    pos=(0, 0.25), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
# Run 'Begin Experiment' code from wth_code_4
record_time = False
wth_word_type_end = 0

# --- Initialize components for Routine "wth_rating" ---
wth_background_3 = visual.ImageStim(
    win=win,
    name='wth_background_3', units='pix', 
    image='Mood Weather Module Artwork/weather input/background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
wth_word_typed = visual.TextStim(win=win, name='wth_word_typed',
    text='',
    font='Malgun Gothic',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
wth_valence_rating = visual.Slider(win=win, name='wth_valence_rating',
    startValue=None, size=(0.45, 0.05), pos=(-0.5, -.1), units=None,
    labels=("부정", "중립", "긍정"), ticks=(-1, 0, 1), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='red', lineColor='black', colorSpace='rgb',
    font='Malgun Gothic', labelHeight=0.03,
    flip=False, ori=0.0, depth=-2, readOnly=False)
wth_valence_txt = visual.TextStim(win=win, name='wth_valence_txt',
    text='단어에서 느껴지는 감정',
    font='Malgun Gothic',
    pos=(-.5, -0.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
wth_self_txt = visual.TextStim(win=win, name='wth_self_txt',
    text='단어가 자신과 관련이 있는 정도',
    font='Malgun Gothic',
    pos=(0.5, -.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
wth_self_rating = visual.Slider(win=win, name='wth_self_rating',
    startValue=None, size=(.45, 0.05), pos=(0.5, -.1), units=None,
    labels=("전혀 나와 관련 없음","나와 관련 매우 많음"), ticks=(0, 1), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='red', lineColor='black', colorSpace='rgb',
    font='Malgun Gothic', labelHeight=0.03,
    flip=False, ori=0.0, depth=-5, readOnly=False)
wth_rating_end = visual.TextBox2(
     win, text='클릭해 주세요', font='Malgun Gothic',
     pos=(-.02, -.42),     letterHeight=0.03,
     size=(0.19, 0.06), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='white', borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='wth_rating_end',
     autoLog=False,
)
wth_mouse = event.Mouse(win=win)
x, y = [None, None]
wth_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "exp_end" ---
wth_end_image = visual.ImageStim(
    win=win,
    name='wth_end_image', units='pix', 
    image='Mood Weather Module Artwork/weather input/background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
exp_end_text = visual.TextStim(win=win, name='exp_end_text',
    text='단어연상 종료\n\n충분히 휴식하시고\n스페이스를 눌러\n다음 과제로 넘어가세요.\n\n(진행자: 키보드 제거)',
    font='Malgun Gothic',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
exp_end_key = keyboard.Keyboard()

# --- Initialize components for Routine "total_loop" ---

# --- Initialize components for Routine "fl_starter_code" ---
# Run 'Begin Experiment' code from fl_random_cb
# neg, neut, pos order


reps = 99 #default 99
testing = 1 #default 1

#fprac = 2 #default 2
#fmain = 15 #default 15

counter_resp = int(expInfo['id*'])%2

#= randint(0, 1)
#stset = randint(1,2)

jkl_resp = 0
lkj_resp = 1




fl_starter_back = visual.ImageStim(
    win=win,
    name='fl_starter_back', units='pix', 
    image='pics/fl_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fl_starter_text = visual.TextStim(win=win, name='fl_starter_text',
    text='집행기능 측정을 시작합니다.\n\n약 7분정도 소요됩니다.\n\n안내영상을 시청하시려면\n화면을 더블클릭하세요.',
    font='Malgun Gothic',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fl_starter = keyboard.Keyboard()
fl_next_click = event.Mouse(win=win)
x, y = [None, None]
fl_next_click.mouseClock = core.Clock()

# --- Initialize components for Routine "fl_inst" ---
fl_inst_img = visual.ImageStim(
    win=win,
    name='fl_inst_img', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fl_inst_resp = keyboard.Keyboard()
fl_inst_text_2 = visual.TextStim(win=win, name='fl_inst_text_2',
    text='스페이스로 넘어가세요',
    font='Malgun Gothic',
    pos=(0, -.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
fl_inst_sound = sound.Sound('ins/fl_inst_click.wav', secs=-1, stereo=True, hamming=True,
    name='fl_inst_sound')
fl_inst_sound.setVolume(1.0)
fl_next_again = event.Mouse(win=win)
x, y = [None, None]
fl_next_again.mouseClock = core.Clock()

# --- Initialize components for Routine "fl_fix_2" ---
back_2 = visual.ImageStim(
    win=win,
    name='back_2', units='pix', 
    image='pics/fl_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fixation_2 = visual.ImageStim(
    win=win,
    name='fixation_2', 
    image='pics/fixation_2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.025, 0.025),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
fl_next = visual.TextStim(win=win, name='fl_next',
    text='시작',
    font='Malgun Gothic',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "fl_tag_prac" ---

# --- Initialize components for Routine "Flanker" ---
# Run 'Begin Experiment' code from fl_anime
he = 200
wi = he

dist_img =""
targ_img =""

a=""
b=""
d=""

# small ones
set1_angry_blink_g_1   = "pics/flan/set1_angry_grey_1.png"

set1_neutral_blink_g_1   = "pics/flan/set1_neutral_grey_1.png"

set1_happy_blink_g_1   = "pics/flan/set1_happy_grey_1.png"


set1_angry_blink_y_1   = "pics/flan/set1_angry_yel_1.png"

set1_neutral_blink_y_1   = "pics/flan/set1_neutral_yel_1.png"

set1_happy_blink_y_1   = "pics/flan/set1_happy_yel_1.png"


set1_angry_g   = "pics/flan/set1_angry_grey_4.png"
set1_neutral_g = "pics/flan/set1_neutral_grey_4.png"
set1_happy_g   = "pics/flan/set1_happy_grey_4.png"

set1_angry_y   = "pics/flan/set1_angry_yel_4.png"
set1_neutral_y = "pics/flan/set1_neutral_yel_4.png"
set1_happy_y   = "pics/flan/set1_happy_yel_4.png"

set2_angry_blink_g_1   = "pics/flan/set2_angry_grey_1.png"

set2_neutral_blink_g_1   = "pics/flan/set2_neutral_grey_1.png"

set2_happy_blink_g_1   = "pics/flan/set2_happy_grey_1.png"


set2_angry_blink_y_1   = "pics/flan/set2_angry_yel_1.png"

set2_neutral_blink_y_1   = "pics/flan/set2_neutral_yel_1.png"

set2_happy_blink_y_1   = "pics/flan/set2_happy_yel_1.png"

set2_angry_g   = "pics/flan/set2_angry_grey_4.png"
set2_neutral_g = "pics/flan/set2_neutral_grey_4.png"
set2_happy_g   = "pics/flan/set2_happy_grey_4.png"

set2_angry_y   = "pics/flan/set2_angry_yel_4.png"
set2_neutral_y = "pics/flan/set2_neutral_yel_4.png"
set2_happy_y   = "pics/flan/set2_happy_yel_4.png"

neg_button = "pics/neg_button.png"
neu_button = "pics/neu_button.png"
pos_button = "pics/pos_button.png"

if counter_resp == jkl_resp:
    tex1 = 'J';
    tex2 = 'K';
    tex3 = 'L';
    j_img = neg_button;
    k_img = neu_button;
    l_img = pos_button;

if counter_resp == lkj_resp:
    tex1 = 'L';
    tex2 = 'K';
    tex3 = 'J';
    j_img = pos_button;
    k_img = neu_button;
    l_img = neg_button;
    

randg = [1,2,1,2,1,2,1,2,1,2];
#rtn = 0;
#colnt = shuffle(randg);
#print(colnt);
# Run 'Begin Experiment' code from fl_code_clik
proper_rt = 0
fl_back_image = visual.ImageStim(
    win=win,
    name='fl_back_image', units='pix', 
    image='pics/fl_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
fl_fix = visual.ImageStim(
    win=win,
    name='fl_fix', 
    image='pics/fixation_2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.025, 0.025),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
dist1 = visual.ImageStim(
    win=win,
    name='dist1', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-he*.7, 0), size=(he, he),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-5.0)
dist2 = visual.ImageStim(
    win=win,
    name='dist2', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-(he+he)*.7, 0), size=(he, he),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-6.0)
dist3 = visual.ImageStim(
    win=win,
    name='dist3', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(he*.7, 0), size=(he, he),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-7.0)
dist4 = visual.ImageStim(
    win=win,
    name='dist4', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=((he+he)*.7, 0), size=(he, he),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-8.0)
targ = visual.ImageStim(
    win=win,
    name='targ', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(he, he),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-9.0)
j_button = visual.ImageStim(
    win=win,
    name='j_button', 
    image=j_img, mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.4), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
k_button = visual.ImageStim(
    win=win,
    name='k_button', 
    image=k_img, mask=None, anchor='center',
    ori=0.0, pos=(0.7, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
l_button = visual.ImageStim(
    win=win,
    name='l_button', 
    image=l_img, mask=None, anchor='center',
    ori=0.0, pos=(0.8, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
fl_mouse = event.Mouse(win=win)
x, y = [None, None]
fl_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "flankerfeedback" ---
fl_back_image2 = visual.ImageStim(
    win=win,
    name='fl_back_image2', units='pix', 
    image='pics/fl_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fl_feedback = visual.TextStim(win=win, name='fl_feedback',
    text='',
    font='Malgun Gothic',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='darkred', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
j_button2 = visual.ImageStim(
    win=win,
    name='j_button2', 
    image=j_img, mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.4), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
k_button2 = visual.ImageStim(
    win=win,
    name='k_button2', 
    image=k_img, mask=None, anchor='center',
    ori=0.0, pos=(0.7, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
l_button2 = visual.ImageStim(
    win=win,
    name='l_button2', 
    image=l_img, mask=None, anchor='center',
    ori=0.0, pos=(0.8, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "fl_say_main" ---
fl_mainback = visual.ImageStim(
    win=win,
    name='fl_mainback', units='pix', 
    image='pics/fl_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fl_main_text = visual.TextStim(win=win, name='fl_main_text',
    text='본 실험으로 넘어가려면\n화면을 더블클릭하세요',
    font='Malgun Gothic',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
fl_key_resp = keyboard.Keyboard()
fl_mouse_m = event.Mouse(win=win)
x, y = [None, None]
fl_mouse_m.mouseClock = core.Clock()

# --- Initialize components for Routine "fl_fix_2" ---
back_2 = visual.ImageStim(
    win=win,
    name='back_2', units='pix', 
    image='pics/fl_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fixation_2 = visual.ImageStim(
    win=win,
    name='fixation_2', 
    image='pics/fixation_2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.025, 0.025),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
fl_next = visual.TextStim(win=win, name='fl_next',
    text='시작',
    font='Malgun Gothic',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "fl_tag_main" ---

# --- Initialize components for Routine "Flanker" ---
# Run 'Begin Experiment' code from fl_anime
he = 200
wi = he

dist_img =""
targ_img =""

a=""
b=""
d=""

# small ones
set1_angry_blink_g_1   = "pics/flan/set1_angry_grey_1.png"

set1_neutral_blink_g_1   = "pics/flan/set1_neutral_grey_1.png"

set1_happy_blink_g_1   = "pics/flan/set1_happy_grey_1.png"


set1_angry_blink_y_1   = "pics/flan/set1_angry_yel_1.png"

set1_neutral_blink_y_1   = "pics/flan/set1_neutral_yel_1.png"

set1_happy_blink_y_1   = "pics/flan/set1_happy_yel_1.png"


set1_angry_g   = "pics/flan/set1_angry_grey_4.png"
set1_neutral_g = "pics/flan/set1_neutral_grey_4.png"
set1_happy_g   = "pics/flan/set1_happy_grey_4.png"

set1_angry_y   = "pics/flan/set1_angry_yel_4.png"
set1_neutral_y = "pics/flan/set1_neutral_yel_4.png"
set1_happy_y   = "pics/flan/set1_happy_yel_4.png"

set2_angry_blink_g_1   = "pics/flan/set2_angry_grey_1.png"

set2_neutral_blink_g_1   = "pics/flan/set2_neutral_grey_1.png"

set2_happy_blink_g_1   = "pics/flan/set2_happy_grey_1.png"


set2_angry_blink_y_1   = "pics/flan/set2_angry_yel_1.png"

set2_neutral_blink_y_1   = "pics/flan/set2_neutral_yel_1.png"

set2_happy_blink_y_1   = "pics/flan/set2_happy_yel_1.png"

set2_angry_g   = "pics/flan/set2_angry_grey_4.png"
set2_neutral_g = "pics/flan/set2_neutral_grey_4.png"
set2_happy_g   = "pics/flan/set2_happy_grey_4.png"

set2_angry_y   = "pics/flan/set2_angry_yel_4.png"
set2_neutral_y = "pics/flan/set2_neutral_yel_4.png"
set2_happy_y   = "pics/flan/set2_happy_yel_4.png"

neg_button = "pics/neg_button.png"
neu_button = "pics/neu_button.png"
pos_button = "pics/pos_button.png"

if counter_resp == jkl_resp:
    tex1 = 'J';
    tex2 = 'K';
    tex3 = 'L';
    j_img = neg_button;
    k_img = neu_button;
    l_img = pos_button;

if counter_resp == lkj_resp:
    tex1 = 'L';
    tex2 = 'K';
    tex3 = 'J';
    j_img = pos_button;
    k_img = neu_button;
    l_img = neg_button;
    

randg = [1,2,1,2,1,2,1,2,1,2];
#rtn = 0;
#colnt = shuffle(randg);
#print(colnt);
# Run 'Begin Experiment' code from fl_code_clik
proper_rt = 0
fl_back_image = visual.ImageStim(
    win=win,
    name='fl_back_image', units='pix', 
    image='pics/fl_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
fl_fix = visual.ImageStim(
    win=win,
    name='fl_fix', 
    image='pics/fixation_2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.025, 0.025),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
dist1 = visual.ImageStim(
    win=win,
    name='dist1', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-he*.7, 0), size=(he, he),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-5.0)
dist2 = visual.ImageStim(
    win=win,
    name='dist2', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-(he+he)*.7, 0), size=(he, he),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-6.0)
dist3 = visual.ImageStim(
    win=win,
    name='dist3', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(he*.7, 0), size=(he, he),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-7.0)
dist4 = visual.ImageStim(
    win=win,
    name='dist4', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=((he+he)*.7, 0), size=(he, he),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-8.0)
targ = visual.ImageStim(
    win=win,
    name='targ', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(he, he),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-9.0)
j_button = visual.ImageStim(
    win=win,
    name='j_button', 
    image=j_img, mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.4), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
k_button = visual.ImageStim(
    win=win,
    name='k_button', 
    image=k_img, mask=None, anchor='center',
    ori=0.0, pos=(0.7, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
l_button = visual.ImageStim(
    win=win,
    name='l_button', 
    image=l_img, mask=None, anchor='center',
    ori=0.0, pos=(0.8, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
fl_mouse = event.Mouse(win=win)
x, y = [None, None]
fl_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "flankerfeedback" ---
fl_back_image2 = visual.ImageStim(
    win=win,
    name='fl_back_image2', units='pix', 
    image='pics/fl_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fl_feedback = visual.TextStim(win=win, name='fl_feedback',
    text='',
    font='Malgun Gothic',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='darkred', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
j_button2 = visual.ImageStim(
    win=win,
    name='j_button2', 
    image=j_img, mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.4), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
k_button2 = visual.ImageStim(
    win=win,
    name='k_button2', 
    image=k_img, mask=None, anchor='center',
    ori=0.0, pos=(0.7, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
l_button2 = visual.ImageStim(
    win=win,
    name='l_button2', 
    image=l_img, mask=None, anchor='center',
    ori=0.0, pos=(0.8, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "para_starter_code" ---
# Run 'Begin Experiment' code from para_random_cb
# This code controls the response counter-balanccing.

#constant for counter conditions
bhya_resp = 0
bayh_resp = 1

counter_resp=int(expInfo['id*'])%2

#
#if counter_resp == bhya_resp:
#    st2_selections = [0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17]
#elif counter_resp == bayh_resp:
#    st2_selections = [0,1,2,3,4,7,8,9,10,11,12,13,14,17,18,19]

""" this snippet randomises the presentation
 order of stimuli between two lists"""
stset = randint(1,2)
if stset == 1:
    st2_set = 'loop\stroop_random1_trial_control.xlsx'
elif stset == 2:
    st2_set = 'loop\stroop_random2_trial_control.xlsx'



para_starter = visual.ImageStim(
    win=win,
    name='para_starter', units='pix', 
    image='pics/st_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
para_starter_text = visual.TextStim(win=win, name='para_starter_text',
    text='주의편향 측정을 시작합니다.\n\n안내영상을 시청하시려면\n화면을 더블클릭하세요.',
    font='Malgun Gothic',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
para_starter_key = keyboard.Keyboard()
para_skip_click = event.Mouse(win=win)
x, y = [None, None]
para_skip_click.mouseClock = core.Clock()

# --- Initialize components for Routine "para_inst" ---
para_inst_img = visual.ImageStim(
    win=win,
    name='para_inst_img', units='pix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
para_inst_sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='para_inst_sound')
para_inst_sound.setVolume(1.0)
para_inst_key = keyboard.Keyboard()
para_click_next = event.Mouse(win=win)
x, y = [None, None]
para_click_next.mouseClock = core.Clock()

# --- Initialize components for Routine "para_fix" ---
para_fix_back = visual.ImageStim(
    win=win,
    name='para_fix_back', units='pix', 
    image='pics/st_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
para_fix_2 = visual.ImageStim(
    win=win,
    name='para_fix_2', 
    image='pics/fixation_2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.025, 0.025),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
para_text_next = visual.TextStim(win=win, name='para_text_next',
    text='시작',
    font='Malgun Gothic',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "para_tag_prc" ---

# --- Initialize components for Routine "parachute" ---
# Run 'Begin Experiment' code from para_code_ani
posx = 960;
posy = 540;

para_yel = "pics/yellow.png"
para_red = "pics/red.png"
para_blu = "pics/blue.png"

randg = [1,2,1,2,1,2,1,2,1,2]

he = 200
wi = he

a=""
b=""
d=""

# small ones
set1_angry_blink_g_1   = "pics/flan/set1_angry_grey_1.png"

set1_neutral_blink_g_1   = "pics/flan/set1_neutral_grey_1.png"

set1_happy_blink_g_1   = "pics/flan/set1_happy_grey_1.png"


set1_angry_blink_y_1   = "pics/flan/set1_angry_yel_1.png"

set1_neutral_blink_y_1   = "pics/flan/set1_neutral_yel_1.png"

set1_happy_blink_y_1   = "pics/flan/set1_happy_yel_1.png"


set1_angry_g   = "pics/flan/set1_angry_grey_4.png"
set1_neutral_g = "pics/flan/set1_neutral_grey_4.png"
set1_happy_g   = "pics/flan/set1_happy_grey_4.png"

set1_angry_y   = "pics/flan/set1_angry_yel_4.png"
set1_neutral_y = "pics/flan/set1_neutral_yel_4.png"
set1_happy_y   = "pics/flan/set1_happy_yel_4.png"

set2_angry_blink_g_1   = "pics/flan/set2_angry_grey_1.png"

set2_neutral_blink_g_1   = "pics/flan/set2_neutral_grey_1.png"

set2_happy_blink_g_1   = "pics/flan/set2_happy_grey_1.png"


set2_angry_blink_y_1   = "pics/flan/set2_angry_yel_1.png"

set2_neutral_blink_y_1   = "pics/flan/set2_neutral_yel_1.png"

set2_happy_blink_y_1   = "pics/flan/set2_happy_yel_1.png"

set2_angry_g   = "pics/flan/set2_angry_grey_4.png"
set2_neutral_g = "pics/flan/set2_neutral_grey_4.png"
set2_happy_g   = "pics/flan/set2_happy_grey_4.png"

set2_angry_y   = "pics/flan/set2_angry_yel_4.png"
set2_neutral_y = "pics/flan/set2_neutral_yel_4.png"
set2_happy_y   = "pics/flan/set2_happy_yel_4.png"

neg_button = "pics/neg_button.png"
neu_button = "pics/neu_button.png"
pos_button = "pics/pos_button.png"

# Run 'Begin Experiment' code from para_code
para_rt = -1
para_back = visual.ImageStim(
    win=win,
    name='para_back', units='pix', 
    image='pics/st_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
para_fix_prac = visual.ImageStim(
    win=win,
    name='para_fix_prac', 
    image='pics/fixation_2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.025, 0.025),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
face_dist_2 = visual.ImageStim(
    win=win,
    name='face_dist_2', units='pix', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(200, 200),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-4.0)
para_targ_2 = visual.ImageStim(
    win=win,
    name='para_targ_2', units='pix', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(200, 200),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-5.0)
mouse_st = event.Mouse(win=win)
x, y = [None, None]
mouse_st.mouseClock = core.Clock()
st2_resp = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Malgun Gothic',
    pos=(0, .3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "para_feedback" ---
para_f_back = visual.ImageStim(
    win=win,
    name='para_f_back', units='pix', 
    image='pics/st_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
para_feed_message = visual.TextStim(win=win, name='para_feed_message',
    text='',
    font='Malgun Gothic',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='darkred', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "para_say_main" ---
para_main_back = visual.ImageStim(
    win=win,
    name='para_main_back', units='pix', 
    image='pics/st_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
para_main_text = visual.TextStim(win=win, name='para_main_text',
    text='충분히 이해되셨나요?\n\n시작하려면 화면을 \n더블클릭하세요',
    font='Malgun Gothic',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
para_mouse = event.Mouse(win=win)
x, y = [None, None]
para_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "para_fix" ---
para_fix_back = visual.ImageStim(
    win=win,
    name='para_fix_back', units='pix', 
    image='pics/st_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
para_fix_2 = visual.ImageStim(
    win=win,
    name='para_fix_2', 
    image='pics/fixation_2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.025, 0.025),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
para_text_next = visual.TextStim(win=win, name='para_text_next',
    text='시작',
    font='Malgun Gothic',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "para_tag_main" ---

# --- Initialize components for Routine "parachute" ---
# Run 'Begin Experiment' code from para_code_ani
posx = 960;
posy = 540;

para_yel = "pics/yellow.png"
para_red = "pics/red.png"
para_blu = "pics/blue.png"

randg = [1,2,1,2,1,2,1,2,1,2]

he = 200
wi = he

a=""
b=""
d=""

# small ones
set1_angry_blink_g_1   = "pics/flan/set1_angry_grey_1.png"

set1_neutral_blink_g_1   = "pics/flan/set1_neutral_grey_1.png"

set1_happy_blink_g_1   = "pics/flan/set1_happy_grey_1.png"


set1_angry_blink_y_1   = "pics/flan/set1_angry_yel_1.png"

set1_neutral_blink_y_1   = "pics/flan/set1_neutral_yel_1.png"

set1_happy_blink_y_1   = "pics/flan/set1_happy_yel_1.png"


set1_angry_g   = "pics/flan/set1_angry_grey_4.png"
set1_neutral_g = "pics/flan/set1_neutral_grey_4.png"
set1_happy_g   = "pics/flan/set1_happy_grey_4.png"

set1_angry_y   = "pics/flan/set1_angry_yel_4.png"
set1_neutral_y = "pics/flan/set1_neutral_yel_4.png"
set1_happy_y   = "pics/flan/set1_happy_yel_4.png"

set2_angry_blink_g_1   = "pics/flan/set2_angry_grey_1.png"

set2_neutral_blink_g_1   = "pics/flan/set2_neutral_grey_1.png"

set2_happy_blink_g_1   = "pics/flan/set2_happy_grey_1.png"


set2_angry_blink_y_1   = "pics/flan/set2_angry_yel_1.png"

set2_neutral_blink_y_1   = "pics/flan/set2_neutral_yel_1.png"

set2_happy_blink_y_1   = "pics/flan/set2_happy_yel_1.png"

set2_angry_g   = "pics/flan/set2_angry_grey_4.png"
set2_neutral_g = "pics/flan/set2_neutral_grey_4.png"
set2_happy_g   = "pics/flan/set2_happy_grey_4.png"

set2_angry_y   = "pics/flan/set2_angry_yel_4.png"
set2_neutral_y = "pics/flan/set2_neutral_yel_4.png"
set2_happy_y   = "pics/flan/set2_happy_yel_4.png"

neg_button = "pics/neg_button.png"
neu_button = "pics/neu_button.png"
pos_button = "pics/pos_button.png"

# Run 'Begin Experiment' code from para_code
para_rt = -1
para_back = visual.ImageStim(
    win=win,
    name='para_back', units='pix', 
    image='pics/st_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
para_fix_prac = visual.ImageStim(
    win=win,
    name='para_fix_prac', 
    image='pics/fixation_2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.025, 0.025),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
face_dist_2 = visual.ImageStim(
    win=win,
    name='face_dist_2', units='pix', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(200, 200),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-4.0)
para_targ_2 = visual.ImageStim(
    win=win,
    name='para_targ_2', units='pix', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(200, 200),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-5.0)
mouse_st = event.Mouse(win=win)
x, y = [None, None]
mouse_st.mouseClock = core.Clock()
st2_resp = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Malgun Gothic',
    pos=(0, .3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "para_feedback" ---
para_f_back = visual.ImageStim(
    win=win,
    name='para_f_back', units='pix', 
    image='pics/st_back.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
para_feed_message = visual.TextStim(win=win, name='para_feed_message',
    text='',
    font='Malgun Gothic',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='darkred', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "fis_initialSet" ---
# Run 'Begin Experiment' code from fis_CounterBalancing_code
name_var = expInfo['id*']
num_var = int(name_var[:3])

if (num_var %2) == 0: #if even number,
    #GreenLoop = 1
    #OrangeLoop = 0
    GOloop = 0;
    GOprac = 'loop/[통합실험]ExpListGreen_Practice.xlsx'
    GOmain = 'loop/[통합실험]ExpListGreen_Round1.xlsx'
    #Green fish would be correct fish
else: #if odd number,
    #GreenLoop = 0
    #OrangeLoop = 1
    #Orange fish would be correct fish 
    GOloop = 1;
    GOprac = 'loop/[통합실험]ExpListOrange_Practice.xlsx'
    GOmain = 'loop/[통합실험]ExpListOrange_Round1.xlsx'
    
    
InstCount = 5 # default 5
PracCount = 5 # default 5
fis_roundN = 1 # default 1
#fis_round_tot = 5; # default 5
Gnum = 0;
Onum = 1;
image = visual.ImageStim(
    win=win,
    name='image', units='pix', 
    image='fis_artwork/fish_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fis_text_2 = visual.TextStim(win=win, name='fis_text_2',
    text='사회적 민감성 측정을 시작합니다.\n\n안내영상을 시청하시려면\n화면을 더블클릭',
    font='Malgun Gothic',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fis_key_resp = keyboard.Keyboard()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "fis_Instruction" ---
fis_backs = visual.ImageStim(
    win=win,
    name='fis_backs', units='pix', 
    image='fis_artwork/fish_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fis_skip_movie = visual.TextStim(win=win, name='fis_skip_movie',
    text='충분히 이해되셨으면\n더블클릭으로 넘어가세요',
    font='Malgun Gothic',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
fis_secret_quit = keyboard.Keyboard()
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
# Run 'Begin Experiment' code from fis_code_9
if GOloop == Gnum:
    GOcon = Gnum;
    insmov= 'fis_artwork/fish_instruction_GreenVersion.mp4'
elif GOloop == Onum:
    GOnum = Onum;
    insmov= 'fis_artwork/fish_instruction_OrangeVersion.mp4'
    
PracCount= 5

# --- Initialize components for Routine "fis_readycount" ---
fis_back = visual.ImageStim(
    win=win,
    name='fis_back', units='pix', 
    image='fis_artwork/fish_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fis_start_prac = visual.TextStim(win=win, name='fis_start_prac',
    text='준비',
    font='Malgun Gothic',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
fis_get_ready = visual.TextStim(win=win, name='fis_get_ready',
    text='시작',
    font='Malgun Gothic',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "fis_practiral" ---
fis_slider_2 = visual.Slider(win=win, name='fis_slider_2',
    startValue=None, size=(0.4, .6), pos=(0, 0.0), units=None,
    labels=('approach','avoid'), ticks=(1,2), granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor=(-0.0039, 1.0000, 0.6627), lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=True, ori=0.0, depth=0, readOnly=False)
fis_BackGround_2 = visual.ImageStim(
    win=win,
    name='fis_BackGround_2', units='pix', 
    image='fis_artwork/fish_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Fish_2 = visual.ImageStim(
    win=win,
    name='Fish_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(1, 1), size=(0.41, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
fis_WordBox_2 = visual.ImageStim(
    win=win,
    name='fis_WordBox_2', 
    image='fis_artwork/speechcloud_long.png', mask=None, anchor='center',
    ori=7.0, pos=[0,0], size=(1, 0.42),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
fis_Words_2 = visual.TextStim(win=win, name='fis_Words_2',
    text='',
    font='Malgun Gothic',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-5.0);

# --- Initialize components for Routine "fis_feedback_prac" ---
fis_BackGround_Feedback_2 = visual.ImageStim(
    win=win,
    name='fis_BackGround_Feedback_2', units='pix', 
    image='fis_artwork/fish_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fis_Feedbacks_2 = visual.TextStim(win=win, name='fis_Feedbacks_2',
    text='',
    font='Malgun Gothic',
    pos=(0, 0.03), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "fis_continue_prac" ---
fis_image_3 = visual.ImageStim(
    win=win,
    name='fis_image_3', units='pix', 
    image='fis_artwork/fish_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fis_Continue_or_not = keyboard.Keyboard()
fis_mouse_skip = event.Mouse(win=win)
x, y = [None, None]
fis_mouse_skip.mouseClock = core.Clock()
fis_next_text = visual.TextStim(win=win, name='fis_next_text',
    text='충분히 이해되셨나요?\n\n정확하고, 최대한 빠르게 반응할수록\n좋은 결과를 얻을 수 있습니다.\n\n화면을 더블클릭하여\n본시행으로 넘어가세요\n',
    font='Malgun Gothic',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "fis_readycount" ---
fis_back = visual.ImageStim(
    win=win,
    name='fis_back', units='pix', 
    image='fis_artwork/fish_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fis_start_prac = visual.TextStim(win=win, name='fis_start_prac',
    text='준비',
    font='Malgun Gothic',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
fis_get_ready = visual.TextStim(win=win, name='fis_get_ready',
    text='시작',
    font='Malgun Gothic',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "fis_main_trial" ---
fis_slider = visual.Slider(win=win, name='fis_slider',
    startValue=None, size=(0.4, .6), pos=(0, 0.0), units=None,
    labels=('approach','avoid'), ticks=(1,2), granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor=(-0.0039, 1.0000, 0.6627), lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=True, ori=0.0, depth=0, readOnly=False)
fis_BackGround = visual.ImageStim(
    win=win,
    name='fis_BackGround', units='pix', 
    image='fis_artwork/fish_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Fish = visual.ImageStim(
    win=win,
    name='Fish', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(1, 1), size=(0.41, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
fis_WordBox = visual.ImageStim(
    win=win,
    name='fis_WordBox', 
    image='fis_artwork/speechcloud_long.png', mask=None, anchor='center',
    ori=7.0, pos=[0,0], size=(1, 0.42),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
fis_Words = visual.TextStim(win=win, name='fis_Words',
    text='',
    font='Malgun Gothic',
    pos=[0,0], height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-5.0);

# --- Initialize components for Routine "fis_feedback_trial" ---
fis_BackGround_Feedback = visual.ImageStim(
    win=win,
    name='fis_BackGround_Feedback', units='pix', 
    image='fis_artwork/fish_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fis_Feedbacks = visual.TextStim(win=win, name='fis_Feedbacks',
    text='',
    font='Malgun Gothic',
    pos=(0, 0.03), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "fis_main_control" ---

# --- Initialize components for Routine "fis_rout_break" ---
fis_break_interval = visual.ImageStim(
    win=win,
    name='fis_break_interval', units='pix', 
    image='fis_artwork/fish_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fis_text = visual.TextStim(win=win, name='fis_text',
    text='30초 휴식 후 다음 라운드를 시작하겠습니다. \n\n특정 요청을 하는 물고기가 더 많아집니다. \n\n말풍선을 유심히 봐주시기 바랍니다. ',
    font='Malgun Gothic',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "fis_interblock" ---
fis_mouse = event.Mouse(win=win)
x, y = [None, None]
fis_mouse.mouseClock = core.Clock()
fis_stratnextround = visual.ImageStim(
    win=win,
    name='fis_stratnextround', units='pix', 
    image='fis_artwork/fish_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fis_stt_round = visual.TextStim(win=win, name='fis_stt_round',
    text='시작하려면 \n화면을 더블클릭 하세요',
    font='Malgun Gothic',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "fis_readycount" ---
fis_back = visual.ImageStim(
    win=win,
    name='fis_back', units='pix', 
    image='fis_artwork/fish_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fis_start_prac = visual.TextStim(win=win, name='fis_start_prac',
    text='준비',
    font='Malgun Gothic',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
fis_get_ready = visual.TextStim(win=win, name='fis_get_ready',
    text='시작',
    font='Malgun Gothic',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "total_end" ---
end_back = visual.ImageStim(
    win=win,
    name='end_back', units='pix', 
    image='fis_artwork/fish_background.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1920,1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
total_end_text = visual.TextStim(win=win, name='total_end_text',
    text='참여해주셔서 감사합니다.\n자동으로 종료됩니다.',
    font='Malgun Gothic',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Total_control" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from time_control


win.mouseVisible = False
# keep track of which components have finished
Total_controlComponents = []
for thisComponent in Total_controlComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Total_control" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Total_controlComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Total_control" ---
for thisComponent in Total_controlComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Total_control" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "general_instruction" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_5
win.fullscr = False
#not sure if this is necessary
win.winHandle.set_fullscreen(False)
win.winHandle.minimize()
win.flip()

win.winHandle.maximize()
win.flip()
gen_inst_resp.keys = []
gen_inst_resp.rt = []
_gen_inst_resp_allKeys = []
# keep track of which components have finished
general_instructionComponents = [wth_inst_image, gen_inst_resp]
for thisComponent in general_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "general_instruction" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wth_inst_image* updates
    if wth_inst_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wth_inst_image.frameNStart = frameN  # exact frame index
        wth_inst_image.tStart = t  # local t and not account for scr refresh
        wth_inst_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wth_inst_image, 'tStartRefresh')  # time at next scr refresh
        wth_inst_image.setAutoDraw(True)
    
    # *gen_inst_resp* updates
    waitOnFlip = False
    if gen_inst_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gen_inst_resp.frameNStart = frameN  # exact frame index
        gen_inst_resp.tStart = t  # local t and not account for scr refresh
        gen_inst_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gen_inst_resp, 'tStartRefresh')  # time at next scr refresh
        gen_inst_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(gen_inst_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(gen_inst_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if gen_inst_resp.status == STARTED and not waitOnFlip:
        theseKeys = gen_inst_resp.getKeys(keyList=['space'], waitRelease=False)
        _gen_inst_resp_allKeys.extend(theseKeys)
        if len(_gen_inst_resp_allKeys):
            gen_inst_resp.keys = _gen_inst_resp_allKeys[-1].name  # just the last key pressed
            gen_inst_resp.rt = _gen_inst_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in general_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "general_instruction" ---
for thisComponent in general_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "general_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
weather = data.TrialHandler(nReps=skip_weather, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='weather')
thisExp.addLoop(weather)  # add the loop to the experiment
thisWeather = weather.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisWeather.rgb)
if thisWeather != None:
    for paramName in thisWeather:
        exec('{} = thisWeather[paramName]'.format(paramName))

for thisWeather in weather:
    currentLoop = weather
    # abbreviate parameter names if possible (e.g. rgb = thisWeather.rgb)
    if thisWeather != None:
        for paramName in thisWeather:
            exec('{} = thisWeather[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "wth_inst" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    wth_instComponents = [wth_movie, key_resp]
    for thisComponent in wth_instComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "wth_inst" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wth_movie* updates
        if wth_movie.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            wth_movie.frameNStart = frameN  # exact frame index
            wth_movie.tStart = t  # local t and not account for scr refresh
            wth_movie.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wth_movie, 'tStartRefresh')  # time at next scr refresh
            wth_movie.setAutoDraw(True)
        if wth_movie.status == FINISHED:  # force-end the routine
            continueRoutine = False
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wth_instComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "wth_inst" ---
    for thisComponent in wth_instComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    wth_movie.stop()
    # the Routine "wth_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    wth_repeat_prac = data.TrialHandler(nReps=wth_repeat_prac_n, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='wth_repeat_prac')
    thisExp.addLoop(wth_repeat_prac)  # add the loop to the experiment
    thisWth_repeat_prac = wth_repeat_prac.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisWth_repeat_prac.rgb)
    if thisWth_repeat_prac != None:
        for paramName in thisWth_repeat_prac:
            exec('{} = thisWth_repeat_prac[paramName]'.format(paramName))
    
    for thisWth_repeat_prac in wth_repeat_prac:
        currentLoop = wth_repeat_prac
        # abbreviate parameter names if possible (e.g. rgb = thisWth_repeat_prac.rgb)
        if thisWth_repeat_prac != None:
            for paramName in thisWth_repeat_prac:
                exec('{} = thisWth_repeat_prac[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "wth_begin_prac" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        wth_next_next.keys = []
        wth_next_next.rt = []
        _wth_next_next_allKeys = []
        # Run 'Begin Routine' code from code_6
        win.fullscr=False
        # keep track of which components have finished
        wth_begin_pracComponents = [wth_background_inst, wth_text, wth_next_next]
        for thisComponent in wth_begin_pracComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "wth_begin_prac" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *wth_background_inst* updates
            if wth_background_inst.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                wth_background_inst.frameNStart = frameN  # exact frame index
                wth_background_inst.tStart = t  # local t and not account for scr refresh
                wth_background_inst.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_background_inst, 'tStartRefresh')  # time at next scr refresh
                wth_background_inst.setAutoDraw(True)
            
            # *wth_text* updates
            if wth_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                wth_text.frameNStart = frameN  # exact frame index
                wth_text.tStart = t  # local t and not account for scr refresh
                wth_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_text, 'tStartRefresh')  # time at next scr refresh
                wth_text.setAutoDraw(True)
            
            # *wth_next_next* updates
            waitOnFlip = False
            if wth_next_next.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                wth_next_next.frameNStart = frameN  # exact frame index
                wth_next_next.tStart = t  # local t and not account for scr refresh
                wth_next_next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_next_next, 'tStartRefresh')  # time at next scr refresh
                wth_next_next.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(wth_next_next.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(wth_next_next.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if wth_next_next.status == STARTED and not waitOnFlip:
                theseKeys = wth_next_next.getKeys(keyList=['space'], waitRelease=False)
                _wth_next_next_allKeys.extend(theseKeys)
                if len(_wth_next_next_allKeys):
                    wth_next_next.keys = _wth_next_next_allKeys[-1].name  # just the last key pressed
                    wth_next_next.rt = _wth_next_next_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wth_begin_pracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "wth_begin_prac" ---
        for thisComponent in wth_begin_pracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "wth_begin_prac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "wth_think_prac" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from wth_code_6
        win.fullscr=False
        # keep track of which components have finished
        wth_think_pracComponents = [wth_background_6, wth_think_instr_2, wth_think_cross_2]
        for thisComponent in wth_think_pracComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "wth_think_prac" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *wth_background_6* updates
            if wth_background_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_background_6.frameNStart = frameN  # exact frame index
                wth_background_6.tStart = t  # local t and not account for scr refresh
                wth_background_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_background_6, 'tStartRefresh')  # time at next scr refresh
                wth_background_6.setAutoDraw(True)
            if wth_background_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wth_background_6.tStartRefresh + stimulus_interval_prac-frameTolerance:
                    # keep track of stop time/frame for later
                    wth_background_6.tStop = t  # not accounting for scr refresh
                    wth_background_6.frameNStop = frameN  # exact frame index
                    wth_background_6.setAutoDraw(False)
            
            # *wth_think_instr_2* updates
            if wth_think_instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_think_instr_2.frameNStart = frameN  # exact frame index
                wth_think_instr_2.tStart = t  # local t and not account for scr refresh
                wth_think_instr_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_think_instr_2, 'tStartRefresh')  # time at next scr refresh
                wth_think_instr_2.setAutoDraw(True)
            if wth_think_instr_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wth_think_instr_2.tStartRefresh + stimulus_interval_prac-frameTolerance:
                    # keep track of stop time/frame for later
                    wth_think_instr_2.tStop = t  # not accounting for scr refresh
                    wth_think_instr_2.frameNStop = frameN  # exact frame index
                    wth_think_instr_2.setAutoDraw(False)
            
            # *wth_think_cross_2* updates
            if wth_think_cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_think_cross_2.frameNStart = frameN  # exact frame index
                wth_think_cross_2.tStart = t  # local t and not account for scr refresh
                wth_think_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_think_cross_2, 'tStartRefresh')  # time at next scr refresh
                wth_think_cross_2.setAutoDraw(True)
            if wth_think_cross_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wth_think_cross_2.tStartRefresh + stimulus_interval_prac-frameTolerance:
                    # keep track of stop time/frame for later
                    wth_think_cross_2.tStop = t  # not accounting for scr refresh
                    wth_think_cross_2.frameNStop = frameN  # exact frame index
                    wth_think_cross_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wth_think_pracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "wth_think_prac" ---
        for thisComponent in wth_think_pracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from wth_code_6
        thisExp.addData('stimulus_interval', stimulus_interval)
        
        # the Routine "wth_think_prac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "wth_word_prac" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from wth_code_2
        win.mouseVisible = True
        # keep track of which components have finished
        wth_word_pracComponents = [wth_word_back, wth_word_instr_4]
        for thisComponent in wth_word_pracComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "wth_word_prac" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *wth_word_back* updates
            if wth_word_back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_word_back.frameNStart = frameN  # exact frame index
                wth_word_back.tStart = t  # local t and not account for scr refresh
                wth_word_back.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_word_back, 'tStartRefresh')  # time at next scr refresh
                wth_word_back.setAutoDraw(True)
            
            # *wth_word_instr_4* updates
            if wth_word_instr_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                wth_word_instr_4.frameNStart = frameN  # exact frame index
                wth_word_instr_4.tStart = t  # local t and not account for scr refresh
                wth_word_instr_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_word_instr_4, 'tStartRefresh')  # time at next scr refresh
                wth_word_instr_4.setAutoDraw(True)
            # Run 'Each Frame' code from wth_code_2
            while t > 1:
                start_time = core.getTime()
                root = Tk()
                root.attributes('-topmost',True)
                
                def retrieve_input():
                    global inputValue, continueRoutine, end_rt, t
                    inputValue=Tx.get("1.0","end-1c")
                    end_rt = core.getTime() - start_time
                    root.destroy()
                    continueRoutine = False
                    record_time = True
                    return inputValue, end_rt
            
                root.overrideredirect(True)
                #Root Geometry
                root_Width = 400
                root_Length = 300
            
                # Coordinates of top left pixel of application for centred
                x_left = int(root.winfo_screenwidth()/2-root_Width/2)
                y_top = int(root.winfo_screenheight()/2-root_Length/2)
                root_Pos = "+" + str(x_left) + "+" + str(y_top)
            
                # Window size and position
                root.geometry(str(root_Width) + "x" + str(root_Length) + root_Pos)
                #root.geometry('400x300+400+200')
            
                Tx = Text(root, font = ("MalgunGothic 30 bold"), height = 5)
                Tx.pack(side = TOP)
            
                button = Button(root, text='입력완료', command=lambda: retrieve_input(), height = 3, width= 20)
                button.pack(expand=1, side = BOTTOM)
                root.attributes('-topmost',True)
                root.update()
                root.mainloop()
                print(inputValue)
                break
            wth_repeat_prac.addData('wth_resp', inputValue) ########
            wth_repeat_prac.addData('wth_rt', end_rt) ########
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wth_word_pracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "wth_word_prac" ---
        for thisComponent in wth_word_pracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "wth_word_prac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "wth_rating_prac" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        wth_word_typed_2.setText(inputValue)
        wth_valence_rating_2.reset()
        wth_self_rating_2.reset()
        wth_rating_end_2.reset()
        # setup some python lists for storing info about the wth_mouse_5
        wth_mouse_5.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from wth_code_8
        win.fullscr=False
        # keep track of which components have finished
        wth_rating_pracComponents = [wth_background_7, wth_word_typed_2, wth_valence_rating_2, wth_valence_txt_2, wth_self_txt_2, wth_self_rating_2, wth_rating_end_2, wth_mouse_5]
        for thisComponent in wth_rating_pracComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "wth_rating_prac" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *wth_background_7* updates
            if wth_background_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_background_7.frameNStart = frameN  # exact frame index
                wth_background_7.tStart = t  # local t and not account for scr refresh
                wth_background_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_background_7, 'tStartRefresh')  # time at next scr refresh
                wth_background_7.setAutoDraw(True)
            
            # *wth_word_typed_2* updates
            if wth_word_typed_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_word_typed_2.frameNStart = frameN  # exact frame index
                wth_word_typed_2.tStart = t  # local t and not account for scr refresh
                wth_word_typed_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_word_typed_2, 'tStartRefresh')  # time at next scr refresh
                wth_word_typed_2.setAutoDraw(True)
            
            # *wth_valence_rating_2* updates
            if wth_valence_rating_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_valence_rating_2.frameNStart = frameN  # exact frame index
                wth_valence_rating_2.tStart = t  # local t and not account for scr refresh
                wth_valence_rating_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_valence_rating_2, 'tStartRefresh')  # time at next scr refresh
                wth_valence_rating_2.setAutoDraw(True)
            
            # *wth_valence_txt_2* updates
            if wth_valence_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_valence_txt_2.frameNStart = frameN  # exact frame index
                wth_valence_txt_2.tStart = t  # local t and not account for scr refresh
                wth_valence_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_valence_txt_2, 'tStartRefresh')  # time at next scr refresh
                wth_valence_txt_2.setAutoDraw(True)
            
            # *wth_self_txt_2* updates
            if wth_self_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_self_txt_2.frameNStart = frameN  # exact frame index
                wth_self_txt_2.tStart = t  # local t and not account for scr refresh
                wth_self_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_self_txt_2, 'tStartRefresh')  # time at next scr refresh
                wth_self_txt_2.setAutoDraw(True)
            
            # *wth_self_rating_2* updates
            if wth_self_rating_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_self_rating_2.frameNStart = frameN  # exact frame index
                wth_self_rating_2.tStart = t  # local t and not account for scr refresh
                wth_self_rating_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_self_rating_2, 'tStartRefresh')  # time at next scr refresh
                wth_self_rating_2.setAutoDraw(True)
            
            # *wth_rating_end_2* updates
            if wth_rating_end_2.status == NOT_STARTED and wth_self_rating_2.rating and wth_valence_rating_2.rating:
                # keep track of start time/frame for later
                wth_rating_end_2.frameNStart = frameN  # exact frame index
                wth_rating_end_2.tStart = t  # local t and not account for scr refresh
                wth_rating_end_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_rating_end_2, 'tStartRefresh')  # time at next scr refresh
                wth_rating_end_2.setAutoDraw(True)
            # *wth_mouse_5* updates
            if wth_mouse_5.status == NOT_STARTED and wth_self_rating_2.rating and wth_valence_rating_2.rating:
                # keep track of start time/frame for later
                wth_mouse_5.frameNStart = frameN  # exact frame index
                wth_mouse_5.tStart = t  # local t and not account for scr refresh
                wth_mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_mouse_5, 'tStartRefresh')  # time at next scr refresh
                wth_mouse_5.status = STARTED
                wth_mouse_5.mouseClock.reset()
                prevButtonState = wth_mouse_5.getPressed()  # if button is down already this ISN'T a new click
            if wth_mouse_5.status == STARTED:  # only update if started and not finished!
                buttons = wth_mouse_5.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(wth_rating_end_2)
                            clickableList = wth_rating_end_2
                        except:
                            clickableList = [wth_rating_end_2]
                        for obj in clickableList:
                            if obj.contains(wth_mouse_5):
                                gotValidClick = True
                                wth_mouse_5.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            # Run 'Each Frame' code from wth_code_8
            wth_valence_rating_2.marker.size = (0.002,0.05)
            wth_self_rating_2.marker.size = (0.002,0.05)
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wth_rating_pracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "wth_rating_prac" ---
        for thisComponent in wth_rating_pracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        wth_repeat_prac.addData('wth_valence_rating_2.response', wth_valence_rating_2.getRating())
        wth_repeat_prac.addData('wth_self_rating_2.response', wth_self_rating_2.getRating())
        # store data for wth_repeat_prac (TrialHandler)
        # the Routine "wth_rating_prac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "wth_end_inst" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        wth_key_resp_4.keys = []
        wth_key_resp_4.rt = []
        _wth_key_resp_4_allKeys = []
        # Run 'Begin Routine' code from wth_code_11
        win.mouseVisible = False
        win.fullscr=False
        # keep track of which components have finished
        wth_end_instComponents = [wth_image_2, wth_text_4, wth_key_resp_4]
        for thisComponent in wth_end_instComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "wth_end_inst" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *wth_image_2* updates
            if wth_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_image_2.frameNStart = frameN  # exact frame index
                wth_image_2.tStart = t  # local t and not account for scr refresh
                wth_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_image_2, 'tStartRefresh')  # time at next scr refresh
                wth_image_2.setAutoDraw(True)
            
            # *wth_text_4* updates
            if wth_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_text_4.frameNStart = frameN  # exact frame index
                wth_text_4.tStart = t  # local t and not account for scr refresh
                wth_text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_text_4, 'tStartRefresh')  # time at next scr refresh
                wth_text_4.setAutoDraw(True)
            
            # *wth_key_resp_4* updates
            waitOnFlip = False
            if wth_key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_key_resp_4.frameNStart = frameN  # exact frame index
                wth_key_resp_4.tStart = t  # local t and not account for scr refresh
                wth_key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_key_resp_4, 'tStartRefresh')  # time at next scr refresh
                wth_key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(wth_key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(wth_key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if wth_key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = wth_key_resp_4.getKeys(keyList=['y','n'], waitRelease=False)
                _wth_key_resp_4_allKeys.extend(theseKeys)
                if len(_wth_key_resp_4_allKeys):
                    wth_key_resp_4.keys = _wth_key_resp_4_allKeys[-1].name  # just the last key pressed
                    wth_key_resp_4.rt = _wth_key_resp_4_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wth_end_instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "wth_end_inst" ---
        for thisComponent in wth_end_instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from wth_code_11
        if wth_key_resp_4.keys == 'y':
            wth_repeat_prac.finished = True
        # the Routine "wth_end_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed wth_repeat_prac_n repeats of 'wth_repeat_prac'
    
    
    # --- Prepare to start Routine "wth_start" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    wth_key_resp_5.keys = []
    wth_key_resp_5.rt = []
    _wth_key_resp_5_allKeys = []
    # keep track of which components have finished
    wth_startComponents = [wth_background_inst_2, wth_text_2, wth_key_resp_5]
    for thisComponent in wth_startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "wth_start" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wth_background_inst_2* updates
        if wth_background_inst_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wth_background_inst_2.frameNStart = frameN  # exact frame index
            wth_background_inst_2.tStart = t  # local t and not account for scr refresh
            wth_background_inst_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wth_background_inst_2, 'tStartRefresh')  # time at next scr refresh
            wth_background_inst_2.setAutoDraw(True)
        
        # *wth_text_2* updates
        if wth_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wth_text_2.frameNStart = frameN  # exact frame index
            wth_text_2.tStart = t  # local t and not account for scr refresh
            wth_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wth_text_2, 'tStartRefresh')  # time at next scr refresh
            wth_text_2.setAutoDraw(True)
        
        # *wth_key_resp_5* updates
        waitOnFlip = False
        if wth_key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wth_key_resp_5.frameNStart = frameN  # exact frame index
            wth_key_resp_5.tStart = t  # local t and not account for scr refresh
            wth_key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wth_key_resp_5, 'tStartRefresh')  # time at next scr refresh
            wth_key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(wth_key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(wth_key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if wth_key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = wth_key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _wth_key_resp_5_allKeys.extend(theseKeys)
            if len(_wth_key_resp_5_allKeys):
                wth_key_resp_5.keys = _wth_key_resp_5_allKeys[-1].name  # just the last key pressed
                wth_key_resp_5.rt = _wth_key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wth_startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "wth_start" ---
    for thisComponent in wth_startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "wth_start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "wth_begin_main" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    wth_begin_mainComponents = [wth_begin_background, wth_begin_text]
    for thisComponent in wth_begin_mainComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "wth_begin_main" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wth_begin_background* updates
        if wth_begin_background.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            wth_begin_background.frameNStart = frameN  # exact frame index
            wth_begin_background.tStart = t  # local t and not account for scr refresh
            wth_begin_background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wth_begin_background, 'tStartRefresh')  # time at next scr refresh
            wth_begin_background.setAutoDraw(True)
        if wth_begin_background.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wth_begin_background.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                wth_begin_background.tStop = t  # not accounting for scr refresh
                wth_begin_background.frameNStop = frameN  # exact frame index
                wth_begin_background.setAutoDraw(False)
        
        # *wth_begin_text* updates
        if wth_begin_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            wth_begin_text.frameNStart = frameN  # exact frame index
            wth_begin_text.tStart = t  # local t and not account for scr refresh
            wth_begin_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wth_begin_text, 'tStartRefresh')  # time at next scr refresh
            wth_begin_text.setAutoDraw(True)
        if wth_begin_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wth_begin_text.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                wth_begin_text.tStop = t  # not accounting for scr refresh
                wth_begin_text.frameNStop = frameN  # exact frame index
                wth_begin_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wth_begin_mainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "wth_begin_main" ---
    for thisComponent in wth_begin_mainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # set up handler to look after randomisation of conditions etc
    wth_trials = data.TrialHandler(nReps=wth_trials_n, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='wth_trials')
    thisExp.addLoop(wth_trials)  # add the loop to the experiment
    thisWth_trial = wth_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisWth_trial.rgb)
    if thisWth_trial != None:
        for paramName in thisWth_trial:
            exec('{} = thisWth_trial[paramName]'.format(paramName))
    
    for thisWth_trial in wth_trials:
        currentLoop = wth_trials
        # abbreviate parameter names if possible (e.g. rgb = thisWth_trial.rgb)
        if thisWth_trial != None:
            for paramName in thisWth_trial:
                exec('{} = thisWth_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "wth_think" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        wth_thinkComponents = [wth_background, wth_think_instr, wth_think_cross]
        for thisComponent in wth_thinkComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "wth_think" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *wth_background* updates
            if wth_background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_background.frameNStart = frameN  # exact frame index
                wth_background.tStart = t  # local t and not account for scr refresh
                wth_background.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_background, 'tStartRefresh')  # time at next scr refresh
                wth_background.setAutoDraw(True)
            if wth_background.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wth_background.tStartRefresh + stimulus_interval+3-frameTolerance:
                    # keep track of stop time/frame for later
                    wth_background.tStop = t  # not accounting for scr refresh
                    wth_background.frameNStop = frameN  # exact frame index
                    wth_background.setAutoDraw(False)
            
            # *wth_think_instr* updates
            if wth_think_instr.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                wth_think_instr.frameNStart = frameN  # exact frame index
                wth_think_instr.tStart = t  # local t and not account for scr refresh
                wth_think_instr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_think_instr, 'tStartRefresh')  # time at next scr refresh
                wth_think_instr.setAutoDraw(True)
            if wth_think_instr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wth_think_instr.tStartRefresh + stimulus_interval-frameTolerance:
                    # keep track of stop time/frame for later
                    wth_think_instr.tStop = t  # not accounting for scr refresh
                    wth_think_instr.frameNStop = frameN  # exact frame index
                    wth_think_instr.setAutoDraw(False)
            
            # *wth_think_cross* updates
            if wth_think_cross.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                wth_think_cross.frameNStart = frameN  # exact frame index
                wth_think_cross.tStart = t  # local t and not account for scr refresh
                wth_think_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_think_cross, 'tStartRefresh')  # time at next scr refresh
                wth_think_cross.setAutoDraw(True)
            if wth_think_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wth_think_cross.tStartRefresh + stimulus_interval-frameTolerance:
                    # keep track of stop time/frame for later
                    wth_think_cross.tStop = t  # not accounting for scr refresh
                    wth_think_cross.frameNStop = frameN  # exact frame index
                    wth_think_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wth_thinkComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "wth_think" ---
        for thisComponent in wth_thinkComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from wth_code
        thisExp.addData('stimulus_interval', stimulus_interval)
        
        # the Routine "wth_think" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "wth_word" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        wth_word_instr.setFont('Malgun Gothic')
        # Run 'Begin Routine' code from wth_code_4
        win.mouseVisible = True
        # keep track of which components have finished
        wth_wordComponents = [wth_background_2, wth_word_instr]
        for thisComponent in wth_wordComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "wth_word" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *wth_background_2* updates
            if wth_background_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_background_2.frameNStart = frameN  # exact frame index
                wth_background_2.tStart = t  # local t and not account for scr refresh
                wth_background_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_background_2, 'tStartRefresh')  # time at next scr refresh
                wth_background_2.setAutoDraw(True)
            
            # *wth_word_instr* updates
            if wth_word_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_word_instr.frameNStart = frameN  # exact frame index
                wth_word_instr.tStart = t  # local t and not account for scr refresh
                wth_word_instr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_word_instr, 'tStartRefresh')  # time at next scr refresh
                wth_word_instr.setAutoDraw(True)
            # Run 'Each Frame' code from wth_code_4
            while t > 1:
                start_time = core.getTime()
                root = Tk()
                root.attributes('-topmost',True)
                
                def retrieve_input():
                    global inputValue, continueRoutine, end_rt, t
                    inputValue=Tx.get("1.0","end-1c")
                    end_rt = core.getTime() - start_time
                    root.destroy()
                    continueRoutine = False
                    record_time = True
                    return inputValue, end_rt
            
                root.overrideredirect(True)
                 #Root Geometry
                root_Width = 400
                root_Length = 300
            
                # Coordinates of top left pixel of application for centred
                x_left = int(root.winfo_screenwidth()/2-root_Width/2)
                y_top = int(root.winfo_screenheight()/2-root_Length/2)
                root_Pos = "+" + str(x_left) + "+" + str(y_top)
            
                # Window size and position
                root.geometry(str(root_Width) + "x" + str(root_Length) + root_Pos)
                #root.geometry('400x300+400+200')
            
                Tx = Text(root, font = ("MalgunGothic 30 bold"), height = 5)
                Tx.pack(side = TOP)
            
                button = Button(root, text='입력완료', command=lambda: retrieve_input(), height = 3, width= 20)
                button.pack(expand=1, side = BOTTOM)
                root.update()
                root.mainloop()
                print(inputValue)
                break
            wth_trials.addData('wth_resp', inputValue) ########
            wth_trials.addData('wth_rt', end_rt) ########
            #if gotValidClick == True:
            #    wth_word_type_end = wth_wordClock.getTime() ###########
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wth_wordComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "wth_word" ---
        for thisComponent in wth_wordComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "wth_word" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "wth_rating" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        wth_word_typed.setText(inputValue)
        wth_valence_rating.reset()
        wth_self_rating.reset()
        wth_rating_end.reset()
        # setup some python lists for storing info about the wth_mouse
        wth_mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        wth_ratingComponents = [wth_background_3, wth_word_typed, wth_valence_rating, wth_valence_txt, wth_self_txt, wth_self_rating, wth_rating_end, wth_mouse]
        for thisComponent in wth_ratingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "wth_rating" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *wth_background_3* updates
            if wth_background_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_background_3.frameNStart = frameN  # exact frame index
                wth_background_3.tStart = t  # local t and not account for scr refresh
                wth_background_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_background_3, 'tStartRefresh')  # time at next scr refresh
                wth_background_3.setAutoDraw(True)
            
            # *wth_word_typed* updates
            if wth_word_typed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_word_typed.frameNStart = frameN  # exact frame index
                wth_word_typed.tStart = t  # local t and not account for scr refresh
                wth_word_typed.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_word_typed, 'tStartRefresh')  # time at next scr refresh
                wth_word_typed.setAutoDraw(True)
            
            # *wth_valence_rating* updates
            if wth_valence_rating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_valence_rating.frameNStart = frameN  # exact frame index
                wth_valence_rating.tStart = t  # local t and not account for scr refresh
                wth_valence_rating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_valence_rating, 'tStartRefresh')  # time at next scr refresh
                wth_valence_rating.setAutoDraw(True)
            
            # *wth_valence_txt* updates
            if wth_valence_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_valence_txt.frameNStart = frameN  # exact frame index
                wth_valence_txt.tStart = t  # local t and not account for scr refresh
                wth_valence_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_valence_txt, 'tStartRefresh')  # time at next scr refresh
                wth_valence_txt.setAutoDraw(True)
            
            # *wth_self_txt* updates
            if wth_self_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_self_txt.frameNStart = frameN  # exact frame index
                wth_self_txt.tStart = t  # local t and not account for scr refresh
                wth_self_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_self_txt, 'tStartRefresh')  # time at next scr refresh
                wth_self_txt.setAutoDraw(True)
            
            # *wth_self_rating* updates
            if wth_self_rating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wth_self_rating.frameNStart = frameN  # exact frame index
                wth_self_rating.tStart = t  # local t and not account for scr refresh
                wth_self_rating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_self_rating, 'tStartRefresh')  # time at next scr refresh
                wth_self_rating.setAutoDraw(True)
            
            # *wth_rating_end* updates
            if wth_rating_end.status == NOT_STARTED and wth_self_rating.rating and wth_valence_rating.rating:
                # keep track of start time/frame for later
                wth_rating_end.frameNStart = frameN  # exact frame index
                wth_rating_end.tStart = t  # local t and not account for scr refresh
                wth_rating_end.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_rating_end, 'tStartRefresh')  # time at next scr refresh
                wth_rating_end.setAutoDraw(True)
            # *wth_mouse* updates
            if wth_mouse.status == NOT_STARTED and wth_self_rating.rating and wth_valence_rating.rating:
                # keep track of start time/frame for later
                wth_mouse.frameNStart = frameN  # exact frame index
                wth_mouse.tStart = t  # local t and not account for scr refresh
                wth_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_mouse, 'tStartRefresh')  # time at next scr refresh
                wth_mouse.status = STARTED
                wth_mouse.mouseClock.reset()
                prevButtonState = wth_mouse.getPressed()  # if button is down already this ISN'T a new click
            if wth_mouse.status == STARTED:  # only update if started and not finished!
                buttons = wth_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(wth_rating_end)
                            clickableList = wth_rating_end
                        except:
                            clickableList = [wth_rating_end]
                        for obj in clickableList:
                            if obj.contains(wth_mouse):
                                gotValidClick = True
                                wth_mouse.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            # Run 'Each Frame' code from wth_code_3
            wth_valence_rating.marker.size = (0.002,0.05)
            wth_self_rating.marker.size = (0.002,0.05)
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wth_ratingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "wth_rating" ---
        for thisComponent in wth_ratingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        wth_trials.addData('wth_valence_rating.response', wth_valence_rating.getRating())
        wth_trials.addData('wth_self_rating.response', wth_self_rating.getRating())
        # store data for wth_trials (TrialHandler)
        # Run 'End Routine' code from wth_code_3
        win.mouseVisible = False
        # the Routine "wth_rating" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed wth_trials_n repeats of 'wth_trials'
    
    
    # --- Prepare to start Routine "exp_end" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    exp_end_key.keys = []
    exp_end_key.rt = []
    _exp_end_key_allKeys = []
    # keep track of which components have finished
    exp_endComponents = [wth_end_image, exp_end_text, exp_end_key]
    for thisComponent in exp_endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "exp_end" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wth_end_image* updates
        if wth_end_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            wth_end_image.frameNStart = frameN  # exact frame index
            wth_end_image.tStart = t  # local t and not account for scr refresh
            wth_end_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wth_end_image, 'tStartRefresh')  # time at next scr refresh
            wth_end_image.setAutoDraw(True)
        
        # *exp_end_text* updates
        if exp_end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exp_end_text.frameNStart = frameN  # exact frame index
            exp_end_text.tStart = t  # local t and not account for scr refresh
            exp_end_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exp_end_text, 'tStartRefresh')  # time at next scr refresh
            exp_end_text.setAutoDraw(True)
        
        # *exp_end_key* updates
        waitOnFlip = False
        if exp_end_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exp_end_key.frameNStart = frameN  # exact frame index
            exp_end_key.tStart = t  # local t and not account for scr refresh
            exp_end_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exp_end_key, 'tStartRefresh')  # time at next scr refresh
            exp_end_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(exp_end_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(exp_end_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if exp_end_key.status == STARTED and not waitOnFlip:
            theseKeys = exp_end_key.getKeys(keyList=['space'], waitRelease=False)
            _exp_end_key_allKeys.extend(theseKeys)
            if len(_exp_end_key_allKeys):
                exp_end_key.keys = _exp_end_key_allKeys[-1].name  # just the last key pressed
                exp_end_key.rt = _exp_end_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exp_endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "exp_end" ---
    for thisComponent in exp_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "exp_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed skip_weather repeats of 'weather'


# set up handler to look after randomisation of conditions etc
total_experiment = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='total_experiment')
thisExp.addLoop(total_experiment)  # add the loop to the experiment
thisTotal_experiment = total_experiment.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTotal_experiment.rgb)
if thisTotal_experiment != None:
    for paramName in thisTotal_experiment:
        exec('{} = thisTotal_experiment[paramName]'.format(paramName))

for thisTotal_experiment in total_experiment:
    currentLoop = total_experiment
    # abbreviate parameter names if possible (e.g. rgb = thisTotal_experiment.rgb)
    if thisTotal_experiment != None:
        for paramName in thisTotal_experiment:
            exec('{} = thisTotal_experiment[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "total_loop" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exp_code
    exp_loop = exp_loop + 1
    boat_loop = 0
    para_loop = 0
    fish_loop = 0
    
    if exp_loop == 2: 
        boat_loop = exp_order1[0]
        para_loop = exp_order1[1]
        fish_loop = exp_order1[2]
        exp_text = '스페이스바를 누르면 두번째 실험으로 넘어갑니다'
    elif exp_loop == 3:
        boat_loop = exp_order2[0]
        para_loop = exp_order2[1]
        fish_loop = exp_order2[2]
        exp_text = '스페이스바를 누르면 세번째 실험으로 넘어갑니다'
    elif exp_loop == 4:
        boat_loop = exp_order3[0]
        para_loop = exp_order3[1]
        fish_loop = exp_order3[2]
        exp_text = '스페이스바를 누르면 마지막 실험으로 넘어갑니다'
    elif exp_loop == 5:
        total_experiment.finished = True
    
    if skip_boat == 1:
        boat_loop = 0
    if skip_para == 1:
        para_loop = 0
    if skip_fish == 1:
        fish_loop = 0
    
    win.fullscr = True
    
    # keep track of which components have finished
    total_loopComponents = []
    for thisComponent in total_loopComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "total_loop" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in total_loopComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "total_loop" ---
    for thisComponent in total_loopComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "total_loop" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    boat = data.TrialHandler(nReps=boat_loop, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='boat')
    thisExp.addLoop(boat)  # add the loop to the experiment
    thisBoat = boat.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBoat.rgb)
    if thisBoat != None:
        for paramName in thisBoat:
            exec('{} = thisBoat[paramName]'.format(paramName))
    
    for thisBoat in boat:
        currentLoop = boat
        # abbreviate parameter names if possible (e.g. rgb = thisBoat.rgb)
        if thisBoat != None:
            for paramName in thisBoat:
                exec('{} = thisBoat[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fl_starter_code" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from fl_random_cb
        win.fullscr = True
        
        if test_mode == 1:
            win.mouseVisible = True
        else:
            win.mouseVisible = False
        fl_starter.keys = []
        fl_starter.rt = []
        _fl_starter_allKeys = []
        # setup some python lists for storing info about the fl_next_click
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        fl_starter_codeComponents = [fl_starter_back, fl_starter_text, fl_starter, fl_next_click]
        for thisComponent in fl_starter_codeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fl_starter_code" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fl_starter_back* updates
            if fl_starter_back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fl_starter_back.frameNStart = frameN  # exact frame index
                fl_starter_back.tStart = t  # local t and not account for scr refresh
                fl_starter_back.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fl_starter_back, 'tStartRefresh')  # time at next scr refresh
                fl_starter_back.setAutoDraw(True)
            
            # *fl_starter_text* updates
            if fl_starter_text.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                fl_starter_text.frameNStart = frameN  # exact frame index
                fl_starter_text.tStart = t  # local t and not account for scr refresh
                fl_starter_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fl_starter_text, 'tStartRefresh')  # time at next scr refresh
                fl_starter_text.setAutoDraw(True)
            
            # *fl_starter* updates
            waitOnFlip = False
            if fl_starter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fl_starter.frameNStart = frameN  # exact frame index
                fl_starter.tStart = t  # local t and not account for scr refresh
                fl_starter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fl_starter, 'tStartRefresh')  # time at next scr refresh
                fl_starter.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(fl_starter.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(fl_starter.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if fl_starter.status == STARTED and not waitOnFlip:
                theseKeys = fl_starter.getKeys(keyList=['space'], waitRelease=False)
                _fl_starter_allKeys.extend(theseKeys)
                if len(_fl_starter_allKeys):
                    fl_starter.keys = _fl_starter_allKeys[-1].name  # just the last key pressed
                    fl_starter.rt = _fl_starter_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # *fl_next_click* updates
            if fl_next_click.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fl_next_click.frameNStart = frameN  # exact frame index
                fl_next_click.tStart = t  # local t and not account for scr refresh
                fl_next_click.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fl_next_click, 'tStartRefresh')  # time at next scr refresh
                fl_next_click.status = STARTED
                fl_next_click.mouseClock.reset()
                prevButtonState = fl_next_click.getPressed()  # if button is down already this ISN'T a new click
            if fl_next_click.status == STARTED:  # only update if started and not finished!
                buttons = fl_next_click.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        continueRoutine = False  # abort routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fl_starter_codeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fl_starter_code" ---
        for thisComponent in fl_starter_codeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for boat (TrialHandler)
        # the Routine "fl_starter_code" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fl_inst" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from fl_inst_cb
        if counter_resp == jkl_resp:
            inst='ins/inst_jkl.png'
        elif counter_resp == lkj_resp:
            inst='ins/inst_lkj.png'
        
        
        nowexp = 1;
        #fl 1 st 2 
        fl_inst_img.setImage('ins/fl_inst_click.PNG')
        fl_inst_resp.keys = []
        fl_inst_resp.rt = []
        _fl_inst_resp_allKeys = []
        fl_inst_sound.setSound('ins/fl_inst_click.wav', hamming=True)
        fl_inst_sound.setVolume(1.0, log=False)
        # setup some python lists for storing info about the fl_next_again
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        fl_instComponents = [fl_inst_img, fl_inst_resp, fl_inst_text_2, fl_inst_sound, fl_next_again]
        for thisComponent in fl_instComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fl_inst" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fl_inst_img* updates
            if fl_inst_img.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                fl_inst_img.frameNStart = frameN  # exact frame index
                fl_inst_img.tStart = t  # local t and not account for scr refresh
                fl_inst_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fl_inst_img, 'tStartRefresh')  # time at next scr refresh
                fl_inst_img.setAutoDraw(True)
            
            # *fl_inst_resp* updates
            waitOnFlip = False
            if fl_inst_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                fl_inst_resp.frameNStart = frameN  # exact frame index
                fl_inst_resp.tStart = t  # local t and not account for scr refresh
                fl_inst_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fl_inst_resp, 'tStartRefresh')  # time at next scr refresh
                fl_inst_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(fl_inst_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(fl_inst_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if fl_inst_resp.status == STARTED and not waitOnFlip:
                theseKeys = fl_inst_resp.getKeys(keyList=['space'], waitRelease=False)
                _fl_inst_resp_allKeys.extend(theseKeys)
                if len(_fl_inst_resp_allKeys):
                    fl_inst_resp.keys = _fl_inst_resp_allKeys[-1].name  # just the last key pressed
                    fl_inst_resp.rt = _fl_inst_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *fl_inst_text_2* updates
            if fl_inst_text_2.status == NOT_STARTED and fl_inst_img.status==FINISHED:
                # keep track of start time/frame for later
                fl_inst_text_2.frameNStart = frameN  # exact frame index
                fl_inst_text_2.tStart = t  # local t and not account for scr refresh
                fl_inst_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fl_inst_text_2, 'tStartRefresh')  # time at next scr refresh
                fl_inst_text_2.setAutoDraw(True)
            # start/stop fl_inst_sound
            if fl_inst_sound.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                fl_inst_sound.frameNStart = frameN  # exact frame index
                fl_inst_sound.tStart = t  # local t and not account for scr refresh
                fl_inst_sound.tStartRefresh = tThisFlipGlobal  # on global time
                fl_inst_sound.play(when=win)  # sync with win flip
            # *fl_next_again* updates
            if fl_next_again.status == NOT_STARTED and t >= 1-frameTolerance:
                # keep track of start time/frame for later
                fl_next_again.frameNStart = frameN  # exact frame index
                fl_next_again.tStart = t  # local t and not account for scr refresh
                fl_next_again.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fl_next_again, 'tStartRefresh')  # time at next scr refresh
                fl_next_again.status = STARTED
                fl_next_again.mouseClock.reset()
                prevButtonState = fl_next_again.getPressed()  # if button is down already this ISN'T a new click
            if fl_next_again.status == STARTED:  # only update if started and not finished!
                buttons = fl_next_again.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        continueRoutine = False  # abort routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fl_instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fl_inst" ---
        for thisComponent in fl_instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fl_inst_sound.stop()  # ensure sound has stopped at end of routine
        # store data for boat (TrialHandler)
        # the Routine "fl_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fl_fix_2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        fl_fix_2Components = [back_2, fixation_2, fl_next]
        for thisComponent in fl_fix_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fl_fix_2" ---
        while continueRoutine and routineTimer.getTime() < 6.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *back_2* updates
            if back_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                back_2.frameNStart = frameN  # exact frame index
                back_2.tStart = t  # local t and not account for scr refresh
                back_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(back_2, 'tStartRefresh')  # time at next scr refresh
                back_2.setAutoDraw(True)
            if back_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > back_2.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    back_2.tStop = t  # not accounting for scr refresh
                    back_2.frameNStop = frameN  # exact frame index
                    back_2.setAutoDraw(False)
            
            # *fixation_2* updates
            if fixation_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                fixation_2.frameNStart = frameN  # exact frame index
                fixation_2.tStart = t  # local t and not account for scr refresh
                fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
                fixation_2.setAutoDraw(True)
            if fixation_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_2.tStop = t  # not accounting for scr refresh
                    fixation_2.frameNStop = frameN  # exact frame index
                    fixation_2.setAutoDraw(False)
            
            # *fl_next* updates
            if fl_next.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                fl_next.frameNStart = frameN  # exact frame index
                fl_next.tStart = t  # local t and not account for scr refresh
                fl_next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fl_next, 'tStartRefresh')  # time at next scr refresh
                fl_next.setAutoDraw(True)
            if fl_next.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fl_next.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    fl_next.tStop = t  # not accounting for scr refresh
                    fl_next.frameNStop = frameN  # exact frame index
                    fl_next.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fl_fix_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fl_fix_2" ---
        for thisComponent in fl_fix_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-6.000000)
        
        # set up handler to look after randomisation of conditions etc
        flanker_prac_loop = data.TrialHandler(nReps=fprac, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('loop/flanker.xlsx'),
            seed=None, name='flanker_prac_loop')
        thisExp.addLoop(flanker_prac_loop)  # add the loop to the experiment
        thisFlanker_prac_loop = flanker_prac_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisFlanker_prac_loop.rgb)
        if thisFlanker_prac_loop != None:
            for paramName in thisFlanker_prac_loop:
                exec('{} = thisFlanker_prac_loop[paramName]'.format(paramName))
        
        for thisFlanker_prac_loop in flanker_prac_loop:
            currentLoop = flanker_prac_loop
            # abbreviate parameter names if possible (e.g. rgb = thisFlanker_prac_loop.rgb)
            if thisFlanker_prac_loop != None:
                for paramName in thisFlanker_prac_loop:
                    exec('{} = thisFlanker_prac_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "fl_tag_prac" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from fl_prac_tag
            dist_cond = flanker_prac_loop.thisTrial["distractor"]
            targ_cond = flanker_prac_loop.thisTrial["target"]
            set_cond  = flanker_prac_loop.thisTrial["set"]
            thisn=flanker_prac_loop.thisN
            
            
            
            ##########TEST MODE###########
            if test_mode == 1 and thisn == 3:
                flanker_prac_loop.finished=True
            
            
            
            
            # keep track of which components have finished
            fl_tag_pracComponents = []
            for thisComponent in fl_tag_pracComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fl_tag_prac" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fl_tag_pracComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fl_tag_prac" ---
            for thisComponent in fl_tag_pracComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from fl_prac_tag
            flanker_prac_loop.addData('main_prac', 'prac')
            
            # the Routine "fl_tag_prac" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Flanker" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from fl_anime
            t = 0
            rotationRate = 0.1  # revs per sec
            flashPeriod = 0.1  # seconds for one B-W cycle (ie 1/Hz)
            frn = 0;
            print(thisn, 'thisn')
            print(dist_cond, 'dis')
            print(targ_cond, 'tar')
            print(set_cond, 'set')
            
            ranint = randint(1,10);
            coln = randg[ranint];
            colnt = coln;
            #coln = randint(1,2);
            #randg = [1,2];
            #randgg = shuffle(randg);
            #rtn = rtn + 1;
            #rtnn = rtn%2 + 1;
            #coln = colnt[rtnn];
            #coln = randgg(rtnn);
            #coln = rtnn;
            print(coln, 'color')
            print(colnt, 'color')
            
            if coln == 1:
                if dist_cond == "negative" and set_cond == 1:
                    d = set1_angry_g
                    b = set1_angry_blink_g_1
            
                elif dist_cond == "negative" and set_cond == 2:
                    d = set2_angry_g
                    b = set2_angry_blink_g_1
             
            
                elif dist_cond == "neutral" and set_cond == 1:
                    d = set1_neutral_g
                    b = set1_neutral_blink_g_1
            
                elif dist_cond == "neutral" and set_cond == 2:
                    d = set2_neutral_g
                    b = set2_neutral_blink_g_1
            
                elif dist_cond == "positive" and set_cond == 1:
                    d = set1_happy_g
                    b = set1_happy_blink_g_1
             
                elif dist_cond == "positive" and set_cond == 2:
                    d = set2_happy_g
                    b = set2_happy_blink_g_1
                #dist_img=b
                
            
            elif coln == 2:
                if dist_cond == "negative" and set_cond == 1:
                    d = set1_angry_y
                    b = set1_angry_blink_y_1
            
            
                elif dist_cond == "negative" and set_cond == 2:
                    d = set2_angry_y
                    b = set2_angry_blink_y_1
             
            
                elif dist_cond == "neutral" and set_cond == 1:
                    d = set1_neutral_y
                    b = set1_neutral_blink_y_1
            
            
                elif dist_cond == "neutral" and set_cond == 2:
                    d = set2_neutral_y
                    b = set2_neutral_blink_y_1
            
                elif dist_cond == "positive" and set_cond == 1:
                    d = set1_happy_y
                    b = set1_happy_blink_y_1
            
                elif dist_cond == "positive" and set_cond == 2:
                    d = set2_happy_y 
                    b = set2_happy_blink_y_1
                #dist_img=b
                
            if colnt == 1:
                if targ_cond == "negative" and set_cond== 1:
                    a = set1_angry_g
            
                elif targ_cond == "negative" and set_cond== 2:
                    a = set2_angry_g
            
                elif targ_cond == "neutral" and set_cond== 1:
                    a = set1_neutral_g
            
                elif targ_cond == "neutral" and set_cond== 2:
                    a = set2_neutral_g
            
                elif targ_cond == "positive" and set_cond == 1:
                    a = set1_happy_g
            
                elif targ_cond == "positive" and set_cond == 2:
                    a = set2_happy_g
                
                #targ_img=a
                
            elif colnt == 2:
                if targ_cond == "negative" and set_cond== 1:
                    a = set1_angry_y
            
                elif targ_cond == "negative" and set_cond== 2:
                    a = set2_angry_y
            
                elif targ_cond == "neutral" and set_cond== 1:
                    a = set1_neutral_y
            
                elif targ_cond == "neutral" and set_cond== 2:
                    a = set2_neutral_y
            
                elif targ_cond == "positive" and set_cond == 1:
                    a = set1_happy_y
            
                elif targ_cond == "positive" and set_cond == 2:
                    a = set2_happy_y
            
            
                
                #targ_img=a
            
            dist_img=b
            targ_img=a
            # The contents of this file are in the public domain.
            thisExp.addData('fl_cold', coln)
            thisExp.addData('fl_colt', colnt)
            thisExp.addData('fl_set', set_cond)
            thisExp.addData('fl_dcond', dist_cond)
            thisExp.addData('fl_tcond', targ_cond)
            # Run 'Begin Routine' code from fl_ans_cb
            #win.mouseVisible = False
            if counter_resp == jkl_resp:
                fl_ans = ans1
                print('answer1 is ',ans1)
                print('fl_ans is ', fl_ans)
                posx = 0.1;
                negx = -0.1;
            elif counter_resp == lkj_resp:
                fl_ans = ans2
                print('answer2 is ',ans2)
                print('fl_ans is ', fl_ans)
            
            print(fl_ans)
            
            
            # Run 'Begin Routine' code from fl_code_clik
            mouserec = fl_mouse.getPos()
            minRT = .2
            
            fl_res = ''
            fl_time = core.Clock()
            dist1.setImage(dist_img)
            dist2.setImage(dist_img)
            dist3.setImage(dist_img)
            dist4.setImage(dist_img)
            targ.setImage(targ_img)
            # setup some python lists for storing info about the fl_mouse
            fl_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            fl_mouse.mouseClock.reset()
            # keep track of which components have finished
            FlankerComponents = [fl_back_image, fl_fix, dist1, dist2, dist3, dist4, targ, j_button, k_button, l_button, fl_mouse]
            for thisComponent in FlankerComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Flanker" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from fl_anime
                nfrn = frameN/20;
                nlit = frameN%20;
                btemp = [9,10,11,12,13,14];
                
                btemp1 = [9,10,18,19];
                btemp2 = [11,12,16,17];
                btemp3 = [13,14,15];
                
                if nlit == 0:
                    blist = [btemp[i]+nfrn*20 for i in range(len(btemp))];
                    blist1 = [btemp1[i]+nfrn*20 for i in range(len(btemp1))];
                    blist2 = [btemp2[i]+nfrn*20 for i in range(len(btemp2))];
                    blist3 = [btemp3[i]+nfrn*20 for i in range(len(btemp3))];
                
                #print(blist, 'blist');
                
                if frameN in blist:  # more accurate to count frames
                    dist1.setImage(b)
                    dist2.setImage(b)
                    dist3.setImage(b)
                    dist4.setImage(b)
                    targ.setImage(a)
                
                else:
                    dist1.setImage(d)
                    dist2.setImage(d)
                    dist3.setImage(d)
                    dist4.setImage(d)
                    targ.setImage(a)
                
                
                #win.flip() 
                # Run 'Each Frame' code from fl_code_clik
                mouseloc = fl_mouse.getPos()
                if mouseloc[0]==mouserec[0] and mouseloc[1]==mouserec[1]:
                    pass
                
                elif j_button.contains(fl_mouse):
                    fl_res = 'j'
                    proper_rt = fl_time.getTime()-1
                    if t>minRT:
                        continueRoutine = False
                    else:
                        mouserec = fl_mouse.getPos()
                
                
                elif k_button.contains(fl_mouse):
                    fl_res = 'k'
                    proper_rt = fl_time.getTime()-1
                    if t>minRT:
                        continueRoutine = False
                    else:
                        mouserec = fl_mouse.getPos()
                
                
                elif l_button.contains(fl_mouse):
                    fl_res = 'l'
                    proper_rt = fl_time.getTime()-1
                    if t>minRT:
                        continueRoutine = False
                    else:
                        mouserec = fl_mouse.getPos()
                     
                
                # *fl_back_image* updates
                if fl_back_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fl_back_image.frameNStart = frameN  # exact frame index
                    fl_back_image.tStart = t  # local t and not account for scr refresh
                    fl_back_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fl_back_image, 'tStartRefresh')  # time at next scr refresh
                    fl_back_image.setAutoDraw(True)
                
                # *fl_fix* updates
                if fl_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fl_fix.frameNStart = frameN  # exact frame index
                    fl_fix.tStart = t  # local t and not account for scr refresh
                    fl_fix.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fl_fix, 'tStartRefresh')  # time at next scr refresh
                    fl_fix.setAutoDraw(True)
                if fl_fix.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fl_fix.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fl_fix.tStop = t  # not accounting for scr refresh
                        fl_fix.frameNStop = frameN  # exact frame index
                        fl_fix.setAutoDraw(False)
                
                # *dist1* updates
                if dist1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    dist1.frameNStart = frameN  # exact frame index
                    dist1.tStart = t  # local t and not account for scr refresh
                    dist1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist1, 'tStartRefresh')  # time at next scr refresh
                    dist1.setAutoDraw(True)
                
                # *dist2* updates
                if dist2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    dist2.frameNStart = frameN  # exact frame index
                    dist2.tStart = t  # local t and not account for scr refresh
                    dist2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist2, 'tStartRefresh')  # time at next scr refresh
                    dist2.setAutoDraw(True)
                
                # *dist3* updates
                if dist3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    dist3.frameNStart = frameN  # exact frame index
                    dist3.tStart = t  # local t and not account for scr refresh
                    dist3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist3, 'tStartRefresh')  # time at next scr refresh
                    dist3.setAutoDraw(True)
                
                # *dist4* updates
                if dist4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    dist4.frameNStart = frameN  # exact frame index
                    dist4.tStart = t  # local t and not account for scr refresh
                    dist4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist4, 'tStartRefresh')  # time at next scr refresh
                    dist4.setAutoDraw(True)
                
                # *targ* updates
                if targ.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    targ.frameNStart = frameN  # exact frame index
                    targ.tStart = t  # local t and not account for scr refresh
                    targ.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(targ, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'targ.started')
                    targ.setAutoDraw(True)
                
                # *j_button* updates
                if j_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    j_button.frameNStart = frameN  # exact frame index
                    j_button.tStart = t  # local t and not account for scr refresh
                    j_button.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(j_button, 'tStartRefresh')  # time at next scr refresh
                    j_button.setAutoDraw(True)
                
                # *k_button* updates
                if k_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    k_button.frameNStart = frameN  # exact frame index
                    k_button.tStart = t  # local t and not account for scr refresh
                    k_button.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(k_button, 'tStartRefresh')  # time at next scr refresh
                    k_button.setAutoDraw(True)
                
                # *l_button* updates
                if l_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    l_button.frameNStart = frameN  # exact frame index
                    l_button.tStart = t  # local t and not account for scr refresh
                    l_button.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(l_button, 'tStartRefresh')  # time at next scr refresh
                    l_button.setAutoDraw(True)
                # *fl_mouse* updates
                if fl_mouse.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    fl_mouse.frameNStart = frameN  # exact frame index
                    fl_mouse.tStart = t  # local t and not account for scr refresh
                    fl_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fl_mouse, 'tStartRefresh')  # time at next scr refresh
                    fl_mouse.status = STARTED
                    prevButtonState = fl_mouse.getPressed()  # if button is down already this ISN'T a new click
                if fl_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = fl_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([j_button, k_button, l_button])
                                clickableList = [j_button, k_button, l_button]
                            except:
                                clickableList = [[j_button, k_button, l_button]]
                            for obj in clickableList:
                                if obj.contains(fl_mouse):
                                    gotValidClick = True
                                    fl_mouse.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # abort routine on response
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in FlankerComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Flanker" ---
            for thisComponent in FlankerComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from fl_anime
            print('frames: ',frameN)
            
            # Run 'End Routine' code from fl_code_clik
            
            #flanker_main_loop.addData('fl_res')
            #if mouse_fl.clicked_name == ['j_button']:
            #    fl_res = 'j'
            #elif mouse_fl.clicked_name == ['k_button']:
            #    fl_res= 'k'
            #elif mouse_fl.clicked_name == ['l_button']:
            #    fl_res = 'l'
            
            fl_mouse.time = fl_time.getTime()-1
            
            if fl_res == fl_ans:
                fl_corr = 1
            elif fl_res != fl_ans:
                fl_corr = 0
            
            thisExp.addData('fl_ans', fl_ans)
            thisExp.addData('fl_res', fl_res)
            thisExp.addData('fl_corr', fl_corr)
            thisExp.addData('fl_rt', fl_mouse.time)
            thisExp.addData('fl_rt_2', proper_rt)
            
            # store data for flanker_prac_loop (TrialHandler)
            # the Routine "Flanker" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "flankerfeedback" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from fl_feed_code
            
            message = ""
            feedur = 0
            
            fl_mouse.time = fl_mouse.time
            
            if fl_mouse.time == []:
                fl_mouse.time = -1
            
            if (fl_mouse.time == -1): 
                message = "더 빨리 응답하세요"
                feedur = 1
            elif (fl_mouse.time < 0.150): 
                message = "고양이를 보고 반응하세요"
                feedur = 3
            elif (fl_mouse.time > 1.5) and (fl_corr == 1): 
                message = "더 빨리 응답하세요"
                feedur = 1
            elif (fl_mouse.time > 1.5) and (fl_corr == 0): 
                message = "오답, 더 빨리 응답하세요"
                feedur = 1
            elif (fl_mouse.time < 1.5) and (fl_corr == 1): 
                message = ""
                feedur = 0
            elif (fl_mouse.time < 1.5) and (fl_corr == 0): 
                message = "오답"
                feedur = 1
            
            
            print('response', fl_res)
            print('accuracy', fl_corr)
            print('rt', fl_mouse.time)
            print('message',message)
            print('feedur',feedur)
            
            
            fl_feedback.setText(message)
            # keep track of which components have finished
            flankerfeedbackComponents = [fl_back_image2, fl_feedback, j_button2, k_button2, l_button2]
            for thisComponent in flankerfeedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "flankerfeedback" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fl_back_image2* updates
                if fl_back_image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fl_back_image2.frameNStart = frameN  # exact frame index
                    fl_back_image2.tStart = t  # local t and not account for scr refresh
                    fl_back_image2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fl_back_image2, 'tStartRefresh')  # time at next scr refresh
                    fl_back_image2.setAutoDraw(True)
                if fl_back_image2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fl_back_image2.tStartRefresh + feedur-frameTolerance:
                        # keep track of stop time/frame for later
                        fl_back_image2.tStop = t  # not accounting for scr refresh
                        fl_back_image2.frameNStop = frameN  # exact frame index
                        fl_back_image2.setAutoDraw(False)
                
                # *fl_feedback* updates
                if fl_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fl_feedback.frameNStart = frameN  # exact frame index
                    fl_feedback.tStart = t  # local t and not account for scr refresh
                    fl_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fl_feedback, 'tStartRefresh')  # time at next scr refresh
                    fl_feedback.setAutoDraw(True)
                if fl_feedback.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fl_feedback.tStartRefresh + feedur-frameTolerance:
                        # keep track of stop time/frame for later
                        fl_feedback.tStop = t  # not accounting for scr refresh
                        fl_feedback.frameNStop = frameN  # exact frame index
                        fl_feedback.setAutoDraw(False)
                
                # *j_button2* updates
                if j_button2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    j_button2.frameNStart = frameN  # exact frame index
                    j_button2.tStart = t  # local t and not account for scr refresh
                    j_button2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(j_button2, 'tStartRefresh')  # time at next scr refresh
                    j_button2.setAutoDraw(True)
                if j_button2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > j_button2.tStartRefresh + feedur-frameTolerance:
                        # keep track of stop time/frame for later
                        j_button2.tStop = t  # not accounting for scr refresh
                        j_button2.frameNStop = frameN  # exact frame index
                        j_button2.setAutoDraw(False)
                
                # *k_button2* updates
                if k_button2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    k_button2.frameNStart = frameN  # exact frame index
                    k_button2.tStart = t  # local t and not account for scr refresh
                    k_button2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(k_button2, 'tStartRefresh')  # time at next scr refresh
                    k_button2.setAutoDraw(True)
                if k_button2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > k_button2.tStartRefresh + feedur-frameTolerance:
                        # keep track of stop time/frame for later
                        k_button2.tStop = t  # not accounting for scr refresh
                        k_button2.frameNStop = frameN  # exact frame index
                        k_button2.setAutoDraw(False)
                
                # *l_button2* updates
                if l_button2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    l_button2.frameNStart = frameN  # exact frame index
                    l_button2.tStart = t  # local t and not account for scr refresh
                    l_button2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(l_button2, 'tStartRefresh')  # time at next scr refresh
                    l_button2.setAutoDraw(True)
                if l_button2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > l_button2.tStartRefresh + feedur-frameTolerance:
                        # keep track of stop time/frame for later
                        l_button2.tStop = t  # not accounting for scr refresh
                        l_button2.frameNStop = frameN  # exact frame index
                        l_button2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in flankerfeedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "flankerfeedback" ---
            for thisComponent in flankerfeedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "flankerfeedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed fprac repeats of 'flanker_prac_loop'
        
        
        # --- Prepare to start Routine "fl_say_main" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        fl_key_resp.keys = []
        fl_key_resp.rt = []
        _fl_key_resp_allKeys = []
        # setup some python lists for storing info about the fl_mouse_m
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        fl_say_mainComponents = [fl_mainback, fl_main_text, fl_key_resp, fl_mouse_m]
        for thisComponent in fl_say_mainComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fl_say_main" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fl_mainback* updates
            if fl_mainback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fl_mainback.frameNStart = frameN  # exact frame index
                fl_mainback.tStart = t  # local t and not account for scr refresh
                fl_mainback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fl_mainback, 'tStartRefresh')  # time at next scr refresh
                fl_mainback.setAutoDraw(True)
            
            # *fl_main_text* updates
            if fl_main_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fl_main_text.frameNStart = frameN  # exact frame index
                fl_main_text.tStart = t  # local t and not account for scr refresh
                fl_main_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fl_main_text, 'tStartRefresh')  # time at next scr refresh
                fl_main_text.setAutoDraw(True)
            
            # *fl_key_resp* updates
            waitOnFlip = False
            if fl_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fl_key_resp.frameNStart = frameN  # exact frame index
                fl_key_resp.tStart = t  # local t and not account for scr refresh
                fl_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fl_key_resp, 'tStartRefresh')  # time at next scr refresh
                fl_key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(fl_key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(fl_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if fl_key_resp.status == STARTED and not waitOnFlip:
                theseKeys = fl_key_resp.getKeys(keyList=['space'], waitRelease=False)
                _fl_key_resp_allKeys.extend(theseKeys)
                if len(_fl_key_resp_allKeys):
                    fl_key_resp.keys = _fl_key_resp_allKeys[-1].name  # just the last key pressed
                    fl_key_resp.rt = _fl_key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # *fl_mouse_m* updates
            if fl_mouse_m.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fl_mouse_m.frameNStart = frameN  # exact frame index
                fl_mouse_m.tStart = t  # local t and not account for scr refresh
                fl_mouse_m.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fl_mouse_m, 'tStartRefresh')  # time at next scr refresh
                fl_mouse_m.status = STARTED
                fl_mouse_m.mouseClock.reset()
                prevButtonState = fl_mouse_m.getPressed()  # if button is down already this ISN'T a new click
            if fl_mouse_m.status == STARTED:  # only update if started and not finished!
                buttons = fl_mouse_m.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        continueRoutine = False  # abort routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fl_say_mainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fl_say_main" ---
        for thisComponent in fl_say_mainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if fl_key_resp.keys in ['', [], None]:  # No response was made
            fl_key_resp.keys = None
        boat.addData('fl_key_resp.keys',fl_key_resp.keys)
        if fl_key_resp.keys != None:  # we had a response
            boat.addData('fl_key_resp.rt', fl_key_resp.rt)
        # store data for boat (TrialHandler)
        # the Routine "fl_say_main" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fl_fix_2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        fl_fix_2Components = [back_2, fixation_2, fl_next]
        for thisComponent in fl_fix_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fl_fix_2" ---
        while continueRoutine and routineTimer.getTime() < 6.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *back_2* updates
            if back_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                back_2.frameNStart = frameN  # exact frame index
                back_2.tStart = t  # local t and not account for scr refresh
                back_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(back_2, 'tStartRefresh')  # time at next scr refresh
                back_2.setAutoDraw(True)
            if back_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > back_2.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    back_2.tStop = t  # not accounting for scr refresh
                    back_2.frameNStop = frameN  # exact frame index
                    back_2.setAutoDraw(False)
            
            # *fixation_2* updates
            if fixation_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                fixation_2.frameNStart = frameN  # exact frame index
                fixation_2.tStart = t  # local t and not account for scr refresh
                fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
                fixation_2.setAutoDraw(True)
            if fixation_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_2.tStop = t  # not accounting for scr refresh
                    fixation_2.frameNStop = frameN  # exact frame index
                    fixation_2.setAutoDraw(False)
            
            # *fl_next* updates
            if fl_next.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                fl_next.frameNStart = frameN  # exact frame index
                fl_next.tStart = t  # local t and not account for scr refresh
                fl_next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fl_next, 'tStartRefresh')  # time at next scr refresh
                fl_next.setAutoDraw(True)
            if fl_next.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fl_next.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    fl_next.tStop = t  # not accounting for scr refresh
                    fl_next.frameNStop = frameN  # exact frame index
                    fl_next.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fl_fix_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fl_fix_2" ---
        for thisComponent in fl_fix_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-6.000000)
        
        # set up handler to look after randomisation of conditions etc
        flanker_main_loop = data.TrialHandler(nReps=fmain, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('loop/flanker.xlsx'),
            seed=None, name='flanker_main_loop')
        thisExp.addLoop(flanker_main_loop)  # add the loop to the experiment
        thisFlanker_main_loop = flanker_main_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisFlanker_main_loop.rgb)
        if thisFlanker_main_loop != None:
            for paramName in thisFlanker_main_loop:
                exec('{} = thisFlanker_main_loop[paramName]'.format(paramName))
        
        for thisFlanker_main_loop in flanker_main_loop:
            currentLoop = flanker_main_loop
            # abbreviate parameter names if possible (e.g. rgb = thisFlanker_main_loop.rgb)
            if thisFlanker_main_loop != None:
                for paramName in thisFlanker_main_loop:
                    exec('{} = thisFlanker_main_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "fl_tag_main" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from fl_main_tag
            dist_cond = flanker_main_loop.thisTrial["distractor"]
            targ_cond = flanker_main_loop.thisTrial["target"]
            set_cond  = flanker_main_loop.thisTrial["set"]
            thisn = flanker_main_loop.thisN
            
            
            
            ##########TEST MODE###########
            if test_mode == 1 and thisn == 3:
                flanker_main_loop.finished=True
            # keep track of which components have finished
            fl_tag_mainComponents = []
            for thisComponent in fl_tag_mainComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fl_tag_main" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fl_tag_mainComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fl_tag_main" ---
            for thisComponent in fl_tag_mainComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from fl_main_tag
            flanker_main_loop.addData('main_prac', 'main')
            
            # the Routine "fl_tag_main" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Flanker" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from fl_anime
            t = 0
            rotationRate = 0.1  # revs per sec
            flashPeriod = 0.1  # seconds for one B-W cycle (ie 1/Hz)
            frn = 0;
            print(thisn, 'thisn')
            print(dist_cond, 'dis')
            print(targ_cond, 'tar')
            print(set_cond, 'set')
            
            ranint = randint(1,10);
            coln = randg[ranint];
            colnt = coln;
            #coln = randint(1,2);
            #randg = [1,2];
            #randgg = shuffle(randg);
            #rtn = rtn + 1;
            #rtnn = rtn%2 + 1;
            #coln = colnt[rtnn];
            #coln = randgg(rtnn);
            #coln = rtnn;
            print(coln, 'color')
            print(colnt, 'color')
            
            if coln == 1:
                if dist_cond == "negative" and set_cond == 1:
                    d = set1_angry_g
                    b = set1_angry_blink_g_1
            
                elif dist_cond == "negative" and set_cond == 2:
                    d = set2_angry_g
                    b = set2_angry_blink_g_1
             
            
                elif dist_cond == "neutral" and set_cond == 1:
                    d = set1_neutral_g
                    b = set1_neutral_blink_g_1
            
                elif dist_cond == "neutral" and set_cond == 2:
                    d = set2_neutral_g
                    b = set2_neutral_blink_g_1
            
                elif dist_cond == "positive" and set_cond == 1:
                    d = set1_happy_g
                    b = set1_happy_blink_g_1
             
                elif dist_cond == "positive" and set_cond == 2:
                    d = set2_happy_g
                    b = set2_happy_blink_g_1
                #dist_img=b
                
            
            elif coln == 2:
                if dist_cond == "negative" and set_cond == 1:
                    d = set1_angry_y
                    b = set1_angry_blink_y_1
            
            
                elif dist_cond == "negative" and set_cond == 2:
                    d = set2_angry_y
                    b = set2_angry_blink_y_1
             
            
                elif dist_cond == "neutral" and set_cond == 1:
                    d = set1_neutral_y
                    b = set1_neutral_blink_y_1
            
            
                elif dist_cond == "neutral" and set_cond == 2:
                    d = set2_neutral_y
                    b = set2_neutral_blink_y_1
            
                elif dist_cond == "positive" and set_cond == 1:
                    d = set1_happy_y
                    b = set1_happy_blink_y_1
            
                elif dist_cond == "positive" and set_cond == 2:
                    d = set2_happy_y 
                    b = set2_happy_blink_y_1
                #dist_img=b
                
            if colnt == 1:
                if targ_cond == "negative" and set_cond== 1:
                    a = set1_angry_g
            
                elif targ_cond == "negative" and set_cond== 2:
                    a = set2_angry_g
            
                elif targ_cond == "neutral" and set_cond== 1:
                    a = set1_neutral_g
            
                elif targ_cond == "neutral" and set_cond== 2:
                    a = set2_neutral_g
            
                elif targ_cond == "positive" and set_cond == 1:
                    a = set1_happy_g
            
                elif targ_cond == "positive" and set_cond == 2:
                    a = set2_happy_g
                
                #targ_img=a
                
            elif colnt == 2:
                if targ_cond == "negative" and set_cond== 1:
                    a = set1_angry_y
            
                elif targ_cond == "negative" and set_cond== 2:
                    a = set2_angry_y
            
                elif targ_cond == "neutral" and set_cond== 1:
                    a = set1_neutral_y
            
                elif targ_cond == "neutral" and set_cond== 2:
                    a = set2_neutral_y
            
                elif targ_cond == "positive" and set_cond == 1:
                    a = set1_happy_y
            
                elif targ_cond == "positive" and set_cond == 2:
                    a = set2_happy_y
            
            
                
                #targ_img=a
            
            dist_img=b
            targ_img=a
            # The contents of this file are in the public domain.
            thisExp.addData('fl_cold', coln)
            thisExp.addData('fl_colt', colnt)
            thisExp.addData('fl_set', set_cond)
            thisExp.addData('fl_dcond', dist_cond)
            thisExp.addData('fl_tcond', targ_cond)
            # Run 'Begin Routine' code from fl_ans_cb
            #win.mouseVisible = False
            if counter_resp == jkl_resp:
                fl_ans = ans1
                print('answer1 is ',ans1)
                print('fl_ans is ', fl_ans)
                posx = 0.1;
                negx = -0.1;
            elif counter_resp == lkj_resp:
                fl_ans = ans2
                print('answer2 is ',ans2)
                print('fl_ans is ', fl_ans)
            
            print(fl_ans)
            
            
            # Run 'Begin Routine' code from fl_code_clik
            mouserec = fl_mouse.getPos()
            minRT = .2
            
            fl_res = ''
            fl_time = core.Clock()
            dist1.setImage(dist_img)
            dist2.setImage(dist_img)
            dist3.setImage(dist_img)
            dist4.setImage(dist_img)
            targ.setImage(targ_img)
            # setup some python lists for storing info about the fl_mouse
            fl_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            fl_mouse.mouseClock.reset()
            # keep track of which components have finished
            FlankerComponents = [fl_back_image, fl_fix, dist1, dist2, dist3, dist4, targ, j_button, k_button, l_button, fl_mouse]
            for thisComponent in FlankerComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Flanker" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from fl_anime
                nfrn = frameN/20;
                nlit = frameN%20;
                btemp = [9,10,11,12,13,14];
                
                btemp1 = [9,10,18,19];
                btemp2 = [11,12,16,17];
                btemp3 = [13,14,15];
                
                if nlit == 0:
                    blist = [btemp[i]+nfrn*20 for i in range(len(btemp))];
                    blist1 = [btemp1[i]+nfrn*20 for i in range(len(btemp1))];
                    blist2 = [btemp2[i]+nfrn*20 for i in range(len(btemp2))];
                    blist3 = [btemp3[i]+nfrn*20 for i in range(len(btemp3))];
                
                #print(blist, 'blist');
                
                if frameN in blist:  # more accurate to count frames
                    dist1.setImage(b)
                    dist2.setImage(b)
                    dist3.setImage(b)
                    dist4.setImage(b)
                    targ.setImage(a)
                
                else:
                    dist1.setImage(d)
                    dist2.setImage(d)
                    dist3.setImage(d)
                    dist4.setImage(d)
                    targ.setImage(a)
                
                
                #win.flip() 
                # Run 'Each Frame' code from fl_code_clik
                mouseloc = fl_mouse.getPos()
                if mouseloc[0]==mouserec[0] and mouseloc[1]==mouserec[1]:
                    pass
                
                elif j_button.contains(fl_mouse):
                    fl_res = 'j'
                    proper_rt = fl_time.getTime()-1
                    if t>minRT:
                        continueRoutine = False
                    else:
                        mouserec = fl_mouse.getPos()
                
                
                elif k_button.contains(fl_mouse):
                    fl_res = 'k'
                    proper_rt = fl_time.getTime()-1
                    if t>minRT:
                        continueRoutine = False
                    else:
                        mouserec = fl_mouse.getPos()
                
                
                elif l_button.contains(fl_mouse):
                    fl_res = 'l'
                    proper_rt = fl_time.getTime()-1
                    if t>minRT:
                        continueRoutine = False
                    else:
                        mouserec = fl_mouse.getPos()
                     
                
                # *fl_back_image* updates
                if fl_back_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fl_back_image.frameNStart = frameN  # exact frame index
                    fl_back_image.tStart = t  # local t and not account for scr refresh
                    fl_back_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fl_back_image, 'tStartRefresh')  # time at next scr refresh
                    fl_back_image.setAutoDraw(True)
                
                # *fl_fix* updates
                if fl_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fl_fix.frameNStart = frameN  # exact frame index
                    fl_fix.tStart = t  # local t and not account for scr refresh
                    fl_fix.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fl_fix, 'tStartRefresh')  # time at next scr refresh
                    fl_fix.setAutoDraw(True)
                if fl_fix.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fl_fix.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fl_fix.tStop = t  # not accounting for scr refresh
                        fl_fix.frameNStop = frameN  # exact frame index
                        fl_fix.setAutoDraw(False)
                
                # *dist1* updates
                if dist1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    dist1.frameNStart = frameN  # exact frame index
                    dist1.tStart = t  # local t and not account for scr refresh
                    dist1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist1, 'tStartRefresh')  # time at next scr refresh
                    dist1.setAutoDraw(True)
                
                # *dist2* updates
                if dist2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    dist2.frameNStart = frameN  # exact frame index
                    dist2.tStart = t  # local t and not account for scr refresh
                    dist2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist2, 'tStartRefresh')  # time at next scr refresh
                    dist2.setAutoDraw(True)
                
                # *dist3* updates
                if dist3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    dist3.frameNStart = frameN  # exact frame index
                    dist3.tStart = t  # local t and not account for scr refresh
                    dist3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist3, 'tStartRefresh')  # time at next scr refresh
                    dist3.setAutoDraw(True)
                
                # *dist4* updates
                if dist4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    dist4.frameNStart = frameN  # exact frame index
                    dist4.tStart = t  # local t and not account for scr refresh
                    dist4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist4, 'tStartRefresh')  # time at next scr refresh
                    dist4.setAutoDraw(True)
                
                # *targ* updates
                if targ.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    targ.frameNStart = frameN  # exact frame index
                    targ.tStart = t  # local t and not account for scr refresh
                    targ.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(targ, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'targ.started')
                    targ.setAutoDraw(True)
                
                # *j_button* updates
                if j_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    j_button.frameNStart = frameN  # exact frame index
                    j_button.tStart = t  # local t and not account for scr refresh
                    j_button.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(j_button, 'tStartRefresh')  # time at next scr refresh
                    j_button.setAutoDraw(True)
                
                # *k_button* updates
                if k_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    k_button.frameNStart = frameN  # exact frame index
                    k_button.tStart = t  # local t and not account for scr refresh
                    k_button.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(k_button, 'tStartRefresh')  # time at next scr refresh
                    k_button.setAutoDraw(True)
                
                # *l_button* updates
                if l_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    l_button.frameNStart = frameN  # exact frame index
                    l_button.tStart = t  # local t and not account for scr refresh
                    l_button.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(l_button, 'tStartRefresh')  # time at next scr refresh
                    l_button.setAutoDraw(True)
                # *fl_mouse* updates
                if fl_mouse.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    fl_mouse.frameNStart = frameN  # exact frame index
                    fl_mouse.tStart = t  # local t and not account for scr refresh
                    fl_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fl_mouse, 'tStartRefresh')  # time at next scr refresh
                    fl_mouse.status = STARTED
                    prevButtonState = fl_mouse.getPressed()  # if button is down already this ISN'T a new click
                if fl_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = fl_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([j_button, k_button, l_button])
                                clickableList = [j_button, k_button, l_button]
                            except:
                                clickableList = [[j_button, k_button, l_button]]
                            for obj in clickableList:
                                if obj.contains(fl_mouse):
                                    gotValidClick = True
                                    fl_mouse.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # abort routine on response
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in FlankerComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Flanker" ---
            for thisComponent in FlankerComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from fl_anime
            print('frames: ',frameN)
            
            # Run 'End Routine' code from fl_code_clik
            
            #flanker_main_loop.addData('fl_res')
            #if mouse_fl.clicked_name == ['j_button']:
            #    fl_res = 'j'
            #elif mouse_fl.clicked_name == ['k_button']:
            #    fl_res= 'k'
            #elif mouse_fl.clicked_name == ['l_button']:
            #    fl_res = 'l'
            
            fl_mouse.time = fl_time.getTime()-1
            
            if fl_res == fl_ans:
                fl_corr = 1
            elif fl_res != fl_ans:
                fl_corr = 0
            
            thisExp.addData('fl_ans', fl_ans)
            thisExp.addData('fl_res', fl_res)
            thisExp.addData('fl_corr', fl_corr)
            thisExp.addData('fl_rt', fl_mouse.time)
            thisExp.addData('fl_rt_2', proper_rt)
            
            # store data for flanker_main_loop (TrialHandler)
            # the Routine "Flanker" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "flankerfeedback" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from fl_feed_code
            
            message = ""
            feedur = 0
            
            fl_mouse.time = fl_mouse.time
            
            if fl_mouse.time == []:
                fl_mouse.time = -1
            
            if (fl_mouse.time == -1): 
                message = "더 빨리 응답하세요"
                feedur = 1
            elif (fl_mouse.time < 0.150): 
                message = "고양이를 보고 반응하세요"
                feedur = 3
            elif (fl_mouse.time > 1.5) and (fl_corr == 1): 
                message = "더 빨리 응답하세요"
                feedur = 1
            elif (fl_mouse.time > 1.5) and (fl_corr == 0): 
                message = "오답, 더 빨리 응답하세요"
                feedur = 1
            elif (fl_mouse.time < 1.5) and (fl_corr == 1): 
                message = ""
                feedur = 0
            elif (fl_mouse.time < 1.5) and (fl_corr == 0): 
                message = "오답"
                feedur = 1
            
            
            print('response', fl_res)
            print('accuracy', fl_corr)
            print('rt', fl_mouse.time)
            print('message',message)
            print('feedur',feedur)
            
            
            fl_feedback.setText(message)
            # keep track of which components have finished
            flankerfeedbackComponents = [fl_back_image2, fl_feedback, j_button2, k_button2, l_button2]
            for thisComponent in flankerfeedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "flankerfeedback" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fl_back_image2* updates
                if fl_back_image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fl_back_image2.frameNStart = frameN  # exact frame index
                    fl_back_image2.tStart = t  # local t and not account for scr refresh
                    fl_back_image2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fl_back_image2, 'tStartRefresh')  # time at next scr refresh
                    fl_back_image2.setAutoDraw(True)
                if fl_back_image2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fl_back_image2.tStartRefresh + feedur-frameTolerance:
                        # keep track of stop time/frame for later
                        fl_back_image2.tStop = t  # not accounting for scr refresh
                        fl_back_image2.frameNStop = frameN  # exact frame index
                        fl_back_image2.setAutoDraw(False)
                
                # *fl_feedback* updates
                if fl_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fl_feedback.frameNStart = frameN  # exact frame index
                    fl_feedback.tStart = t  # local t and not account for scr refresh
                    fl_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fl_feedback, 'tStartRefresh')  # time at next scr refresh
                    fl_feedback.setAutoDraw(True)
                if fl_feedback.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fl_feedback.tStartRefresh + feedur-frameTolerance:
                        # keep track of stop time/frame for later
                        fl_feedback.tStop = t  # not accounting for scr refresh
                        fl_feedback.frameNStop = frameN  # exact frame index
                        fl_feedback.setAutoDraw(False)
                
                # *j_button2* updates
                if j_button2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    j_button2.frameNStart = frameN  # exact frame index
                    j_button2.tStart = t  # local t and not account for scr refresh
                    j_button2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(j_button2, 'tStartRefresh')  # time at next scr refresh
                    j_button2.setAutoDraw(True)
                if j_button2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > j_button2.tStartRefresh + feedur-frameTolerance:
                        # keep track of stop time/frame for later
                        j_button2.tStop = t  # not accounting for scr refresh
                        j_button2.frameNStop = frameN  # exact frame index
                        j_button2.setAutoDraw(False)
                
                # *k_button2* updates
                if k_button2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    k_button2.frameNStart = frameN  # exact frame index
                    k_button2.tStart = t  # local t and not account for scr refresh
                    k_button2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(k_button2, 'tStartRefresh')  # time at next scr refresh
                    k_button2.setAutoDraw(True)
                if k_button2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > k_button2.tStartRefresh + feedur-frameTolerance:
                        # keep track of stop time/frame for later
                        k_button2.tStop = t  # not accounting for scr refresh
                        k_button2.frameNStop = frameN  # exact frame index
                        k_button2.setAutoDraw(False)
                
                # *l_button2* updates
                if l_button2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    l_button2.frameNStart = frameN  # exact frame index
                    l_button2.tStart = t  # local t and not account for scr refresh
                    l_button2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(l_button2, 'tStartRefresh')  # time at next scr refresh
                    l_button2.setAutoDraw(True)
                if l_button2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > l_button2.tStartRefresh + feedur-frameTolerance:
                        # keep track of stop time/frame for later
                        l_button2.tStop = t  # not accounting for scr refresh
                        l_button2.frameNStop = frameN  # exact frame index
                        l_button2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in flankerfeedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "flankerfeedback" ---
            for thisComponent in flankerfeedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "flankerfeedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed fmain repeats of 'flanker_main_loop'
        
        thisExp.nextEntry()
        
    # completed boat_loop repeats of 'boat'
    
    
    # set up handler to look after randomisation of conditions etc
    para = data.TrialHandler(nReps=para_loop, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='para')
    thisExp.addLoop(para)  # add the loop to the experiment
    thisPara = para.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPara.rgb)
    if thisPara != None:
        for paramName in thisPara:
            exec('{} = thisPara[paramName]'.format(paramName))
    
    for thisPara in para:
        currentLoop = para
        # abbreviate parameter names if possible (e.g. rgb = thisPara.rgb)
        if thisPara != None:
            for paramName in thisPara:
                exec('{} = thisPara[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "para_starter_code" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from para_random_cb
        win.fullscr = True
        
        if test_mode == 1:
            win.mouseVisible = True
        else:
            win.mouseVisible = False
        para_starter_key.keys = []
        para_starter_key.rt = []
        _para_starter_key_allKeys = []
        # setup some python lists for storing info about the para_skip_click
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        para_starter_codeComponents = [para_starter, para_starter_text, para_starter_key, para_skip_click]
        for thisComponent in para_starter_codeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "para_starter_code" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *para_starter* updates
            if para_starter.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                para_starter.frameNStart = frameN  # exact frame index
                para_starter.tStart = t  # local t and not account for scr refresh
                para_starter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_starter, 'tStartRefresh')  # time at next scr refresh
                para_starter.setAutoDraw(True)
            
            # *para_starter_text* updates
            if para_starter_text.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                para_starter_text.frameNStart = frameN  # exact frame index
                para_starter_text.tStart = t  # local t and not account for scr refresh
                para_starter_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_starter_text, 'tStartRefresh')  # time at next scr refresh
                para_starter_text.setAutoDraw(True)
            
            # *para_starter_key* updates
            waitOnFlip = False
            if para_starter_key.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                para_starter_key.frameNStart = frameN  # exact frame index
                para_starter_key.tStart = t  # local t and not account for scr refresh
                para_starter_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_starter_key, 'tStartRefresh')  # time at next scr refresh
                para_starter_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(para_starter_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(para_starter_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if para_starter_key.status == STARTED and not waitOnFlip:
                theseKeys = para_starter_key.getKeys(keyList=['space'], waitRelease=False)
                _para_starter_key_allKeys.extend(theseKeys)
                if len(_para_starter_key_allKeys):
                    para_starter_key.keys = _para_starter_key_allKeys[-1].name  # just the last key pressed
                    para_starter_key.rt = _para_starter_key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # *para_skip_click* updates
            if para_skip_click.status == NOT_STARTED and t >= 2-frameTolerance:
                # keep track of start time/frame for later
                para_skip_click.frameNStart = frameN  # exact frame index
                para_skip_click.tStart = t  # local t and not account for scr refresh
                para_skip_click.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_skip_click, 'tStartRefresh')  # time at next scr refresh
                para_skip_click.status = STARTED
                para_skip_click.mouseClock.reset()
                prevButtonState = para_skip_click.getPressed()  # if button is down already this ISN'T a new click
            if para_skip_click.status == STARTED:  # only update if started and not finished!
                buttons = para_skip_click.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        continueRoutine = False  # abort routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in para_starter_codeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "para_starter_code" ---
        for thisComponent in para_starter_codeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for para (TrialHandler)
        # the Routine "para_starter_code" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "para_inst" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from para_rep_code
        if counter_resp == bhya_resp:
            inst='ins/st2_bhya.png'
            aud= 'ins/st2_bhya.wav'
            theanswer = '정답: 파랑-웃음, 노랑-화남'
        elif counter_resp == bayh_resp:
            inst='ins/st2_bayh.png'
            aud= 'ins/st2_bayh.wav'
            theanswer = '정답: 노랑-웃음, 파랑-화남'
            
        
        para_inst_img.setImage(inst)
        para_inst_sound.setSound(aud, hamming=True)
        para_inst_sound.setVolume(1.0, log=False)
        para_inst_key.keys = []
        para_inst_key.rt = []
        _para_inst_key_allKeys = []
        # setup some python lists for storing info about the para_click_next
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        para_instComponents = [para_inst_img, para_inst_sound, para_inst_key, para_click_next]
        for thisComponent in para_instComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "para_inst" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *para_inst_img* updates
            if para_inst_img.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                para_inst_img.frameNStart = frameN  # exact frame index
                para_inst_img.tStart = t  # local t and not account for scr refresh
                para_inst_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_inst_img, 'tStartRefresh')  # time at next scr refresh
                para_inst_img.setAutoDraw(True)
            # start/stop para_inst_sound
            if para_inst_sound.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                para_inst_sound.frameNStart = frameN  # exact frame index
                para_inst_sound.tStart = t  # local t and not account for scr refresh
                para_inst_sound.tStartRefresh = tThisFlipGlobal  # on global time
                para_inst_sound.play(when=win)  # sync with win flip
            
            # *para_inst_key* updates
            waitOnFlip = False
            if para_inst_key.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                para_inst_key.frameNStart = frameN  # exact frame index
                para_inst_key.tStart = t  # local t and not account for scr refresh
                para_inst_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_inst_key, 'tStartRefresh')  # time at next scr refresh
                para_inst_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(para_inst_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(para_inst_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if para_inst_key.status == STARTED and not waitOnFlip:
                theseKeys = para_inst_key.getKeys(keyList=['space'], waitRelease=False)
                _para_inst_key_allKeys.extend(theseKeys)
                if len(_para_inst_key_allKeys):
                    para_inst_key.keys = _para_inst_key_allKeys[-1].name  # just the last key pressed
                    para_inst_key.rt = _para_inst_key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # *para_click_next* updates
            if para_click_next.status == NOT_STARTED and t >= 1-frameTolerance:
                # keep track of start time/frame for later
                para_click_next.frameNStart = frameN  # exact frame index
                para_click_next.tStart = t  # local t and not account for scr refresh
                para_click_next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_click_next, 'tStartRefresh')  # time at next scr refresh
                para_click_next.status = STARTED
                para_click_next.mouseClock.reset()
                prevButtonState = para_click_next.getPressed()  # if button is down already this ISN'T a new click
            if para_click_next.status == STARTED:  # only update if started and not finished!
                buttons = para_click_next.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        continueRoutine = False  # abort routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in para_instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "para_inst" ---
        for thisComponent in para_instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from para_rep_code
        backpic = 'pics\st_back.png';
        
        nowexp = 2;
        #fl 1 st 2 
        para_inst_sound.stop()  # ensure sound has stopped at end of routine
        # store data for para (TrialHandler)
        # the Routine "para_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "para_fix" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        para_fixComponents = [para_fix_back, para_fix_2, para_text_next]
        for thisComponent in para_fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "para_fix" ---
        while continueRoutine and routineTimer.getTime() < 6.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *para_fix_back* updates
            if para_fix_back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                para_fix_back.frameNStart = frameN  # exact frame index
                para_fix_back.tStart = t  # local t and not account for scr refresh
                para_fix_back.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_fix_back, 'tStartRefresh')  # time at next scr refresh
                para_fix_back.setAutoDraw(True)
            if para_fix_back.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > para_fix_back.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    para_fix_back.tStop = t  # not accounting for scr refresh
                    para_fix_back.frameNStop = frameN  # exact frame index
                    para_fix_back.setAutoDraw(False)
            
            # *para_fix_2* updates
            if para_fix_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                para_fix_2.frameNStart = frameN  # exact frame index
                para_fix_2.tStart = t  # local t and not account for scr refresh
                para_fix_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_fix_2, 'tStartRefresh')  # time at next scr refresh
                para_fix_2.setAutoDraw(True)
            if para_fix_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > para_fix_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    para_fix_2.tStop = t  # not accounting for scr refresh
                    para_fix_2.frameNStop = frameN  # exact frame index
                    para_fix_2.setAutoDraw(False)
            
            # *para_text_next* updates
            if para_text_next.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                para_text_next.frameNStart = frameN  # exact frame index
                para_text_next.tStart = t  # local t and not account for scr refresh
                para_text_next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_text_next, 'tStartRefresh')  # time at next scr refresh
                para_text_next.setAutoDraw(True)
            if para_text_next.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > para_text_next.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    para_text_next.tStop = t  # not accounting for scr refresh
                    para_text_next.frameNStop = frameN  # exact frame index
                    para_text_next.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in para_fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "para_fix" ---
        for thisComponent in para_fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-6.000000)
        
        # set up handler to look after randomisation of conditions etc
        para_prac_loop = data.TrialHandler(nReps=para_prac, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('loop/stroop_prac.xlsx'),
            seed=None, name='para_prac_loop')
        thisExp.addLoop(para_prac_loop)  # add the loop to the experiment
        thisPara_prac_loop = para_prac_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPara_prac_loop.rgb)
        if thisPara_prac_loop != None:
            for paramName in thisPara_prac_loop:
                exec('{} = thisPara_prac_loop[paramName]'.format(paramName))
        
        for thisPara_prac_loop in para_prac_loop:
            currentLoop = para_prac_loop
            # abbreviate parameter names if possible (e.g. rgb = thisPara_prac_loop.rgb)
            if thisPara_prac_loop != None:
                for paramName in thisPara_prac_loop:
                    exec('{} = thisPara_prac_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "para_tag_prc" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from para_prac_tag
            dist_cond = para_prac_loop.thisTrial["distractor"]
            targ_cond = para_prac_loop.thisTrial["target"]
            set_cond  = para_prac_loop.thisTrial["set"]
            thisn = para_prac_loop.thisN
            
            
            
            
            ##########TEST MODE###########
            if test_mode == 1 and thisn == 3:
                para_prac_loop.finished=True
            # keep track of which components have finished
            para_tag_prcComponents = []
            for thisComponent in para_tag_prcComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "para_tag_prc" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in para_tag_prcComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "para_tag_prc" ---
            for thisComponent in para_tag_prcComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from para_prac_tag
            para_prac_loop.addData('main_prac', 'prac')
            
            # the Routine "para_tag_prc" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "parachute" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from para_code_ani
            print(thisn)
            print(dist_cond)
            print(targ_cond)
            print(set_cond)
            
            #xrand = randint(-5,5);
            #yrand = randint(-5,5);
            #posx = 0.02*xrand;
            #posy = 0.02*yrand;
            posx = 0.0;
            posy = 0.0;
            
            
            ranint = randint(1,10);
            coln = randg[ranint];
            print(coln, 'color')
            
            
            if dist_cond == "negative" and set_cond == 1 and coln == 1:
                d = set1_angry_g
                b = set1_angry_blink_g_1
            
            elif dist_cond == "negative" and set_cond == 1 and coln == 2:
                d = set1_angry_y
                b = set1_angry_blink_y_1
                
            elif dist_cond == "neutral" and set_cond == 1 and coln == 1:
                d  = set1_neutral_g
                b = set1_neutral_blink_g_1
            
            elif dist_cond == "neutral" and set_cond == 1 and coln == 2:
                d  = set1_neutral_y
                b = set1_neutral_blink_y_1
                
            elif dist_cond == "positive" and set_cond == 1 and coln == 1:
                d  = set1_happy_g
                b = set1_happy_blink_g_1
            
            elif dist_cond == "positive" and set_cond == 1 and coln == 2:
                d  = set1_happy_y
                b = set1_happy_blink_y_1
                
            if dist_cond == "negative" and set_cond == 2 and coln == 1:
                d = set2_angry_g
                b = set2_angry_blink_g_1
            
            elif dist_cond == "negative" and set_cond == 2 and coln == 2:
                d = set2_angry_y
                b = set2_angry_blink_y_1
            
            elif dist_cond == "neutral" and set_cond == 2 and coln == 1:
                d  = set2_neutral_g
                b = set2_neutral_blink_g_1
            
            elif dist_cond == "neutral" and set_cond == 2 and coln == 2:
                d  = set2_neutral_y
                b = set2_neutral_blink_y_1
                
            elif dist_cond == "positive" and set_cond == 2 and coln == 1:
                d  = set2_happy_g
                b = set2_happy_blink_g_1
            
            elif dist_cond == "positive" and set_cond == 2 and coln == 2:
                d  = set2_happy_y
                b = set2_happy_blink_y_1
            
            
            if targ_cond == "blue":
                a = para_blu
                c = para_blu
            elif targ_cond == "blue":
                a = para_blu
                c = para_blu
            elif targ_cond == "blue":
                a = para_blu
                c = para_blu
            elif targ_cond == "red":
                a = para_red
                c = para_red
            elif targ_cond == "red":
                a = para_red
                c = para_red
            elif targ_cond == "red":
                a = para_red
                c = para_red
            elif targ_cond == "yellow":
                a = para_yel
                c = para_yel
            elif targ_cond == "yellow":
                a = para_yel
                c = para_yel
            elif targ_cond == "yellow":
                a = para_yel
                c = para_yel
            
            
            
            
            # The contents of this file are in the public domain.
            # Run 'Begin Routine' code from para_code
            if counter_resp == bhya_resp:
                st2_ans = ans1
                print('answer1 is ',ans1)
            elif counter_resp == bayh_resp:
                st2_ans = ans2
                print('answer2 is ',ans2)
            print(st2_ans)
            
            mouserec=mouse_st.getPos()
            minRT = .2
            
            
            st_res = None
            st_time = core.Clock()
            face_dist_2.setPos((posx, posy))
            para_targ_2.setPos((posx, posy))
            # setup some python lists for storing info about the mouse_st
            mouse_st.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_st.mouseClock.reset()
            st2_resp.keys = []
            st2_resp.rt = []
            _st2_resp_allKeys = []
            text.setText(theanswer)
            # keep track of which components have finished
            parachuteComponents = [para_back, para_fix_prac, face_dist_2, para_targ_2, mouse_st, st2_resp, text]
            for thisComponent in parachuteComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "parachute" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from para_code_ani
                nfrn = frameN/20;
                nlit = frameN%20;
                btemp = [9,10,11,12,13,14];
                
                if nlit == 0:
                    blist = [btemp[i]+nfrn*20 for i in range(len(btemp))];
                #if frameN in [18,19,20,38,39,40]:  # more accurate to count frames
                if frameN in blist:
                    face_dist_2.setImage(b)
                    para_targ_2.setImage(a)
                else:
                    face_dist_2.setImage(d)
                    para_targ_2.setImage(c)
                    
                if st2_ans !='k' and t >=2.5:
                    continueRoutine = False
                # Run 'Each Frame' code from para_code
                mouseloc = mouse_st.getPos()
                if mouseloc[0]==mouserec[0] and mouseloc[1]==mouserec[1]:
                    pass
                
                elif para_targ_2.contains(mouse_st):
                    st_res = 'k'
                    para_rt = st_time.getTime()-1
                
                    if t>minRT:
                        continueRoutine = False
                    else:
                        mouserec = mouse_st.getPos()
                
                # *para_back* updates
                if para_back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    para_back.frameNStart = frameN  # exact frame index
                    para_back.tStart = t  # local t and not account for scr refresh
                    para_back.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(para_back, 'tStartRefresh')  # time at next scr refresh
                    para_back.setAutoDraw(True)
                
                # *para_fix_prac* updates
                if para_fix_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    para_fix_prac.frameNStart = frameN  # exact frame index
                    para_fix_prac.tStart = t  # local t and not account for scr refresh
                    para_fix_prac.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(para_fix_prac, 'tStartRefresh')  # time at next scr refresh
                    para_fix_prac.setAutoDraw(True)
                if para_fix_prac.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > para_fix_prac.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        para_fix_prac.tStop = t  # not accounting for scr refresh
                        para_fix_prac.frameNStop = frameN  # exact frame index
                        para_fix_prac.setAutoDraw(False)
                
                # *face_dist_2* updates
                if face_dist_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    face_dist_2.frameNStart = frameN  # exact frame index
                    face_dist_2.tStart = t  # local t and not account for scr refresh
                    face_dist_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(face_dist_2, 'tStartRefresh')  # time at next scr refresh
                    face_dist_2.setAutoDraw(True)
                
                # *para_targ_2* updates
                if para_targ_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    para_targ_2.frameNStart = frameN  # exact frame index
                    para_targ_2.tStart = t  # local t and not account for scr refresh
                    para_targ_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(para_targ_2, 'tStartRefresh')  # time at next scr refresh
                    para_targ_2.setAutoDraw(True)
                # *mouse_st* updates
                if mouse_st.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_st.frameNStart = frameN  # exact frame index
                    mouse_st.tStart = t  # local t and not account for scr refresh
                    mouse_st.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_st, 'tStartRefresh')  # time at next scr refresh
                    mouse_st.status = STARTED
                    prevButtonState = mouse_st.getPressed()  # if button is down already this ISN'T a new click
                if mouse_st.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_st.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter(para_targ_2)
                                clickableList = para_targ_2
                            except:
                                clickableList = [para_targ_2]
                            for obj in clickableList:
                                if obj.contains(mouse_st):
                                    gotValidClick = True
                                    mouse_st.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # abort routine on response
                
                # *st2_resp* updates
                waitOnFlip = False
                if st2_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    st2_resp.frameNStart = frameN  # exact frame index
                    st2_resp.tStart = t  # local t and not account for scr refresh
                    st2_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(st2_resp, 'tStartRefresh')  # time at next scr refresh
                    st2_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(st2_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(st2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if st2_resp.status == STARTED and not waitOnFlip:
                    theseKeys = st2_resp.getKeys(keyList=['k'], waitRelease=False)
                    _st2_resp_allKeys.extend(theseKeys)
                    if len(_st2_resp_allKeys):
                        st2_resp.keys = _st2_resp_allKeys[-1].name  # just the last key pressed
                        st2_resp.rt = _st2_resp_allKeys[-1].rt
                        # was this correct?
                        if (st2_resp.keys == str(st2_ans)) or (st2_resp.keys == st2_ans):
                            st2_resp.corr = 1
                        else:
                            st2_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *text* updates
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    text.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in parachuteComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "parachute" ---
            for thisComponent in parachuteComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from para_code_ani
            print('frames',frameN)
            
            # Run 'End Routine' code from para_code
            #if mouse_st.clicked_name == ['para_targ_2']:
            #    st_res = 'k'
            #else : 
            #    st_res = None
            
            mouse_st.time = st_time.getTime()
            mouse_st.time = mouse_st.time-1
            if st_res == st2_ans :
                st_corr = 1
            elif st_res != st2_ans :
                st_corr = 0
            
            print('corr',st_corr)
            
            thisExp.addData('st_ans', st2_ans)
            thisExp.addData('st_res', st_res)
            thisExp.addData('st_corr', st_corr)
            thisExp.addData('st_rt', mouse_st.time)
            thisExp.addData('st_rt2', para_rt)
            # store data for para_prac_loop (TrialHandler)
            # check responses
            if st2_resp.keys in ['', [], None]:  # No response was made
                st2_resp.keys = None
                # was no response the correct answer?!
                if str(st2_ans).lower() == 'none':
                   st2_resp.corr = 1;  # correct non-response
                else:
                   st2_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for para_prac_loop (TrialHandler)
            para_prac_loop.addData('st2_resp.keys',st2_resp.keys)
            para_prac_loop.addData('st2_resp.corr', st2_resp.corr)
            if st2_resp.keys != None:  # we had a response
                para_prac_loop.addData('st2_resp.rt', st2_resp.rt)
            # the Routine "parachute" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "para_feedback" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from para_feed_code
            message = ""
            feedur = 0
            
            print('rt', mouse_st.time)
            print('st_cor', st_corr)
            if (mouse_st.time > 1.5) and (st_corr == 1) and (st2_ans == 'k'): 
                message = "좀 더 빨리 응답하세요"
                feedur = 1
            elif (mouse_st.time < 0.150):
                message = "고양이를 보고 반응하세요"
                feedur = 3
            elif (mouse_st.time > 1.5) and (st_corr == 0) and (st2_ans == 'k'):
                message = "오답, 좀 더 빨리 응답하세요"
                feedur = 1
            elif (st2_ans == 'k') and (st_corr == 1): 
                message = ""
                feedur = 0.0
            elif (st2_ans != 'k') and (st_corr == 1): 
                message = ""
                feedur = 0.0
            elif (st2_ans == 'k') and (st_corr == 0): 
                message = "오답"
                feedur = 1
            elif (st2_ans != 'k') and (st_corr == 0): 
                message = "오답"
                feedur = 1
            
            
            
            
            para_feed_message.setText(message)
            # keep track of which components have finished
            para_feedbackComponents = [para_f_back, para_feed_message]
            for thisComponent in para_feedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "para_feedback" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *para_f_back* updates
                if para_f_back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    para_f_back.frameNStart = frameN  # exact frame index
                    para_f_back.tStart = t  # local t and not account for scr refresh
                    para_f_back.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(para_f_back, 'tStartRefresh')  # time at next scr refresh
                    para_f_back.setAutoDraw(True)
                if para_f_back.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > para_f_back.tStartRefresh + feedur-frameTolerance:
                        # keep track of stop time/frame for later
                        para_f_back.tStop = t  # not accounting for scr refresh
                        para_f_back.frameNStop = frameN  # exact frame index
                        para_f_back.setAutoDraw(False)
                
                # *para_feed_message* updates
                if para_feed_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    para_feed_message.frameNStart = frameN  # exact frame index
                    para_feed_message.tStart = t  # local t and not account for scr refresh
                    para_feed_message.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(para_feed_message, 'tStartRefresh')  # time at next scr refresh
                    para_feed_message.setAutoDraw(True)
                if para_feed_message.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > para_feed_message.tStartRefresh + feedur-frameTolerance:
                        # keep track of stop time/frame for later
                        para_feed_message.tStop = t  # not accounting for scr refresh
                        para_feed_message.frameNStop = frameN  # exact frame index
                        para_feed_message.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in para_feedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "para_feedback" ---
            for thisComponent in para_feedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "para_feedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed para_prac repeats of 'para_prac_loop'
        
        
        # --- Prepare to start Routine "para_say_main" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # setup some python lists for storing info about the para_mouse
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        para_say_mainComponents = [para_main_back, para_main_text, para_mouse]
        for thisComponent in para_say_mainComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "para_say_main" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *para_main_back* updates
            if para_main_back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                para_main_back.frameNStart = frameN  # exact frame index
                para_main_back.tStart = t  # local t and not account for scr refresh
                para_main_back.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_main_back, 'tStartRefresh')  # time at next scr refresh
                para_main_back.setAutoDraw(True)
            
            # *para_main_text* updates
            if para_main_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                para_main_text.frameNStart = frameN  # exact frame index
                para_main_text.tStart = t  # local t and not account for scr refresh
                para_main_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_main_text, 'tStartRefresh')  # time at next scr refresh
                para_main_text.setAutoDraw(True)
            # *para_mouse* updates
            if para_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                para_mouse.frameNStart = frameN  # exact frame index
                para_mouse.tStart = t  # local t and not account for scr refresh
                para_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_mouse, 'tStartRefresh')  # time at next scr refresh
                para_mouse.status = STARTED
                para_mouse.mouseClock.reset()
                prevButtonState = para_mouse.getPressed()  # if button is down already this ISN'T a new click
            if para_mouse.status == STARTED:  # only update if started and not finished!
                buttons = para_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        continueRoutine = False  # abort routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in para_say_mainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "para_say_main" ---
        for thisComponent in para_say_mainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for para (TrialHandler)
        # the Routine "para_say_main" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "para_fix" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        para_fixComponents = [para_fix_back, para_fix_2, para_text_next]
        for thisComponent in para_fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "para_fix" ---
        while continueRoutine and routineTimer.getTime() < 6.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *para_fix_back* updates
            if para_fix_back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                para_fix_back.frameNStart = frameN  # exact frame index
                para_fix_back.tStart = t  # local t and not account for scr refresh
                para_fix_back.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_fix_back, 'tStartRefresh')  # time at next scr refresh
                para_fix_back.setAutoDraw(True)
            if para_fix_back.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > para_fix_back.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    para_fix_back.tStop = t  # not accounting for scr refresh
                    para_fix_back.frameNStop = frameN  # exact frame index
                    para_fix_back.setAutoDraw(False)
            
            # *para_fix_2* updates
            if para_fix_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                para_fix_2.frameNStart = frameN  # exact frame index
                para_fix_2.tStart = t  # local t and not account for scr refresh
                para_fix_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_fix_2, 'tStartRefresh')  # time at next scr refresh
                para_fix_2.setAutoDraw(True)
            if para_fix_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > para_fix_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    para_fix_2.tStop = t  # not accounting for scr refresh
                    para_fix_2.frameNStop = frameN  # exact frame index
                    para_fix_2.setAutoDraw(False)
            
            # *para_text_next* updates
            if para_text_next.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                para_text_next.frameNStart = frameN  # exact frame index
                para_text_next.tStart = t  # local t and not account for scr refresh
                para_text_next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(para_text_next, 'tStartRefresh')  # time at next scr refresh
                para_text_next.setAutoDraw(True)
            if para_text_next.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > para_text_next.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    para_text_next.tStop = t  # not accounting for scr refresh
                    para_text_next.frameNStop = frameN  # exact frame index
                    para_text_next.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in para_fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "para_fix" ---
        for thisComponent in para_fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-6.000000)
        
        # set up handler to look after randomisation of conditions etc
        para_main_loop = data.TrialHandler(nReps=para_main, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(st2_set),
            seed=None, name='para_main_loop')
        thisExp.addLoop(para_main_loop)  # add the loop to the experiment
        thisPara_main_loop = para_main_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPara_main_loop.rgb)
        if thisPara_main_loop != None:
            for paramName in thisPara_main_loop:
                exec('{} = thisPara_main_loop[paramName]'.format(paramName))
        
        for thisPara_main_loop in para_main_loop:
            currentLoop = para_main_loop
            # abbreviate parameter names if possible (e.g. rgb = thisPara_main_loop.rgb)
            if thisPara_main_loop != None:
                for paramName in thisPara_main_loop:
                    exec('{} = thisPara_main_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "para_tag_main" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from para_main_tag
            dist_cond = para_main_loop.thisTrial["distractor"]
            targ_cond = para_main_loop.thisTrial["target"]
            set_cond  = para_main_loop.thisTrial["set"]
            thisn = para_main_loop.thisN
            
            ##########TEST MODE###########
            if test_mode == 1 and thisn == 3:
                para_main_loop.finished=True
                
                
            theanswer=''
            # keep track of which components have finished
            para_tag_mainComponents = []
            for thisComponent in para_tag_mainComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "para_tag_main" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in para_tag_mainComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "para_tag_main" ---
            for thisComponent in para_tag_mainComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from para_main_tag
            para_main_loop.addData('main_prac', 'main')
            
            # the Routine "para_tag_main" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "parachute" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from para_code_ani
            print(thisn)
            print(dist_cond)
            print(targ_cond)
            print(set_cond)
            
            #xrand = randint(-5,5);
            #yrand = randint(-5,5);
            #posx = 0.02*xrand;
            #posy = 0.02*yrand;
            posx = 0.0;
            posy = 0.0;
            
            
            ranint = randint(1,10);
            coln = randg[ranint];
            print(coln, 'color')
            
            
            if dist_cond == "negative" and set_cond == 1 and coln == 1:
                d = set1_angry_g
                b = set1_angry_blink_g_1
            
            elif dist_cond == "negative" and set_cond == 1 and coln == 2:
                d = set1_angry_y
                b = set1_angry_blink_y_1
                
            elif dist_cond == "neutral" and set_cond == 1 and coln == 1:
                d  = set1_neutral_g
                b = set1_neutral_blink_g_1
            
            elif dist_cond == "neutral" and set_cond == 1 and coln == 2:
                d  = set1_neutral_y
                b = set1_neutral_blink_y_1
                
            elif dist_cond == "positive" and set_cond == 1 and coln == 1:
                d  = set1_happy_g
                b = set1_happy_blink_g_1
            
            elif dist_cond == "positive" and set_cond == 1 and coln == 2:
                d  = set1_happy_y
                b = set1_happy_blink_y_1
                
            if dist_cond == "negative" and set_cond == 2 and coln == 1:
                d = set2_angry_g
                b = set2_angry_blink_g_1
            
            elif dist_cond == "negative" and set_cond == 2 and coln == 2:
                d = set2_angry_y
                b = set2_angry_blink_y_1
            
            elif dist_cond == "neutral" and set_cond == 2 and coln == 1:
                d  = set2_neutral_g
                b = set2_neutral_blink_g_1
            
            elif dist_cond == "neutral" and set_cond == 2 and coln == 2:
                d  = set2_neutral_y
                b = set2_neutral_blink_y_1
                
            elif dist_cond == "positive" and set_cond == 2 and coln == 1:
                d  = set2_happy_g
                b = set2_happy_blink_g_1
            
            elif dist_cond == "positive" and set_cond == 2 and coln == 2:
                d  = set2_happy_y
                b = set2_happy_blink_y_1
            
            
            if targ_cond == "blue":
                a = para_blu
                c = para_blu
            elif targ_cond == "blue":
                a = para_blu
                c = para_blu
            elif targ_cond == "blue":
                a = para_blu
                c = para_blu
            elif targ_cond == "red":
                a = para_red
                c = para_red
            elif targ_cond == "red":
                a = para_red
                c = para_red
            elif targ_cond == "red":
                a = para_red
                c = para_red
            elif targ_cond == "yellow":
                a = para_yel
                c = para_yel
            elif targ_cond == "yellow":
                a = para_yel
                c = para_yel
            elif targ_cond == "yellow":
                a = para_yel
                c = para_yel
            
            
            
            
            # The contents of this file are in the public domain.
            # Run 'Begin Routine' code from para_code
            if counter_resp == bhya_resp:
                st2_ans = ans1
                print('answer1 is ',ans1)
            elif counter_resp == bayh_resp:
                st2_ans = ans2
                print('answer2 is ',ans2)
            print(st2_ans)
            
            mouserec=mouse_st.getPos()
            minRT = .2
            
            
            st_res = None
            st_time = core.Clock()
            face_dist_2.setPos((posx, posy))
            para_targ_2.setPos((posx, posy))
            # setup some python lists for storing info about the mouse_st
            mouse_st.clicked_name = []
            gotValidClick = False  # until a click is received
            mouse_st.mouseClock.reset()
            st2_resp.keys = []
            st2_resp.rt = []
            _st2_resp_allKeys = []
            text.setText(theanswer)
            # keep track of which components have finished
            parachuteComponents = [para_back, para_fix_prac, face_dist_2, para_targ_2, mouse_st, st2_resp, text]
            for thisComponent in parachuteComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "parachute" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from para_code_ani
                nfrn = frameN/20;
                nlit = frameN%20;
                btemp = [9,10,11,12,13,14];
                
                if nlit == 0:
                    blist = [btemp[i]+nfrn*20 for i in range(len(btemp))];
                #if frameN in [18,19,20,38,39,40]:  # more accurate to count frames
                if frameN in blist:
                    face_dist_2.setImage(b)
                    para_targ_2.setImage(a)
                else:
                    face_dist_2.setImage(d)
                    para_targ_2.setImage(c)
                    
                if st2_ans !='k' and t >=2.5:
                    continueRoutine = False
                # Run 'Each Frame' code from para_code
                mouseloc = mouse_st.getPos()
                if mouseloc[0]==mouserec[0] and mouseloc[1]==mouserec[1]:
                    pass
                
                elif para_targ_2.contains(mouse_st):
                    st_res = 'k'
                    para_rt = st_time.getTime()-1
                
                    if t>minRT:
                        continueRoutine = False
                    else:
                        mouserec = mouse_st.getPos()
                
                # *para_back* updates
                if para_back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    para_back.frameNStart = frameN  # exact frame index
                    para_back.tStart = t  # local t and not account for scr refresh
                    para_back.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(para_back, 'tStartRefresh')  # time at next scr refresh
                    para_back.setAutoDraw(True)
                
                # *para_fix_prac* updates
                if para_fix_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    para_fix_prac.frameNStart = frameN  # exact frame index
                    para_fix_prac.tStart = t  # local t and not account for scr refresh
                    para_fix_prac.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(para_fix_prac, 'tStartRefresh')  # time at next scr refresh
                    para_fix_prac.setAutoDraw(True)
                if para_fix_prac.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > para_fix_prac.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        para_fix_prac.tStop = t  # not accounting for scr refresh
                        para_fix_prac.frameNStop = frameN  # exact frame index
                        para_fix_prac.setAutoDraw(False)
                
                # *face_dist_2* updates
                if face_dist_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    face_dist_2.frameNStart = frameN  # exact frame index
                    face_dist_2.tStart = t  # local t and not account for scr refresh
                    face_dist_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(face_dist_2, 'tStartRefresh')  # time at next scr refresh
                    face_dist_2.setAutoDraw(True)
                
                # *para_targ_2* updates
                if para_targ_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    para_targ_2.frameNStart = frameN  # exact frame index
                    para_targ_2.tStart = t  # local t and not account for scr refresh
                    para_targ_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(para_targ_2, 'tStartRefresh')  # time at next scr refresh
                    para_targ_2.setAutoDraw(True)
                # *mouse_st* updates
                if mouse_st.status == NOT_STARTED and t >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_st.frameNStart = frameN  # exact frame index
                    mouse_st.tStart = t  # local t and not account for scr refresh
                    mouse_st.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_st, 'tStartRefresh')  # time at next scr refresh
                    mouse_st.status = STARTED
                    prevButtonState = mouse_st.getPressed()  # if button is down already this ISN'T a new click
                if mouse_st.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_st.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter(para_targ_2)
                                clickableList = para_targ_2
                            except:
                                clickableList = [para_targ_2]
                            for obj in clickableList:
                                if obj.contains(mouse_st):
                                    gotValidClick = True
                                    mouse_st.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # abort routine on response
                
                # *st2_resp* updates
                waitOnFlip = False
                if st2_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    st2_resp.frameNStart = frameN  # exact frame index
                    st2_resp.tStart = t  # local t and not account for scr refresh
                    st2_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(st2_resp, 'tStartRefresh')  # time at next scr refresh
                    st2_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(st2_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(st2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if st2_resp.status == STARTED and not waitOnFlip:
                    theseKeys = st2_resp.getKeys(keyList=['k'], waitRelease=False)
                    _st2_resp_allKeys.extend(theseKeys)
                    if len(_st2_resp_allKeys):
                        st2_resp.keys = _st2_resp_allKeys[-1].name  # just the last key pressed
                        st2_resp.rt = _st2_resp_allKeys[-1].rt
                        # was this correct?
                        if (st2_resp.keys == str(st2_ans)) or (st2_resp.keys == st2_ans):
                            st2_resp.corr = 1
                        else:
                            st2_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *text* updates
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    text.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in parachuteComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "parachute" ---
            for thisComponent in parachuteComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from para_code_ani
            print('frames',frameN)
            
            # Run 'End Routine' code from para_code
            #if mouse_st.clicked_name == ['para_targ_2']:
            #    st_res = 'k'
            #else : 
            #    st_res = None
            
            mouse_st.time = st_time.getTime()
            mouse_st.time = mouse_st.time-1
            if st_res == st2_ans :
                st_corr = 1
            elif st_res != st2_ans :
                st_corr = 0
            
            print('corr',st_corr)
            
            thisExp.addData('st_ans', st2_ans)
            thisExp.addData('st_res', st_res)
            thisExp.addData('st_corr', st_corr)
            thisExp.addData('st_rt', mouse_st.time)
            thisExp.addData('st_rt2', para_rt)
            # store data for para_main_loop (TrialHandler)
            # check responses
            if st2_resp.keys in ['', [], None]:  # No response was made
                st2_resp.keys = None
                # was no response the correct answer?!
                if str(st2_ans).lower() == 'none':
                   st2_resp.corr = 1;  # correct non-response
                else:
                   st2_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for para_main_loop (TrialHandler)
            para_main_loop.addData('st2_resp.keys',st2_resp.keys)
            para_main_loop.addData('st2_resp.corr', st2_resp.corr)
            if st2_resp.keys != None:  # we had a response
                para_main_loop.addData('st2_resp.rt', st2_resp.rt)
            # the Routine "parachute" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "para_feedback" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from para_feed_code
            message = ""
            feedur = 0
            
            print('rt', mouse_st.time)
            print('st_cor', st_corr)
            if (mouse_st.time > 1.5) and (st_corr == 1) and (st2_ans == 'k'): 
                message = "좀 더 빨리 응답하세요"
                feedur = 1
            elif (mouse_st.time < 0.150):
                message = "고양이를 보고 반응하세요"
                feedur = 3
            elif (mouse_st.time > 1.5) and (st_corr == 0) and (st2_ans == 'k'):
                message = "오답, 좀 더 빨리 응답하세요"
                feedur = 1
            elif (st2_ans == 'k') and (st_corr == 1): 
                message = ""
                feedur = 0.0
            elif (st2_ans != 'k') and (st_corr == 1): 
                message = ""
                feedur = 0.0
            elif (st2_ans == 'k') and (st_corr == 0): 
                message = "오답"
                feedur = 1
            elif (st2_ans != 'k') and (st_corr == 0): 
                message = "오답"
                feedur = 1
            
            
            
            
            para_feed_message.setText(message)
            # keep track of which components have finished
            para_feedbackComponents = [para_f_back, para_feed_message]
            for thisComponent in para_feedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "para_feedback" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *para_f_back* updates
                if para_f_back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    para_f_back.frameNStart = frameN  # exact frame index
                    para_f_back.tStart = t  # local t and not account for scr refresh
                    para_f_back.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(para_f_back, 'tStartRefresh')  # time at next scr refresh
                    para_f_back.setAutoDraw(True)
                if para_f_back.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > para_f_back.tStartRefresh + feedur-frameTolerance:
                        # keep track of stop time/frame for later
                        para_f_back.tStop = t  # not accounting for scr refresh
                        para_f_back.frameNStop = frameN  # exact frame index
                        para_f_back.setAutoDraw(False)
                
                # *para_feed_message* updates
                if para_feed_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    para_feed_message.frameNStart = frameN  # exact frame index
                    para_feed_message.tStart = t  # local t and not account for scr refresh
                    para_feed_message.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(para_feed_message, 'tStartRefresh')  # time at next scr refresh
                    para_feed_message.setAutoDraw(True)
                if para_feed_message.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > para_feed_message.tStartRefresh + feedur-frameTolerance:
                        # keep track of stop time/frame for later
                        para_feed_message.tStop = t  # not accounting for scr refresh
                        para_feed_message.frameNStop = frameN  # exact frame index
                        para_feed_message.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in para_feedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "para_feedback" ---
            for thisComponent in para_feedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "para_feedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed para_main repeats of 'para_main_loop'
        
        thisExp.nextEntry()
        
    # completed para_loop repeats of 'para'
    
    
    # set up handler to look after randomisation of conditions etc
    fish = data.TrialHandler(nReps=fish_loop, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='fish')
    thisExp.addLoop(fish)  # add the loop to the experiment
    thisFish = fish.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFish.rgb)
    if thisFish != None:
        for paramName in thisFish:
            exec('{} = thisFish[paramName]'.format(paramName))
    
    for thisFish in fish:
        currentLoop = fish
        # abbreviate parameter names if possible (e.g. rgb = thisFish.rgb)
        if thisFish != None:
            for paramName in thisFish:
                exec('{} = thisFish[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fis_initialSet" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from fis_CounterBalancing_code
        
        win.fullscr = True
        
        if test_mode == 1:
            win.mouseVisible = True
        else:
            win.mouseVisible = False
        fis_key_resp.keys = []
        fis_key_resp.rt = []
        _fis_key_resp_allKeys = []
        # setup some python lists for storing info about the mouse
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        fis_initialSetComponents = [image, fis_text_2, fis_key_resp, mouse]
        for thisComponent in fis_initialSetComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fis_initialSet" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            
            # *fis_text_2* updates
            if fis_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fis_text_2.frameNStart = frameN  # exact frame index
                fis_text_2.tStart = t  # local t and not account for scr refresh
                fis_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_text_2, 'tStartRefresh')  # time at next scr refresh
                fis_text_2.setAutoDraw(True)
            
            # *fis_key_resp* updates
            waitOnFlip = False
            if fis_key_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                fis_key_resp.frameNStart = frameN  # exact frame index
                fis_key_resp.tStart = t  # local t and not account for scr refresh
                fis_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_key_resp, 'tStartRefresh')  # time at next scr refresh
                fis_key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(fis_key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(fis_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if fis_key_resp.status == STARTED and not waitOnFlip:
                theseKeys = fis_key_resp.getKeys(keyList=['space'], waitRelease=False)
                _fis_key_resp_allKeys.extend(theseKeys)
                if len(_fis_key_resp_allKeys):
                    fis_key_resp.keys = _fis_key_resp_allKeys[-1].name  # just the last key pressed
                    fis_key_resp.rt = _fis_key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        continueRoutine = False  # abort routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fis_initialSetComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fis_initialSet" ---
        for thisComponent in fis_initialSetComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for fish (TrialHandler)
        # the Routine "fis_initialSet" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fis_Instruction" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        fis_movie = visual.MovieStim3(
            win=win, name='fis_movie', units='pix',
            noAudio = False,
            filename=insmov,
            ori=0.0, pos=(0, 0), opacity=None,
            loop=False, anchor='center',
            size=(1920,1080),
            depth=-1.0,
            )
        fis_secret_quit.keys = []
        fis_secret_quit.rt = []
        _fis_secret_quit_allKeys = []
        # setup some python lists for storing info about the mouse_2
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from fis_code_9
        
        fish_trials = 1
        # keep track of which components have finished
        fis_InstructionComponents = [fis_backs, fis_movie, fis_skip_movie, fis_secret_quit, mouse_2]
        for thisComponent in fis_InstructionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fis_Instruction" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fis_backs* updates
            if fis_backs.status == NOT_STARTED and fis_movie.status==FINISHED:
                # keep track of start time/frame for later
                fis_backs.frameNStart = frameN  # exact frame index
                fis_backs.tStart = t  # local t and not account for scr refresh
                fis_backs.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_backs, 'tStartRefresh')  # time at next scr refresh
                fis_backs.setAutoDraw(True)
            
            # *fis_movie* updates
            if fis_movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fis_movie.frameNStart = frameN  # exact frame index
                fis_movie.tStart = t  # local t and not account for scr refresh
                fis_movie.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_movie, 'tStartRefresh')  # time at next scr refresh
                fis_movie.setAutoDraw(True)
            
            # *fis_skip_movie* updates
            if fis_skip_movie.status == NOT_STARTED and fis_movie.status==FINISHED:
                # keep track of start time/frame for later
                fis_skip_movie.frameNStart = frameN  # exact frame index
                fis_skip_movie.tStart = t  # local t and not account for scr refresh
                fis_skip_movie.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_skip_movie, 'tStartRefresh')  # time at next scr refresh
                fis_skip_movie.setAutoDraw(True)
            
            # *fis_secret_quit* updates
            waitOnFlip = False
            if fis_secret_quit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fis_secret_quit.frameNStart = frameN  # exact frame index
                fis_secret_quit.tStart = t  # local t and not account for scr refresh
                fis_secret_quit.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_secret_quit, 'tStartRefresh')  # time at next scr refresh
                fis_secret_quit.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(fis_secret_quit.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(fis_secret_quit.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if fis_secret_quit.status == STARTED and not waitOnFlip:
                theseKeys = fis_secret_quit.getKeys(keyList=['space'], waitRelease=False)
                _fis_secret_quit_allKeys.extend(theseKeys)
                if len(_fis_secret_quit_allKeys):
                    fis_secret_quit.keys = _fis_secret_quit_allKeys[-1].name  # just the last key pressed
                    fis_secret_quit.rt = _fis_secret_quit_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # *mouse_2* updates
            if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_2.frameNStart = frameN  # exact frame index
                mouse_2.tStart = t  # local t and not account for scr refresh
                mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
                mouse_2.status = STARTED
                mouse_2.mouseClock.reset()
                prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
            if mouse_2.status == STARTED:  # only update if started and not finished!
                buttons = mouse_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        continueRoutine = False  # abort routine on response            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fis_InstructionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fis_Instruction" ---
        for thisComponent in fis_InstructionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fis_movie.stop()
        # store data for fish (TrialHandler)
        # the Routine "fis_Instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fis_readycount" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        fis_readycountComponents = [fis_back, fis_start_prac, fis_get_ready]
        for thisComponent in fis_readycountComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fis_readycount" ---
        while continueRoutine and routineTimer.getTime() < 7.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fis_back* updates
            if fis_back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fis_back.frameNStart = frameN  # exact frame index
                fis_back.tStart = t  # local t and not account for scr refresh
                fis_back.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_back, 'tStartRefresh')  # time at next scr refresh
                fis_back.setAutoDraw(True)
            if fis_back.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fis_back.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    fis_back.tStop = t  # not accounting for scr refresh
                    fis_back.frameNStop = frameN  # exact frame index
                    fis_back.setAutoDraw(False)
            
            # *fis_start_prac* updates
            if fis_start_prac.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                fis_start_prac.frameNStart = frameN  # exact frame index
                fis_start_prac.tStart = t  # local t and not account for scr refresh
                fis_start_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_start_prac, 'tStartRefresh')  # time at next scr refresh
                fis_start_prac.setAutoDraw(True)
            if fis_start_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fis_start_prac.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    fis_start_prac.tStop = t  # not accounting for scr refresh
                    fis_start_prac.frameNStop = frameN  # exact frame index
                    fis_start_prac.setAutoDraw(False)
            
            # *fis_get_ready* updates
            if fis_get_ready.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                # keep track of start time/frame for later
                fis_get_ready.frameNStart = frameN  # exact frame index
                fis_get_ready.tStart = t  # local t and not account for scr refresh
                fis_get_ready.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_get_ready, 'tStartRefresh')  # time at next scr refresh
                fis_get_ready.setAutoDraw(True)
            if fis_get_ready.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fis_get_ready.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    fis_get_ready.tStop = t  # not accounting for scr refresh
                    fis_get_ready.frameNStop = frameN  # exact frame index
                    fis_get_ready.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fis_readycountComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fis_readycount" ---
        for thisComponent in fis_readycountComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-7.000000)
        
        # set up handler to look after randomisation of conditions etc
        fis_temp = data.TrialHandler(nReps=fish_practice_reps, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(GOprac),
            seed=None, name='fis_temp')
        thisExp.addLoop(fis_temp)  # add the loop to the experiment
        thisFis_temp = fis_temp.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisFis_temp.rgb)
        if thisFis_temp != None:
            for paramName in thisFis_temp:
                exec('{} = thisFis_temp[paramName]'.format(paramName))
        
        for thisFis_temp in fis_temp:
            currentLoop = fis_temp
            # abbreviate parameter names if possible (e.g. rgb = thisFis_temp.rgb)
            if thisFis_temp != None:
                for paramName in thisFis_temp:
                    exec('{} = thisFis_temp[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "fis_practiral" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            fis_slider_2.reset()
            # Run 'Begin Routine' code from fis_code_2
            fis_slider_2.marker = Fish_2
            fis_slider_2.markerPos = 1.5
            
            print(_thisDir)
            Fish_2.setImage(os.path.join(_thisDir,"fis_artwork", str(FishTypeFile)))
            fis_Words_2.setText(Word)
            # keep track of which components have finished
            fis_practiralComponents = [fis_slider_2, fis_BackGround_2, Fish_2, fis_WordBox_2, fis_Words_2]
            for thisComponent in fis_practiralComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fis_practiral" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fis_slider_2* updates
                if fis_slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fis_slider_2.frameNStart = frameN  # exact frame index
                    fis_slider_2.tStart = t  # local t and not account for scr refresh
                    fis_slider_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fis_slider_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fis_slider_2.started')
                    fis_slider_2.setAutoDraw(True)
                
                # Check fis_slider_2 for response to end routine
                if fis_slider_2.getRating() is not None and fis_slider_2.status == STARTED:
                    continueRoutine = False
                # Run 'Each Frame' code from fis_code_2
                TextPosition_2 = (fis_slider_2.markerPos-1.1)/1.65
                BoxPosition_2 = TextPosition_2 +0.023
                
                # *fis_BackGround_2* updates
                if fis_BackGround_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fis_BackGround_2.frameNStart = frameN  # exact frame index
                    fis_BackGround_2.tStart = t  # local t and not account for scr refresh
                    fis_BackGround_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fis_BackGround_2, 'tStartRefresh')  # time at next scr refresh
                    fis_BackGround_2.setAutoDraw(True)
                
                # *Fish_2* updates
                if Fish_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Fish_2.frameNStart = frameN  # exact frame index
                    Fish_2.tStart = t  # local t and not account for scr refresh
                    Fish_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Fish_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fish_2.started')
                    Fish_2.setAutoDraw(True)
                
                # *fis_WordBox_2* updates
                if fis_WordBox_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fis_WordBox_2.frameNStart = frameN  # exact frame index
                    fis_WordBox_2.tStart = t  # local t and not account for scr refresh
                    fis_WordBox_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fis_WordBox_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fis_WordBox_2.started')
                    fis_WordBox_2.setAutoDraw(True)
                if fis_WordBox_2.status == STARTED:  # only update if drawing
                    fis_WordBox_2.setPos([0, BoxPosition_2], log=False)
                
                # *fis_Words_2* updates
                if fis_Words_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fis_Words_2.frameNStart = frameN  # exact frame index
                    fis_Words_2.tStart = t  # local t and not account for scr refresh
                    fis_Words_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fis_Words_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fis_Words_2.started')
                    fis_Words_2.setAutoDraw(True)
                if fis_Words_2.status == STARTED:  # only update if drawing
                    fis_Words_2.setPos([-0.03,TextPosition_2], log=False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fis_practiralComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fis_practiral" ---
            for thisComponent in fis_practiralComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            fis_temp.addData('fis_slider_2.response', fis_slider_2.getRating())
            fis_temp.addData('fis_slider_2.rt', fis_slider_2.getRT())
            # Run 'End Routine' code from fis_code_2
            if fis_slider_2.getRating() > 1.55: 
                Response_2 = "ScrollUp"
            else:
                if fis_slider_2.getRating() < 1.45:
                    Response_2 = "ScrollDown"
                else:
                    Response_2 = "NoResponse"
                    
            if CorrectResp == Response_2:
                Feedback_2 = '정답'
            else:
                if Response_2 == "NoResponse":
                    Feedback_2 = '무응답'
                else:
                    Feedback_2 = "오답"
                
            fish.addData('Response_2', Response_2)
            fish.addData('Feedback_2', Feedback_2)
            # the Routine "fis_practiral" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "fis_feedback_prac" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            fis_Feedbacks_2.setText(str(Feedback_2))
            # keep track of which components have finished
            fis_feedback_pracComponents = [fis_BackGround_Feedback_2, fis_Feedbacks_2]
            for thisComponent in fis_feedback_pracComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fis_feedback_prac" ---
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fis_BackGround_Feedback_2* updates
                if fis_BackGround_Feedback_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fis_BackGround_Feedback_2.frameNStart = frameN  # exact frame index
                    fis_BackGround_Feedback_2.tStart = t  # local t and not account for scr refresh
                    fis_BackGround_Feedback_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fis_BackGround_Feedback_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fis_BackGround_Feedback_2.started')
                    fis_BackGround_Feedback_2.setAutoDraw(True)
                if fis_BackGround_Feedback_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fis_BackGround_Feedback_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fis_BackGround_Feedback_2.tStop = t  # not accounting for scr refresh
                        fis_BackGround_Feedback_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fis_BackGround_Feedback_2.stopped')
                        fis_BackGround_Feedback_2.setAutoDraw(False)
                
                # *fis_Feedbacks_2* updates
                if fis_Feedbacks_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fis_Feedbacks_2.frameNStart = frameN  # exact frame index
                    fis_Feedbacks_2.tStart = t  # local t and not account for scr refresh
                    fis_Feedbacks_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fis_Feedbacks_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fis_Feedbacks_2.started')
                    fis_Feedbacks_2.setAutoDraw(True)
                if fis_Feedbacks_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fis_Feedbacks_2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        fis_Feedbacks_2.tStop = t  # not accounting for scr refresh
                        fis_Feedbacks_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fis_Feedbacks_2.stopped')
                        fis_Feedbacks_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fis_feedback_pracComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fis_feedback_prac" ---
            for thisComponent in fis_feedback_pracComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed fish_practice_reps repeats of 'fis_temp'
        
        
        # --- Prepare to start Routine "fis_continue_prac" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        fis_Continue_or_not.keys = []
        fis_Continue_or_not.rt = []
        _fis_Continue_or_not_allKeys = []
        # setup some python lists for storing info about the fis_mouse_skip
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        fis_continue_pracComponents = [fis_image_3, fis_Continue_or_not, fis_mouse_skip, fis_next_text]
        for thisComponent in fis_continue_pracComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fis_continue_prac" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fis_image_3* updates
            if fis_image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fis_image_3.frameNStart = frameN  # exact frame index
                fis_image_3.tStart = t  # local t and not account for scr refresh
                fis_image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_image_3, 'tStartRefresh')  # time at next scr refresh
                fis_image_3.setAutoDraw(True)
            
            # *fis_Continue_or_not* updates
            waitOnFlip = False
            if fis_Continue_or_not.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fis_Continue_or_not.frameNStart = frameN  # exact frame index
                fis_Continue_or_not.tStart = t  # local t and not account for scr refresh
                fis_Continue_or_not.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_Continue_or_not, 'tStartRefresh')  # time at next scr refresh
                fis_Continue_or_not.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(fis_Continue_or_not.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(fis_Continue_or_not.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if fis_Continue_or_not.status == STARTED and not waitOnFlip:
                theseKeys = fis_Continue_or_not.getKeys(keyList=['space'], waitRelease=False)
                _fis_Continue_or_not_allKeys.extend(theseKeys)
                if len(_fis_Continue_or_not_allKeys):
                    fis_Continue_or_not.keys = _fis_Continue_or_not_allKeys[-1].name  # just the last key pressed
                    fis_Continue_or_not.rt = _fis_Continue_or_not_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # *fis_mouse_skip* updates
            if fis_mouse_skip.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fis_mouse_skip.frameNStart = frameN  # exact frame index
                fis_mouse_skip.tStart = t  # local t and not account for scr refresh
                fis_mouse_skip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_mouse_skip, 'tStartRefresh')  # time at next scr refresh
                fis_mouse_skip.status = STARTED
                fis_mouse_skip.mouseClock.reset()
                prevButtonState = fis_mouse_skip.getPressed()  # if button is down already this ISN'T a new click
            if fis_mouse_skip.status == STARTED:  # only update if started and not finished!
                buttons = fis_mouse_skip.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        continueRoutine = False  # abort routine on response            
            # *fis_next_text* updates
            if fis_next_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fis_next_text.frameNStart = frameN  # exact frame index
                fis_next_text.tStart = t  # local t and not account for scr refresh
                fis_next_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_next_text, 'tStartRefresh')  # time at next scr refresh
                fis_next_text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fis_continue_pracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fis_continue_prac" ---
        for thisComponent in fis_continue_pracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for fish (TrialHandler)
        # the Routine "fis_continue_prac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fis_readycount" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        fis_readycountComponents = [fis_back, fis_start_prac, fis_get_ready]
        for thisComponent in fis_readycountComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fis_readycount" ---
        while continueRoutine and routineTimer.getTime() < 7.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fis_back* updates
            if fis_back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fis_back.frameNStart = frameN  # exact frame index
                fis_back.tStart = t  # local t and not account for scr refresh
                fis_back.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_back, 'tStartRefresh')  # time at next scr refresh
                fis_back.setAutoDraw(True)
            if fis_back.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fis_back.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    fis_back.tStop = t  # not accounting for scr refresh
                    fis_back.frameNStop = frameN  # exact frame index
                    fis_back.setAutoDraw(False)
            
            # *fis_start_prac* updates
            if fis_start_prac.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                fis_start_prac.frameNStart = frameN  # exact frame index
                fis_start_prac.tStart = t  # local t and not account for scr refresh
                fis_start_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_start_prac, 'tStartRefresh')  # time at next scr refresh
                fis_start_prac.setAutoDraw(True)
            if fis_start_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fis_start_prac.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    fis_start_prac.tStop = t  # not accounting for scr refresh
                    fis_start_prac.frameNStop = frameN  # exact frame index
                    fis_start_prac.setAutoDraw(False)
            
            # *fis_get_ready* updates
            if fis_get_ready.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                # keep track of start time/frame for later
                fis_get_ready.frameNStart = frameN  # exact frame index
                fis_get_ready.tStart = t  # local t and not account for scr refresh
                fis_get_ready.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fis_get_ready, 'tStartRefresh')  # time at next scr refresh
                fis_get_ready.setAutoDraw(True)
            if fis_get_ready.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fis_get_ready.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    fis_get_ready.tStop = t  # not accounting for scr refresh
                    fis_get_ready.frameNStop = frameN  # exact frame index
                    fis_get_ready.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fis_readycountComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fis_readycount" ---
        for thisComponent in fis_readycountComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-7.000000)
        
        # set up handler to look after randomisation of conditions etc
        fis_round = data.TrialHandler(nReps=fis_round_tot, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='fis_round')
        thisExp.addLoop(fis_round)  # add the loop to the experiment
        thisFis_round = fis_round.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisFis_round.rgb)
        if thisFis_round != None:
            for paramName in thisFis_round:
                exec('{} = thisFis_round[paramName]'.format(paramName))
        
        for thisFis_round in fis_round:
            currentLoop = fis_round
            # abbreviate parameter names if possible (e.g. rgb = thisFis_round.rgb)
            if thisFis_round != None:
                for paramName in thisFis_round:
                    exec('{} = thisFis_round[paramName]'.format(paramName))
            
            # set up handler to look after randomisation of conditions etc
            fis_trials = data.TrialHandler(nReps=fish_trials, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions(GOmain),
                seed=None, name='fis_trials')
            thisExp.addLoop(fis_trials)  # add the loop to the experiment
            thisFis_trial = fis_trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisFis_trial.rgb)
            if thisFis_trial != None:
                for paramName in thisFis_trial:
                    exec('{} = thisFis_trial[paramName]'.format(paramName))
            
            for thisFis_trial in fis_trials:
                currentLoop = fis_trials
                # abbreviate parameter names if possible (e.g. rgb = thisFis_trial.rgb)
                if thisFis_trial != None:
                    for paramName in thisFis_trial:
                        exec('{} = thisFis_trial[paramName]'.format(paramName))
                
                # --- Prepare to start Routine "fis_main_trial" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                fis_slider.reset()
                # Run 'Begin Routine' code from fis_code
                fis_slider.marker = Fish
                fis_slider.markerPos = 1.5
                my_text = visual.TextStim(win, text=Word, font='NanumSquare_acB.ttf')
                
                print(_thisDir)
                Fish.setImage(os.path.join(_thisDir,"fis_artwork", str(FishTypeFile)))
                fis_Words.setText(Word)
                # Run 'Begin Routine' code from fis_test_mode
                thisn = fis_trials.thisN
                
                ##########TEST MODE###########
                if test_mode == 1 and thisn == 3:
                    fis_trials.finished=True
                    fis_round.finished=True
                    fish.finished=True
                # keep track of which components have finished
                fis_main_trialComponents = [fis_slider, fis_BackGround, Fish, fis_WordBox, fis_Words]
                for thisComponent in fis_main_trialComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "fis_main_trial" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *fis_slider* updates
                    if fis_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fis_slider.frameNStart = frameN  # exact frame index
                        fis_slider.tStart = t  # local t and not account for scr refresh
                        fis_slider.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fis_slider, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fis_slider.started')
                        fis_slider.setAutoDraw(True)
                    
                    # Check fis_slider for response to end routine
                    if fis_slider.getRating() is not None and fis_slider.status == STARTED:
                        continueRoutine = False
                    # Run 'Each Frame' code from fis_code
                    TextPosition = (fis_slider.markerPos-1.1)/1.65
                    BoxPosition = TextPosition +0.023
                    
                    # *fis_BackGround* updates
                    if fis_BackGround.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fis_BackGround.frameNStart = frameN  # exact frame index
                        fis_BackGround.tStart = t  # local t and not account for scr refresh
                        fis_BackGround.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fis_BackGround, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fis_BackGround.started')
                        fis_BackGround.setAutoDraw(True)
                    
                    # *Fish* updates
                    if Fish.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        Fish.frameNStart = frameN  # exact frame index
                        Fish.tStart = t  # local t and not account for scr refresh
                        Fish.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Fish, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Fish.started')
                        Fish.setAutoDraw(True)
                    
                    # *fis_WordBox* updates
                    if fis_WordBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fis_WordBox.frameNStart = frameN  # exact frame index
                        fis_WordBox.tStart = t  # local t and not account for scr refresh
                        fis_WordBox.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fis_WordBox, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fis_WordBox.started')
                        fis_WordBox.setAutoDraw(True)
                    if fis_WordBox.status == STARTED:  # only update if drawing
                        fis_WordBox.setPos([0, BoxPosition], log=False)
                    
                    # *fis_Words* updates
                    if fis_Words.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fis_Words.frameNStart = frameN  # exact frame index
                        fis_Words.tStart = t  # local t and not account for scr refresh
                        fis_Words.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fis_Words, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fis_Words.started')
                        fis_Words.setAutoDraw(True)
                    if fis_Words.status == STARTED:  # only update if drawing
                        fis_Words.setPos([-0.03,TextPosition], log=False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in fis_main_trialComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "fis_main_trial" ---
                for thisComponent in fis_main_trialComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                fis_trials.addData('fis_slider.response', fis_slider.getRating())
                fis_trials.addData('fis_slider.rt', fis_slider.getRT())
                # Run 'End Routine' code from fis_code
                if fis_slider.getRating() > 1.55: 
                    Response = "ScrollUp"
                else:
                    if fis_slider.getRating() < 1.45:
                        Response = "ScrollDown"
                    else:
                        Response = "NoResponse"
                        
                if CorrectResp == Response:
                    Feedback = '정답'
                else:
                    if Response == "NoResponse":
                        Feedback = '무응답'
                    else:
                        Feedback = "오답"
                    
                fis_temp.addData('Response', Response)
                fis_temp.addData('Feedback', Feedback)
                # the Routine "fis_main_trial" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "fis_feedback_trial" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                fis_Feedbacks.setText(str(Feedback))
                # keep track of which components have finished
                fis_feedback_trialComponents = [fis_BackGround_Feedback, fis_Feedbacks]
                for thisComponent in fis_feedback_trialComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "fis_feedback_trial" ---
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *fis_BackGround_Feedback* updates
                    if fis_BackGround_Feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fis_BackGround_Feedback.frameNStart = frameN  # exact frame index
                        fis_BackGround_Feedback.tStart = t  # local t and not account for scr refresh
                        fis_BackGround_Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fis_BackGround_Feedback, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fis_BackGround_Feedback.started')
                        fis_BackGround_Feedback.setAutoDraw(True)
                    if fis_BackGround_Feedback.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fis_BackGround_Feedback.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            fis_BackGround_Feedback.tStop = t  # not accounting for scr refresh
                            fis_BackGround_Feedback.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fis_BackGround_Feedback.stopped')
                            fis_BackGround_Feedback.setAutoDraw(False)
                    
                    # *fis_Feedbacks* updates
                    if fis_Feedbacks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fis_Feedbacks.frameNStart = frameN  # exact frame index
                        fis_Feedbacks.tStart = t  # local t and not account for scr refresh
                        fis_Feedbacks.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fis_Feedbacks, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fis_Feedbacks.started')
                        fis_Feedbacks.setAutoDraw(True)
                    if fis_Feedbacks.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fis_Feedbacks.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            fis_Feedbacks.tStop = t  # not accounting for scr refresh
                            fis_Feedbacks.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fis_Feedbacks.stopped')
                            fis_Feedbacks.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in fis_feedback_trialComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "fis_feedback_trial" ---
                for thisComponent in fis_feedback_trialComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
            # completed fish_trials repeats of 'fis_trials'
            
            
            # --- Prepare to start Routine "fis_main_control" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from fis_code_4
            
            if fis_roundN == 3:
                fis_mainbreak = 0
            else:
                fis_mainbreak = 1
                
                
            fis_roundN = fis_roundN + 1
            fis_round.addData('fis_roundN', fis_roundN)
            
            
            
            if GOloop == Gnum:
                if fis_roundN == 2: 
                    GOmain = 'loop/[통합실험]ExpListGreen_Round2.xlsx'
                elif fis_roundN == 3:
                    GOmain = 'loop/[통합실험]ExpListGreen_Round3.xlsx'
                elif fis_roundN == 4:
                    GOmain = 'loop/[통합실험]ExpListGreen_Round4.xlsx'
                elif fis_roundN == 5:
                    GOmain = 'loop/[통합실험]ExpListGreen_Round5.xlsx'
            elif GOloop == Onum:
                if fis_roundN == 2: 
                    GOmain = 'loop/[통합실험]ExpListOrange_Round2.xlsx'
                elif fis_roundN == 3:
                    GOmain = 'loop/[통합실험]ExpListOrange_Round3.xlsx'
                elif fis_roundN == 4:
                    GOmain = 'loop/[통합실험]ExpListOrange_Round4.xlsx'
                elif fis_roundN == 5:
                    GOmain = 'loop/[통합실험]ExpListOrange_Round5.xlsx'
            
            if test_mode == 1:
                fis_mainbreak = 0
                #fis_round.finished=True
                #fish.finished=True
                #fish_loop = 0
            
            
            # keep track of which components have finished
            fis_main_controlComponents = []
            for thisComponent in fis_main_controlComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fis_main_control" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fis_main_controlComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fis_main_control" ---
            for thisComponent in fis_main_controlComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "fis_main_control" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            fis_main_break = data.TrialHandler(nReps=fis_mainbreak, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='fis_main_break')
            thisExp.addLoop(fis_main_break)  # add the loop to the experiment
            thisFis_main_break = fis_main_break.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisFis_main_break.rgb)
            if thisFis_main_break != None:
                for paramName in thisFis_main_break:
                    exec('{} = thisFis_main_break[paramName]'.format(paramName))
            
            for thisFis_main_break in fis_main_break:
                currentLoop = fis_main_break
                # abbreviate parameter names if possible (e.g. rgb = thisFis_main_break.rgb)
                if thisFis_main_break != None:
                    for paramName in thisFis_main_break:
                        exec('{} = thisFis_main_break[paramName]'.format(paramName))
                
                # --- Prepare to start Routine "fis_rout_break" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                # keep track of which components have finished
                fis_rout_breakComponents = [fis_break_interval, fis_text]
                for thisComponent in fis_rout_breakComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "fis_rout_break" ---
                while continueRoutine and routineTimer.getTime() < 30.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *fis_break_interval* updates
                    if fis_break_interval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fis_break_interval.frameNStart = frameN  # exact frame index
                        fis_break_interval.tStart = t  # local t and not account for scr refresh
                        fis_break_interval.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fis_break_interval, 'tStartRefresh')  # time at next scr refresh
                        fis_break_interval.setAutoDraw(True)
                    if fis_break_interval.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fis_break_interval.tStartRefresh + 30.0-frameTolerance:
                            # keep track of stop time/frame for later
                            fis_break_interval.tStop = t  # not accounting for scr refresh
                            fis_break_interval.frameNStop = frameN  # exact frame index
                            fis_break_interval.setAutoDraw(False)
                    
                    # *fis_text* updates
                    if fis_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fis_text.frameNStart = frameN  # exact frame index
                        fis_text.tStart = t  # local t and not account for scr refresh
                        fis_text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fis_text, 'tStartRefresh')  # time at next scr refresh
                        fis_text.setAutoDraw(True)
                    if fis_text.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fis_text.tStartRefresh + 30.0-frameTolerance:
                            # keep track of stop time/frame for later
                            fis_text.tStop = t  # not accounting for scr refresh
                            fis_text.frameNStop = frameN  # exact frame index
                            fis_text.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in fis_rout_breakComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "fis_rout_break" ---
                for thisComponent in fis_rout_breakComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-30.000000)
                
                # --- Prepare to start Routine "fis_interblock" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                # setup some python lists for storing info about the fis_mouse
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                fis_interblockComponents = [fis_mouse, fis_stratnextround, fis_stt_round]
                for thisComponent in fis_interblockComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "fis_interblock" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # *fis_mouse* updates
                    if fis_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fis_mouse.frameNStart = frameN  # exact frame index
                        fis_mouse.tStart = t  # local t and not account for scr refresh
                        fis_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fis_mouse, 'tStartRefresh')  # time at next scr refresh
                        fis_mouse.status = STARTED
                        fis_mouse.mouseClock.reset()
                        prevButtonState = fis_mouse.getPressed()  # if button is down already this ISN'T a new click
                    if fis_mouse.status == STARTED:  # only update if started and not finished!
                        buttons = fis_mouse.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                continueRoutine = False  # abort routine on response                    
                    # *fis_stratnextround* updates
                    if fis_stratnextround.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fis_stratnextround.frameNStart = frameN  # exact frame index
                        fis_stratnextround.tStart = t  # local t and not account for scr refresh
                        fis_stratnextround.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fis_stratnextround, 'tStartRefresh')  # time at next scr refresh
                        fis_stratnextround.setAutoDraw(True)
                    
                    # *fis_stt_round* updates
                    if fis_stt_round.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fis_stt_round.frameNStart = frameN  # exact frame index
                        fis_stt_round.tStart = t  # local t and not account for scr refresh
                        fis_stt_round.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fis_stt_round, 'tStartRefresh')  # time at next scr refresh
                        fis_stt_round.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in fis_interblockComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "fis_interblock" ---
                for thisComponent in fis_interblockComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store data for fis_main_break (TrialHandler)
                # the Routine "fis_interblock" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "fis_readycount" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                # keep track of which components have finished
                fis_readycountComponents = [fis_back, fis_start_prac, fis_get_ready]
                for thisComponent in fis_readycountComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "fis_readycount" ---
                while continueRoutine and routineTimer.getTime() < 7.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *fis_back* updates
                    if fis_back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fis_back.frameNStart = frameN  # exact frame index
                        fis_back.tStart = t  # local t and not account for scr refresh
                        fis_back.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fis_back, 'tStartRefresh')  # time at next scr refresh
                        fis_back.setAutoDraw(True)
                    if fis_back.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fis_back.tStartRefresh + 7-frameTolerance:
                            # keep track of stop time/frame for later
                            fis_back.tStop = t  # not accounting for scr refresh
                            fis_back.frameNStop = frameN  # exact frame index
                            fis_back.setAutoDraw(False)
                    
                    # *fis_start_prac* updates
                    if fis_start_prac.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                        # keep track of start time/frame for later
                        fis_start_prac.frameNStart = frameN  # exact frame index
                        fis_start_prac.tStart = t  # local t and not account for scr refresh
                        fis_start_prac.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fis_start_prac, 'tStartRefresh')  # time at next scr refresh
                        fis_start_prac.setAutoDraw(True)
                    if fis_start_prac.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fis_start_prac.tStartRefresh + 2-frameTolerance:
                            # keep track of stop time/frame for later
                            fis_start_prac.tStop = t  # not accounting for scr refresh
                            fis_start_prac.frameNStop = frameN  # exact frame index
                            fis_start_prac.setAutoDraw(False)
                    
                    # *fis_get_ready* updates
                    if fis_get_ready.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                        # keep track of start time/frame for later
                        fis_get_ready.frameNStart = frameN  # exact frame index
                        fis_get_ready.tStart = t  # local t and not account for scr refresh
                        fis_get_ready.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fis_get_ready, 'tStartRefresh')  # time at next scr refresh
                        fis_get_ready.setAutoDraw(True)
                    if fis_get_ready.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fis_get_ready.tStartRefresh + 2-frameTolerance:
                            # keep track of stop time/frame for later
                            fis_get_ready.tStop = t  # not accounting for scr refresh
                            fis_get_ready.frameNStop = frameN  # exact frame index
                            fis_get_ready.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in fis_readycountComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "fis_readycount" ---
                for thisComponent in fis_readycountComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-7.000000)
                thisExp.nextEntry()
                
            # completed fis_mainbreak repeats of 'fis_main_break'
            
            thisExp.nextEntry()
            
        # completed fis_round_tot repeats of 'fis_round'
        
        thisExp.nextEntry()
        
    # completed fish_loop repeats of 'fish'
    
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'total_experiment'


# --- Prepare to start Routine "total_end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
total_endComponents = [end_back, total_end_text]
for thisComponent in total_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "total_end" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_back* updates
    if end_back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_back.frameNStart = frameN  # exact frame index
        end_back.tStart = t  # local t and not account for scr refresh
        end_back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_back, 'tStartRefresh')  # time at next scr refresh
        end_back.setAutoDraw(True)
    if end_back.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_back.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            end_back.tStop = t  # not accounting for scr refresh
            end_back.frameNStop = frameN  # exact frame index
            end_back.setAutoDraw(False)
    
    # *total_end_text* updates
    if total_end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        total_end_text.frameNStart = frameN  # exact frame index
        total_end_text.tStart = t  # local t and not account for scr refresh
        total_end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(total_end_text, 'tStartRefresh')  # time at next scr refresh
        total_end_text.setAutoDraw(True)
    if total_end_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > total_end_text.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            total_end_text.tStop = t  # not accounting for scr refresh
            total_end_text.frameNStop = frameN  # exact frame index
            total_end_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in total_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "total_end" ---
for thisComponent in total_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
