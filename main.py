import os
import time
import streamlit as st
from pytube import YouTube
from streamlit_lottie import st_lottie
import json

# Load the Lottie animations
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_download = load_lottiefile("doload.json")
lottie_continue = load_lottiefile("contiload.json")

def on_progress_callback(stream, chunk, bytes_remaining, progress_bar, progress_text):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = int(bytes_downloaded / total_size * 100)
    progress_bar.progress(percentage / 100.0)
    progress_text.text(f"Download progress: {percentage}%")

def download_video_with_progress(url, download_folder, video_id, video_quality, progress_bar, progress_text, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            yt = YouTube(url, on_progress_callback=lambda stream, chunk, bytes_remaining: on_progress_callback(stream, chunk, bytes_remaining, progress_bar, progress_text))
            
            video = yt.streams.filter(res=video_quality).first()

            if not video:
                st.warning(f"No {video_quality} stream available. Falling back to highest resolution.")
                video = yt.streams.get_highest_resolution()
            if video:
                filename = f"video_{video_id}.mp4"
                file_path = os.path.join(download_folder, filename)

                st.markdown(f"**_Starting download for {yt.title}_**")

                video.download(download_folder, filename=filename)
                
                st.markdown(f"**_Download completed for {yt.title}_**")
                return file_path

            else:
                st.write(f"No stream available for {url}")
                return None

        except Exception as e:
            st.write(f"Exception occurred while downloading {url}: {str(e)}")
            retries += 1
            time.sleep(5)

    st.write(f"Failed to download {url} after {max_retries} attempts")
    return None

# st.title("Youtube Video Downloader 🤘")
st.image("title.png", use_column_width=True)
st.write("niku nachina video nachinattu download chesko mowa..!!")
video_url = st.text_input("Enter YouTube video URL:")

video_quality = st.selectbox(
    "Select video quality:",
    ["1080p", "720p", "480p", "360p", "240p", "144p"]
)

progress_bar = st.progress(0)
progress_text = st.empty()

if 'video_downloaded' not in st.session_state:
    st.session_state.video_downloaded = False

if not st.session_state.video_downloaded:
    if st.button("Download Video"):
        if video_url:
            download_folder = os.getcwd()
            video_id = int(time.time())
            st.write("Downloading... 🌟🚀💫")
            st_lottie(lottie_download, height=300, key="download_animation")
            file_path = download_video_with_progress(video_url, download_folder, video_id, video_quality, progress_bar, progress_text)

            if file_path:
                st.session_state.file_path = file_path
                st.session_state.video_downloaded = True
                st.rerun()
            else:
                st.error("Failed to download video.")
        else:
            st.error("Please enter a valid YouTube video URL.")
else:
    file_path = st.session_state.file_path
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            video_data = file.read()

        st.download_button(
            label="continue",
            data=video_data,
            file_name=os.path.basename(file_path),
            mime="video/mp4"
        )
        st.success("click on continue:")
        st_lottie(lottie_continue, height=200, key="continue_animation")
        try:
            os.remove(file_path)
            st.session_state.video_downloaded = False
        except Exception as e:
            st.error(f"Error deleting file: {str(e)}")
    else:
        st.error(f"File not found: {file_path}")

st.text("") 
st.text("") 
st.text("") 
st.text("") 
st.text("") 
st.text("") 
if st.button("About Creator🧐", key="about_creator_button"):
    with st.expander("kalkeesh jami"):
        st.image("mepic.jpg", use_column_width=True)
        st.write("""
        Hello! I'm KALKEESH JAMI #AKA Kalki, a passionate developer exploring the world of AI and programming.
        
        - I love building applications that make life easier.
        - I'm good at Python and data analysis.
        - Don't misunderstand me as a nerd; I'm socially adept too! 😄
        - Thank you for checking out my app!
        
        Do check out my [LinkedIn](https://www.linkedin.com/in/kalkeesh-jami-42891b260/) and [GitHub](https://github.com/kalkeesh/).
        """)



# import os
# import time
# import streamlit as st
# from pytube import YouTube

# def on_progress_callback(stream, chunk, bytes_remaining, progress_bar, progress_text):
#     total_size = stream.filesize
#     bytes_downloaded = total_size - bytes_remaining
#     percentage = int(bytes_downloaded / total_size * 100)
#     progress_bar.progress(percentage / 100.0)
#     progress_text.text(f"Download progress: {percentage}%")

# def download_video_with_progress(url, download_folder, video_id, video_quality, progress_bar, progress_text, max_retries=3):
#     retries = 0
#     while retries < max_retries:
#         try:
#             yt = YouTube(url, on_progress_callback=lambda stream, chunk, bytes_remaining: on_progress_callback(stream, chunk, bytes_remaining, progress_bar, progress_text))
            
#             video = yt.streams.filter(res=video_quality).first()  

#             if not video:
#                 st.warning(f"No {video_quality} stream available. Falling back to highest resolution.")
#                 video = yt.streams.get_highest_resolution() 
#             if video:
#                 filename = f"video_{video_id}.mp4"
#                 file_path = os.path.join(download_folder, filename)

#                 st.markdown(f"**_Starting download for {yt.title}_**")

#                 video.download(download_folder, filename=filename)
                
#                 st.markdown(f"**_Download completed for {yt.title}_**")
#                 return file_path  

#             else:
#                 st.write(f"No stream available for {url}")
#                 return None

#         except Exception as e:
#             st.write(f"Exception occurred while downloading {url}: {str(e)}")
#             retries += 1
#             time.sleep(5)

#     st.write(f"Failed to download {url} after {max_retries} attempts")
#     return None

# # st.title("Youtube Video Downloader 🤘")
# st.image("title.png", use_column_width=True)  
# st.write("niku nachina video nachinattu download chesko mowa..!!")
# video_url = st.text_input("Enter YouTube video URL:")

# video_quality = st.selectbox(
#     "Select video quality:",
#     ["1080p", "720p", "480p", "360p", "240p", "144p"]
# )

# progress_bar = st.progress(0)
# progress_text = st.empty()

# if 'video_downloaded' not in st.session_state:
#     st.session_state.video_downloaded = False

# if not st.session_state.video_downloaded:
#     if st.button("Download Video"):
#         if video_url:
#             download_folder = os.getcwd()  
#             video_id = int(time.time())
#             st.write("Downloading... 🌟🚀💫")
#             file_path = download_video_with_progress(video_url, download_folder, video_id, video_quality, progress_bar, progress_text)

#             if file_path:
#                 st.session_state.file_path = file_path
#                 st.session_state.video_downloaded = True
#                 st.rerun()
#             else:
#                 st.error("Failed to download video.")
#         else:
#             st.error("Please enter a valid YouTube video URL.")
# else:
#     file_path = st.session_state.file_path
#     if os.path.exists(file_path):
#         with open(file_path, "rb") as file:
#             video_data = file.read()

#         st.download_button(
#             label="continue",
#             data=video_data,
#             file_name=os.path.basename(file_path),
#             mime="video/mp4"
#         )
#         st.success(f"click on continue:")
#         try:
#             os.remove(file_path)
#             st.session_state.video_downloaded = False  
#         except Exception as e:
#             st.error(f"Error deleting file: {str(e)}")
#     else:
#         st.error(f"File not found: {file_path}")

# st.text("") 
# st.text("") 
# st.text("") 
# st.text("") 
# st.text("") 
# st.text("") 
# if st.button("About Creator🧐", key="about_creator_button"):
#     with st.expander("kalkeesh jami"):
#         st.image("mepic.jpg", use_column_width=True)  
#         st.write("""
#         Hello! I'm KALKEESH JAMI #AKA Kalki, a passionate developer exploring the world of AI and programming.
        
#         - I love building applications that make life easier.
#         - I'm good at Python and data analysis.
#         - Don't misunderstand me as a nerd; I'm socially adept too! 😄
#         - Thank you for checking out my app!
        
#         Do check out my [LinkedIn](https://www.linkedin.com/in/kalkeesh-jami-42891b260/) and [GitHub](https://github.com/kalkeesh/).
#         """)

