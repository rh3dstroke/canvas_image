import customtkinter as ctk    # customtkinter      5.2.2  
import tkinter                 # tk                 0.1.0
from tkinter import ttk
import os
import openai                  # openai             0.28.0 
from PIL import Image, ImageTk # pillow             10.2.0
import requests, io            # requests           2.31.0
"""
(image we’re promoting), (5 description keywords or phrases), 
(camera model and lens), (lighting), 
(style of photograph), (type of fllm)
"""
def generate():
    # Attempt to get the OPENAI_API_KEY from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    # Check if the API key was successfully retrieved
    if api_key is None:
        raise ValueError("OPENAI_API_KEY environment variable not found.")
    else:
        # Set the API key for the OpenAI package, model = "dall-e-3"
        openai.api_key = api_key
        print("OPENAI_API_KEY found and set successfully!")
    
    user_prompt = prompt_entry.get("0.0", tkinter.END)
    # style_dropdown_1-9
    user_prompt += "in style: "+ style_dropdown_1.get()+ style_dropdown_2.get()+ style_dropdown_3.get()+ style_dropdown_4.get()+ style_dropdown_5.get()+ style_dropdown_6.get()+ style_dropdown_7.get()+ style_dropdown_8.get()+ style_dropdown_9.get()
    # user prompt
    response = openai.Image.create(
        prompt=user_prompt,
        n=int(number_slider.get()),
        # size 512x512
        size="512x512"
    )

    image_urls = []
    for i in range(len(response['data'])):
        image_urls.append(response['data'][i]['url'])
    print(image_urls)

    images = []
    for url in image_urls:
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        photo_image = ImageTk.PhotoImage(image)
        images.append(photo_image)

    def update_image(index=0):
        canvas.image = images[index]
        canvas.create_image(0, 0, anchor="nw", image=images[index])
        index = (index + 1) % len(images) 
        canvas.after(5000, update_image, index)

    update_image()

if __name__ == '__main__': 
    window = ctk.CTk()    
    window.title("AI Image Generator")
    window.iconbitmap('image/Gartoon-python.ico')

    ctk.set_appearance_mode("dark")

    input_frame = ctk.CTkFrame(window)
    input_frame.pack(side="left", expand=True, padx=20, pady=20)

    # insert ->         ->        ->   padx=5, pady=5
    # style_label_1    row=1        
    style_label_1 = ctk.CTkLabel(input_frame, text="Style")
    style_label_1.grid(row=1,column=0, padx=5, pady=5)
    style_dropdown_1 = ctk.CTkComboBox(input_frame, values=["Photography", "Cartoon", "Anime", "Cinematic", "Comic Book", "Fantasy Art"])
    style_dropdown_1.grid(row=1, column=1, padx=5, pady=5)

    # style_label_2    row=2
    style_label_2 = ctk.CTkLabel(input_frame, text="Gender")
    style_label_2.grid(row=2,column=0, padx=5, pady=5)
    style_dropdown_2 = ctk.CTkComboBox(input_frame, values=["I single Male", "I single Famale", "I single Other"])
    style_dropdown_2.grid(row=2, column=1, padx=5, pady=5)

    # style_label_3    row=3
    style_label_3 = ctk.CTkLabel(input_frame, text="Place to go")
    style_label_3.grid(row=3,column=0, padx=5, pady=5)
    style_dropdown_3 = ctk.CTkComboBox(input_frame, values=["a Desk", "a Gym", "a Golf", "a Yoga", "a Car", "a Truck", "a Patio"])
    style_dropdown_3.grid(row=3, column=1, padx=5, pady=5)

    # style_label_4    row=4
    style_label_4 = ctk.CTkLabel(input_frame, text="Handicap")
    style_label_4.grid(row=4,column=0, padx=5, pady=5)
    style_dropdown_4 = ctk.CTkComboBox(input_frame, values=["Holding on a cane", "In a wheelchair", "Holding to canes"])
    style_dropdown_4.grid(row=4, column=1, padx=5, pady=5)

    # style_label_5    row=5
    style_label_5 = ctk.CTkLabel(input_frame, text="Build")
    style_label_5.grid(row=5,column=0, padx=5, pady=5)
    style_dropdown_5 = ctk.CTkComboBox(input_frame, values=["Light build", "Medium build", "Large build"])
    style_dropdown_5.grid(row=5, column=1, padx=5, pady=5)

    # style_label_6    row=6
    style_label_6 = ctk.CTkLabel(input_frame, text="Head Hair")
    style_label_6.grid(row=6,column=0, padx=5, pady=5)
    style_dropdown_6 = ctk.CTkComboBox(input_frame, values=["Head No hair", "Head Short hair", "Head Medium hair", "Head Long hair"])
    style_dropdown_6.grid(row=6, column=1, padx=5, pady=5)

    # style_label_7    row=7                    Adaptive
    style_label_7 = ctk.CTkLabel(input_frame, text="Facial Hair")
    style_label_7.grid(row=7,column=0, padx=5, pady=5)
    style_dropdown_7 = ctk.CTkComboBox(input_frame, values=["clean shaven", "with a goatee", "with a moustache", "with a beard"])
    style_dropdown_7.grid(row=7, column=1, padx=5, pady=5)

    # style_label_8    row=8
    style_label_8 = ctk.CTkLabel(input_frame, text="Glasses")
    style_label_8.grid(row=8,column=0, padx=5, pady=5)
    style_dropdown_8 = ctk.CTkComboBox(input_frame, values=["", "glasses square frames", "glasses with medium frames", "with glasses big frames"])
    style_dropdown_8.grid(row=8, column=1, padx=5, pady=5)

    # style_label_9    row=9
    style_label_9 = ctk.CTkLabel(input_frame, text="Close")
    style_label_9.grid(row=9,column=0, padx=5, pady=5)
    style_dropdown_9 = ctk.CTkComboBox(input_frame, values=["Jeans and T-shirt red", "Blue Suit", "Shorts and T-shirt", "Dress", "Skirt and top"])
    style_dropdown_9.grid(row=9, column=1, padx=5, pady=5)

    prompt_label = ctk.CTkLabel(input_frame, text="Prompt")
    prompt_label.grid(row=10,column=0, padx=10, pady=10)
    prompt_entry = ctk.CTkTextbox(input_frame, height=10)
    prompt_entry.grid(row=10,column=1, padx=10, pady=10)

    style_label_10 = ttk.Label(master=window, text='label')
    """
    #CTkButton
    exercise_button = ctk.CTkButton(master=window, text='The button', command=button_func)
    exercise_button.pack()
    """
    number_label = ctk.CTkLabel(input_frame, text="# Images")
    number_label.grid(row=11,column=0)
    number_slider = ctk.CTkSlider(input_frame, from_=1, to=2, number_of_steps=3)
    number_slider.grid(row=11,column=1)

    generate_button = ctk.CTkButton(input_frame, text="Generate", command=generate)
    generate_button.grid(row=12, column=0, columnspan=2, sticky="news", padx=10, pady=10)

    canvas = tkinter.Canvas(window, width=512, height=512)
    canvas.pack(side="left")
    #mail()  #window()  #app()  #root()  =Add()
    window.mainloop()    