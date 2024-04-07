

import sqlite3

con = sqlite3.connect('youtube.db')

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS videos
             (id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
            time TEXT NOT NULL)''')

def show_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)

def add_video(name, time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(video_id, new_name, new_time):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name,new_time, video_id))
    con.commit()
    

def delete_video(video_id):
    cur.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()

def main():
    while True:

        print("\nYoutube Manager app With Database | Choose an option: ")
        print("1. Show Videos")
        print("2. Add Videos")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_videos()

        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)

        elif choice == '3':
            video_id = input("Enter video id to update: ")
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(video_id, name, time) 


        elif choice == '4':
            video_id = input("Enter video id to delete: ")
            delete_video(video_id)

        elif choice == '5':
            break

        else:
            print("Invalid Choice")

    con.close()




if __name__ == '__main__':
    main()