var msg = new SpeechSynthesisUtterance();
var voices = window.speechSynthesis.getVoices();
msg.voiceURI = 'native';
msg.volume = 1; // 0 to 1
msg.rate = 0.5; // 0.1 to 10
msg.pitch = 1; //0 to 2
msg.text = 'Pójdzie jak po lodzie potem słońce w samochodzie';
msg.lang = 'pl';
speechSynthesis.speak(msg);