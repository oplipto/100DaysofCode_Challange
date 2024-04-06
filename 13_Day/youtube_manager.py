
import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            test =  json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 75)
    for index, video in enumerate(videos, start=1):
     print(f"{index}. {video['name']}, Duration: {video['time']}")

    print("\n")
    print("*" * 75)

def add_video(videos):
    input_title = input("Enter the title of the video: ")
    input_length = input("Enter the length of the video: ")
    videos.append({"title": input_title, "length": input_length})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {"title": name, "length": time}
        save_data_helper(videos)
    else:
        print("Invalid video number!")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid video number!")


def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager | Choose an option:")
        print("1. Show All Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case "1":
                list_all_videos(videos)

            case "2":
                add_video(videos)

            case "3":
                update_video(videos)

            case "4":
                delete_video(videos)

            case "5":
                print("Exiting Youtube Manager...")
                break
            
            case _:
                    print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
