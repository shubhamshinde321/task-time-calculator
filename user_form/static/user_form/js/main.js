
function pad(val) {
    valString = val + "";
    if(valString.length < 2) {
        return "0" + valString;
        } else {
        return valString;
        }
}

var totalSeconds = 0;
var minutesLabel = 0;
var secondsLabel = 0;
var hourLabel = 0;
function setTime(minutesLabel, secondsLabel) {
    totalSeconds++;
    secondsLabel = pad(totalSeconds%60);
    minutesLabel = pad(parseInt(totalSeconds/60));
    hourLabel = pad(parseInt(totalSeconds/3600));
    document.getElementById("total_time").value = hourLabel + ":" +minutesLabel + ":" + secondsLabel;
}

function set_timer() {
    my_int = setInterval(function() { setTime(minutesLabel, secondsLabel)}, 1000);
}

function startTimer() {
    var startTime = new Date().toLocaleString();
    document.getElementById("start_time").value = startTime
    set_timer();
    document.getElementById('start_timer').style.display = "none"
    document.getElementById('stop_timer').style.display = "block"
}

function stopTimer() {
    var endTime = new Date().toLocaleString();
    document.getElementById("end_time").value = endTime
    clearInterval(my_int);
    document.getElementById('submit').style.display = "block"
    document.getElementById('stop_timer').style.display = "none"
}


