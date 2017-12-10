#!/usr/bin/python
import sys
import threading
from clock import Clock
#from tail import tail
import time

from pylcdsysinfo import LCDSysInfo, TextLines, BackgroundColours, TextColours


class LCD():

    bg = BackgroundColours.BLACK

    def __init__(self):
        self.d = LCDSysInfo()
        self.d.clear_lines(TextLines.ALL, self.bg)
        self.d.dim_when_idle(False)
        self.d.set_brightness(127)
        self.d.save_brightness(127, 255)
        self.d.set_text_background_colour(self.bg)

        self.start_clock_thread()

    def run(self):
        try:
            while True:
                self.display_clock(self.c.time)

#                self.d.display_text_on_line(4, 'aaaaaaa', False, None, TextColours.GREEN)
#                time.sleep(2)
#                self.d.clear_lines(TextLines.LINE_4, self.bg)
#                time.sleep(2)
#                for i in range(0, tail_rows):
#                    d.display_text_on_line(6-i, t.p[i], False, None, i)

        except KeyboardInterrupt:
            self.c.exit = True
            self.d.display_text_on_line(3, 'Bye!', False, 0, TextColours.PINK)
            #t.exit = True

    def start_tail_thread(self):
        self.t = tail(tail_rows)
        threading.Thread(target=self.t.run).start()

    def start_clock_thread(self):
        self.c = Clock()
        threading.Thread(target=self.c.run).start()

    def display_clock(self, time):
        self.d.display_text_on_line(1, time[11:19], False, None, TextColours.GREEN)
        self.d.display_text_anywhere(150, 0, time[:3], TextColours.RED)
        self.d.display_text_anywhere(222, 0, time[4:10], TextColours.GOLD)


if __name__ == "__main__":
    lcd = LCD()
    lcd.run()

    sys.exit(0)
