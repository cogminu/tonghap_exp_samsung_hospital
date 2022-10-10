#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on 10월 09, 2022, at 23:05
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
    originPath='C:\\Users\\cogmi\\내 드라이브\\dtx_SMC_ver\\dtx_exp_trial_control_weather_test.py',
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
    monitor='testMonitor', color=[0.0039, 0.0039, 0.0039], colorSpace='rgb',
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
stimulus_interval = 5 #original 30
# 전환시간 2초
transition_duration = 2


# Run 'Begin Experiment' code from total_code_2

tot_order = int(expInfo['id*'])%6 + 1

if tot_order == 1:
    exp_order1 = [1,0,0]
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
# Run 'Begin Experiment' code from trial_numbers

# you can change trial numbers for test

# weather
wth_repeat_prac_n = 99 # default 99 
wth_trials_n = 4; # 마음날씨 시행반복횟수, 기본 4회 (삼성병원실험)

# flanker (boat)
fprac = 2 #default 2
fmain = 8 #default 15 trial control 8

# parachute
para_prac = 2 #default 2 (practice loop)
para_main = 1 #default 1 (main loop)

# fish 
fis_round_tot = 3; # default 5 trial control 3


# --- Initialize components for Routine "general_instruction" ---
wth_inst_image = visual.ImageStim(
    win=win,
    name='wth_inst_image', units='pix', 
    image='fis_artwork/general_instruction.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[1920, 1080],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
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
wth_inst_text = visual.TextStim(win=win, name='wth_inst_text',
    text='스페이스로 넘어가세요',
    font='Noto Sans KR',
    pos=(0, -.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
wth_shadow_skip = keyboard.Keyboard()

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
    text='단어연상 연습이 시작됩니다.',
    font='Noto Sans KR',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

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
    font='Noto Sans KR',
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
    font='Noto Sans KR',
    pos=(0, 0.25), height=0.07, wrapWidth=None, ori=0.0, 
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
    font='Noto Sans KR',
    pos=(0, 0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
wth_valence_rating_2 = visual.Slider(win=win, name='wth_valence_rating_2',
    startValue=None, size=(0.45, 0.05), pos=(-0.5, -.1), units=None,
    labels=("부정", "중립", "긍정"), ticks=(-1, 0, 1), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='red', lineColor='black', colorSpace='rgb',
    font='Noto Sans KR', labelHeight=0.03,
    flip=False, ori=0.0, depth=-2, readOnly=False)
wth_valence_txt_2 = visual.TextStim(win=win, name='wth_valence_txt_2',
    text='단어에서 느껴지는 감정',
    font='Noto Sans KR',
    pos=(-.5, -0.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
wth_self_txt_2 = visual.TextStim(win=win, name='wth_self_txt_2',
    text='단어가 자신과 관련이 있는 정도',
    font='Noto Sans KR',
    pos=(0.5, -.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
wth_self_rating_2 = visual.Slider(win=win, name='wth_self_rating_2',
    startValue=None, size=(.45, 0.05), pos=(0.5, -.1), units=None,
    labels=("전혀 나와 관련 없음","나와 관련 매우 많음"), ticks=(0, 1), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='red', lineColor='black', colorSpace='rgb',
    font='Noto Sans KR', labelHeight=0.03,
    flip=False, ori=0.0, depth=-5, readOnly=False)
wth_rating_end_2 = visual.TextBox2(
     win, text='클릭해 주세요', font='Noto Sans KR',
     pos=(-.02, -.42),     letterHeight=0.03,
     size=(0.19, 0.05), borderWidth=2.0,
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
    font='Noto Sans KR',
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
    font='Noto Sans KR',
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
    font='Noto Sans KR',
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
    font='Noto Sans KR',
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
    font='Noto Sans KR',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
wth_valence_rating = visual.Slider(win=win, name='wth_valence_rating',
    startValue=None, size=(0.45, 0.05), pos=(-0.5, -.1), units=None,
    labels=("부정", "중립", "긍정"), ticks=(-1, 0, 1), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='red', lineColor='black', colorSpace='rgb',
    font='Noto Sans KR', labelHeight=0.03,
    flip=False, ori=0.0, depth=-2, readOnly=False)
wth_valence_txt = visual.TextStim(win=win, name='wth_valence_txt',
    text='단어에서 느껴지는 감정',
    font='Noto Sans KR',
    pos=(-.5, -0.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
wth_self_txt = visual.TextStim(win=win, name='wth_self_txt',
    text='단어가 자신과 관련이 있는 정도',
    font='Noto Sans KR',
    pos=(0.5, -.02), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
wth_self_rating = visual.Slider(win=win, name='wth_self_rating',
    startValue=None, size=(.45, 0.05), pos=(0.5, -.1), units=None,
    labels=("전혀 나와 관련 없음","나와 관련 매우 많음"), ticks=(0, 1), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='red', lineColor='black', colorSpace='rgb',
    font='Noto Sans KR', labelHeight=0.03,
    flip=False, ori=0.0, depth=-5, readOnly=False)
wth_rating_end = visual.TextBox2(
     win, text='클릭해 주세요', font='Noto Sans KR',
     pos=(-.02, -.42),     letterHeight=0.03,
     size=(0.19, 0.05), borderWidth=2.0,
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
    font='Noto Sans KR',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
exp_end_key = keyboard.Keyboard()

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
weather = data.TrialHandler(nReps=1.0, method='random', 
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
    wth_shadow_skip.keys = []
    wth_shadow_skip.rt = []
    _wth_shadow_skip_allKeys = []
    # keep track of which components have finished
    wth_instComponents = [wth_movie, wth_inst_text, wth_shadow_skip]
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
        
        # *wth_inst_text* updates
        if wth_inst_text.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            wth_inst_text.frameNStart = frameN  # exact frame index
            wth_inst_text.tStart = t  # local t and not account for scr refresh
            wth_inst_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wth_inst_text, 'tStartRefresh')  # time at next scr refresh
            wth_inst_text.setAutoDraw(True)
        
        # *wth_shadow_skip* updates
        waitOnFlip = False
        if wth_shadow_skip.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            wth_shadow_skip.frameNStart = frameN  # exact frame index
            wth_shadow_skip.tStart = t  # local t and not account for scr refresh
            wth_shadow_skip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wth_shadow_skip, 'tStartRefresh')  # time at next scr refresh
            wth_shadow_skip.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(wth_shadow_skip.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(wth_shadow_skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if wth_shadow_skip.status == STARTED and not waitOnFlip:
            theseKeys = wth_shadow_skip.getKeys(keyList=['space'], waitRelease=False)
            _wth_shadow_skip_allKeys.extend(theseKeys)
            if len(_wth_shadow_skip_allKeys):
                wth_shadow_skip.keys = _wth_shadow_skip_allKeys[-1].name  # just the last key pressed
                wth_shadow_skip.rt = _wth_shadow_skip_allKeys[-1].rt
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
        # keep track of which components have finished
        wth_begin_pracComponents = [wth_background_inst, wth_text]
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
            if wth_background_inst.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wth_background_inst.tStartRefresh + transition_duration+3-frameTolerance:
                    # keep track of stop time/frame for later
                    wth_background_inst.tStop = t  # not accounting for scr refresh
                    wth_background_inst.frameNStop = frameN  # exact frame index
                    wth_background_inst.setAutoDraw(False)
            
            # *wth_text* updates
            if wth_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                wth_text.frameNStart = frameN  # exact frame index
                wth_text.tStart = t  # local t and not account for scr refresh
                wth_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wth_text, 'tStartRefresh')  # time at next scr refresh
                wth_text.setAutoDraw(True)
            if wth_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wth_text.tStartRefresh + transition_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    wth_text.tStop = t  # not accounting for scr refresh
                    wth_text.frameNStop = frameN  # exact frame index
                    wth_text.setAutoDraw(False)
            
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
        # Run 'End Routine' code from wth_code_2
        thisExp.addData('stimulus_interval', stimulus_interval)
        
        # the Routine "wth_think" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "wth_word" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        wth_word_instr.setFont('Noto Sans KR')
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
# completed 1.0 repeats of 'weather'


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
