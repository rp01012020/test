import smtplib
import sys, getopt


def usage():
    print('sendemail.py -u <username> -p <password> -t <sendto> -m <message>')

def main(argv):
    username = ''
    password = ''
    sendto = ''
    message = ''
    print('Helloworld')
    try:
        opts, args = getopt.getopt(argv, 'h:u:p:t:m:', ['username=', 'password=', 'sendto=', 'message='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    print('options :',  opts)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(2)
        elif opt in ('-u', '--username'):
            username = arg
        elif opt in ('-p', '--password'):
            password = arg
        elif opt in ('-t', '--sendto'):
            sendto = arg
        elif opt in ('-m', '--message'):
            message = arg
        else:
            usage()
            sys.exit(2)
    smtpsrv = 'smtp.office365.com'
    smtpserver = smtplib.SMTP(smtpsrv, 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(username, password)
    header = 'To:' + sendto + 'n' + 'From: ' + username + 'n' + 'Subject:testing n'
    print(header)
    msgbody = header + 'n %s nn' % message
    smtpserver.sendmail(username, sendto, msgbody)
    print('done!')
    smtpserver.close()
if __name__ == '__main__':
    main(sys.argv[1:])
