# BASIC WORKFLOW

# PSUEDOCODE PROCEDURE (core features)

> [] if youtube install show bander when press/type youtubed
> [] show key values of what to download (v->(video),a->(audio),q->(exits),f->(searching/filtering) )
> (User : prompt user for a youtube video url(audioo/video selection))
> [] with video (selection quality)
> [] display progress of download
> [] show Completion when finished download with destinations

### Additional features

-[] Search/filters functionality
-[] Automate path of downloads
-[] Via sync both from different devices
-[] float panes
-[] show preview thumbnail through the terminal

# A program is required to download a video from YouTube, the program should download normal youtube video , Playlist, show title or even channel name, before it start downloading,should be able to convert video to audio and output message "completed!" with the correct paths

# input --> youtube video , Playlist, title , channel

# output --> paths(destination),completed when done

# processing --> downloading, and converting from one state to the other

#

# PSEUDOCODE IMPLEMENTATION

```
FUNCTION download_youtube_content(input_url, download_type):
    # Input validation
    IF input_url is empty OR invalid:
        DISPLAY "Error: Invalid YouTube URL"
        RETURN
    
    # Determine content type
    content_type = detect_content_type(input_url)  # video, playlist, channel
    
    # Get download preferences
    media_type = ask_user("Download video (v) or audio (a)?")
    
    # Set download path
    download_path = get_default_download_path()
    
    TRY:
        # Initialize YouTube/Playlist/Channel object
        IF content_type == "video":
            media = YouTube(input_url)
        ELSE IF content_type == "playlist":
            media = Playlist(input_url)
        ELSE IF content_type == "channel":
            media = Channel(input_url)
        
        # Download each item
        FOR each item IN media:
            IF media_type == "audio":
                # Convert to audio
                stream = item.get_audio_only()
                file_path = stream.download(output_path=download_path)
            ELSE:
                # Download highest quality video
                stream = item.get_highest_resolution()
                file_path = stream.download(output_path=download_path)
            
            DISPLAY "Downloading: " + item.title
        
        # Completion message
        DISPLAY "completed!"
        DISPLAY "Files saved to: " + download_path
        
    EXCEPT Exception as e:
        DISPLAY "Error: " + str(e)
        RETURN
    
    RETURN True
```

# okay additional features system destinations

# one you need internet connection to download the video

---

## Development Conversation History

### Code Review and Learning Session

**User Question**: "read the codebase in the cli youtube downoloader and tell , why am struggle to write this program , the structures , why am not getting it , where to improve even without ai or ai how i should approach certains things or is because am dump and can't code or is it because am using an external library which is way out of reach to me so give me your take"

**Analysis Results**:

**Issues in Current Code**:
1. **Function Logic Errors** (line 8): `if youtube_download == video:` compares function name to parameter, never true
2. **Undefined Variables** (line 23): `yt` doesn't exist in `audio()` function scope
3. **Incomplete Structure**: Functions not properly connected, audio function never called

**Why You're Struggling**:
It's NOT because you're dumb - it's because:
1. **Library Overload**: `pytubefix` handles complex YouTube internals - you're learning the API while coding
2. **Scope Issues**: Python variable scope trips up everyone initially
3. **Flow Control**: Managing user input, validation, and multiple download paths is complex

**How to Improve (Without AI)**:
1. **Start Small**: Master one feature first (just video download)
2. **Read Library Docs**: Focus on `pytubefix` examples and methods
3. **Debug Step-by-Step**: Add print statements to see what's happening
4. **Test in Python REPL**: Try library commands interactively first

**Suggested Approach**:
```python
# 1. Get basic video working
def download_video():
    url = input("URL: ")
    yt = YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams.get_highest_resolution()
    stream.download("/home/shoyo/Downloads/")
    print("completed!")

# 2. Add user choices later
```

**Key Insight**: You're trying to build the full feature list at once. Build ONE working feature, then expand. This is normal - every developer does this.

---
