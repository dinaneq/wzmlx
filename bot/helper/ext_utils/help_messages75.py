#!/usr/bin/env python3
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.ext_utils.TRANSLATE import default_desp

YT_HELP_MESSAGE = ["""<i>Kirim tautan / file bersama dengan cmd atau balas cmd ke mirror atau leech yang didukung ytdl di Telegram atau GDrive atau DDLs dengan Mesin berbeda seperti RClone atau yt-dlp</i>

<blockquote expandable>➲ <b><u>Available Args</u></b>:

1.  <b> - n atau-name: < / b> Ganti nama berkas.
2.  <b> - z atau-zip: < / b> Berkas zip atau Tautan
3.  < b>-naik atau-unggah: < / b> Unggah ke Drive Anda atau RClone atau DDL
4.  <b> - b atau-bulk: < / b> Unduh tautan massal.
5.  <b>-i: < /b> Unduh banyak tautan dengan balas
6.  <b> - m atau-sd atau-samedir: < / b> Unduh banyak tautan dalam direktori unggahan yang sama.
7.  < b>-opt or-options: < / b> Lampirkan opsi yt-dlp Khusus untuk ditautkan
8.  < b>-s atau-select: < / b> Pilih file dari tautan yt-dlp meskipun kualitas ditentukan
9.  < b>-rcf: < / b> RClone Bendera tambahan
10. < b>-id: < / b> Id atau tautan Folder GDrive
11. <b> - indeks: < / b> Url indeks untuk gdrive_arg
12. <b> - c or-category: < / b> Kategori Gdrive untuk Diunggah, Nama Spesifik (tidak peka huruf besar / kecil)
13. < b > -ud atau-dump: < / b> Buang kategori yang akan Diunggah, Nama Tertentu (tidak peka huruf besar / kecil) atau chat_id atau chat_username
14. <b> - ss atau-screenshots: < / b> Hasilkan Tangkapan Layar untuk File Leeched
15. <b> - t atau-thumb: < / b> Tumbnail Khusus untuk Hasil leech Tertentu</blockquote>
""", """
<blockquote expandable>➲ <b><i>Kirim tautan bersama dengan baris perintah</i></b>:
<code>/cmd</code> link -s -n nama baru -opt x:y|x1:y1

➲ <b><i>Dengan membalas tautan</i></b>:
<code>/cmd</code> -n  nama baru -z password -opt x:y|x1:y1

➲ <b><i>Nama Baru</i></b>: -n or -name
<code>/cmd</code> link -n nama baru
<b> Catatan: </b> Jangan menambahkan ekstensi file

➲ <b><i>Pembuatan Tangkapan Layar</b>: -ss or -screenshots
<code>/cmd</code> link -ss number ,Screenshots untuk setiap File Video

➲ <b><i>Custom Thumbnail</b>: -t or -thumb
<code>/cmd</code> link -t tglink|dl_link
<b>Direct Link:</b> dl_link specifies download link, where it is Image url
<b>Tg Link:</b> Give Public/Private/Super Link to download Image from Tg

➲ <b><i>Quality Buttons</i></b>: -s or -select
Memetikan kualitas default ditambahkan dari opsi yt-dlp menggunakan opsi format dan Anda perlu memilih kualitas untuk tautan atau tautan tertentu dengan fitur multi tautan.
<code>/cmd</code> link -s

➲ <b<i>Zip files (dengan/tanpa pasword)</i></b>: -z or -zip password
<code>/cmd</code> link -z (zip)
<code>/cmd</code> link -z password (pasword zip)

➲ <b><i>Options</i></b>: -opt or -options
<code>/cmd</code> link -opt playliststart:^10|fragment_retries:^inf|matchtitle:S13|writesubtitles:true|live_from_start:true|postprocessor_args:{"ffmpeg": ["-threads", "4"]}|wait_for_video:(5, 100)
<b>Note:</b> Tambahkan `^` sebelum integer atau float, beberapa nilai harus berupa numerik dan beberapa string.
Seperti playlist_items:10 berfungsi dengan string, jadi tidak perlu menambahkan "^" sebelum angka tetapi playlistend hanya berfungsi dengan integer jadi Anda harus menambahkan "^" sebelum angka seperti contoh di atas.
Anda juga dapat menambahkan Tuple dan dict. Gunakan tanda kutip ganda di dalam dict.

➲ <b><i>Multi tautan hanya dengan membalas tautan pertama</i></b>: -i
<code>/cmd</code> -i 10(jumlah link)

➲ <b><i>Multi tautan dalam direktori unggahan yang sama hanya dengan membalas tautan pertama</i></b>: -m or -sd or -samedir
<code>/cmd</code> -i 10(jumlah link) -m nama folder

➲ <b><i>Upload Custom Drive:</i></b> -id & -index(Optional)
<code>/{cmd}</code> -id <code>drive_folder_link</code> or <code>drive_id</code> -index <code>https://example.com/0:</code>
Di sini, drive_id harus berupa id folder atau tautan folder dan indeks harus berupa url jika tidak maka tidak akan diterima.

➲ <b><i>Custom Category Select:</i></b> -c or -category
<code>/{cmd}</code> -c <code>category_name</code>
Ini berfungsi untuk Kategori Bot dan juga UserTDs (jika diaktifkan)
Anda juga dapat memilih Drive Upload dari Buttons jika memiliki lebih dari 1 dan argumen ini tidak ditentukan

➲ <b><i>Custom Dump Select:</i></b> -ud or -dump
<code>/{cmd}</code> -ud <code>dump_name</code> or <code>@username</code> or <code>-100xxxxxx chat_id</code> or all
Anda juga dapat memilih Buang Obrolan dari Tombol jika memiliki lebih dari 1 dan argumen ini tidak ditentukan
Anda -ud semua untuk Mengunggah di semua Dump Obrolan Anda
Pastikan Bot sudah menjadi Admin jika tidak, Bot tidak akan menerima.

➲ <b><i>Upload</i></b>: -up or -upload
<code>/cmd</code> link -up <code>rcl</code> (Untuk memilih konfigurasi rclone, remote dan path)
<code>/cmd</code> link -up <code>ddl</code>
Anda dapat langsung menambahkan jalur unggah: -up remote:dir/subdir

Jika DEFAULT_UPLOAD adalah rc maka Anda dapat meneruskan: gd untuk mengunggah menggunakan alat gdrive ke GDRIVE_ID.
Jika DEFAULT_UPLOAD adalah gd maka Anda dapat meneruskan: rc untuk mengunggah ke RCLONE_PATH.
Jika DEFAULT_UPLOAD adalah ddl maka Anda dapat melewatkan: rc atau gd untuk mengunggah ke RCLONE_PATH atau GDRIVE_ID
Jika Anda ingin menambahkan jalur secara manual dari konfigurasi Anda (diunggah dari usetting) tambahkan mrcc: sebelum jalur tanpa spasi
<code>/cmd</code> link -up <code>mrcc:</code>main:dump

➲ <b><i>RClone Flags</i></b>: -rcf
<code>/cmd</code> link -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
This will override all other flags except --exclude
Check here all <a href='https://rclone.org/flags/'>RcloneFlags</a>.

➲ <b><i>Unduhan Massal</i></b>: -b or -bulk
Massal dapat digunakan melalui pesan teks dan dengan membalas file teks berisi tautan yang dipisahkan oleh baris baru.
Anda dapat menggunakannya hanya dengan membalas pesan (teks/file).
Semua opsi harus disertai tautan!
<b>Contoh:</b>
link1 -n nama baru -up remote1:path1 -rcf |key:value|key:value
link2 -z -n nama baru -up remote2:path2
link3 -z -n nama baru -opt ytdlpoptions

<b>Note:</b> Anda tidak dapat menambahkan -m arg hanya untuk beberapa tautan, lakukan untuk semua tautan atau gunakan multi tanpa massal!
tautan pswd: pass(zip) opt: ytdlpoptions up: remote2:path2
Balas contoh ini dengan cmd /cmd b(bulk) ini
Anda dapat mengatur awal dan akhir tautan dari massal dengan -b start:end atau hanya diakhiri dengan -b :end atau hanya dimulai dengan -b start. Awal defaultnya adalah dari nol (tautan pertama) hingga inf.

➲ <b>NOTES:</b>
Periksa semua opsi API yt-dlp dari <a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184'>FILE</a> ini </blockquote>
"""]


MIRROR_HELP_MESSAGE = ["""<i>Kirim tautan/file bersama dengan cmd atau balas cmd ke mirror atau leech di Telegram atau GDrive atau DDL dengan Mesin berbeda seperti RClone, Aria2 atau qBit</i>

<blockquote expandable>➲ <b><u>Argumen yang tersedia</u></b>:

1. <b>-n atau -name : </b> </b> </b> Ganti nama file.
2. <b>-z atau -zip : </b> File zip atau Tautan
3. <b>-e atau -extract atau -uz atau -unzip : </b> Ekstrak/Unzip file dari Arsip
4. <b>-up atau -upload : </b> Unggah ke Drive atau RClone atau DDL Anda
6. <b>-b atau -bulk : </b> Unduh tautan massal.
7. <b>-i : </b> Unduh multi tautan dengan membalas
9. <b>-m atau -sd atau -samedir : </b> Unduh multi tautan dalam direktori unggahan yang sama.
10. <b>-d atau -seed : </b> torrent benih Bittorrent.
11. <b>-s atau -select : </b> Pilih file dari torrent melalui Bittorrent
12. <b>-u atau -user : </b> Masukkan nama pengguna untuk Auth
13. <b>-p atau -pass : </b> Masukkan kata sandi untuk Auth
14. <b>-j atau -join : </b> Menggabungkan Banyak File.
15. <b>-rcf : </b> RClone Bendera tambahan
16. <b>-id : </b> Id atau tautan Folder GDrive
17. <b>-index: Indeks url untuk gdrive_arg
18. <b>-c atau -category : </b> Kategori Gdrive yang akan diunggah, Nama Tertentu (tidak peka huruf besar-kecil)
19. <b>-ud atau -dump : </b> Buang kategori untuk Diunggah, Nama Tertentu (tidak peka huruf besar/kecil) atau chat_id atau chat_username
20. <b>-ss atau -screenshots : </b> Menghasilkan Tangkapan Layar untuk File Leeched
21. <b>-t atau -thumb : </b> Jempol Khusus untuk Lintah Tertentu</blockquote>
""", """
<blockquote expandable>➲ <b><i>By along the cmd</i></b>:
<code>/cmd</code> link -n nama baru

➲ <b><i>By replying to link/file</i></b>:
<code>/cmd</code> -n nama baru -z -e -up upload_destination

➲ <b><i>Custom New Name</i></b>: -n or -name
<code>/cmd</code> link -n nama baru
<b>NOTES</b>: Doesn't work with torrents.

➲ <b><i>Direct Link Authorization</i></b>: -u -p or -user -pass
<code>/cmd</code> link -u username -p password

➲ <b><i>Direct link custom headers</i></b>: -h or -headers
<code>/cmd</code> link -h key: value key1: value1

➲ <b><i>Pembuat tangkapan layar</b>: -ss or -screenshots
<code>/cmd</code> link -ss number ,Screenshots for each Video File

➲ <b><i>Custom Thumbnail</b>: -t or -thumb
<code>/cmd</code> link -t tglink|dl_link
<b>Direct Link:</b> dl_link specifies download link, where it is Image url
<b>Tg Link:</b> Give Public/Private/Super Link to download Image from Tg

➲ <b><i>Extract / Zip</i></b>: -uz -z or -zip -unzip or -e -extract
<code>/cmd</code> link -e password (extract password protected)
<code>/cmd</code> link -z password (zip password protected)
<code>/cmd</code> link -z password -e (extract and zip password protected)
<code>/cmd</code> link -e password -z password (extract password protected and zip password protected)
<b>NOTES:</b> Ketika ekstrak dan zip ditambahkan dengan cmd, ia akan mengekstrak terlebih dahulu lalu zip, jadi selalu ekstrak terlebih dahulu

➲ <b><i>qBittorrent selection</i></b>: -s or -select
<code>/cmd</code> link -s or by replying to file/link

➲ <b><i>qBittorrent / Aria2 Seed</i></b>: -d or -seed
<code>/cmd</code> link -d ratio:seed_time or by replying to file/link
To specify ratio and seed time add -d ratio:time. Ex: -d 0.7:10 (ratio and time) or -d 0.7 (only ratio) or -d :10 (only time) where time in minutes.

➲ <b><i>Multi tautan hanya dengan membalas tautan/file pertama</i></b>: -i
<code>/cmd</code> -i 10(Jumlah link)

➲ <b><i>Multi tautan dalam direktori unggahan yang sama hanya dengan membalas tautan/file pertama</i></b>: -m or -sd or -samedir
<code>/cmd</code> -i 10(Jumlah link) -m folder name (multi message)
<code>/cmd</code> -b -m Nama folder (bulk-message/file)

➲ <b><i>Upload Custom Drive:</i></b> -id & -index(Optional)
<code>/{cmd}</code> -id <code>drive_folder_link</code> or <code>drive_id</code> -index <code>https://example.com/0:</code>
Di sini, drive_id harus berupa id folder atau tautan folder dan indeks harus berupa url jika tidak maka tidak akan diterima.

➲ <b><i>Custom Category Select:</i></b> -c or -category
<code>/{cmd}</code> -c <code>category_name</code>
Ini berfungsi untuk Kategori Bot dan juga UserTDs (jika diaktifkan)
Anda juga dapat memilih Drive Upload dari Buttons jika memiliki lebih dari 1 dan argumen ini tidak ditentukan🔴

➲ <b><i>Custom Dump Select:</i></b> -ud or -dump
<code>/{cmd}</code> -ud <code>dump_name</code> or <code>@username</code> or <code>-100xxxxxx chat_id</code> or all
You can also select Dump Chat from Buttons if having more than 1 and this arg not specified
You -ud all for Uploading in all Dump Chats of yours
Make Sure Bot is already Admin else it will not accept.

➲ <b><i>Custom Upload</i></b>: -up or -upload
<code>/cmd</code> link -up <code>rcl</code> (To select rclone config, remote and path)
<code>/cmd</code> link -up <code>ddl</code>
You can directly add the upload path: -up remote:dir/subdir

If DEFAULT_UPLOAD is `rc` then you can pass up: `gd` to upload using gdrive tools to GDRIVE_ID.
If DEFAULT_UPLOAD is `gd` then you can pass up: `rc` to upload to RCLONE_PATH.
If DEFAULT_UPLOAD is `ddl` then you can pass up: `rc` or `gd` to upload to RCLONE_PATH or GDRIVE_ID
If you want to add path manually from your config (uploaded from usetting) add <code>mrcc:</code> before the path without space
<code>/cmd</code> link -up <code>mrcc:</code>main:dump

➲ <b><i>RClone Flags</i></b>: -rcf
<code>/cmd</code> link|path|rcl -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
This will override all other flags except --exclude
Check here all <a href='https://rclone.org/flags/'>RcloneFlags</a>.</blockquote>

<blockquote expandable>➲ <b><i>Bulk Download</i></b>: -b or -bulk
Bulk can be used by text message and by replying to text file contains links seperated by new line.
You can use it only by reply to message(text/file).
All options should be along with link!
<b>Some Examples:</b>
link1 -n nama baru -up remote1:path1 -rcf |key:value|key:value
link2 -z -n nama baru -up remote2:path2
link3 -uz -n nama baru -up remote2:path2
<b>NOTES:</b> You can't add -m arg for some links only, do it for all links or use multi without bulk!
Reply to this example by this cmd <code>/cmd</code> -b(bulk)
You can set start and end of the links from the bulk like seed, with -b start:end or only end by -b :end or only start by -b start. The default start is from zero(first link) to inf.

➲ <b><i>Join Splitted Files</i></b>: -j or -join
This option will only work before extract and zip, so mostly it will be used with -m argument (samedir)
This option is not Merging of Two links/files.
<b>By Reply:</b>
<code>/cmd</code> -i 3 -j -m folder name
<code>/cmd</code> -b -j -m folder name
If you have link which has splitted files:
<code>/cmd</code> link -j

➲ <b><i>RClone Download</i></b>:
Treat rclone paths exactly like links
<code>/cmd</code> main:dump/ubuntu.iso or <code>rcl</code>(To select config, remote and path)
Users can add their own rclone from user settings

If you want to add path manually from your config add <code>mrcc:</code> before the path without space
<code>/cmd</code> <code>mrcc:</code>main:dump/ubuntu.iso

➲ <b><i>TG Links</i></b>:
Treat tg links like any direct link
Some links need user access so sure you must add USER_SESSION_STRING for it.
<b><u>Types of links:</u></b>
• <b>Public:</b> <code>https://t.me/channel_name/message_id</code>
• <b>Private:</b> <code>tg://openmessage?user_id=xxxxxx&message_id=xxxxx</code>
• <b>Super:</b> <code>https://t.me/c/channel_id/message_id</code>

➲ <b>NOTES:</b>
1. Commands that start with <b>qb</b> are ONLY for torrents.</blockquote>
"""]

RSS_HELP_MESSAGE = """
<blockquote expandable>➲ <b>Format to adding feed url(s):</b>
Title1 link (required)
Title2 link -c cmd -inf xx -exf xx
Title3 link -c cmd -d ratio:time -z password

➲ <b><i>Argument Details:</i></b>
-c command + any arg
-inf For included words filter.
-exf For excluded words filter.

<b>Example:</b> Title https://www.rss-url.com inf: 1080 or 720 or 144p|mkv or mp4|hevc exf: flv or web|xxx opt: up: mrcc:remote:path/subdir rcf: --buffer-size:8M|key|key:value
This filter will parse links that it's titles contains `(1080 or 720 or 144p) and (mkv or mp4) and hevc` and doesn't conyain (flv or web) and xxx` words. You can add whatever you want.

Another example: inf:  1080  or 720p|.web. or .webrip.|hvec or x264. This will parse titles that contains ( 1080  or 720p) and (.web. or .webrip.) and (hvec or x264). I have added space before and after 1080 to avoid wrong matching. If this `10805695` number in title it will match 1080 if added 1080 without spaces after it.

➲ <b><i>Filter Notes:</i></b>
1. | means and.
2. Add `or` between similar keys, you can add it between qualities or between extensions, so don't add filter like this f: 1080|mp4 or 720|web because this will parse 1080 and (mp4 or 720) and web ... not (1080 and mp4) or (720 and web)."
3. You can add `or` and `|` as much as you want."
4. Take look on title if it has static special character after or before the qualities or extensions or whatever and use them in filter to avoid wrong match.</blockquote>

<b>Timeout:</b> 60 sec.
"""

CLONE_HELP_MESSAGE = ["""<i>Send Gdrive | Gdtot | Filepress | Filebee | Appdrive | Gdflix link or RClone path along with or by replying to the link/rc_path by command with args.</i>

<blockquote expandable>➲ <b><u>Available Args</u></b>:

1. <b>-up or -upload :</b> Upload to your Drive or RClone or DDL
2. <b>-i :</b> Download multi links by reply
3. <b>-rcf :</b> RClone additional Flags
4. <b>-id :</b> GDrive Folder id or link
5. <b>-index:</b> Index url for gdrive_arg
6. <b>-c or -category :</b> Gdrive category to Upload, Specific Name (case insensitive)</blockquote>""",
"""➲ <b><i>Links:</i></b>
Gdrive | Gdtot | Filepress | Filebee | Appdrive | Gdflix link or rclone path

<blockquote expandable>➲ <b><i>Multi Links (only by replying to first gdlink or rclone_path):</i></b>
<code>/cmd</code> -i 10(number of links/paths)

➲ <b><i>Gdrive Link:</i></b>
<code>/cmd</code> gdrive_link

➲ <b><i>RClone Path with RC Flags:</i></b> -rcf
<code>/cmd</code> (rcl or rclone_path) -up (rcl or rclone_path) -rcf flagkey:flagvalue|flagkey|flagkey:flagvalue

➲ <b><i>Upload Custom Drive:</i></b> -id & -index(Optional)
<code>/{cmd}</code> -id <code>drive_folder_link</code> or <code>drive_id</code> -index <code>https://example.com/0:</code>

➲ <b><i>Custom Category Select:</i></b> -c or -category
<code>/{cmd}</code> -c <code>category_name</code>

<b>NOTES:</b>
1. If -up or -upload not specified then rclone destination will be the RCLONE_PATH from <code>config.env</code>.
2. If UserTD enabled, then only it will upload to UserTD either by direct arg or category buttons.
3. For Multi Custom Upload always use Arg in respective msgs and then reply with /cmd -i 10(number)</blockquote>
"""]

CATEGORY_HELP_MESSAGE = """Reply to an active /{cmd} which was used to start the download or add gid along with {cmd}
This command mainly for change category incase you decided to change category from already added download.
But you can always use -c or -category with to select category before download start.

<blockquote expandable>➲ <b><i>Upload Custom Drive</i></b>
<code>/{cmd}</code> -id <code>drive_folder_link</code> or <code>drive_id</code> -index <code>https://example.com/0:</code> gid or by replying to active download

<b>NOTE:</b> drive_id must be folder id or folder link and index must be url else it will not accept.
"""

help_string = [f'''⌬ <b><i>Bᴀsɪᴄ Cᴏᴍᴍᴀɴᴅs!</i></b>

<blockquote expandable><b>Use Mirror commands to download your link/file/rcl</b>
┠ /{BotCommands.MirrorCommand[0]} or /{BotCommands.MirrorCommand[1]}: Download via file/url/media to Upload to Cloud Drive.
┖ /{BotCommands.CategorySelect}: Select Custom category to Upload to Cloud Drive from UserTds or Bot Categories.

<b>Use qBit commands for torrents only:</b>
┠ /{BotCommands.QbMirrorCommand[0]} or /{BotCommands.QbMirrorCommand[1]}: Download using qBittorrent and Upload to Cloud Drive.
┖ /{BotCommands.BtSelectCommand}: Select files from torrents by btsel_gid or reply.

<b>Use yt-dlp commands for YouTube or any supported sites:</b>
┖ /{BotCommands.YtdlCommand[0]} or /{BotCommands.YtdlCommand[1]}: Mirror yt-dlp supported link.

<b>Use Leech commands for upload to Telegram:</b>
┠ /{BotCommands.LeechCommand[0]} or /{BotCommands.LeechCommand[1]}: Upload to Telegram.
┠ /{BotCommands.QbLeechCommand[0]} or /{BotCommands.QbLeechCommand[1]}: Download using qBittorrent and upload to Telegram(For torrents only).
┖ /{BotCommands.YtdlLeechCommand[0]} or /{BotCommands.YtdlLeechCommand[1]}: Download using Yt-Dlp(supported link) and upload to telegram.

<b>G-Drive commands:</b>
┠ /{BotCommands.CloneCommand[0]}: Copy file/folder to Cloud Drive.
┠ /{BotCommands.CountCommand} [drive_url]: Count file/folder of Google Drive.
┖ /{BotCommands.DeleteCommand} [drive_url]: Delete file/folder from Google Drive (Only Owner & Sudo).

<b>Cancel Tasks:</b>
┖ /{BotCommands.CancelMirror}: Cancel task by cancel_gid or reply.</blockquote>''',

f'''⌬ <b><i>Usᴇʀs Cᴏᴍᴍᴀɴᴅs!</i></b>

<blockquote expandable><b>Bot Settings:</b>
┖ /{BotCommands.UserSetCommand[0]} or /{BotCommands.UserSetCommand[1]} [query]: Open User Settings (PM also)

<b>Authentication:</b>
┖ /login: Login to Bot to Access Bot without Temp Pass System (Private)

<b>Bot Stats:</b>
┠ /{BotCommands.StatusCommand[0]} or /{BotCommands.StatusCommand[1]}: Shows a status page of all active tasks.
┠ /{BotCommands.StatsCommand[0]} or /{BotCommands.StatsCommand[1]}: Show Server detailed stats.
┖ /{BotCommands.PingCommand[0]} or /{BotCommands.PingCommand[1]}: Check how long it takes to Ping the Bot.

<b>RSS Feed:</b>
┖ /{BotCommands.RssCommand}: Open RSS Menu (Sub/Unsub/Start/Pause)</blockquote>''',

f'''⌬ <b><i>Oᴡɴᴇʀ ᴏʀ Sᴜᴅᴏs Cᴏᴍᴍᴀɴᴅs!</i></b>

<blockquote expandable><b>Bot Settings:</b>
┠ /{BotCommands.BotSetCommand[0]} or /{BotCommands.BotSetCommand[1]} [query]: Open Bot Settings (Only Owner & Sudo).
┖ /{BotCommands.UsersCommand}: Show User Stats Info (Only Owner & Sudo).

<b>Authentication:</b>
┠ /{BotCommands.AuthorizeCommand[0]} or /{BotCommands.AuthorizeCommand[1]}: Authorize a chat or a user to use the bot (Only Owner & Sudo).
┠ /{BotCommands.UnAuthorizeCommand[0]} or /{BotCommands.UnAuthorizeCommand[1]}: Unauthorize a chat or a user to use the bot (Only Owner & Sudo).
┠ /{BotCommands.AddSudoCommand}: Add sudo user (Only Owner).
┠ /{BotCommands.RmSudoCommand}: Remove sudo users (Only Owner).
┠ /{BotCommands.AddBlackListCommand[0]} or /{BotCommands.AddBlackListCommand[1]}: Add User in BlackListed, so that user can't use the Bot anymore.
┖ /{BotCommands.RmBlackListCommand[0]} or /{BotCommands.RmBlackListCommand[1]}: Remove a BlackListed User, so that user can again use the Bot.

<b>Bot Stats:</b>
┖ /{BotCommands.BroadcastCommand[0]} or /{BotCommands.BroadcastCommand[1]} [reply_msg]: Broadcast to PM users who have started the bot anytime.

<b>G-Drive commands:</b>
┖ /{BotCommands.GDCleanCommand[0]} or /{BotCommands.GDCleanCommand[1]} [drive_id]: Delete all files from specific folder in Google Drive.

<b>Cancel Tasks:</b>
┖ /{BotCommands.CancelAllCommand[0]}: Cancel all Tasks & /{BotCommands.CancelAllCommand[1]} for Multiple Bots.

<b>Maintainance:</b>
┠ /{BotCommands.RestartCommand[0]} or /{BotCommands.RestartCommand[1]}: Restart and Update the Bot (Only Owner & Sudo).
┠ /{BotCommands.RestartCommand[2]}: Restart and Update all Bots (Only Owner & Sudo).
┖ /{BotCommands.LogCommand}: Get a log file of the bot. Handy for getting crash reports (Only Owner & Sudo).

<b>Executors:</b>
┠ /{BotCommands.ShellCommand}: Run shell commands (Only Owner).
┠ /{BotCommands.EvalCommand}: Run Python Code Line | Lines (Only Owner).
┠ /{BotCommands.ExecCommand}: Run Commands In Exec (Only Owner).
┠ /{BotCommands.ClearLocalsCommand}: Clear {BotCommands.EvalCommand} or {BotCommands.ExecCommand} locals (Only Owner).
┖ /exportsession: Generate User StringSession of Same Pyro Version (Only Owner).

<b>RSS Feed:</b>
┖ /{BotCommands.RssCommand}: Open RSS Menu (Sub/Unsub/Start/Pause)

<b>Extras:</b>
┠ /{BotCommands.AddImageCommand} [url/photo]: Add Images in Bot
┖ /{BotCommands.ImagesCommand}: Generate grid of Stored Images.</blockquote>''',

f'''⌬ <b><i>Mɪsᴄᴇʟʟᴀɴᴇᴏᴜs Cᴏᴍᴍᴀɴᴅs!</i></b>

<blockquote expandable><b>Extras:</b>
┠ /{BotCommands.SpeedCommand[0]} or /{BotCommands.SpeedCommand[1]}: Check Speed in VPS/Server.
┖ /{BotCommands.MediaInfoCommand[0]} or /{BotCommands.MediaInfoCommand[1]} [url/media]: Generate MediaInfo of Media or DL Urls

<b>Torrent/Drive Search:</b>
┠ /{BotCommands.ListCommand} [query]: Search in Google Drive(s).
┖ /{BotCommands.SearchCommand} [query]: Search for torrents with API.

<b>Movie/TV Shows/Drama Search:</b>
┠ /{BotCommands.IMDBCommand}: Search in IMDB.
┠ /{BotCommands.AniListCommand}: Search for anime in AniList.
┠ /{BotCommands.AnimeHelpCommand}: Anime help guide.
┖ /{BotCommands.MyDramaListCommand}: Search in MyDramaList.</blockquote>
''']

PASSWORD_ERROR_MESSAGE = """
<blockquote expandable><b>This link requires a password!</b>
- Insert sign <b>::</b> after the link and write the password after the sign.
<b>Example:</b> {}::love you
Note: No spaces between the signs <b>::</b>
For the password, you can use a space!</blockquote>
"""