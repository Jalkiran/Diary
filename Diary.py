from datetime import date
while True:
    choice=int(input("1.Add\n2.Show\n3.Quit\nEnter your choice:"))
    
    if choice==1:
        entry=input("entry:")
        with open("Diary.txt","a")as file:
          file.write(f"[{date.today()}] {entry}\n")
        print("Saved")
    if choice==2:
        try:
            with open("Diary.txt","r")as file:
                print(file.read())
        except FileNotFoundError:
            print("File not found!")
    if choice==3:
        print("Bye👋")
        break
