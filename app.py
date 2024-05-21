from flask import Flask, render_template, redirect
import os
import cv2
import pyautogui
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/learn')
def learn():
    youtube_url = "https://youtube.com/playlist?list=PLxYMaKXKMMcMgg4f47WkG7AM0bb3AyjTi&si=GG2_V1yxcBhZtk_c"
    return redirect(youtube_url, code=302)

@app.route('/interpret')
def interpret():
    return render_template('interpret.html')

@app.route('/opencam')
def opencam():
    os.system("python yolov5\detect.py --weights best.pt --img 416 --conf 0.5 --source 0")
    return 'cam open'

@app.route('/closecam')
def closecam():
    pyautogui.press('q')
    return "camera closed"

if __name__ == '__main__':
    app.run(debug=True)