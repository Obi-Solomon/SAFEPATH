import os
import csv
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("Light") 

class EchoesOfHomeApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.init_csv()

        # Window Setup
        self.title("Safepath - Aina Onabolu Project")
        self.geometry("1000x750")
        self.configure(fg_color="#F4EBE1")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Load Gallery Images
        try:
            self.image_list = [
                ctk.CTkImage(light_image=Image.open("Rectangle 25.png"), size=(230, 140)),
                ctk.CTkImage(light_image=Image.open("Rectangle 26.png"), size=(230, 140)),
                ctk.CTkImage(light_image=Image.open("Rectangle 27.png"), size=(230, 140))
            ]
        except FileNotFoundError:
            self.image_list = [None, None, None]

        # Load Sidebar Icons (Kept fallback infrastructure if needed)
        icon_files = {
            "Dashboard": "dashboard_icon.png", "Situation Check": "situation_icon.png",
            "Report Case": "report_icon.png", "Records": "records_icon.png",
            "Insights": "insights_icon.png", "Resources": "resources_icon.png",
            "Echoes of Home": "echoes_icon.png", "Settings": "settings_icon.png"
        }
        
        self.icons = {}
        for name, file in icon_files.items():
            try:
                self.icons[name] = ctk.CTkImage(light_image=Image.open(file), size=(20, 20))
            except FileNotFoundError:
                self.icons[name] = None

        # --- SIDEBAR OUTLINE ---
        self.sidebar_frame = ctk.CTkFrame(self, fg_color="#4A2711", corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        # CHANGED: Updated App Name to Safepath and set the leading icon/text to an Olive Branch Emoji 🌿
        self.app_name = ctk.CTkLabel(
            self.sidebar_frame, 
            text="🌿 Safepath", 
            font=("Georgia", 24, "bold"), 
            text_color="#FFFFFF"
        )
        self.app_name.pack(pady=(40, 30), padx=20, anchor="w")

        # CHANGED: Replaced image icons with matching emojis directly inside the button text strings
        menu_items = {
            "Dashboard": "🏠 Dashboard",
            "Situation Check": "⚠️ Situation Check",
            "Report Case": "📝 Report Case",
            "Records": "📁 Records",
            "Insights": "📈 Insights",
            "Resources": "🎧 Resources"
        }

        for item, display_text in menu_items.items():
            btn = ctk.CTkButton(
                self.sidebar_frame, 
                text=f"  {display_text}", 
                fg_color="transparent", 
                text_color="#D1C2B7", 
                hover_color="#5D3216", 
                anchor="w", 
                font=("Arial", 14)
            )
            btn.pack(fill="x", padx=10, pady=5)

        # CHANGED: Added Globe emoji to Echoes of Home active button
        self.active_btn = ctk.CTkButton(
            self.sidebar_frame, 
            text="  🌐 Echoes of Home", 
            fg_color="#A0522D", 
            text_color="#FFFFFF", 
            anchor="w", 
            font=("Arial", 14, "bold"), 
            corner_radius=8
        )
        self.active_btn.pack(fill="x", padx=10, pady=5)

        # CHANGED: Added Gear emoji to Settings button
        self.settings_btn = ctk.CTkButton(
            self.sidebar_frame, 
            text="  ⚙️ Settings", 
            fg_color="transparent", 
            text_color="#D1C2B7", 
            hover_color="#5D3216", 
            anchor="w", 
            font=("Arial", 14)
        )
        self.settings_btn.pack(fill="x", padx=10, pady=5)

        self.tagline = ctk.CTkLabel(self.sidebar_frame, text="Awareness.Protection.Freedom", font=("Arial", 11, "italic"), text_color="#D1C2B7")
        self.tagline.pack(side="bottom", pady=20)

        # --- VIEW CONTAINERS ---
        self.main_container = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.main_container.grid(row=0, column=1, sticky="nsew", padx=40, pady=30)
        self.confirmation_container = ctk.CTkFrame(self, fg_color="transparent")

        # --- BUILD MAIN FORM PAGE ---
        self.title_label = ctk.CTkLabel(self.main_container, text="Echoes of Home", font=("Georgia", 28, "bold"), text_color="#2B1A0F")
        self.title_label.pack(anchor="w", pady=(0, 2))

        self.subtitle_label = ctk.CTkLabel(self.main_container, text="Exploring stories of displacement, resilience, and cultural reconnection.", font=("Arial", 14), text_color="#6E5D53")
        self.subtitle_label.pack(anchor="w", pady=(0, 25))

        self.cards_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.cards_frame.pack(fill="x", pady=(0, 30))
        
        for i in range(3):
            self.cards_frame.columnconfigure(i, weight=1, uniform="card")
            card = ctk.CTkFrame(self.cards_frame, height=140, fg_color="#D9C3B0", corner_radius=15)
            card.grid(row=0, column=i, padx=5, sticky="ew")
            card.grid_propagate(False)
            if self.image_list[i]:
                ctk.CTkLabel(card, text="", image=self.image_list[i]).pack(fill="both", expand=True)
            else:
                ctk.CTkLabel(card, text="Missing Image", text_color="#555").pack(expand=True)

        # Form Setup
        self.form_frame = ctk.CTkFrame(self.main_container, fg_color="#E6D5C3", border_color="#8B5A2B", border_width=1, corner_radius=15)
        self.form_frame.pack(fill="both", expand=True, pady=10, ipady=20)

        self.form_title = ctk.CTkLabel(self.form_frame, text="Share Your Story", font=("Georgia", 20, "bold"), text_color="#4A2711")
        self.form_title.pack(pady=(20, 15))

        self.input_row = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        self.input_row.pack(fill="x", padx=30, pady=5)
        self.input_row.columnconfigure(0, weight=1)
        self.input_row.columnconfigure(1, weight=1)

        self.name_entry = ctk.CTkEntry(self.input_row, placeholder_text="Name", font=("Georgia", 13, "italic"), fg_color="#F4EBE1", border_width=0, height=40, corner_radius=8, text_color="#4A2711")
        self.name_entry.grid(row=0, column=0, padx=(0, 10), sticky="ew")

        self.country_entry = ctk.CTkEntry(self.input_row, placeholder_text="Country", font=("Georgia", 13, "italic"), fg_color="#F4EBE1", border_width=0, height=40, corner_radius=8, text_color="#4A2711")
        self.country_entry.grid(row=0, column=1, padx=(10, 0), sticky="ew")

        # --- FIXED TEXTBOX WITH REACTIVE PLACEHOLDER ---
        self.placeholder_text = "Story"
        self.story_textbox = ctk.CTkTextbox(self.form_frame, font=("Georgia", 13, "italic"), fg_color="#F4EBE1", border_width=0, height=150, corner_radius=8, text_color="#A09084")
        self.story_textbox.pack(fill="x", padx=30, pady=15)
        
        # Inject the default message initially
        self.story_textbox.insert("1.0", self.placeholder_text)
        
        # Bind interactions to monitor mouse clicks/focus
        self.story_textbox.bind("<FocusIn>", self.clear_placeholder)
        self.story_textbox.bind("<FocusOut>", self.restore_placeholder)

        self.error_label = ctk.CTkLabel(self.form_frame, text="", font=("Arial", 12, "bold"), text_color="#A02D2D")
        self.error_label.pack(pady=(0, 5))

        self.submit_btn = ctk.CTkButton(self.form_frame, text="Submit Story", font=("Arial", 14, "bold"), fg_color="#4A2711", hover_color="#5D3216", text_color="#E6D5C3", height=40, width=200, corner_radius=20, command=self.submit_story)
        self.submit_btn.pack(pady=(10, 10))

        # --- BUILD CONFIRMATION PAGE ---
        inner_box = ctk.CTkFrame(self.confirmation_container, fg_color="#E6D5C3", border_color="#8B5A2B", border_width=1, corner_radius=15)
        inner_box.pack(expand=True, padx=40, pady=100, ipady=40, ipadx=40)

        self.conf_title = ctk.CTkLabel(inner_box, text="Thank You!", font=("Georgia", 32, "bold"), text_color="#4A2711")
        self.conf_title.pack(pady=(40, 15))

        self.conf_message = ctk.CTkLabel(inner_box, text="", font=("Arial", 15), text_color="#6E5D53", justify="center")
        self.conf_message.pack(pady=(0, 30), padx=20)

        self.back_btn = ctk.CTkButton(inner_box, text="Submit Another Story", font=("Arial", 14, "bold"), fg_color="#4A2711", hover_color="#5D3216", text_color="#E6D5C3", height=40, width=220, corner_radius=20, command=self.go_back)
        self.back_btn.pack(pady=(10, 20))

    def init_csv(self):
        if not os.path.exists("people's story.csv"):
            with open("people's story.csv", mode="w", newline="", encoding="utf-8") as file:
                csv.writer(file).writerow(["Name", "Country", "Story"])

    # --- PLACEHOLDER ENGINE ACTIONS ---
    def clear_placeholder(self, event):
        current_text = self.story_textbox.get("1.0", "end-1c").strip()
        if current_text == self.placeholder_text:
            self.story_textbox.delete("1.0", "end")
            self.story_textbox.configure(text_color="#4A2711")

    def restore_placeholder(self, event):
        current_text = self.story_textbox.get("1.0", "end-1c").strip()
        if not current_text:
            self.story_textbox.insert("1.0", self.placeholder_text)
            self.story_textbox.configure(text_color="#A09084")

    # --- BUTTON ACTIONS ---
    def submit_story(self):
        name = self.name_entry.get().strip()
        country = self.country_entry.get().strip()
        story = self.story_textbox.get("1.0", "end-1c").strip()

        if not name or not country or not story or story == self.placeholder_text:
            self.error_label.configure(text="Please fill out all fields before submitting.")
            return

        try:
            with open("people's story.csv", mode="a", newline="", encoding="utf-8") as file:
                cleaned_story = story.replace("\n", " ") 
                csv.writer(file).writerow([name, country, cleaned_story])
        except Exception as e:
            self.error_label.configure(text=f"File Error: Could not save data. ({e})")
            return

        msg = f"Thank you, {name}!\nYour story from {country} has been successfully logged.\n\nWe appreciate your contribution."
        self.conf_message.configure(text=msg)
        
        self.error_label.configure(text="")
        self.name_entry.delete(0, "end")
        self.country_entry.delete(0, "end")
        
        self.story_textbox.delete("1.0", "end")
        self.story_textbox.insert("1.0", self.placeholder_text)
        self.story_textbox.configure(text_color="#A09084")

        self.main_container.grid_forget()
        self.confirmation_container.grid(row=0, column=1, sticky="nsew", padx=40, pady=30)

    def go_back(self):
        self.confirmation_container.grid_forget()
        self.main_container.grid(row=0, column=1, sticky="nsew", padx=40, pady=30)


if __name__ == "__main__":
    app = EchoesOfHomeApp()
    app.mainloop()