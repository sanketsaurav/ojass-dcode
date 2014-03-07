bgLoop = new Audio('/static/audio/bg-loop-cc.ogg');
bgLoop.addEventListener('ended', function() {
	this.currentTime = 0;
	this.play();
}, false);
bgLoop.play();
var mute = function () {bgLoop.muted=!bgLoop.muted;}