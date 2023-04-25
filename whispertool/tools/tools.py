import speech_recognition as sr
from gtts import gTTS
import os
PORT=65426
#HOST='192.0.0.1'
HOST='0.0.0.0'

FROMIDIOM="es"
TOIDIOM="de"
def recordAudio3():
    phrase_time = None
    last_sample = bytes()
    data_queue = Queue()
    recorder = sr.Recognizer()
    recorder.energy_threshold = 1000
    recorder.dynamic_energy_threshold = False
    audio_model = whisper.load_model("large")
    temp_file = NamedTemporaryFile().name
    with source:
        recorder.adjust_for_ambient_noise(source)
    def record_callback(_, audio:sr.AudioData) -> None:
        data = audio.get_raw_data()
        data_queue.put(data)
    recorder.listen_in_background(source, record_callback, phrase_time_limit=record_timeout)
    now = datetime.utcnow()
    if not data_queue.empty():
        phrase_complete = False
        if phrase_time and now - phrase_time > timedelta(seconds=phrase_timeout):
            last_sample = bytes()
            phrase_complete = True
        phrase_time = now
        while not data_queue.empty():
            data = data_queue.get()
            last_sample += data
        audio_data = sr.AudioData(last_sample, source.SAMPLE_RATE, source.SAMPLE_WIDTH)
        wav_data = io.BytesIO(audio_data.get_wav_data())
        with open(temp_file, 'w+b') as f:
            f.write(wav_data.read())
        result = audio_model.transcribe(temp_file, fp16=torch.cuda.is_available())
        text = result['text'].strip()
        if phrase_complete:
            transcription.append(text)
        else:
            transcription[-1] = text
        #os.system('cls' if os.name=='nt' else 'clear')
        for line in transcription:
            yield line
        sleep(0.25)
    #save file
    #transcribe, return
def recordAudio2():
    phrase_time = None
    last_sample = bytes()
    data_queue = Queue()
    recorder = sr.Recognizer()
    recorder.energy_threshold = 1000#args.energy_threshold
    recorder.dynamic_energy_threshold = False
    if 'linux' in platform:
        mic_name = 'pulse'#args.default_microphone
        if not mic_name or mic_name == 'list':
            print("Available microphone devices are: ")
            for index, name in enumerate(sr.Microphone.list_microphone_names()):
                print(f"Microphone with name \"{name}\" found")   
            return
        else:
            for index, name in enumerate(sr.Microphone.list_microphone_names()):
                if mic_name in name:
                    source = sr.Microphone(sample_rate=16000, device_index=index)
                    break
    else:
        source = sr.Microphone(sample_rate=16000)
    model = "large"
    audio_model = whisper.load_model(model)
    record_timeout = 2
    phrase_timeout = 3#tiempo de fase
    temp_file = NamedTemporaryFile().name
    transcription = ['']

    with source:
        recorder.adjust_for_ambient_noise(source)
    def record_callback(_, audio:sr.AudioData) -> None:
        """
        Threaded callback function to recieve audio data when recordings finish.
        audio: An AudioData containing the recorded bytes.
        """
        # Grab the raw bytes and push it into the thread safe queue.
        data = audio.get_raw_data()
        data_queue.put(data)
    recorder.listen_in_background(source, record_callback, phrase_time_limit=record_timeout)
    print("Model loaded.\n")
    while True:
        try:
            now = datetime.utcnow()
            if not data_queue.empty():
                phrase_complete = False
                if phrase_time and now - phrase_time > timedelta(seconds=phrase_timeout):
                    last_sample = bytes()
                    phrase_complete = True
                phrase_time = now
                while not data_queue.empty():
                    data = data_queue.get()
                    last_sample += data
                audio_data = sr.AudioData(last_sample, source.SAMPLE_RATE, source.SAMPLE_WIDTH)
                wav_data = io.BytesIO(audio_data.get_wav_data())
                with open(temp_file, 'w+b') as f:
                    f.write(wav_data.read())
                result = audio_model.transcribe(temp_file, fp16=torch.cuda.is_available())
                text = result['text'].strip()
                if phrase_complete:
                    transcription.append(text)
                else:
                    transcription[-1] = text
                os.system('cls' if os.name=='nt' else 'clear')
                for line in transcription:
                    yield line
                sleep(0.25)
        except KeyboardInterrupt:
            break

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    
        data = ""
        try:
            data = r.recognize_google(audio)
            print("You said: " + data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            speak("I couldn't understand you")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        data = data.lower()
        return data
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")
def webTranslate(txt,writeIn,translateTo):
	"""
	webTranslate(txt,writeIn,translateTo )
	  - txt			  -text to trasnlate
	  - writeIn		  -in which language is it written
	  - translateTo	  -language to be translated
	rember language prefix
	en -> english
	es -> spanish 
	...
	"""
	from deep_translator import GoogleTranslator 
	translatedTxt = GoogleTranslator(source=writeIn, target=translateTo).translate(txt)
	return translatedTxt