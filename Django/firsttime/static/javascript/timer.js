var timer;
var minutesLabel = document.getElementById("minutes");
var secondsLabel = document.getElementById("seconds");
var totalSeconds = 1500; // 25 minutes * 60 seconds
var isTimerRunning = false;
var isTimerPaused = false;

function startTimer() {
  if (!isTimerRunning) {
    timer = setInterval(setTime, 1000);
    isTimerRunning = true;
  }
}

function pauseTimer() {
  if (isTimerRunning && !isTimerPaused) {
    clearInterval(timer);
    isTimerPaused = true;
  }
}

function resumeTimer() {
  if (isTimerRunning && isTimerPaused) {
    timer = setInterval(setTime, 1000);
    isTimerPaused = false;
  }
}

function resetTimer() {
  clearInterval(timer);
  totalSeconds = 1500;
  minutesLabel.textContent = pad(parseInt(totalSeconds / 60));
  secondsLabel.textContent = pad(totalSeconds % 60);
  isTimerRunning = false;
  isTimerPaused = false;
}

function setTime() {
  if (totalSeconds > 0) {
    --totalSeconds;
    secondsLabel.textContent = pad(totalSeconds % 60);
    minutesLabel.textContent = pad(parseInt(totalSeconds / 60));
  } else {
    resetTimer();
  }
}

function pad(val) {
  var valString = val + "";
  if (valString.length < 2) {
    return "0" + valString;
  } else {
    return valString;
  }
}

// Attach event listeners to buttons
document.getElementById("start-btn").addEventListener("click", startTimer);
document.getElementById("pause-btn").addEventListener("click", pauseTimer);
document.getElementById("resume-btn").addEventListener("click", resumeTimer);
document.getElementById("reset-btn").addEventListener("click", resetTimer);
