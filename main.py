import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import csv


class MainWindow():
    def __init__(self, window):
        self.window = window

        self.pre_index = "/PW20210224-0225-"

        self.result = []
        self.datalog = 'result.csv'

        self.image_ID = 1
        self.image_height = 1100
        self.image_width = 1100

        self.current_img = None

        self.format = ".jpg"

        self.read_log()

        self.set_up_window(window)


    def load_image(self):
        self.directory = filedialog.askdirectory()
        self.update_img()
        self.one_btn.config(state="normal")
        self.two_btn.config(state="normal")
        self.three_btn.config(state="normal")
        self.four_btn.config(state="normal")
        self.five_btn.config(state="normal")

        self.previous.config(state="normal")
        self.next.config(state="normal")

    def read_log(self):
        try:
            with open(self.datalog) as logfile:
                spamreader = csv.reader(logfile, delimiter=' ')
                i = 1
                for row in spamreader:
                    self.result.append(["PW20210224-0225-{}".format(i), row[0]])
                    i += 1
        except:
            self.create_img_log()
            self.read_log()

    def change_log(self, rate):
        self.result[self.image_ID - 1][1] = rate

    def create_img_log(self):
        try:
            with open(self.datalog, 'w', newline='') as logfile:
                csvwriter = csv.writer(logfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for i in range(1,729):
                    csvwriter.writerow(["None"])
        except:
            pass

    def write_log(self, rate, ID):
        log = open(self.datalog, 'a')
        log.write("{}|{}\n".format(rate, ID))

    def get_previous(self):
        if self.image_ID == 1:
            tk.messagebox.showinfo(message="This is the first image!")
        else:
            self.image_ID -= 1
            self.update_img()

    def get_next(self):
        if self.image_ID == 728:
            tk.messagebox.showinfo(message="This is the last image!")
        else:
            self.image_ID += 1
            self.update_img()

    def one_pt(self):
        self.photo_ID_lb.config(text="PW20210224-0225-{}".format(self.image_ID))
        self.change_log(1)

        self.image_ID += 1
        self.update_img()

    def two_pt(self):
        self.photo_ID_lb.config(text="PW20210224-0225-{}".format(self.image_ID))
        self.change_log(2)

        self.image_ID += 1
        self.update_img()

    def three_pt(self):
        self.photo_ID_lb.config(text="PW20210224-0225-{}".format(self.image_ID))
        self.change_log(3)

        self.image_ID += 1
        self.update_img()

    def four_pt(self):
        self.photo_ID_lb.config(text="PW20210224-0225-{}".format(self.image_ID))
        self.change_log(4)

        self.image_ID += 1
        self.update_img()

    def five_pt(self):
        self.photo_ID_lb.config(text="PW20210224-0225-{}".format(self.image_ID))
        self.change_log(5)

        self.image_ID += 1
        self.update_img()

    def convert2tk(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # to RGB
        img = Image.fromarray(img)  # to PIL format
        img = ImageTk.PhotoImage(img)  # to ImageTk format
        return img

    def update_img(self):
        try:
            self.current_img = cv2.imread(self.directory + self.pre_index + str(self.image_ID) + self.format)
            self.photo_ID_lb.config(text="PW20210224-0225-{}".format(self.image_ID))
            scale_percent = 18  # percent of original size
            width = int(self.current_img.shape[1] * scale_percent / 100)
            height = int(self.current_img.shape[0] * scale_percent / 100)
            dim = (width, height)
            self.current_img = cv2.resize(self.current_img, dim, interpolation=cv2.INTER_AREA)
            self.tk_img = self.convert2tk(self.current_img)

            self.canvas_ori.create_image(width / 2, height / 2, anchor=tk.CENTER, image=self.tk_img)

            if self.result[self.image_ID - 1][1] != 'None':
                self.rate_lb.config(text=str(self.result[self.image_ID - 1][1]))
            else:
                self.rate_lb.config(text="")
        except:
            tk.messagebox.showinfo(title="Warning", message="Wrong folder!")

    def set_up_window(self, window):
        window.title("Gallery")
        # window.geometry("{}x{}".format(window_width, window_height))

        # Image Canvas
        self.canvas_ori = tk.Canvas(window, width=self.image_width, height=self.image_height)
        self.canvas_ori.grid(row=0, column=0, rowspan=3, columnspan=4, padx=5, pady=5)

        # Rate Label

        self.rate_lb = tk.Label(window, text="", font="Helvetica 40 bold", width = 5)
        self.rate_lb.grid(row=1, column=5, padx=5, pady=5)

        # # Buttons
        self.one_btn = tk.Button(window, text="1", command=self.one_pt,
                                 font="Helvetica 16 bold", width=10, bg='#adadad', fg='black', state='disabled')
        self.one_btn.grid(row=6, column=0, padx=5, pady=5)

        self.two_btn = tk.Button(window, text="2", command=self.two_pt,
                                 font="Helvetica 16 bold", width=10, bg='#adadad', fg='black', state='disabled')
        self.two_btn.grid(row=6, column=1, padx=5, pady=5)

        self.three_btn = tk.Button(window, text="3", command=self.three_pt,
                                   font="Helvetica 16 bold", width=10, bg='#adadad', fg='black', state='disabled')
        self.three_btn.grid(row=6, column=2, padx=5, pady=5)

        self.four_btn = tk.Button(window, text="4", command=self.four_pt,
                                  font="Helvetica 16 bold", width=10, bg='#adadad', fg='black', state='disabled')
        self.four_btn.grid(row=6, column=3, padx=5, pady=5)

        self.five_btn = tk.Button(window, text="5", command=self.five_pt,
                                  font="Helvetica 16 bold", width=10, bg='#adadad', fg='black', state='disabled')
        self.five_btn.grid(row=6, column=4, padx=5, pady=5)

        self.Load_images = tk.Button(window, text="Load Images", command=self.load_image,
                                     font="Helvetica 16 bold", width=79, bg='#3b38ff', fg='white')
        self.Load_images.grid(row=7, column=0, columnspan=5, padx=5, pady=5)

        self.previous = tk.Button(window, text="Previous", command=self.get_previous,
                                  font="Helvetica 16 bold", width=10, bg='#3b38ff', fg='white', state='disabled')
        self.previous.grid(row=4, column=1, padx=5, pady=5)

        self.next = tk.Button(window, text="Next", command=self.get_next,
                              font="Helvetica 16 bold", width=10, bg='#3b38ff', fg='white', state='disabled')
        self.next.grid(row=4, column=3, padx=5, pady=5)

        self.photo_ID_lb = tk.Label(window, text="", font="Helvetica 12 bold")
        self.photo_ID_lb.grid(row=4, column=2, padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    main_window = MainWindow(root)
    root.mainloop()
    with open(main_window.datalog, 'w', newline='') as logfile:
        csvwriter = csv.writer(logfile, delimiter=' ',
                               quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(1, 729):
            csvwriter.writerow([main_window.result[i - 1][1]])
