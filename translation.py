class Translation(object):
    START_TEXT = """Yo, I am a Powefull URL Upload Bot 🤓!

I can support Hotstar, Google Drive, and much more Links😌!

Send Me Any Direct Download URL Link, I Can Upload To Telegram As File/Video!

Added Permanent Thumbnail Support💯😋!!

Support Group : @HxSupport
"""

    ABOUT_TEXT = """⭕️<b>My Name : @HxURLuploadBot</b>

⭕️<b>Creater : @Kirodewal</b>

⭕️<b>Language : Python3</b>

⭕️<b>Library : Pyrogram 1.2.9</b>

⭕️<b>Source Code : 👉 <a href='https://github.com/Kirodewal/URLuploader-With-Hotstar'>Click Here</a></b>"""

    FORMAT_SELECTION = """<b>Choose appropriate option</b> <a href='{}'>⬇️</a>
🎞  - Stream format
📁  - File format
<i>NOTE : Taking high resolutions may result in files above 2GB and hence cannot Upload to TG. So better select a medium resolution.</i> 😇
    
Send your custum thumbnail if required.
You can use /deletethumbnail to delete the auto-generated thumbnail."""

    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""

    DOWNLOAD_START = "Trying to download your file..."

    UPLOAD_START = "Now Uploading.."

    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."

    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thanks for using @hx_urluploadbot"

    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds.\n\n@hx_urluploadbot"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."

    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."

    CUSTOM_CAPTION_UL_FILE = "{}"

    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"

    HELP_USER = """It's not that complicated😅
    
1. Send Me A Tumbnail if required. It'll be saved permanently.💯
2. If Thumbnail Wasn't Set By You, It'll Be Auto Generated From The File.🥳
3. Send Me Any Link To Be Uploaded To Telegram.
4. Press /deletthumbnail To Delete Your Current Custom Thumbnail
5. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File with Screenshots
   Video  - Give File as video without Screenshots
   DFile  - Give File without Screenshots
NB : It is Recommended To Use A Custom Thubnail Because, Some Time Wont Upload The File Without a Custom Thubnail.
Support Group : @HxSupport
"""

    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /genthumbnail to a media album, to generate custom thumbnail"

    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."

    CANCEL_STR = "Process Cancelled"

    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"

    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
