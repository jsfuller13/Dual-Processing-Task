/****************** 
 * Dual Task Test *
 ******************/

import { PsychoJS } from 'https://pavlovia.org/lib/core-3.2.js';
import * as core from 'https://pavlovia.org/lib/core-3.2.js';
import { TrialHandler } from 'https://pavlovia.org/lib/data-3.2.js';
import { Scheduler } from 'https://pavlovia.org/lib/util-3.2.js';
import * as util from 'https://pavlovia.org/lib/util-3.2.js';
import * as visual from 'https://pavlovia.org/lib/visual-3.2.js';
import { Sound } from 'https://pavlovia.org/lib/sound-3.2.js';

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'Dual Task';  // from the Builder filename that created this script
let expInfo = {'participant': '1', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const B1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(B1LoopBegin, B1LoopScheduler);
flowScheduler.add(B1LoopScheduler);
flowScheduler.add(B1LoopEnd);
const B2_instrLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(B2_instrLoopBegin, B2_instrLoopScheduler);
flowScheduler.add(B2_instrLoopScheduler);
flowScheduler.add(B2_instrLoopEnd);
flowScheduler.add(block_2RoutineBegin);
flowScheduler.add(block_2RoutineEachFrame);
flowScheduler.add(block_2RoutineEnd);
const B3_instrLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(B3_instrLoopBegin, B3_instrLoopScheduler);
flowScheduler.add(B3_instrLoopScheduler);
flowScheduler.add(B3_instrLoopEnd);
const B3_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(B3_trialsLoopBegin, B3_trialsLoopScheduler);
flowScheduler.add(B3_trialsLoopScheduler);
flowScheduler.add(B3_trialsLoopEnd);
flowScheduler.add(thanksRoutineBegin);
flowScheduler.add(thanksRoutineEachFrame);
flowScheduler.add(thanksRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var instrClock;
var instructions_text;
var key_resp;
var next_text;
var sound_2Clock;
var sound_stim;
var stim_resp_text;
var B1_trialClock;
var B1_prompt;
var block_2Clock;
var B2_text;
var sound_1;
var B3_trialClock;
var B3_prompt;
var thanksClock;
var thx_txt;
var thx_key;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_text',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  next_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'next_text',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "sound_2"
  sound_2Clock = new util.Clock();
  sound_stim = new Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 1.0,
    });
  sound_stim.setVolume(1);
  stim_resp_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'stim_resp_text',
    text: 'Respond as quickly as possible.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "B1_trial"
  B1_trialClock = new util.Clock();
  B1_prompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'B1_prompt',
    text: 'Respond as quickly as possible.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_text',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  next_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'next_text',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "block_2"
  block_2Clock = new util.Clock();
  B2_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'B2_text',
    text: 'Respond as quickly as possible.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  sound_1 = new Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 1.0,
    });
  sound_1.setVolume(1);
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_text',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  next_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'next_text',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "sound_2"
  sound_2Clock = new util.Clock();
  sound_stim = new Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 1.0,
    });
  sound_stim.setVolume(1);
  stim_resp_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'stim_resp_text',
    text: 'Respond as quickly as possible.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "B3_trial"
  B3_trialClock = new util.Clock();
  B3_prompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'B3_prompt',
    text: 'Respond as quickly as possible.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  thx_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'thx_txt',
    text: 'Good work!\n\nYou have completed this task.\n\nPress SPACE to exit.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  thx_key = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var B1;
var currentLoop;
function B1LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  B1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'DPT_Blocks.xlsx',
    seed: undefined, name: 'B1'});
  psychoJS.experiment.addLoop(B1); // add the loop to the experiment
  currentLoop = B1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisB1 of B1) {
    thisScheduler.add(importConditions(B1));
    const instructionsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(instructionsLoopBegin, instructionsLoopScheduler);
    thisScheduler.add(instructionsLoopScheduler);
    thisScheduler.add(instructionsLoopEnd);
    const B1_trialsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(B1_trialsLoopBegin, B1_trialsLoopScheduler);
    thisScheduler.add(B1_trialsLoopScheduler);
    thisScheduler.add(B1_trialsLoopEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}

var instructions;
function instructionsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  instructions = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: instr_file,
    seed: undefined, name: 'instructions'});
  psychoJS.experiment.addLoop(instructions); // add the loop to the experiment
  currentLoop = instructions;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisInstruction of instructions) {
    thisScheduler.add(importConditions(instructions));
    thisScheduler.add(instrRoutineBegin);
    thisScheduler.add(instrRoutineEachFrame);
    thisScheduler.add(instrRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function instructionsLoopEnd() {
  psychoJS.experiment.removeLoop(instructions);

  return Scheduler.Event.NEXT;
}

var B1_trials;
function B1_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  B1_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: trial_file,
    seed: undefined, name: 'B1_trials'});
  psychoJS.experiment.addLoop(B1_trials); // add the loop to the experiment
  currentLoop = B1_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisB1_trial of B1_trials) {
    thisScheduler.add(importConditions(B1_trials));
    thisScheduler.add(sound_2RoutineBegin);
    thisScheduler.add(sound_2RoutineEachFrame);
    thisScheduler.add(sound_2RoutineEnd);
    thisScheduler.add(B1_trialRoutineBegin);
    thisScheduler.add(B1_trialRoutineEachFrame);
    thisScheduler.add(B1_trialRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function B1_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(B1_trials);

  return Scheduler.Event.NEXT;
}


function B1LoopEnd() {
  psychoJS.experiment.removeLoop(B1);

  return Scheduler.Event.NEXT;
}

var B2_instr;
function B2_instrLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  B2_instr = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'DPT_instr2.xlsx',
    seed: undefined, name: 'B2_instr'});
  psychoJS.experiment.addLoop(B2_instr); // add the loop to the experiment
  currentLoop = B2_instr;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisB2_instr of B2_instr) {
    thisScheduler.add(importConditions(B2_instr));
    thisScheduler.add(instrRoutineBegin);
    thisScheduler.add(instrRoutineEachFrame);
    thisScheduler.add(instrRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function B2_instrLoopEnd() {
  psychoJS.experiment.removeLoop(B2_instr);

  return Scheduler.Event.NEXT;
}

var B3_instr;
function B3_instrLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  B3_instr = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'DPT_instr3.xlsx',
    seed: undefined, name: 'B3_instr'});
  psychoJS.experiment.addLoop(B3_instr); // add the loop to the experiment
  currentLoop = B3_instr;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisB3_instr of B3_instr) {
    thisScheduler.add(importConditions(B3_instr));
    thisScheduler.add(instrRoutineBegin);
    thisScheduler.add(instrRoutineEachFrame);
    thisScheduler.add(instrRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function B3_instrLoopEnd() {
  psychoJS.experiment.removeLoop(B3_instr);

  return Scheduler.Event.NEXT;
}

var B3_trials;
function B3_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  B3_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'DPT_B3.xlsx',
    seed: undefined, name: 'B3_trials'});
  psychoJS.experiment.addLoop(B3_trials); // add the loop to the experiment
  currentLoop = B3_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisB3_trial of B3_trials) {
    thisScheduler.add(importConditions(B3_trials));
    thisScheduler.add(sound_2RoutineBegin);
    thisScheduler.add(sound_2RoutineEachFrame);
    thisScheduler.add(sound_2RoutineEnd);
    thisScheduler.add(B3_trialRoutineBegin);
    thisScheduler.add(B3_trialRoutineEachFrame);
    thisScheduler.add(B3_trialRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function B3_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(B3_trials);

  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var instrComponents;
function instrRoutineBegin() {
  //------Prepare to start Routine 'instr'-------
  t = 0;
  instrClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  instructions_text.setText(instr_text);
  key_resp.keys = undefined;
  key_resp.rt = undefined;
  next_text.setText(cont_text);
  // keep track of which components have finished
  instrComponents = [];
  instrComponents.push(instructions_text);
  instrComponents.push(key_resp);
  instrComponents.push(next_text);
  
  for (const thisComponent of instrComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function instrRoutineEachFrame() {
  //------Loop for each frame of Routine 'instr'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instrClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instructions_text* updates
  if (t >= 0.0 && instructions_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instructions_text.tStart = t;  // (not accounting for frame time here)
    instructions_text.frameNStart = frameN;  // exact frame index
    instructions_text.setAutoDraw(true);
  }

  
  // *key_resp* updates
  if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp.tStart = t;  // (not accounting for frame time here)
    key_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
  }

  if (key_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *next_text* updates
  if (t >= 0 && next_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    next_text.tStart = t;  // (not accounting for frame time here)
    next_text.frameNStart = frameN;  // exact frame index
    next_text.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of instrComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instrRoutineEnd() {
  //------Ending Routine 'instr'-------
  for (const thisComponent of instrComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "instr" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var sound_2Components;
function sound_2RoutineBegin() {
  //------Prepare to start Routine 'sound_2'-------
  t = 0;
  sound_2Clock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.500000);
  // update component parameters for each repeat
  sound_stim = new Sound({
    win: psychoJS.window,
    value: SoundFile,
    secs: 1.0,
    });
  sound_stim.secs=1.0;
  sound_stim.setVolume(1);
  // keep track of which components have finished
  sound_2Components = [];
  sound_2Components.push(sound_stim);
  sound_2Components.push(stim_resp_text);
  
  for (const thisComponent of sound_2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function sound_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'sound_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = sound_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  // start/stop sound_stim
  if (t >= 0.5 && sound_stim.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    sound_stim.tStart = t;  // (not accounting for frame time here)
    sound_stim.frameNStart = frameN;  // exact frame index
    psychoJS.window.callOnFlip(function(){ sound_stim.play(); });  // screen flip
    sound_stim.status = PsychoJS.Status.STARTED;
  }
  frameRemains = 0.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (sound_stim.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    if (1.0 > 0.5) {  sound_stim.stop();  // stop the sound (if longer than duration)
      sound_stim.status = PsychoJS.Status.FINISHED;
    }
  }
  
  // *stim_resp_text* updates
  if (t >= 0 && stim_resp_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    stim_resp_text.tStart = t;  // (not accounting for frame time here)
    stim_resp_text.frameNStart = frameN;  // exact frame index
    stim_resp_text.setAutoDraw(true);
  }

  frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (stim_resp_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    stim_resp_text.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of sound_2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function sound_2RoutineEnd() {
  //------Ending Routine 'sound_2'-------
  for (const thisComponent of sound_2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  sound_stim.stop();  // ensure sound has stopped at end of routine
  return Scheduler.Event.NEXT;
}

var B1_trialComponents;
function B1_trialRoutineBegin() {
  //------Prepare to start Routine 'B1_trial'-------
  t = 0;
  B1_trialClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.500000);
  // update component parameters for each repeat
  // keep track of which components have finished
  B1_trialComponents = [];
  B1_trialComponents.push(B1_prompt);
  
  for (const thisComponent of B1_trialComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function B1_trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'B1_trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = B1_trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *B1_prompt* updates
  if (t >= 0.0 && B1_prompt.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    B1_prompt.tStart = t;  // (not accounting for frame time here)
    B1_prompt.frameNStart = frameN;  // exact frame index
    B1_prompt.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (B1_prompt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    B1_prompt.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of B1_trialComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function B1_trialRoutineEnd() {
  //------Ending Routine 'B1_trial'-------
  for (const thisComponent of B1_trialComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var block_2Components;
function block_2RoutineBegin() {
  //------Prepare to start Routine 'block_2'-------
  t = 0;
  block_2Clock.reset(); // clock
  frameN = -1;
  routineTimer.add(120.000000);
  // update component parameters for each repeat
  sound_1.secs=1.0;
  sound_1.setVolume(1);
  // keep track of which components have finished
  block_2Components = [];
  block_2Components.push(B2_text);
  block_2Components.push(sound_1);
  
  for (const thisComponent of block_2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function block_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'block_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = block_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *B2_text* updates
  if (t >= 0.0 && B2_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    B2_text.tStart = t;  // (not accounting for frame time here)
    B2_text.frameNStart = frameN;  // exact frame index
    B2_text.setAutoDraw(true);
  }

  frameRemains = 120.0  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (B2_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    B2_text.setAutoDraw(false);
  }
  // start/stop sound_1
  if (t >= 119 && sound_1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    sound_1.tStart = t;  // (not accounting for frame time here)
    sound_1.frameNStart = frameN;  // exact frame index
    psychoJS.window.callOnFlip(function(){ sound_1.play(); });  // screen flip
    sound_1.status = PsychoJS.Status.STARTED;
  }
  frameRemains = 119 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (sound_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    if (1.0 > 0.5) {  sound_1.stop();  // stop the sound (if longer than duration)
      sound_1.status = PsychoJS.Status.FINISHED;
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of block_2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function block_2RoutineEnd() {
  //------Ending Routine 'block_2'-------
  for (const thisComponent of block_2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  sound_1.stop();  // ensure sound has stopped at end of routine
  return Scheduler.Event.NEXT;
}

var B3_trialComponents;
function B3_trialRoutineBegin() {
  //------Prepare to start Routine 'B3_trial'-------
  t = 0;
  B3_trialClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.500000);
  // update component parameters for each repeat
  // keep track of which components have finished
  B3_trialComponents = [];
  B3_trialComponents.push(B3_prompt);
  
  for (const thisComponent of B3_trialComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function B3_trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'B3_trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = B3_trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *B3_prompt* updates
  if (t >= 0.0 && B3_prompt.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    B3_prompt.tStart = t;  // (not accounting for frame time here)
    B3_prompt.frameNStart = frameN;  // exact frame index
    B3_prompt.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (B3_prompt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    B3_prompt.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of B3_trialComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function B3_trialRoutineEnd() {
  //------Ending Routine 'B3_trial'-------
  for (const thisComponent of B3_trialComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var thanksComponents;
function thanksRoutineBegin() {
  //------Prepare to start Routine 'thanks'-------
  t = 0;
  thanksClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  thx_key.keys = undefined;
  thx_key.rt = undefined;
  // keep track of which components have finished
  thanksComponents = [];
  thanksComponents.push(thx_txt);
  thanksComponents.push(thx_key);
  
  for (const thisComponent of thanksComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function thanksRoutineEachFrame() {
  //------Loop for each frame of Routine 'thanks'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = thanksClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *thx_txt* updates
  if (t >= 0.0 && thx_txt.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    thx_txt.tStart = t;  // (not accounting for frame time here)
    thx_txt.frameNStart = frameN;  // exact frame index
    thx_txt.setAutoDraw(true);
  }

  
  // *thx_key* updates
  if (t >= 0.0 && thx_key.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    thx_key.tStart = t;  // (not accounting for frame time here)
    thx_key.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { thx_key.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { thx_key.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { thx_key.clearEvents(); });
  }

  if (thx_key.status === PsychoJS.Status.STARTED) {
    let theseKeys = thx_key.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of thanksComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function thanksRoutineEnd() {
  //------Ending Routine 'thanks'-------
  for (const thisComponent of thanksComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "thanks" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
