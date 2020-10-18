#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on September 12, 2019, at 14:56
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'Dual Task VK no blocks'  # from the Builder filename that created this script
expInfo = {'participant': '1', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Jordan\\Documents\\Experiment Building\\2. Dual Processing Task\\Dual Task VK no blocks_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='Built_In_Display', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
next_text = visual.TextStim(win=win, name='next_text',
    text='default text',
    font='Arial',
    pos=(0, -.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "sound_3"
sound_3Clock = core.Clock()
stim = sound.Sound('A', secs=1.0, stereo=True)
stim.setVolume(1)
sound_prompt = visual.TextStim(win=win, name='sound_prompt',
    text='Respond as quickly as possible.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "record"
recordClock = core.Clock()
prompt = visual.TextStim(win=win, name='prompt',
    text='Respond as quickly as possible.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# The import and pyo_init should always come early on:
import psychopy.voicekey as vk
vk.pyo_init(rate=44100, buffersize=256)

# What signaler class to use? Here just the demo signaler:
from psychopy.voicekey.demo_vks import DemoVoiceKeySignal as Signaler

# To use a LabJack as a signaling device:
#from voicekey.signal.labjack_vks import LabJackU3VoiceKeySignal as Signaler

# Initialize components for Routine "instr"
instrClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
next_text = visual.TextStim(win=win, name='next_text',
    text='default text',
    font='Arial',
    pos=(0, -.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "block_2"
block_2Clock = core.Clock()
B2_text = visual.TextStim(win=win, name='B2_text',
    text='Respond as quickly as possible.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instr"
instrClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
next_text = visual.TextStim(win=win, name='next_text',
    text='default text',
    font='Arial',
    pos=(0, -.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "record"
recordClock = core.Clock()
prompt = visual.TextStim(win=win, name='prompt',
    text='Respond as quickly as possible.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# The import and pyo_init should always come early on:
import psychopy.voicekey as vk
vk.pyo_init(rate=44100, buffersize=256)

# What signaler class to use? Here just the demo signaler:
from psychopy.voicekey.demo_vks import DemoVoiceKeySignal as Signaler

# To use a LabJack as a signaling device:
#from voicekey.signal.labjack_vks import LabJackU3VoiceKeySignal as Signaler

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thx_txt = visual.TextStim(win=win, name='thx_txt',
    text='Good work!\n\nYou have completed this task.\n\nPress SPACE to exit.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instructions = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('DPT_instr1.xlsx'),
    seed=None, name='instructions')
thisExp.addLoop(instructions)  # add the loop to the experiment
thisInstruction = instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
if thisInstruction != None:
    for paramName in thisInstruction:
        exec('{} = thisInstruction[paramName]'.format(paramName))

for thisInstruction in instructions:
    currentLoop = instructions
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
    if thisInstruction != None:
        for paramName in thisInstruction:
            exec('{} = thisInstruction[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr"-------
    t = 0
    instrClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    instructions_text.setText(instr_text)
    key_resp = keyboard.Keyboard()
    next_text.setText(cont_text)
    # keep track of which components have finished
    instrComponents = [instructions_text, key_resp, next_text]
    for thisComponent in instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instr"-------
    while continueRoutine:
        # get current time
        t = instrClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_text* updates
        if t >= 0.0 and instructions_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions_text.tStart = t  # not accounting for scr refresh
            instructions_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
            instructions_text.setAutoDraw(True)
        
        # *key_resp* updates
        if t >= 0.0 and key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp.tStart = t  # not accounting for scr refresh
            key_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *next_text* updates
        if t >= 0 and next_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            next_text.tStart = t  # not accounting for scr refresh
            next_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(next_text, 'tStartRefresh')  # time at next scr refresh
            next_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr"-------
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'instructions'


# set up handler to look after randomisation of conditions etc
B1_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('DPT_B1.xlsx'),
    seed=None, name='B1_trials')
thisExp.addLoop(B1_trials)  # add the loop to the experiment
thisB1_trial = B1_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisB1_trial.rgb)
if thisB1_trial != None:
    for paramName in thisB1_trial:
        exec('{} = thisB1_trial[paramName]'.format(paramName))

for thisB1_trial in B1_trials:
    currentLoop = B1_trials
    # abbreviate parameter names if possible (e.g. rgb = thisB1_trial.rgb)
    if thisB1_trial != None:
        for paramName in thisB1_trial:
            exec('{} = thisB1_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "sound_3"-------
    t = 0
    sound_3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    stim.setSound(SoundFile, secs=1.0)
    stim.setVolume(1, log=False)
    # keep track of which components have finished
    sound_3Components = [stim, sound_prompt]
    for thisComponent in sound_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "sound_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = sound_3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop stim
        if t >= 0.0 and stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim.tStart = t  # not accounting for scr refresh
            stim.frameNStart = frameN  # exact frame index
            win.timeOnFlip(stim, 'tStartRefresh')  # time at next scr refresh
            win.callOnFlip(stim.play)  # screen flip
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if stim.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            stim.tStop = t  # not accounting for scr refresh
            stim.frameNStop = frameN  # exact frame index
            win.timeOnFlip(stim, 'tStopRefresh')  # time at next scr refresh
            if 1.0 > 0.5:  # don't force-stop brief sounds
                stim.stop()
        
        # *sound_prompt* updates
        if t >= 0.0 and sound_prompt.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_prompt.tStart = t  # not accounting for scr refresh
            sound_prompt.frameNStart = frameN  # exact frame index
            win.timeOnFlip(sound_prompt, 'tStartRefresh')  # time at next scr refresh
            sound_prompt.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if sound_prompt.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            sound_prompt.tStop = t  # not accounting for scr refresh
            sound_prompt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_prompt, 'tStopRefresh')  # time at next scr refresh
            sound_prompt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sound_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sound_3"-------
    for thisComponent in sound_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stim.stop()  # ensure sound has stopped at end of routine
    B1_trials.addData('sound_prompt.started', sound_prompt.tStartRefresh)
    B1_trials.addData('sound_prompt.stopped', sound_prompt.tStopRefresh)
    
    # ------Prepare to start Routine "record"-------
    t = 0
    recordClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # Create a voice-key to be used:
    vpvk = vk.OnsetVoiceKey(
        sec=2, 
        file_out='data/trial_'+str(B1_trials.thisN).zfill(3)+'_'+Stim+'.wav')
    
    # Start it recording (and detecting):
      # non-blocking; don't block when using Builder
    vpvk.start()
    # keep track of which components have finished
    recordComponents = [prompt]
    for thisComponent in recordComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "record"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = recordClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prompt* updates
        if t >= 0.0 and prompt.status == NOT_STARTED:
            # keep track of start time/frame for later
            prompt.tStart = t  # not accounting for scr refresh
            prompt.frameNStart = frameN  # exact frame index
            win.timeOnFlip(prompt, 'tStartRefresh')  # time at next scr refresh
            prompt.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if prompt.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            prompt.tStop = t  # not accounting for scr refresh
            prompt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(prompt, 'tStopRefresh')  # time at next scr refresh
            prompt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recordComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "record"-------
    for thisComponent in recordComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    B1_trials.addData('prompt.started', prompt.tStartRefresh)
    B1_trials.addData('prompt.stopped', prompt.tStopRefresh)
    # The recorded sound is saved upon .stop() by default. But
    # its a good idea to call .stop() explicitly, eg, if there's much slippage:
    
    vpvk.stop()
    
    # Add the detected time into the PsychoPy data file:
    thisExp.addData('vocal_RT', round(vpvk.event_onset, 3))
    thisExp.addData('bad_baseline', vpvk.bad_baseline)
    thisExp.addData('filename', vpvk.filename)
    thisExp.nextEntry()
    thisExp.nextEntry()
    
# completed 1 repeats of 'B1_trials'


# set up handler to look after randomisation of conditions etc
B2_instr = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('DPT_instr2.xlsx'),
    seed=None, name='B2_instr')
thisExp.addLoop(B2_instr)  # add the loop to the experiment
thisB2_instr = B2_instr.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisB2_instr.rgb)
if thisB2_instr != None:
    for paramName in thisB2_instr:
        exec('{} = thisB2_instr[paramName]'.format(paramName))

for thisB2_instr in B2_instr:
    currentLoop = B2_instr
    # abbreviate parameter names if possible (e.g. rgb = thisB2_instr.rgb)
    if thisB2_instr != None:
        for paramName in thisB2_instr:
            exec('{} = thisB2_instr[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr"-------
    t = 0
    instrClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    instructions_text.setText(instr_text)
    key_resp = keyboard.Keyboard()
    next_text.setText(cont_text)
    # keep track of which components have finished
    instrComponents = [instructions_text, key_resp, next_text]
    for thisComponent in instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instr"-------
    while continueRoutine:
        # get current time
        t = instrClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_text* updates
        if t >= 0.0 and instructions_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions_text.tStart = t  # not accounting for scr refresh
            instructions_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
            instructions_text.setAutoDraw(True)
        
        # *key_resp* updates
        if t >= 0.0 and key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp.tStart = t  # not accounting for scr refresh
            key_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *next_text* updates
        if t >= 0 and next_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            next_text.tStart = t  # not accounting for scr refresh
            next_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(next_text, 'tStartRefresh')  # time at next scr refresh
            next_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr"-------
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'B2_instr'


# ------Prepare to start Routine "block_2"-------
t = 0
block_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
block_2Components = [B2_text]
for thisComponent in block_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "block_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = block_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *B2_text* updates
    if t >= 0.0 and B2_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        B2_text.tStart = t  # not accounting for scr refresh
        B2_text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(B2_text, 'tStartRefresh')  # time at next scr refresh
        B2_text.setAutoDraw(True)
    frameRemains = 10.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if B2_text.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        B2_text.tStop = t  # not accounting for scr refresh
        B2_text.frameNStop = frameN  # exact frame index
        win.timeOnFlip(B2_text, 'tStopRefresh')  # time at next scr refresh
        B2_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "block_2"-------
for thisComponent in block_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
B3_instr = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('DPT_instr3.xlsx'),
    seed=None, name='B3_instr')
thisExp.addLoop(B3_instr)  # add the loop to the experiment
thisB3_instr = B3_instr.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisB3_instr.rgb)
if thisB3_instr != None:
    for paramName in thisB3_instr:
        exec('{} = thisB3_instr[paramName]'.format(paramName))

for thisB3_instr in B3_instr:
    currentLoop = B3_instr
    # abbreviate parameter names if possible (e.g. rgb = thisB3_instr.rgb)
    if thisB3_instr != None:
        for paramName in thisB3_instr:
            exec('{} = thisB3_instr[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr"-------
    t = 0
    instrClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    instructions_text.setText(instr_text)
    key_resp = keyboard.Keyboard()
    next_text.setText(cont_text)
    # keep track of which components have finished
    instrComponents = [instructions_text, key_resp, next_text]
    for thisComponent in instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instr"-------
    while continueRoutine:
        # get current time
        t = instrClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_text* updates
        if t >= 0.0 and instructions_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions_text.tStart = t  # not accounting for scr refresh
            instructions_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
            instructions_text.setAutoDraw(True)
        
        # *key_resp* updates
        if t >= 0.0 and key_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp.tStart = t  # not accounting for scr refresh
            key_resp.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *next_text* updates
        if t >= 0 and next_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            next_text.tStart = t  # not accounting for scr refresh
            next_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(next_text, 'tStartRefresh')  # time at next scr refresh
            next_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr"-------
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'B3_instr'


# set up handler to look after randomisation of conditions etc
B3_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('DPT_B3.xlsx'),
    seed=None, name='B3_trials')
thisExp.addLoop(B3_trials)  # add the loop to the experiment
thisB3_trial = B3_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisB3_trial.rgb)
if thisB3_trial != None:
    for paramName in thisB3_trial:
        exec('{} = thisB3_trial[paramName]'.format(paramName))

for thisB3_trial in B3_trials:
    currentLoop = B3_trials
    # abbreviate parameter names if possible (e.g. rgb = thisB3_trial.rgb)
    if thisB3_trial != None:
        for paramName in thisB3_trial:
            exec('{} = thisB3_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "record"-------
    t = 0
    recordClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # Create a voice-key to be used:
    vpvk = vk.OnsetVoiceKey(
        sec=2, 
        file_out='data/trial_'+str(B1_trials.thisN).zfill(3)+'_'+Stim+'.wav')
    
    # Start it recording (and detecting):
      # non-blocking; don't block when using Builder
    vpvk.start()
    # keep track of which components have finished
    recordComponents = [prompt]
    for thisComponent in recordComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "record"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = recordClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prompt* updates
        if t >= 0.0 and prompt.status == NOT_STARTED:
            # keep track of start time/frame for later
            prompt.tStart = t  # not accounting for scr refresh
            prompt.frameNStart = frameN  # exact frame index
            win.timeOnFlip(prompt, 'tStartRefresh')  # time at next scr refresh
            prompt.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if prompt.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            prompt.tStop = t  # not accounting for scr refresh
            prompt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(prompt, 'tStopRefresh')  # time at next scr refresh
            prompt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recordComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "record"-------
    for thisComponent in recordComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    B3_trials.addData('prompt.started', prompt.tStartRefresh)
    B3_trials.addData('prompt.stopped', prompt.tStopRefresh)
    # The recorded sound is saved upon .stop() by default. But
    # its a good idea to call .stop() explicitly, eg, if there's much slippage:
    
    vpvk.stop()
    
    # Add the detected time into the PsychoPy data file:
    thisExp.addData('vocal_RT', round(vpvk.event_onset, 3))
    thisExp.addData('bad_baseline', vpvk.bad_baseline)
    thisExp.addData('filename', vpvk.filename)
    thisExp.nextEntry()
    thisExp.nextEntry()
    
# completed 1 repeats of 'B3_trials'


# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
thx_key = keyboard.Keyboard()
# keep track of which components have finished
thanksComponents = [thx_txt, thx_key]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thx_txt* updates
    if t >= 0.0 and thx_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        thx_txt.tStart = t  # not accounting for scr refresh
        thx_txt.frameNStart = frameN  # exact frame index
        win.timeOnFlip(thx_txt, 'tStartRefresh')  # time at next scr refresh
        thx_txt.setAutoDraw(True)
    
    # *thx_key* updates
    if t >= 0.0 and thx_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        thx_key.tStart = t  # not accounting for scr refresh
        thx_key.frameNStart = frameN  # exact frame index
        win.timeOnFlip(thx_key, 'tStartRefresh')  # time at next scr refresh
        thx_key.status = STARTED
        # keyboard checking is just starting
        thx_key.clearEvents(eventType='keyboard')
    if thx_key.status == STARTED:
        theseKeys = thx_key.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
