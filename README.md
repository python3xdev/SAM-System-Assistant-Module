# SAM (System Assistant Module)

#### DISCLAIMER - some commands might not work for operating systems other than windows.

Sam was developed on a windows 10 operating system. So the voice commands for opening programs will not work on other operating systems (unless you customize/edit the paths).

### Package Installation

Open a cmd/terminal in Sam's root directory. Type in the following command:

```
pip install -r requirements.txt
```

This will install all the required dependencies.

#### Problems you might run into during package installation:

If you get a **PyAudio** install error during package installation (like I did), find a version of **PyAudio** that is compatible with your python version and your systems architecture (32-bit/64-bit) on this site:

##### https://www.lfd.uci.edu/~gohlke/pythonlibs/

Then install the **.whl** file using **pip**. After that's done, run the previous command again (Just to be sure everything has installed properly).

### How To Use:

Before using Sam you must setup your config.json file. To do so, run the setup.py script, answer all the questions and a config.json file will be generated. Now you can start Sam by running the __ init__.pyw file (not in the cmd/terminal). Sam will be running in the background and waiting for keywords like 'Sam', 'Hey Sam', 'Ok Sam'. You can say 'Hey Google', 'Hey Siri' or 'Hey Alexa' for a special response.

**Tip**: after saying one of the activation commands, wait ~0.5 seconds after Sam says 'Yes?'. This way you don't repeat your self, it takes some time for Sam to start listening.

#### Commands:

After saying one of the activation commands ('Sam', 'Hey Sam', 'Ok Sam'), Sam will say 'Yes?'. Then he will start listening for additional commands. At this point you can use these commands:

| Voice Commands                                              | Explanation/Description                                      |
| ----------------------------------------------------------- | ------------------------------------------------------------ |
| what is 2 times 2 plus 4 squared minus 3 to the power of 4? | Sam can do math                                              |
| reboot                                                      | restart Sam                                                  |
| shutdown                                                    | shutdown Sam, exit the program                               |
| what is your name?                                          | Sam tells you his short and full name                        |
| help                                                        | opens this list of commands                                  |
| what can you do?                                            | same as 'help' command                                       |
| nevermind                                                   | Sam goes back to listening for activation keywords, his response: 'Ok' |
| what's the time?                                            | Sam tells you the time in the 24 hour format                 |
| what's the date?                                            | Sam tells you the day, month and year                        |
| open YouTube                                                | opens the YouTube website. Also works with: GitHub, Stack Overflow, Weather.com, Google Translate and Gmail |
| translate dog to Russian                                    | opens the Google Translate website with the word(s) translated to Russian |
| translate cat to Ukrainian                                  | opens the Google Translate website with the word(s) translated to Ukrainian |
| open {YOUR_BROWSER_NAME}                                    | this will open the 'custom' browser you specified during setup |
| open Google Chrome                                          | opens Google Chrome on *Windows 10* if it is in the default installation location |
| open Sublime Text                                           | opens Sublime Text 3 on *Windows 10* if it is in the default installation location |
| Dwayne Johnson Wikipedia                                    | reads out the first 2 sentences of the wiki page on what you asked |
| what is claustrophobia?                                     | explains what somethings means, first 2 sentences of the wiki page |
| send an email to {CONTACT_NAME}                             | send emails to contacts that you have specified during setup |

## Social Media

<a target="_blank" href="https://www.twitter.com/python3x_dev"><img src="https://icons-for-free.com/iconfiles/png/512/twitter+icon-1320185153780096253.png" width="100" height="100"></a>  <a target="_blank" href="https://www.github.com/python3xdev"><img src="https://icons-for-free.com/iconfiles/png/512/github+logo+social+social+network+website+icon-1320191930698657711.png" width="100" height="100"></a>  <a target="_blank" href="https://www.linkedin.com/in/daniel-martin-a59144125/"><img src="https://icons-for-free.com/iconfiles/png/512/linkedin+logo+social+social+network+website+icon-1320191931394618705.png" width="100" height="100"></a>