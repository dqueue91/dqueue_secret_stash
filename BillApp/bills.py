import io
import csv
import main

def folder_creation():
    #initiate file handling
    p = main.p
    #set variable to determine if file exists and if it doesn't, we create it
    folder_exists = None
    #check if directory exists and create it and parent folders if not
    if not p.exists():
        p = Path('/home/wiggly/Documents/Finances')
        p.mkdir(parents=True, exist_ok=True)

def file_handler():
    folder_creation()
    filename = main.file_loc
    #alerts if dict is empty
    if not main.names:
        print("No data to write!")
        return

    fieldnames = list(main.names[0].keys())
    # if main.f exists(file to be written) then append else write new file ('a' or 'w')
    print(f"{main.f.exists()}")
    mode = 'a' if main.f.exists() else 'w'
    print(f" mode is set to: {mode}")
    with open(filename, mode, newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if mode == 'w':
            csv_writer.writeheader()

        csv_writer.writerows(main.names)
        main.names.clear()

        

def read_file():
    # navigate to folder housing document
    folder_creation()
     #First call up directory in case it already exists, else pointer will be in the parent directory
    #time to create our file, ask user what they want to call it
   
    p_dir = str(p)
    file_name = 'bills'
    file_loc = p_dir + "/" + file_name
   
    total = 0


    with open(file_loc, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile, fieldnames = main.keynames)
        #print("Name     ","Price    ", "Date")
            
        for i in csv_reader:
            name = i["Name"]
            price = i["Price"]
            date = i["Date"]
            total = total + float(price)
            print(f"{name} {price} due on the {date}")
        print(f"Monthly expenses are: {total}")

    
        