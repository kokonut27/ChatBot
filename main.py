import time, os, sys, random
import requests, json

owner = os.environ['REPL_OWNER']
botnames = ["Default","ChatBot",'PyBot']
botname = random.choice(botnames)

def clear():
  os.system('clear')

Format=False

def formatcheck():
  if Format == True:
    print()
  else:
    pass

from pprint import pprint
def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
	return res.json()
def print_weather(result,city):
	print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
	print("Wind speed: {} m/s".format(result['wind']['speed']))
	print("Description: {}".format(result['weather'][0]['description']))
	print("Weather: {}".format(result['weather'][0]['main']))
def main():
  city=input(f'[{botname}]: Enter the city/capital/country/state,\n:> ')
  formatcheck()
  try:
    query='q='+city
    w_data=weather_data(query)
    print_weather(w_data, city)
    formatcheck()
    print(f"[{botname}]: Hello {owner}! What can I do for you?")
  except:
    print(f'[{botname}]: City/capital/country/state name not found...')

#colours
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
cyan_back = "\033[0;46m"
purple_back = "\033[0;45m"
white_back = "\033[0;47m"
blue_back = "\033[0;44m"
orange_back = "\033[0;43m"
green_back = "\033[0;42m"
pink_back = "\033[0;41m"
grey_back = "\033[0;40m"
grey = '\033[38;4;236m'
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
invisible='\033[08m'
reverse='\033[07m'
reset='\033[0m'
grey = "\x1b[90m"


clear()
print(f"[{botname}]: Hello {owner}! Feel free to chat with me as much as you want!")
alltext=[]

chatting=True
while chatting:
  formatcheck()
  ci = input(':> ').lower()
  formatcheck()
  alltext.append(ci)

  if ci == 'hi' or ci == 'hoi' or ci == 'hai' or ci == 'hey' or ci == 'hello' or ci == 'howdy' or ci == 'how are you?' or ci == 'how are you' or ci == 'how r u?' or ci == 'how r u':#lol, yes.
    print(f"[{botname}]: Hi! What can I do for you?")

  elif ci == f'chatbot.commands':
    print(f"[{botname}]: I don't have that much commands. There are only a few. Would you like to hear them?")
    formatcheck()
    yn = input(":> ").lower()

    if yn == "yes" or yn == 'y':
      formatcheck()
      print(f"[{botname}]: Ok, here they are:\n- chatbot.clear\n- chatbot.commands\n- chatbot.format\n- chatbot.quit\n- chatbot.save")#add saving
      time.sleep(2)
      formatcheck()
      print(f"[{botname}]: If you ever need help with the commands, just put \"HELP-chatbot.'command'\"")
    elif yn == 'no' or yn == 'n' or yn == 'nope':
      print(f"[{botname}]: Ok then. If you want to hear them, try again later!")
    else:
      print(f"[{botname}]: Hmmm, I didn't understand that. Could you try that again?")
  
  elif ci == 'chatbot.clear':
    print(f"[{botname}]: Clearing Chat!")
    time.sleep(1)
    clear()
    print(f"[{botname}]: Hi! What can I do for you?")
  
  elif ci == 'chatbot.format':
    if Format == True:
      print(f"[{botname}]: Turning off format!")
      Format=False
    else:
      print(f"[{botname}]: Formatting text to be clearer!")
      Format=True
  
  elif ci == 'chatbot.quit':
    print(f"[{botname}]: I hope you have a great day!")
    quit()
  
  elif ci == 'chatbot.save':
    print(f"[{botname}]: Saving chat...")
    formatcheck()
    try:
      print(f"[{botname}]: Successfully saved chat! Note that it will disappear once you reload the site!")
      alltext2="\n".join(alltext)
      with open("ChatText.txt","a") as file:
        file.write(alltext2)
        file.close()
      
    except:
      print(f"[{botname}]: There was an error trying to save! Try again later!")
  

  #all the help cmds
  elif ci == 'help-chatbot.clear':
    print(f"[{botname}]: That command clears the chat area!")
  
  elif ci == 'help-chatbot.commands':
    print(f"[{botname}]: That command lists all the commands!")

  elif ci == 'help-chatbot.format':
    print(f"[{botname}]: That command makes the chat text clearer to read!")
  
  elif ci == 'help-chatbot.quit':
    print(f"[{botname}]: That command exits out of the chatbot!")

  elif ci == 'help-chatbot.save':
    print(f"[{botname}]: That command saves the chat!")
  #done with help's


  elif ci == 'local-date' or ci == 'date' or ci == 'localdate' or ci == 'local date' or ci == 'current date':
    local = time.strftime("%Y-%m-%d", time.localtime())
    print(f"[{botname}]: The local date is currently: "+local)
  
  elif ci == 'local-time' or ci == 'time' or ci == 'localtime' or ci == 'local time' or ci == 'current time':
    local = time.strftime("%H-%M-%S%z", time.localtime())
    print(f"[{botname}]: The local time is currently: "+local)

  elif ci == 'local-weather' or ci == 'localweather' or ci == 'local weather' or ci == 'weather' or ci == 'current weather':
    if __name__ == '__main__':
      main()
    
  elif ci == 'game' or ci == 'play' or ci == 'play-game' or ci == 'playgame' or ci == 'play game':
    print(f"[{botname}]: Loading games...")
    formatcheck()
    time.sleep(2)
    print(f"[{botname}]: I currently have '3' games. Do you want me to list them for you?")#change number frequently
    formatcheck()
    yn = input(':> ').lower()
    formatcheck()

    if yn == 'y' or yn == 'yes' or yn == 'yep':
      print(f"[{botname}]: Ok. Here they are:\n1. Hangman\n2. Guess the Animal\n3. Guess the number\nWhich game do you want to play?")
      formatcheck()
      game = input(":> ")
      formatcheck()

      if game == '1':
        print(f"[{botname}]: Loading game...")
        time.sleep(2)
        clear()
        hangman=True
        while hangman:
          from random_words import RandomWords
          r = RandomWords()
          word = r.random_word()
          while True:
            if len(word) < 5:
              word = RandomWords.random_word()
            else:
              break
          
          missedletters = ""
          correctletters = ""

          print("H A N G M A N!")
          time.sleep(2)
          clear()

          guesses=7
          vowels = ["a","e","i","o","u"]

          def getGuess(alreadyguessed):
            while True:
              guess = input("Guess a single letter: ").lower()
              if len(guess) != 1:
                print("Please guess only one letter!")
              elif guess in alreadyguessed:
                print("You already guessed that letter. Try again")
              elif guess not in "abcdefghijklmnopqrstuvwxyz":
                print("Please enter a letter")
              else:
                return guess
          
          def display(missedletters, correctletters, word):
            print("Already guessed: ",end="")
            for i in missedletters:
              print(i, end=" ")
            print()

            for letter in word:
              if letter in correctletters:
                print(letter,end=" ")
              else:
                print("_",end=" ")
            
            print()
          
          def isWin(correctletters, word):
            for i in word:
              if i not in correctletters:
                return False
                break
            return True

          while True:
            display(missedletters,correctletters,word)
            guess = getGuess(missedletters+correctletters)

            if guess in word:
              correctletters=correctletters+guess
              time.sleep(2)
              clear()
            if isWin(correctletters, word):
              print(f"You won! You had {guesses} guess left. Going back to main lobby...")
              time.sleep(2)
              clear()
              hangman=False
              break
              print(f"[{botname}]: Hello {owner}! What can I do for you?")
            if guess not in word:
              print("Not in word!")
              missedletters = missedletters+guess
              guesses-=1
              print(f"You have {guesses} guesses left")
              time.sleep(2)
              clear()

              if guesses == 0:
                print("You lost!")
                print(f"The correct word was {word}")
                time.sleep(2)
                clear()
                hangman=False
                break
              if guesses == 1:
                print("Heads up, you have 1 guess left!")
                time.sleep(2)

      elif game == '2':
        print(f"[{botname}]: Loading game...")
        time.sleep(2)
        clear()
        animal = {
          'lion': ['mane', 'teeth', 'pride',           'Africa', 'predator'],
          'tiger': ['stripes', 'fur', 'endangered', 'cat', 'claws'],
          'bear': ['hibernates', 'North America', 'Brown', 'Fur', 'Strong'],
          'owl': ['hoot', 'nocturnal', 'flies', 'big eyes', 'eats mice'],
          'frog': ['pond', 'green', 'tongue', 'amphibian', 'eats flies'],
          'toucan': ['rainbow', 'long beak', 'South America', 'tropical', 'wings'],
          'monkey': ['eats bananas', 'trees', 'tail', 'swing', 'primate'],
          'shark': ['ocean', 'dangeous', 'cartilege', 'sharp teeth', 'fins'],
          'zebra': ['stripes', 'black and white', 'africa', 'safari', 'hoofs'],
          'wolverine': ['vicious', 'skunk bear', 'brown', 'small', 'fast']}

        ranimal = random.choice(dict(enumerate(animal)))
        val = animal[ranimal]
        guesses = 7
        print("A N I M A L-G A M E!")
        time.sleep(2)
        clear()
        print("Try to guess the animal. You have 7 tries. It is in all lowercase.")
        input(':> ')
        clear()
        while True:
          print("Clues:",', '.join(val))
          guess = input("Animal: ")
          if guess == ranimal:
            print(f"Correct answer! You guessed it in {guesses} tries! Heading back to main lobby...")
            time.sleep(2)
            clear()
            break
          if guess in animal.keys():
            guesses-=1
            print(f"Try again! You have {guesses} tries left.")
            time.sleep(2)
            clear()
          if guesses == 0:
            print(f"You lost! The correct animal was {ranimal}.")
            time.sleep(2)
            clear()
            break
          else:
            guesses-=1
            print(f"Wrong! You have {guesses} tries left.")
            time.sleep(2)
            clear()
        print(f"[{botname}]: Hello {owner}! What can I do for you?")

      elif game == '3':
        print(f"[{botname}]: Loading game...")
        time.sleep(2)
        clear()
        guesses = 1
        guessesleft = 7
        rnum = random.randint(1,100)

        print("N U M B E R-G A M E!")
        time.sleep(2)
        clear()
        print("Try to guess the number. It is in between 1-100. Try to guess it and you have 7 tries.")
        input(':> ')
        clear()
          
        while True:
          try:
            ask = int(input('Number: '))
          except:
            print("Not a number!")
            time.sleep(2)
            clear()
            continue
            
          if ask == rnum:
            print(f"You won! You guessed it in {guessesleft} tries!")
            time.sleep(2)
            clear()
            break
          if ask > rnum:
            guesses+=1
            guessesleft-=1
            print(f"Too high! You have {guessesleft} tries left")
            time.sleep(2)
            clear()
          if ask < rnum:
            guesses+=1
            guessesleft-=1
            print(f"Too low! You have {guessesleft} tries left")
            time.sleep(2)
            clear()
          if guessesleft == 0:
            print(f"You lost! The correct number was {rnum}!")
            time.sleep(2)
            clear()
            break

        print(f"[{botname}]: Hello {owner}! What can I do for you?")

      else:
        print(f"[{botname}]: Sorry, I couldn't quite understand that. Try again")
    
    elif yn == 'n' or yn == 'nope' or yn == 'no' or yn == 'shut up':
      print(f"[{botname}]: Ok. Heading back to main lobby...")
      time.sleep(2)
    
    else:
      print(f"[{botname}]: Sorry, I couldn't understand that. Try again!")
  

  #useless
  elif ci == 'i love you' or ci == 'i luv u' or ci == 'i love u' or ci == 'i luv you':
    print(f"[{botname}]: Really? I hate you. >:D")
  
  elif ci == 'shutup' or ci == 'shut up':
    print(f"[{botname}]: Please do not say such offensive words. I am trying to help as much as I can.")

  elif ci == 'play music' or ci == 'playmusic' or ci == 'play-music':
    pass

  #else
  else:
    print(f"[{botname}]: Sorry, I couldn't understand that. Could you say that again?")