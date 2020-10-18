#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on November 19, 2019, at 15:16
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
expName = 'Dual Task'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Jordan\\Documents\\Experiment Building\\2. Dual Processing Task\\Dual Task_lastrun.py',
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

# Initialize components for Routine "sound_2"
sound_2Clock = core.Clock()
sound_stim = sound.Sound('A', secs=1.0, stereo=True)
sound_stim.setVolume(1)
stim_resp_text = visual.TextStim(win=win, name='stim_resp_text',
    text='Respond as quickly as possible.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "B1_trial"
B1_trialClock = core.Clock()
B1_prompt = visual.TextStim(win=win, name='B1_prompt',
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
sound_1 = sound.Sound('A', secs=1.0, stereo=True)
sound_1.setVolume(1)

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

# Initialize components for Routine "sound_2"
sound_2Clock = core.Clock()
sound_stim = sound.Sound('A', secs=1.0, stereo=True)
sound_stim.setVolume(1)
stim_resp_text = visual.TextStim(win=win, name='stim_resp_text',
    text='Respond as quickly as possible.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "B3_trial"
B3_trialClock = core.Clock()
B3_prompt = visual.TextStim(win=win, name='B3_prompt',
    text='Respond as quickly as possible.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

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
B1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('DPT_Blocks.xlsx'),
    seed=None, name='B1')
thisExp.addLoop(B1)  # add the loop to the experiment
thisB1 = B1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisB1.rgb)
if thisB1 != None:
    for paramName in thisB1:
        exec('{} = thisB1[paramName]'.format(paramName))

for thisB1 in B1:
    currentLoop = B1
    # abbreviate parameter names if possible (e.g. rgb = thisB1.rgb)
    if thisB1 != None:
        for paramName in thisB1:
            exec('{} = thisB1[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    instructions = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(instr_file),
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
        trialList=data.importConditions(trial_file),
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
        
        # ------Prepare to start Routine "sound_2"-------
        t = 0
        sound_2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        sound_stim.setSound(SoundFile, secs=1.0)
        sound_stim.setVolume(1, log=False)
        # keep track of which components have finished
        sound_2Components = [sound_stim, stim_resp_text]
        for thisComponent in sound_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "sound_2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = sound_2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop sound_stim
            if t >= 0.5 and sound_stim.status == NOT_STARTED:
                # keep track of start time/frame for later
                sound_stim.tStart = t  # not accounting for scr refresh
                sound_stim.frameNStart = frameN  # exact frame index
                win.timeOnFlip(sound_stim, 'tStartRefresh')  # time at next scr refresh
                win.callOnFlip(sound_stim.play)  # screen flip
            frameRemains = 0.5 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if sound_stim.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                sound_stim.tStop = t  # not accounting for scr refresh
                sound_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_stim, 'tStopRefresh')  # time at next scr refresh
                if 1.0 > 0.5:  # don't force-stop brief sounds
                    sound_stim.stop()
            
            # *stim_resp_text* updates
            if t >= 0 and stim_resp_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                stim_resp_text.tStart = t  # not accounting for scr refresh
                stim_resp_text.frameNStart = frameN  # exact frame index
                win.timeOnFlip(stim_resp_text, 'tStartRefresh')  # time at next scr refresh
                stim_resp_text.setAutoDraw(True)
            frameRemains = 0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if stim_resp_text.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                stim_resp_text.tStop = t  # not accounting for scr refresh
                stim_resp_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stim_resp_text, 'tStopRefresh')  # time at next scr refresh
                stim_resp_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sound_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sound_2"-------
        for thisComponent in sound_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_stim.stop()  # ensure sound has stopped at end of routine
        
        # ------Prepare to start Routine "B1_trial"-------
        t = 0
        B1_trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        # Create a voice-key to be used:
        vpvk = vk.OnsetVoiceKey(
            sec=1.5, 
            file_out='data/trial_'+Block+str(B1_trials.thisN).zfill(3)+'_'+Stim+'.wav')
        
        # Start it recording (and detecting):
          # non-blocking; don't block when using Builder
        vpvk.start()
        # keep track of which components have finished
        B1_trialComponents = [B1_prompt]
        for thisComponent in B1_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "B1_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = B1_trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *B1_prompt* updates
            if t >= 0.0 and B1_prompt.status == NOT_STARTED:
                # keep track of start time/frame for later
                B1_prompt.tStart = t  # not accounting for scr refresh
                B1_prompt.frameNStart = frameN  # exact frame index
                win.timeOnFlip(B1_prompt, 'tStartRefresh')  # time at next scr refresh
                B1_prompt.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if B1_prompt.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                B1_prompt.tStop = t  # not accounting for scr refresh
                B1_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(B1_prompt, 'tStopRefresh')  # time at next scr refresh
                B1_prompt.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in B1_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "B1_trial"-------
        for thisComponent in B1_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
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
    
# completed 1 repeats of 'B1'


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
routineTimer.add(120.000000)
# update component parameters for each repeat
sound_1.setSound('A', secs=1.0)
sound_1.setVolume(1, log=False)
# keep track of which components have finished
block_2Components = [B2_text, sound_1]
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
    frameRemains = 120.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if B2_text.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        B2_text.tStop = t  # not accounting for scr refresh
        B2_text.frameNStop = frameN  # exact frame index
        win.timeOnFlip(B2_text, 'tStopRefresh')  # time at next scr refresh
        B2_text.setAutoDraw(False)
    # start/stop sound_1
    if t >= 119 and sound_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_1.tStart = t  # not accounting for scr refresh
        sound_1.frameNStart = frameN  # exact frame index
        win.timeOnFlip(sound_1, 'tStartRefresh')  # time at next scr refresh
        win.callOnFlip(sound_1.play)  # screen flip
    frameRemains = 119 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if sound_1.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        sound_1.tStop = t  # not accounting for scr refresh
        sound_1.frameNStop = frameN  # exact frame index
        win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
        if 1.0 > 0.5:  # don't force-stop brief sounds
            sound_1.stop()
    
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
sound_1.stop()  # ensure sound has stopped at end of routine

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
    
    # ------Prepare to start Routine "sound_2"-------
    t = 0
    sound_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    sound_stim.setSound(SoundFile, secs=1.0)
    sound_stim.setVolume(1, log=False)
    # keep track of which components have finished
    sound_2Components = [sound_stim, stim_resp_text]
    for thisComponent in sound_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "sound_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = sound_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_stim
        if t >= 0.5 and sound_stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_stim.tStart = t  # not accounting for scr refresh
            sound_stim.frameNStart = frameN  # exact frame index
            win.timeOnFlip(sound_stim, 'tStartRefresh')  # time at next scr refresh
            win.callOnFlip(sound_stim.play)  # screen flip
        frameRemains = 0.5 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if sound_stim.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            sound_stim.tStop = t  # not accounting for scr refresh
            sound_stim.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_stim, 'tStopRefresh')  # time at next scr refresh
            if 1.0 > 0.5:  # don't force-stop brief sounds
                sound_stim.stop()
        
        # *stim_resp_text* updates
        if t >= 0 and stim_resp_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim_resp_text.tStart = t  # not accounting for scr refresh
            stim_resp_text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(stim_resp_text, 'tStartRefresh')  # time at next scr refresh
            stim_resp_text.setAutoDraw(True)
        frameRemains = 0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if stim_resp_text.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            stim_resp_text.tStop = t  # not accounting for scr refresh
            stim_resp_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(stim_resp_text, 'tStopRefresh')  # time at next scr refresh
            stim_resp_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sound_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sound_2"-------
    for thisComponent in sound_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_stim.stop()  # ensure sound has stopped at end of routine
    
    # ------Prepare to start Routine "B3_trial"-------
    t = 0
    B3_trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    vpvk = vk.OnsetVoiceKey(
        sec=1.5, 
        file_out='data/trial_'+Block+str(B3_trials.thisN).zfill(3)+'_'+Stim+'.wav')
    
    # Start it recording (and detecting):
      # non-blocking; don't block when using Builder
    vpvk.start()
    # keep track of which components have finished
    B3_trialComponents = [B3_prompt]
    for thisComponent in B3_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "B3_trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = B3_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *B3_prompt* updates
        if t >= 0.0 and B3_prompt.status == NOT_STARTED:
            # keep track of start time/frame for later
            B3_prompt.tStart = t  # not accounting for scr refresh
            B3_prompt.frameNStart = frameN  # exact frame index
            win.timeOnFlip(B3_prompt, 'tStartRefresh')  # time at next scr refresh
            B3_prompt.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if B3_prompt.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            B3_prompt.tStop = t  # not accounting for scr refresh
            B3_prompt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(B3_prompt, 'tStopRefresh')  # time at next scr refresh
            B3_prompt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in B3_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "B3_trial"-------
    for thisComponent in B3_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
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
