from kivy.app import App
from kivy.uix.label import Label

class ESP32App(App):
    def build(self):
        return Label(text="ESP32 App Ready")

if __name__ == "__main__":
    ESP32App().run()
  
