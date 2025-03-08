''' This code was developed by Ateufo Arthur. '''
#coding: utf-8
import time

class Chrono:
    def __init__(self):
        self.t_start = 0.0  # initialize t_start
        self.t_end = 0.0    # initialize t_end

    def start(self):
        self.t_start = time.time()  # record start time

    def end(self):
        self.t_end = time.time()  # record end time
        duration = self.t_end - self.t_start  # Calculate the program duration

        # Convert the duration in hours, minutes, seconds, millisecond
        heures = int(duration // 3600)
        minutes = int((duration % 3600) // 60)
        seconds = int(duration % 60)
        millisecond = int((duration - int(duration))* 1000)

        # Display the résultat in format hh:mm:ss:ms
        print(f"{heures:02}:{minutes:02}:{seconds:02}:{millisecond:3}")

if __name__ =='__main__':
    test=Chrono()
    test.start()
    time.sleep(1)
    test.end()
    print("this program is working true")
