#importing speech recognition package from google api
import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
import webbrowser

num = 1;
j=0;
status="wakeup"
#*********************************************************
# function used to open application
	# present inside the system.
def programming():
	while(1):
		assistant_speaks("lets continue to describe your program!")
		pr_text=get_audio();
		if "make a summation" in pr_text:
			assistant_speaks("ok sir,i make a summation!")
			memo="x=input('please enter your first number')"+"\n"+"y=input('please enter your second number')"+"\n"+"sum=int(x)+int(y);"+"\n"+"print(sum);"
			print(memo)
			file = open("counter.txt", "w+")
			file.write(memo)
			assistant_speaks("i export programming syntax in a text file,it names is counter")
		if "end of programming" in pr_text:
			assistant_speaks("ok sir,come back to main menu!")
			break;


	return

def open_application(input):

		assistant_speaks("in open aplication")

		if "chrome" in input:
			assistant_speaks("Google Chrome")
			os.system("C:\Program Files\nodejs\node.exe")
			#os.system("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
			return

		if "firefox" in input or "mozilla" in input:
			assistant_speaks("Opening Mozilla Firefox")
			os.startfile('C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
			return

		if "word" in input or "Word" in input:
			assistant_speaks("Opening Microsoft Word")
			os.startfile('D:\ptest\\new.docx')
			return

		if "excel" in input:
			assistant_speaks("Opening Microsoft Excel")
			os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\\Excel 2010.lnk')
			return

		else:

			assistant_speaks("Application not available")
			return
#************************************************************************
#--------------------
def process_text(input):
	try:


		if "who are you" in input or "define yourself" in input:
			speak = '''Hello, I am melody. Your personal Assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as calculating sums or opening applications etcetra'''
			assistant_speaks(speak)
			return

		if "who made you" in input or "created you" in input:
			speak = "my father is sina,I have been created by sina majidi."
			assistant_speaks(speak)
			return

		if "open" in input or "Open" in input:

			# another function to open
			# different application availaible
			assistant_speaks("ok sir,i will " + input.lower())
			open_application(input.lower())

			return

		if "find" in input or "search about" in input:
			query = input
			url = "https://www.google.com.tr/search?q="+query
			webbrowser.open_new_tab(url)
			assistant_speaks("ok sir")
			return

		if "you born" in input or "old are you" in input :


			assistant_speaks("i was born on 18 march 2020")


			return

		if "start programming" in input or "want to programming" in input :


			assistant_speaks("good,lets start programming")
			programming();


			return



		if "wait" in input or "stay" in input or "sleep" in input:
			assistant_speaks("ok sir")
			while 1:
				status="sleep"
				wakeup_text=get_audio()
				if "wakeup" in wakeup_text or "wake" in wakeup_text:
					status = "wakeup"
					break;




	except:

		assistant_speaks("i can't do any thing right now");
	return;


#--------------------------------

def assistant_speaks(output):
	global num;

	# num to rename every audio file
	# with different name to remove ambiguity
	num += 1;
	print("melody:", output);

	toSpeak = gTTS(text=output, lang='en', slow=False);
	# saving the audio file given by google text to speech
	file = str(num) + ".mp3";
	toSpeak.save(file);

	# playsound package is used to play the same file.
	playsound.playsound(file, True);
	#os.system(file);
	os.remove(file);


def get_audio():
	rObject = sr.Recognizer();
	audio = '';

	with sr.Microphone() as source:
		rObject.adjust_for_ambient_noise(source);
		print("Speak...");

		# recording the audio using speech recognition
		audio = rObject.listen(source, phrase_time_limit=5);
	print("Stop.");  # limit 5 secs

	try:

		text = rObject.recognize_google(audio, language='en-US');
		print("You : ", text);
		return text;

	except:

		#assistant_speaks("Could not understand your audio, PLease try again !");
		text="";
		return text;


# Driver Code
if __name__ == "__main__":
	assistant_speaks("hello human,my name is melody,What's your name,please type it");
	name = 'Human';
	#name = get_audio();
	name=input();
	assistant_speaks("Hello " + name +", at your service");

	while (1):


		assistant_speaks("What can i do for you?");
		text = get_audio();


		if text == 0:
			continue

		if "exit" in str(text) or "bye" in str(text):
			assistant_speaks("Ok bye, " + name + '.');
			break;
		# calling process text to process the query
		process_text(text);







