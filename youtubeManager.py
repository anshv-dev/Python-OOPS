
def list_all_videos(videos):
  pass

def add_video(videos):
  pass

def update_video(videos):
  pass

def delete_video(videos):
  pass

def main():  
  videos=[]


  while True:
    print("\n Youtube Manager")
    print("1. List a all youtube videos")
    print("2. Add a youtube video")
    print("3. Update a youtube video details")
    print("4. Delete a youtube video")
    print("5. Exit the app")
    choice=input("Enter Your choice")

    match choice:
      case '1':
        list_all_videos(videos)
      case '2':
        add_video(videos)  
      case '3':
        update_video(videos)
      case '4':
        delete_video(videos)
      case '5':
        break  
      case _:
        print("Invalid choice")  

if __name__== "__main__":
  main()       

