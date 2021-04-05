from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from tkinter import *

first = 1


def enter_button():
    global first
    if first == 1:
        shearch = browser.find_element_by_xpath("//div[2]/div[1]/div[1]/div/div[2]/input")
        first = 0
    else:
        shearch = browser.find_element_by_xpath("//div[2]/div[1]/div[2]/div/div[2]/input")
        shearch.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
    shearch.send_keys(str(city.get()) + " weather")
    shearch.send_keys(Keys.ENTER)
    weather = browser.find_element_by_id("wob_tm")
    weather_text = Label(window, text="The temperature in " + str(city.get()) + " is " + str(weather.text) + "°C.",
                         font=("arial", 30, "bold"), bg="#8dcff4", fg="white").place(x=533, y=510)


window_size = "1920,1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % window_size)
browser = webdriver.Chrome('chromedriver', options=chrome_options)
browser.get("https://www.google.com/")

window = Tk()
window.geometry("1300x900")
photo = PhotoImage(file='WeatherForecast.png')
labelPhoto = Label(window, image=photo)
labelPhoto.pack()

city = StringVar()
entryBox = Entry(window, textvariable=city, width=25, bg="lightblue").place(x=290, y=525)
button = Button(window, text="Enter", width=10, height=1, bg="lightblue", command=enter_button).place(x=448, y=522)

window.mainloop()

