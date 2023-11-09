import customtkinter
import os
from PIL import Image
import pandas as pd
import plotly.graph_objects as go

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Trading Bot GUI")
        self.geometry("1280x700")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "logo_testLIGHT.png")),
                                                  dark_image=Image.open(os.path.join(image_path, "logo_test.png")),size=(150, 60))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CANDLE_STICK_chart.jpg")), size=(1000, 400))
        self.large_test_image2 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "StochRSI_chart.jpg")), size=(1000, 200))
        self.large_test_image3 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "table_data.png")), size=(580, 620))
        self.image_icon_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "refresh_light.png")),
                                                        dark_image=Image.open(os.path.join(image_path, "refresh_dark.png")),size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chart.png")),
                                                dark_image=Image.open(os.path.join(image_path, "chartLIGHT.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "list.png")),
                                                dark_image=Image.open(os.path.join(image_path, "listLIGHT.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "bar-chart.png")),
                                                    dark_image=Image.open(os.path.join(image_path, "bar-chartLIGHT.png")), size=(20, 20))
        
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=10, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=10, height=40, border_spacing=10, text="CHARTS",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=10, height=40, border_spacing=10, text="TRADES",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=10, height=40, border_spacing=10, text="SETTINGS",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=[ "Light", "Dark", "System"], 
                                                                fg_color=("gray70", "gray25"),button_color=("gray70", "gray30"),
                                                                button_hover_color=("gray60", "gray50"), text_color=("gray10", "gray90"),
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image,corner_radius=0) #CANDLE STICK
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_large_image_label2 = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image2) # STOCH RSI
        self.home_frame_large_image_label2.grid(row=1, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, image=self.image_icon_image, corner_radius=10, height=40, 
                                                           border_spacing=10, text="REFRESH",fg_color=("gray85", "gray25"), 
                                                           text_color=("gray10", "gray90"), hover_color=("gray70", "gray40"), 
                                                           command=self.reload_images)
        self.home_frame_button_1.grid(row=2, column=0, padx=20, pady=10)
        #self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        #self.home_frame_button_2.grid(row=1, column=0, padx=20, pady=10)
        #self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        #self.home_frame_button_3.grid(row=1, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)

        # create Dataframe image
        self.second_frame_large_image_label = customtkinter.CTkLabel(self.second_frame, text="", image=self.large_test_image3,corner_radius=0) #DATA FRAME
        self.second_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)


        self.second_frame_button_1 = customtkinter.CTkButton(self.second_frame, image=self.image_icon_image, corner_radius=10, height=40, 
                                                           border_spacing=10, text="HISTORICAL DATA",fg_color=("gray85", "gray25"), 
                                                           text_color=("gray10", "gray90"), hover_color=("gray70", "gray40"), 
                                                           command=self.data_http_viewer)
        self.second_frame_button_1.grid(row=2, column=0, padx=20, pady=10)
        

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("CHARTS")

    def reload_images(self):
         #reload images
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CANDLE_STICK_chart.jpg")), size=(1000, 400))
        self.large_test_image2 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "StochRSI_chart.jpg")), size=(1000, 200))

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image,corner_radius=0) #CANDLE STICK
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_large_image_label2 = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image2) # STOCH RSI
        self.home_frame_large_image_label2.grid(row=1, column=0, padx=20, pady=10)

    # View historical data in HTTP mode
    def data_http_viewer(self):
        df = pd.read_csv('historic_CHART_values.csv')
        df = df.sort_index(ascending=False)

        fig = go.Figure(data=[go.Table(
            header=dict(values=list(df.columns),
                        fill_color='paleturquoise',align='left'),
            cells=dict(values=[df['Time'].str.slice(0, 16), df['Open'], df['High'], df['Low'], 
                            df['Close'], df['stochrsi_k'], df['Buy'],df['Sell']],
                    fill_color='lavender',align='left'))])
        fig.show()

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "CHARTS" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "TRADES" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "SETTINGS" else "transparent")

        # show selected frame
        if name == "CHARTS":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "TRADES":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "SETTINGS":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("CHARTS")

    def frame_2_button_event(self):
        self.select_frame_by_name("TRADES")

    def frame_3_button_event(self):
        self.select_frame_by_name("SETTINGS")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()