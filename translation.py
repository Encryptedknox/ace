class Translation(object):
    START_TEXT = """Hi {} 🤗,
I'm <b>Url Uploader Bot! ✨</b>

Send me a direct link and I will upload it to telegram as a file/video.</b>

/help for more details <a href='https://telegram.me/aceknox'> !
"""
    ADD_CAPTION_HELP = """Select an uploaded file/video or forward me <b>Any Telegram File</b> and just write the text you want to be on the file <b>as a reply to the file</b> and the text you wrote will be attached as the caption! 🤩
    
Ex: <a href='https://telegra.ph/file/0d4cf1d5677dda9311135.png'>See This!</a> 👇"""
    INCORRECT_REQUEST = """Make sure you submit your request correctly
    
/help for more details!"""
    DISPLAY_PROGRESS = """[{0}{1}] {2}%
 🗃️ {3}
▫️ Finished :</b> {4} of {5}
▫️ Speed :</b> {6}/s
▫️ Time Left :</b> {7}"""
    FORMAT_SELECTION = """<b> thumbnail will automatically generated if you not set <b>
    
Select and choose format 
<b>larger than 2 GB not support.</b>"""
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    DOWNLOAD_START = """<b>File detected:</b> {}
    
<b>Initiating download... </b>"""
    UPLOAD_START = "<b>Uploading to Telegram... </b>"
    RCHD_TG_API_LIMIT = """<b>The file couldn't be uploaded</b>
Sorry. I cannot upload files greater than 2GB due to Telegram API limitations.
▫️ File Detected:</b> {}
▫️ Downloaded:</b> in {} seconds
▫️ File Size:</b> {}"""
    UNKNOWN_ERROR = """Unknown error"""
    AFTER_SUCCESSFUL_UPLOAD_MSG = " Thanks for using @knoxprojects."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = """◽ Downloaded in <b>{} seconds</b>
◽ Uploaded in <b>{} seconds</b>"""
    SAVED_CUSTOM_THUMB_NAIL = "◽ Custom video/file thumbnail saved. This image will be used in the video/file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "◽ Custom thumbnail cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_FILE_FOUND = """I couldn't find any video/file
Go check if you can access the content in the URL from your browser first!"""
    NO_VOID_FORMAT_FOUND = """Something went wrong 
I think you have entered an unaccessible URL or a private URL.
Additional info:
{}"""
    HELP_USER = """<b>How to use me?</b> 🤔
Follow these steps! 👇
    
<b>1. Send URL</b>
If you want a custom caption on your video/file send the name/text you want to set on the video/file in the following format 👇
<b>Link * caption</b> (without extension). 
<i>[Separate the link and the caption name with "*" mark].</i>
<u>It is important that you separate with spaces the URL, * and the caption.</u>
<b>👍 Send something like this:</b>
<code>https://www.website.com/video.mp4 * caption text</code>
<b>🤡 Not like this:</b>
<code>❌ https://www.website.com/video.mp4*caption text ❌</code>
The caption/text you type will be automatically set as the custom name of the uploaded file 😎
<i><b>Note:</b> You can change/add any caption later if you want as explained in the end.</i>
<b>2. Then send custom thumbnail when asked while uploading the URL</b> (This step is optional) 
🔹 It means it is not necessary to send an image to include as an thumbnail.
If you don't send a thumbnail the video/file will be uploaded with an auto generated thumbnail from the video.
<i>(The thumbnail you send will be used for your next uploads)</i>
🔹 Press /delthumbnail if you want to delete the previously saved thumbnail.
<i>(Then the video will be uploaded with an auto-genarated thumbnail)</i>
<b>3. Select the button</b>
  <u>Video-option</u>: Give video/file in video format
  <u>File-option</u>: Give video/file in file format
   
<b>👉 Special feature: Set caption to any file you want! ✨</b>
🔹 Select an uploaded file/video or forward me <b>Any Telegram File</b> and just write the text you want to be on the file <b>as a reply to the file</b> by selecting it (as replying to a message) and the text you wrote will be attached as caption! 🤩
Ex: <a href='https://telegra.ph/file/0d4cf1d5677dda9311135.png'>Send Like This! It's Easy</a> 🥳"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail."
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
You can use /rename command after receiving file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "Process Cancelled."
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds."
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DONATE = """ <b>appreciate my work</b>
             Contact admin : @aceknox """
    ABOUT =""" 
◽ My Name  : Url Uploader Bot
◽ Channel : @knoxprojects
◽ Support  : @knoxsupport
◽ Source : [Ace](https://github.com/aceknox)
◽ Server  : [Heroku](https://heroku.com)
◽ Language : [Python 3.10.5](https://www.python.org/)
◽ Framework  : [Pyrogram 1.8.30](https://docs.pyrogram.org/)
◽ Developer  : @aceknox
"""
    COMMANDS = """
◽ /start - check status
◽ /help - for more
◽ /about - me
◽ /donate - contribution
"""
