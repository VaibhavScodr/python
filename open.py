# import cv2

# face_cap = cv2.CascadeClassifier("C:/site-packages/cv2/data/haarcascade_frontalface_default.xml")
# video_cap=cv2.VideoCapture(0)

# while True:
#     ret , video_data = video_cap.read()
#     col=cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
#     faces = face_cap.detectMultiScale(
#         col,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30,30),
#         flag=cv2.CASCADE_SCALE_IMAGE
#     )
#     for(x,y,w,h) in faces:
#         cv2.rectange(video_data,(x,y),(x+w,y+h),(0,255,0),2)
#     cv2.imshow("video_live",video_data)
#     if(cv2.waitKey(10) == ord("a")):
#         break
# video_cap.release()

from tkinter import *
from tkinter import ttk
import requests

def data_get():
        city=city_name.get()
        data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=30c972d60396968a6bc65e5bb2b61a3b").json()
        w1_label.config(text=data["weather"][0]["main"])
        wb1_label.config(text=(data["weather"][0]["description"]))
        wt1_label.config(text=data["main"]["temp"]-273.15)
        wp1_label.config(text=data["main"]["pressure"])

win= Tk()
win.title("Weather App")
win.config(bg="skyblue")
win.geometry('500x570')
name_label= Label(win,text='Weather APP',font=("Time New Roman",40,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

city_name = StringVar()
com = ttk.Combobox(win,text='Weather APP',values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

#done_button =Button(win,text='Done',font=("Time New Roman",20,"bold"))
#done_button.place(y=190,height=50,width=100,x=200)

w_label= Label(win,text='Weather Climate',font=("Time New Roman",17))
w_label.place(x=25,y=260,height=50,width=210)
w1_label= Label(win,text='',font=("Time New Roman",20))
w1_label.place(x=250,y=260,height=50,width=210)


wb_label= Label(win,text='Weather Description',font=("Time New Roman",15))
wb_label.place(x=25,y=330,height=50,width=210)
wb1_label= Label(win,text='',font=("Time New Roman",20))
wb1_label.place(x=250,y=330,height=50,width=210)


wt_label= Label(win,text='Temprature',font=("Time New Roman",17))
wt_label.place(x=25,y=400,height=50,width=210)
wt1_label= Label(win,text='',font=("Time New Roman",20))
wt1_label.place(x=250,y=400,height=50,width=210)


wp_label= Label(win,text='Pressure',font=("Time New Roman",20))
wp_label.place(x=25,y=470,height=50,width=210)
wp1_label= Label(win,text='',font=("Time New Roman",20))
wp1_label.place(x=250,y=470,height=50,width=210)

done_button =Button(win,text='Done',font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)


win.mainloop()