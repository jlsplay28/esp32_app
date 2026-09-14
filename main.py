from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import serial
import serial.tools.list_ports

class ESP32ControllerApp(App):
    def build(self):
        self.title = "ESP32 USB-OTG Controller"
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.status_label = Label(text='Status: Desconectado', font_size=18)
        self.layout.add_widget(self.status_label)
        
        btn_connect = Button(text='Conectar ESP32 (USB)', size_hint=(1, 0.2))
        btn_connect.bind(on_press=self.connect_esp32)
        self.layout.add_widget(btn_connect)
        
        btn_led = Button(text='Enviar Comando LED', size_hint=(1, 0.2))
        btn_led.bind(on_press=self.send_command)
        self.layout.add_widget(btn_led)
        
        return self.layout

    def connect_esp32(self, instance):
        try:
            ports = list(serial.tools.list_ports.comports())
            if not ports:
                self.status_label.text = 'Nenhuma porta USB encontrada!'
                return
            
            port_name = ports[0].device
            self.serial_conn = serial.Serial(port_name, 115200, timeout=1)
            self.status_label.text = f'Conectado em: {port_name}'
        except Exception as e:
            self.status_label.text = f'Erro: {str(e)}'

    def send_command(self, instance):
        try:
            if hasattr(self, 'serial_conn') and self.serial_conn.is_open:
                self.serial_conn.write(b'LED_ON\n')
                self.status_label.text = 'Comando enviado!'
            else:
                self.status_label.text = 'Erro: Porta nao aberta'
        except Exception as e:
            self.status_label.text = f'Erro ao enviar: {str(e)}'

if __name__ == '__main__':
    ESP32ControllerApp().run()
    
