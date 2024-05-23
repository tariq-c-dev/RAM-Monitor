import psutil
import rumps
import subprocess
import os


def toggle_root():
    root.deiconify()

class RamUsageApp(rumps.App):
    def __init__(self):
        super(RamUsageApp, self).__init__("RAM")
        self.menu = [
            rumps.MenuItem('Memory Usage'),
        ]

    @rumps.timer(5)
    def update_ram_usage(self, _):
        usagePercent = psutil.virtual_memory().percent
        self.title = f"{usagePercent:.2f}%"
        self.menu['Memory Usage'].title = f"Usage: {usagePercent:.2f}%"

if __name__ == '__main__':
    app = RamUsageApp()
    app.run()
    root.mainloop()
