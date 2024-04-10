import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from tkcalendar import DateEntry
from CountryNames_and_CountryCodes import CountryNames_and_CountryCodes, Get_CountryName, Get_CountryCode
import re
import json
import webbrowser

class DBMS_Lite:
    def __init__(self, Window):
        self.Window = Window
        self.Window.title("DBMS (Lite)")
        
        self.Menu()
        self.Frame()

        # Data Storage for Export
        self.UserData = []

    def Menu(self):
        # Create Menu 
        self.Menu = tk.Menu(self.Window)
        self.Window.config(menu=self.Menu)

        # File Menu 'File'
        File = tk.Menu(self.Menu, tearoff=False)
        self.Menu.add_cascade(label="File", menu=File)
        File.add_command(label="Import", command=self.Import)
        File.add_command(label="Export", command=self.Export)
        File.add_separator()
        File.add_command(label="Exit", command=self.Window.quit)

        # Create Menu 'Help'
        self.Help = tk.Menu(self.Menu, tearoff=0)
        self.Menu.add_cascade(label="Help", menu=self.Help)
        self.Help.add_command(label="Check for Updates", command=self.Check_for_Updates)
        self.Help.add_separator()
        self.Help.add_command(label="About", command=self.About)

    def Import(self):
        FilePATH_Import = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if FilePATH_Import:
            with open(FilePATH_Import, "r") as File_Import:
                try:
                    UserData_Import = json.load(File_Import)
                    self.UserData.extend(UserData_Import)
                    self.IB_Import(UserData_Import)
                    messagebox.showinfo("Imported", "Data imported successfully!")
                except json.JSONDecodeError:
                    messagebox.showerror("Error", "Invalid JSON file format")

    def IB_Import(self, UserData_Import):
        # Prepare Data for Import
        UserData_Map = {
            "First_Name": self.UD_FirstName,
            "Middle_Name": self.UD_MiddleName,
            "Last_Name": self.UD_LastName,
            "Date_of_Birth": self.IB_DOB,
            "Country_Name": self.UD_CountryName,
            "Country_Code": self.UD_CountryCode,
            "Phone_Number": self.UD_PhoneNumber,
            "Email": self.UD_Email,

            "Father's_First_Name": self.UD_FatherFirstName,
            "Father's_Middle_Name": self.UD_FatherMiddleName,
            "Father's_Last_Name": self.UD_FatherLastName,
            "Father's_Date_of_Birth": self.IB_FatherDOB,
            "Father's_Country_Name": self.UD_FatherCountryName,
            "Father's_Country_Code": self.UD_FatherCountryCode,
            "Father's_Phone_Number": self.UD_FatherPhoneNumber,
            "Father's_Email": self.UD_FatherEmail,

            "Mother's_First_Name": self.UD_MotherFirstName,
            "Mother's_Middle_Name": self.UD_MotherMiddleName,
            "Mother's_Last_Name": self.UD_MotherLastName,
            "Mother's_Date_of_Birth": self.IB_MotherDOB,
            "Mother's_Country_Name": self.UD_MotherCountryName,
            "Mother's_Country_Code": self.UD_MotherCountryCode,
            "Mother's_Phone_Number": self.UD_MotherPhoneNumber,
            "Mother's_Email": self.UD_MotherEmail,
        }

        for Data_Extraction in UserData_Import:
            for Key, Value in Data_Extraction.items():
                if Key in UserData_Map:
                    IB_From = UserData_Map[Key]
                    IB_From.set(Value)

    def Export(self):
        # Prepare Data for Export
        UserData = {
            "First_Name": self.UD_FirstName.get(),
            "Middle_Name": self.UD_MiddleName.get(),
            "Last_Name": self.UD_LastName.get(),
            "Full_Name": self.UD_FullName.get(),
            "Date_of_Birth": self.IB_DOB.get(),
            "Country_Name": self.UD_CountryName.get(),
            "Country_Code": self.UD_CountryCode.get(),
            "Phone_Number": self.UD_PhoneNumber.get(),
            "Email": self.UD_Email.get(),

            "Father's_First_Name": self.UD_FatherFirstName.get(),
            "Father's_Middle_Name": self.UD_FatherMiddleName.get(),
            "Father's_Last_Name": self.UD_FatherLastName.get(),
            "Father's_Full_Name": self.UD_FatherFullName.get(),
            "Father's_Date_of_Birth": self.IB_FatherDOB.get(),
            "Father's_Country_Name": self.UD_FatherCountryName.get(),
            "Father's_Country_Code": self.UD_FatherCountryCode.get(),
            "Father's_Phone_Number": self.UD_FatherPhoneNumber.get(),
            "Father's_Email": self.UD_FatherEmail.get(),

            "Mother's_First_Name": self.UD_MotherFirstName.get(),
            "Mother's_Middle_Name": self.UD_MotherMiddleName.get(),
            "Mother's_Last_Name": self.UD_MotherLastName.get(),
            "Mother's_Full_Name": self.UD_MotherFullName.get(),
            "Mother's_Date_of_Birth": self.IB_MotherDOB.get(),
            "Mother's_Country_Name": self.UD_MotherCountryName.get(),
            "Mother's_Country_Code": self.UD_MotherCountryCode.get(),
            "Mother's_Phone_Number": self.UD_MotherPhoneNumber.get(),
            "Mother's_Email": self.UD_MotherEmail.get(),
        }

        # Append Data to UserData
        self.UserData.append(UserData)
        
        FilePATH_Export = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if FilePATH_Export:
            with open(FilePATH_Export, "w") as File_Export:
                json.dump(self.UserData, File_Export, indent=4)
                messagebox.showinfo("Exported", "Data exported successfully!")

    def Check_for_Updates(self):
        webbrowser.open("https://www.github.com/satishkumarsingh2024/DBMS-Lite")

    def About(self):
        messagebox.showinfo("About", "DBMS (Lite) (v1.0)\nDeveloped by Satish Kumar Singh")

    def Frame(self):
        # Create InputBox
        self.UD_FirstName = tk.StringVar()
        self.UD_MiddleName = tk.StringVar()
        self.UD_LastName = tk.StringVar()
        self.UD_FullName = tk.StringVar()
        self.IB_DOB = tk.StringVar()
        self.UD_CountryName = tk.StringVar()
        self.UD_CountryCode = tk.StringVar()
        self.UD_PhoneNumber = tk.StringVar()
        self.UD_Email = tk.StringVar()

        self.UD_FatherFirstName = tk.StringVar()
        self.UD_FatherMiddleName = tk.StringVar()
        self.UD_FatherLastName = tk.StringVar()
        self.UD_FatherFullName = tk.StringVar()
        self.IB_FatherDOB = tk.StringVar()
        self.UD_FatherCountryName = tk.StringVar()
        self.UD_FatherCountryCode = tk.StringVar()
        self.UD_FatherPhoneNumber = tk.StringVar()
        self.UD_FatherEmail = tk.StringVar()

        self.UD_MotherFirstName = tk.StringVar()
        self.UD_MotherMiddleName = tk.StringVar()
        self.UD_MotherLastName = tk.StringVar()
        self.UD_MotherFullName = tk.StringVar()
        self.IB_MotherDOB = tk.StringVar()
        self.UD_MotherCountryName = tk.StringVar()
        self.UD_MotherCountryCode = tk.StringVar()
        self.UD_MotherPhoneNumber = tk.StringVar()
        self.UD_MotherEmail = tk.StringVar()
        
        # Create a Frame for InputBox
        Frame_for_IB = tk.Frame(self.Window)
        Frame_for_IB.pack(pady=10)
        
        # Label 'First Name' and InputBox
        Label_FirstName = tk.Label(Frame_for_IB, text="First Name:")
        Label_FirstName.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        IB_FirstName = tk.Entry(Frame_for_IB, textvariable=self.UD_FirstName)
        IB_FirstName.grid(row=0, column=1, padx=5, pady=5)
        
        # Label 'Middle Name' and InputBox
        Label_MiddleName = tk.Label(Frame_for_IB, text="Middle Name:")
        Label_MiddleName.grid(row=0, column=2, padx=5, pady=5, sticky="e")
        IB_MiddleName = tk.Entry(Frame_for_IB, textvariable=self.UD_MiddleName)
        IB_MiddleName.grid(row=0, column=3, padx=5, pady=5)
        
        # Label 'Last Name' and InputBox
        Label_LastName = tk.Label(Frame_for_IB, text="Last Name:")
        Label_LastName.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        IB_LastName = tk.Entry(Frame_for_IB, textvariable=self.UD_LastName)
        IB_LastName.grid(row=0, column=5, padx=5, pady=5)
        
        # Label 'Full Name' and InputBox
        Label_FullName = tk.Label(Frame_for_IB, text="Full Name:")
        Label_FullName.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        IB_FullName = tk.Entry(Frame_for_IB, textvariable=self.UD_FullName, state='readonly')
        IB_FullName.grid(row=1, column=1, columnspan=5, padx=5, pady=5, sticky="ew")

        # Bind 'First Name', 'Middle Name', and 'Last Name' to Callback Function
        self.UD_FirstName.trace_add('write', self.Update_FullName)
        self.UD_MiddleName.trace_add('write', self.Update_FullName)
        self.UD_LastName.trace_add('write', self.Update_FullName)
        
        # Label 'Date of Birth' and InputBox with Calendar
        Label_DOB = tk.Label(Frame_for_IB, text="Date of Birth:")
        Label_DOB.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        IB_DOB = DateEntry(Frame_for_IB, textvariable=self.IB_DOB, date_pattern='dd/mm/yyyy')
        IB_DOB.grid(row=2, column=1, columnspan=5, padx=5, pady=5, sticky="ew")
        
        # Label 'Country' and Dropdown
        Label_Country = tk.Label(Frame_for_IB, text="Country:")
        Label_Country.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        Countries = list(CountryNames_and_CountryCodes.keys())
        self.UD_CountryName.set(Countries[0])
        DD_Country = tk.OptionMenu(Frame_for_IB, self.UD_CountryName, *Countries)
        DD_Country.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Label 'Country Code' and Dropdown
        Label_CountryCode = tk.Label(Frame_for_IB, text="Country Code:")
        Label_CountryCode.grid(row=3, column=2, padx=5, pady=5, sticky="e")
        CountryCodes = list(CountryNames_and_CountryCodes.values())
        self.UD_CountryCode.set(CountryCodes[0])  # Set default value
        DD_CountryCode = tk.OptionMenu(Frame_for_IB, self.UD_CountryCode, *CountryCodes)
        DD_CountryCode.grid(row=3, column=3, padx=5, pady=5, sticky="w")

        # Bind 'Country Name' and 'Country Code' to Callback Function
        self.UD_CountryCode.trace_add('write', self.Update_CountryName)
        self.UD_CountryName.trace_add('write', self.Update_CountryCode)
        
        # Label 'Phone Number' and InputBox
        Label_PhoneNumber = tk.Label(Frame_for_IB, text="Phone Number:")
        Label_PhoneNumber.grid(row=3, column=4, padx=5, pady=5, sticky="e")
        IB_PhoneNumber = tk.Entry(Frame_for_IB, textvariable=self.UD_PhoneNumber)
        IB_PhoneNumber.grid(row=3, column=5, padx=5, pady=5)

        # Label 'Email' and InputBox
        Label_Email = tk.Label(Frame_for_IB, text="Email:")
        Label_Email.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        IB_Email = tk.Entry(Frame_for_IB, textvariable=self.UD_Email)
        IB_Email.grid(row=4, column=1, columnspan=5, padx=5, pady=5, sticky="ew")

        # Bind 'Email' to Callback Function
        self.UD_Email.trace_add('write', self.Update_Email)

        # Create a Horizontal Separator
        HS_1 = ttk.Separator(Frame_for_IB, orient='horizontal')
        HS_1.grid(row=5, column=0, columnspan=6, pady=10, sticky="ew")

        # Label 'Father's First Name' and InputBox
        Label_FatherFirstName = tk.Label(Frame_for_IB, text="Father's First Name:")
        Label_FatherFirstName.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        IB_FatherFirstName = tk.Entry(Frame_for_IB, textvariable=self.UD_FatherFirstName)
        IB_FatherFirstName.grid(row=6, column=1, padx=5, pady=5)

        # Label 'Father's Middle Name' and InputBox
        Label_FatherMiddleName = tk.Label(Frame_for_IB, text="Father's Middle Name:")
        Label_FatherMiddleName.grid(row=6, column=2, padx=5, pady=5, sticky="e")
        IB_FatherMiddleName = tk.Entry(Frame_for_IB, textvariable=self.UD_FatherMiddleName)
        IB_FatherMiddleName.grid(row=6, column=3, padx=5, pady=5)

        # Label 'Father's Last Name' and InputBox
        Label_FatherLastName = tk.Label(Frame_for_IB, text="Father's Last Name:")
        Label_FatherLastName.grid(row=6, column=4, padx=5, pady=5, sticky="e")
        IB_FatherLastName = tk.Entry(Frame_for_IB, textvariable=self.UD_FatherLastName)
        IB_FatherLastName.grid(row=6, column=5, padx=5, pady=5)

        # Label 'Father's Full Name' and InputBox
        Label_FatherFullName = tk.Label(Frame_for_IB, text="Father's Full Name:")
        Label_FatherFullName.grid(row=7, column=0, padx=5, pady=5, sticky="e")
        IB_FatherFullName = tk.Entry(Frame_for_IB, textvariable=self.UD_FatherFullName, state='readonly')
        IB_FatherFullName.grid(row=7, column=1, columnspan=5, padx=5, pady=5, sticky="ew")

        # Bind 'Father's First Name', 'Father's Middle Name', and 'Father's Last Name' to Callback Function
        self.UD_FatherFirstName.trace_add('write', self.Update_FatherFullName)
        self.UD_FatherMiddleName.trace_add('write', self.Update_FatherFullName)
        self.UD_FatherLastName.trace_add('write', self.Update_FatherFullName)

        # Label 'Father's Date of Birth' and InputBox with Calendar
        Label_FatherDOB = tk.Label(Frame_for_IB, text="Father's Date of Birth:")
        Label_FatherDOB.grid(row=8, column=0, padx=5, pady=5, sticky="e")
        IB_FatherDOB = DateEntry(Frame_for_IB, textvariable=self.IB_FatherDOB, date_pattern='dd/mm/yyyy')
        IB_FatherDOB.grid(row=8, column=1, columnspan=5, padx=5, pady=5, sticky="ew")
        
        # Label 'Father's Country' and Dropdown
        Label_FatherCountry = tk.Label(Frame_for_IB, text="Father's Country:")
        Label_FatherCountry.grid(row=9, column=0, padx=5, pady=5, sticky="e")
        Countries = list(CountryNames_and_CountryCodes.keys())
        self.UD_FatherCountryName.set(Countries[0])
        DD_FatherCountry = tk.OptionMenu(Frame_for_IB, self.UD_FatherCountryName, *Countries)
        DD_FatherCountry.grid(row=9, column=1, padx=5, pady=5, sticky="w")
        
        # Label 'Father's Country Code' and Dropdown
        Label_FatherCountryCode = tk.Label(Frame_for_IB, text="Father's Country Code:")
        Label_FatherCountryCode.grid(row=9, column=2, padx=5, pady=5, sticky="e")
        CountryCodes = list(CountryNames_and_CountryCodes.values())
        self.UD_FatherCountryCode.set(CountryCodes[0])  # Set default value
        DD_FatherCountryCode = tk.OptionMenu(Frame_for_IB, self.UD_FatherCountryCode, *CountryCodes)
        DD_FatherCountryCode.grid(row=9, column=3, padx=5, pady=5, sticky="w")

        # Bind 'Father's Country Name' and 'Father's Country Code' to Callback Function
        self.UD_FatherCountryCode.trace_add('write', self.Update_FatherCountryName)
        self.UD_FatherCountryName.trace_add('write', self.Update_FatherCountryCode)
        
        # Label 'Father's Phone Number' and InputBox
        Label_FatherPhoneNumber = tk.Label(Frame_for_IB, text="Father's Phone Number:")
        Label_FatherPhoneNumber.grid(row=9, column=4, padx=5, pady=5, sticky="e")
        IB_FatherPhoneNumber = tk.Entry(Frame_for_IB, textvariable=self.UD_FatherPhoneNumber)
        IB_FatherPhoneNumber.grid(row=9, column=5, padx=5, pady=5)

        # Label 'Father's Email' and InputBox
        Label_FatherEmail = tk.Label(Frame_for_IB, text="Father's Email:")
        Label_FatherEmail.grid(row=10, column=0, padx=5, pady=5, sticky="e")
        IB_FatherEmail = tk.Entry(Frame_for_IB, textvariable=self.UD_FatherEmail)
        IB_FatherEmail.grid(row=10, column=1, columnspan=5, padx=5, pady=5, sticky="ew")

        # Bind 'Father's Email' to Callback Function
        self.UD_FatherEmail.trace_add('write', self.Update_FatherEmail)

        # Create a Horizontal Separator
        HS_2 = ttk.Separator(Frame_for_IB, orient='horizontal')
        HS_2.grid(row=11, column=0, columnspan=6, pady=10, sticky="ew")

        # Label 'Mother's First Name' and InputBox
        Label_MotherFirstName = tk.Label(Frame_for_IB, text="Mother's First Name:")
        Label_MotherFirstName.grid(row=12, column=0, padx=5, pady=5, sticky="e")
        IB_MotherFirstName = tk.Entry(Frame_for_IB, textvariable=self.UD_MotherFirstName)
        IB_MotherFirstName.grid(row=12, column=1, padx=5, pady=5)

        # Label 'Mother's Middle Name' and InputBox
        Label_MotherMiddleName = tk.Label(Frame_for_IB, text="Mother's Middle Name:")
        Label_MotherMiddleName.grid(row=12, column=2, padx=5, pady=5, sticky="e")
        IB_MotherMiddleName = tk.Entry(Frame_for_IB, textvariable=self.UD_MotherMiddleName)
        IB_MotherMiddleName.grid(row=12, column=3, padx=5, pady=5)

        # Label 'Mother's Last Name' and InputBox
        Label_MotherLastName = tk.Label(Frame_for_IB, text="Mother's Last Name:")
        Label_MotherLastName.grid(row=12, column=4, padx=5, pady=5, sticky="e")
        IB_MotherLastName = tk.Entry(Frame_for_IB, textvariable=self.UD_MotherLastName)
        IB_MotherLastName.grid(row=12, column=5, padx=5, pady=5)

        # Label 'Mother's Full Name' and InputBox
        Label_MotherFullName = tk.Label(Frame_for_IB, text="Mother's Full Name:")
        Label_MotherFullName.grid(row=13, column=0, padx=5, pady=5, sticky="e")
        IB_MotherFullName = tk.Entry(Frame_for_IB, textvariable=self.UD_MotherFullName, state='readonly')
        IB_MotherFullName.grid(row=13, column=1, columnspan=5, padx=5, pady=5, sticky="ew")

        # Bind 'Mother's First Name', 'Mother's Middle Name', and 'Mother's Last Name' to Callback Function
        self.UD_MotherFirstName.trace_add('write', self.Update_MotherFullName)
        self.UD_MotherMiddleName.trace_add('write', self.Update_MotherFullName)
        self.UD_MotherLastName.trace_add('write', self.Update_MotherFullName)

        # Label 'Mother's Date of Birth' and InputBox with Calendar
        Label_MotherDOB = tk.Label(Frame_for_IB, text="Mother's Date of Birth:")
        Label_MotherDOB.grid(row=14, column=0, padx=5, pady=5, sticky="e")
        IB_MotherDOB = DateEntry(Frame_for_IB, textvariable=self.IB_MotherDOB, date_pattern='dd/mm/yyyy')
        IB_MotherDOB.grid(row=14, column=1, columnspan=5, padx=5, pady=5, sticky="ew")
        
        # Label 'Mother's Country' and Dropdown
        Label_MotherCountry = tk.Label(Frame_for_IB, text="Mother's Country:")
        Label_MotherCountry.grid(row=15, column=0, padx=5, pady=5, sticky="e")
        Countries = list(CountryNames_and_CountryCodes.keys())
        self.UD_MotherCountryName.set(Countries[0])
        DD_MotherCountry = tk.OptionMenu(Frame_for_IB, self.UD_MotherCountryName, *Countries)
        DD_MotherCountry.grid(row=15, column=1, padx=5, pady=5, sticky="w")
        
        # Label 'Mother's Country Code' and Dropdown
        Label_MotherCountryCode = tk.Label(Frame_for_IB, text="Mother's Country Code:")
        Label_MotherCountryCode.grid(row=15, column=2, padx=5, pady=5, sticky="e")
        CountryCodes = list(CountryNames_and_CountryCodes.values())
        self.UD_MotherCountryCode.set(CountryCodes[0])  # Set default value
        DD_MotherCountryCode = tk.OptionMenu(Frame_for_IB, self.UD_MotherCountryCode, *CountryCodes)
        DD_MotherCountryCode.grid(row=15, column=3, padx=5, pady=5, sticky="w")

        # Bind 'Mother's Country Name' and 'Mother's Country Code' to Callback Function
        self.UD_MotherCountryCode.trace_add('write', self.Update_MotherCountryName)
        self.UD_MotherCountryName.trace_add('write', self.Update_MotherCountryCode)
        
        # Label 'Mother's Phone Number' and InputBox
        Label_MotherPhoneNumber = tk.Label(Frame_for_IB, text="Mother's Phone Number:")
        Label_MotherPhoneNumber.grid(row=15, column=4, padx=5, pady=5, sticky="e")
        IB_MotherPhoneNumber = tk.Entry(Frame_for_IB, textvariable=self.UD_MotherPhoneNumber)
        IB_MotherPhoneNumber.grid(row=15, column=5, padx=5, pady=5)

        # Label 'Mother's Email' and InputBox
        Label_MotherEmail = tk.Label(Frame_for_IB, text="Mother's Email:")
        Label_MotherEmail.grid(row=16, column=0, padx=5, pady=5, sticky="e")
        IB_MotherEmail = tk.Entry(Frame_for_IB, textvariable=self.UD_MotherEmail)
        IB_MotherEmail.grid(row=16, column=1, columnspan=5, padx=5, pady=5, sticky="ew")

        # Bind 'Mother's Email' to Callback Function
        self.UD_MotherEmail.trace_add('write', self.Update_MotherEmail)
        
    def Update_FullName(self, *args):
        First_Name = self.UD_FirstName.get()
        Middle_Name = self.UD_MiddleName.get()
        Last_Name = self.UD_LastName.get()
        Full_Name = f"{First_Name} {Middle_Name} {Last_Name}".strip()
        self.UD_FullName.set(Full_Name)

    def Update_CountryName(self, *args):
        Country_Code = self.UD_CountryCode.get()
        Country_Name = Get_CountryName(Country_Code, CountryNames_and_CountryCodes)
        if Country_Name:
            self.UD_CountryName.set(Country_Name)
        else:
            self.UD_CountryName.set("")

    def Update_CountryCode(self, *args):
        Country_Name = self.UD_CountryName.get()
        Country_Code = Get_CountryCode(Country_Name, CountryNames_and_CountryCodes)
        if Country_Code:
            self.UD_CountryCode.set(Country_Code)
        else:
            self.UD_CountryCode.set("")

    def Update_Email(self, *args):
        pass

    def Update_FatherFullName(self, *args):
        Father_First_Name = self.UD_FatherFirstName.get()
        Father_Middle_Name = self.UD_FatherMiddleName.get()
        Father_Last_Name = self.UD_FatherLastName.get()
        Father_Full_Name = f"{Father_First_Name} {Father_Middle_Name} {Father_Last_Name}".strip()
        self.UD_FatherFullName.set(Father_Full_Name)

    def Update_FatherCountryName(self, *args):
        Father_Country_Code = self.UD_FatherCountryCode.get()
        Father_Country_Name = Get_CountryName(Father_Country_Code, CountryNames_and_CountryCodes)
        if Father_Country_Name:
            self.UD_FatherCountryName.set(Father_Country_Name)
        else:
            self.UD_FatherCountryName.set("")

    def Update_FatherCountryCode(self, *args):
        Father_Country_Name = self.UD_FatherCountryName.get()
        Father_Country_Code = Get_CountryCode(Father_Country_Name, CountryNames_and_CountryCodes)
        if Father_Country_Code:
            self.UD_FatherCountryCode.set(Father_Country_Code)
        else:
            self.UD_FatherCountryCode.set("")

    def Update_FatherEmail(self, *args):
        pass

    def Update_MotherFullName(self, *args):
        Mother_First_Name = self.UD_MotherFirstName.get()
        Mother_Middle_Name = self.UD_MotherMiddleName.get()
        Mother_Last_Name = self.UD_MotherLastName.get()
        Mother_Full_Name = f"{Mother_First_Name} {Mother_Middle_Name} {Mother_Last_Name}".strip()
        self.UD_MotherFullName.set(Mother_Full_Name)

    def Update_MotherCountryName(self, *args):
        Mother_Country_Code = self.UD_MotherCountryCode.get()
        Mother_Country_Name = Get_CountryName(Mother_Country_Code, CountryNames_and_CountryCodes)
        if Mother_Country_Name:
            self.UD_MotherCountryName.set(Mother_Country_Name)
        else:
            self.UD_MotherCountryName.set("")

    def Update_MotherCountryCode(self, *args):
        Mother_Country_Name = self.UD_MotherCountryName.get()
        Mother_Country_Code = Get_CountryCode(Mother_Country_Name, CountryNames_and_CountryCodes)
        if Mother_Country_Code:
            self.UD_MotherCountryCode.set(Mother_Country_Code)
        else:
            self.UD_MotherCountryCode.set("")

    def Update_MotherEmail(self, *args):
        pass

def main():
    root = tk.Tk()
    Application = DBMS_Lite(root)
    root.mainloop()

if __name__ == "__main__":
    main()