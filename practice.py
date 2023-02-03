class Car(object):

    def __init__(self,model,color,speed) :
        self.model = model
        self.color = color
        self.speed = speed

    def start(self):
        print("started")

    def stop(self):
        print("stopped")    

audi = Car ("A6","black","200")
audi.start()
audi.stop()