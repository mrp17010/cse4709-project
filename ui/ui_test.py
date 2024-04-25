import paho.mqtt.publish as publish
import tkinter as tk

class PublishUI:
    def __init__(self): 
        self.root = tk.Tk()
        
        self.options = [
            "Car 1",
            "Car 2",
            "All"
        ]

        self.label = tk.Label(self.root, text="Please specify the host of the mqtt broker in the field below\nUse the buttons below to control the car. Alternatively you can move with the arrow keys on your keyboard.", font=("Arial",16),)
        self.label.pack(pady='10')

        self.selectedTopic = tk.StringVar(self.root)

        self.textbox_host = tk.Text(self.root, font=('Arial',14))
        self.textbox_host.pack()

        self.topic_select = tk.OptionMenu(self.root, self.selectedTopic, *self.options)
        self.topic_select.pack()

        self.button_forward = tk.Button(self.root, text="Forward", font=('Arial', 12), command=self.move_forward)
        self.button_forward.pack(padx=10, pady=5)

        self.button_backward = tk.Button(self.root, text="Backward", font=('Arial', 12), command=self.move_backward)
        self.button_backward.pack(padx=10, pady=5)

        self.button_stop = tk.Button(self.root, text="Stop", font=('Arial', 12), command=self.move_stop)
        self.button_stop.pack(padx=10, pady=5)

        self.root.mainloop()


    def show_message(self):
        print(self.textbox.get('1.0','end-1c'))

    def move_forward(self):
        if(self.selectedTopic.get() == "Car 1"):
            publish.single("car_test1", 1, hostname=self.textbox_host.get("1.0",'end-1c'))
        if(self.selectedTopic.get() == "Car 2"):
            publish.single("car_test2", 1, hostname=self.textbox_host.get("1.0",'end-1c'))
        if(self.selectedTopic.get() == "All"):
            publish.single("car_test1", 1, hostname=self.textbox_host.get("1.0",'end-1c'))
            publish.single("car_test2", 1, hostname=self.textbox_host.get("1.0",'end-1c'))

    def move_backward(self):
        if(self.selectedTopic.get() == "Car 1"):
            publish.single("car_test1", 2, hostname=self.textbox_host.get("1.0",'end-1c'))
        if(self.selectedTopic.get() == "Car 2"):
            publish.single("car_test2", 2, hostname=self.textbox_host.get("1.0",'end-1c'))
        if(self.selectedTopic.get() == "All"):
            publish.single("car_test1", 2, hostname=self.textbox_host.get("1.0",'end-1c'))
            publish.single("car_test2", 2, hostname=self.textbox_host.get("1.0",'end-1c'))

    def move_stop(self):
        if(self.selectedTopic.get() == "Car 1"):
            publish.single("car_test1", 0, hostname=self.textbox_host.get("1.0",'end-1c'))
        elif(self.selectedTopic.get() == "Car 2"):
            publish.single("car_test2", 0, hostname=self.textbox_host.get("1.0",'end-1c'))
        elif(self.selectedTopic.get() == "All"):
            publish.single("car_test1", 0, hostname=self.textbox_host.get("1.0",'end-1c'))
            publish.single("car_test2", 0, hostname=self.textbox_host.get("1.0",'end-1c'))

PublishUI()