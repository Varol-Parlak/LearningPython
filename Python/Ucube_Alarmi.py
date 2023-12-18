import cv2 as cv
import imutils
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

counter = 0
sent = False
password = "plkn mhnl febb gacp"
from_email = "pvarolyilmaz@gmail.com"
to_email = "tolgacaner710@gmail.com"

server = smtplib.SMTP(host="smtp.gmail.com", port=587)
server.starttls()
server.login(from_email, password)

def send_email(to_email, from_email,frame):
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = "Ucube Alarmı!"
    message.attach(MIMEText("Varol, Bir Ucube Bilgisayarına Girmeye Çalışıyor!"))
  
    _, buffer = cv.imencode(".jpg", frame)
    photo = MIMEImage(buffer.tobytes(), name="ucube_foto.jpg")
    message.attach(photo)

    server.sendmail(from_email, to_email, message.as_string())

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)

_, first_frame = cap.read()

first_frame = imutils.resize(first_frame, width=500)
first_frame = cv.cvtColor(first_frame, cv.COLOR_BGR2GRAY)
first_frame = cv.GaussianBlur(first_frame, (21, 21), 0)


while True:
    _, frame = cap.read()
    frame = imutils.resize(frame, width=500)

    frame_bw = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_bw = cv.GaussianBlur(frame_bw, (5, 5), 0)

    diff = cv.absdiff(frame_bw, first_frame)

    _, threshold = cv.threshold(diff, 25, 255, cv.THRESH_BINARY)

    first_frame = frame_bw

    if threshold.sum() > 600:
        counter += 1

    else:
        if counter > 0 :
            counter -=1

    if counter > 20:
        if sent==False:
            send_email(to_email,from_email,frame)
            sent = True
            break

    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
