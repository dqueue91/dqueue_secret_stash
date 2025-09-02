import io
from pathlib import Path
import csv


## save bill recepient and amount as dict
## save the date as list

appName = "Bill Collector"
banner = ''


def folder_creation():
    #initiate file handling
    p = Path('/home/wiggly/Documents/')
    #set variable to determine if file exists and if it doesn't, we create it
    folder_exists = True
    #iterate through directories
    for child in p.iterdir():
        if child.name == 'Finances':
            folder_exists = True
            break
        else:
            folder_exists = False

    if folder_exists == False:
        print("Directory doesn't exist, creating it now... ")
        p = Path('/home/wiggly/Documents/Finances')
        p.mkdir(exist_ok=True)

def file_handler():
    pass
    

def main():
    # navigate to folder housing document
    folder_creation()
     #First call up directory in case it already exists, else pointer will be in the parent directory
    #time to create our file, ask user what they want to call it
    p = Path('/home/wiggly/Documents/Finances')
    p_dir = str(p)
    file_name = 'bills'
    file_loc = p_dir + "/" + file_name
    ##variable to choose option
    choice = input("Select an option to continue: \n1: View entries\n2: Add entries\n3: Close program\n")
    
    if choice == '1':
        total = 0
        fieldnames = ["Name", "Price", "Date"]

        with open(file_loc, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile, fieldnames = fieldnames)
            #print("Name     ","Price    ", "Date")
            
            for i in csv_reader:
                name = i["Name"]
                price = i["Price"]
                date = i["Date"]
                total = total + float(price)
                print(f"{name} {price} due on the {date}")
            print(f"Monthly expenses are: {total}")

    elif choice == '2':

        print("Adding new entries\n")
        num_entries = int(input("How many bills are you adding?"))
        with open(file_loc, 'a', newline='') as csvfile:
            keynames = ['Name', 'Price', 'Due Date']
            csv_writer = csv.writer(csvfile, keynames)
            for i in range(num_entries):
                name = input("Enter the name of the expense. (ex. Hulu, Rent, etc.)\n")
                price = input("And how much is the expense?\n")
                date = input("What date is the bill due?\n")
                csv_writer.writerow([name, price, date])
        


    elif choice == '3':
        exit
        print("you fool")
            
############################################################################################################################

#3 add a banner around app name when program launches
for x in appName:
    banner += "-"

print(' ' + banner + '\n' + '|' + appName + '|' + '\n' + ' ' + banner)
print("Welcome back to your bill viewer ")

#program begins here  
main()

