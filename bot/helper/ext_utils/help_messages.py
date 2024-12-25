#!/usr/bin/env python3
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.ext_utils.TRANSLATE import default_desp , MIRROR_HELP_MESSAGE
from bot.helper.ext_utils.translate_optional import PASSWORD_ERROR_MESSAGE , CLONE_HELP_MESTY[[[[["https://telegra.ph/Help-12-25-1              
  
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


CATEGORY_HELP_MESSAGE = """id: Balas ke aktif /{cmd} yang digunakan untuk memulai pengunduhan atau tambahkan gid bersama dengan {cmd}
Perintah ini terutama untuk mengubah kategori jika Anda memutuskan untuk mengubah kategori dari unduhan yang sudah ditambahkan..
Tetapi Anda selalu dapat menggunakan-c atau -category with untuk memilih kategori sebelum pengunduhan dimulai.

<blockquote dapat diperluas>➲
<code> / {cmd}</code> - id <code>drive_folder_link<code> atau <code>drive_id</code> -indeks <code>https://example.com/0: </code> gid atau dengan membalas unduhan aktif

<b>CATATAN: </b> drive_id harus berupa id folder atau tautan folder dan indeks harus berupa url jika tidak maka tidak akan diterima
"""

help_string = [f'''⌬ <bold><i>Perintah Dasar!</i></bold>

<bold>Gunakan perintah Mirror untuk mengunduh link/file/rcl</bold>
• /{BotCommands.MirrorCommand[0]} or /{BotCommands.MirrorCommand[1]}: Unduh melalui file/url/media untuk Diunggah ke Cloud Drive.
• /{BotCommands.CategorySelect}: Pilih kategori Khusus untuk Diunggah ke Cloud Drive dari Kategori UserTds atau Bot.

<bold>Gunakan perintah qBit hanya untuk torrent:</bold>
• /{BotCommands.QbMirrorCommand[0]} or /{BotCommands.QbMirrorCommand[1]}: Unduh menggunakan qBittorrent dan Unggah ke Cloud Drive.
• /{BotCommands.BtSelectCommand}: Select files from torrents by btsel_gid or reply.

<bold>Gunakan perintah yt-dlp untuk YouTube atau situs apa pun yang didukung:</bold>
• /{BotCommands.YtdlCommand[0]} atau /{BotCommands.YtdlCommand[1]}: Mencerminkan tautan yang didukung yt-dlp.

<bold>Gunakan perintah Leech untuk mengunggah ke Telegram:</bold>
• /{BotCommands.LeechCommand[0]} atau /{BotCommands.LeechCommand[1]}: Unggah ke Telegram.
• /{BotCommands.QbLeechCommand[0]} atau /{BotCommands.QbLeechCommand[1]}: Unduh menggunakan qBittorrent dan unggah ke Telegram (Hanya untuk torrent).
• /{BotCommands.YtdlLeechCommand[0]} atau /{BotCommands.YtdlLeechCommand[1]}: Unduh menggunakan Yt-Dlp (tautan yang didukung) dan unggah ke telegram.

<bold>Perintah G-Drive:</bold>
• /{BotCommands.CloneCommand[0]}: Salin file/folder ke Cloud Drive.
• /{BotCommands.CountCommand} [drive_url]: Menghitung file/folder Google Drive.
• /{BotCommands.DeleteCommand} [drive_url]: Hapus file/folder dari Google Drive (Hanya Pemilik & Sudo).

<bold>Batalkan Tugas:</bold>
• /{BotCommands.CancelMirror}: Batalkan tugas dengan cancel_gid atau balas.''',

f'''⌬ <bold><i>Perintah Pengguna</i></bold>

<bold>Bot Settings:</bold>
• /{BotCommands.UserSetCommand[0]} or /{BotCommands.UserSetCommand[1]} [query]: Buka Bot Setting hanya di PM

<bold>Otentikasi:</bold>
• /login: Login ke Bot untuk Mengakses Bot tanpa Sistem Temp Pass (Pribadi)

<bold>Statistik Bot:</bold>
• /{BotCommands.StatusCommand[0]} atau /{BotCommands.StatusCommand[1]}: Menampilkan halaman status dari semua tugas aktif.
• /{BotCommands.StatsCommand[0]} atau /{BotCommands.StatsCommand[1]}: Menampilkan statistik detail Server.
• /{BotCommands.PingCommand[0]} atau /{BotCommands.PingCommand[1]}: Periksa berapa lama waktu yang dibutuhkan untuk melakukan Ping ke Bot.

<bold>RSS Feed:</bold>
• /{BotCommands.RssCommand}: Open RSS Menu (Sub/Unsub/Start/Pause)''',

f'''⌬ <bold><i>Perintah Admin</i></bold>

<bold>Bot Settings:</bold>
• /{BotCommands.BotSetCommand[0]} atau /{BotCommands.BotSetCommand[1]} [query]: Buka Pengaturan Bot (Hanya Pemilik & Sudo).
• /{BotCommands.UsersCommand}: Menampilkan Info Statistik Pengguna (Hanya Pemilik & Sudo).

<bold>Otentikasi:</bold>
• /{BotCommands.AuthorizeCommand[0]} atau /{BotCommands.AuthorizeCommand[1]}: Mengotorisasi obrolan atau pengguna untuk menggunakan bot (Hanya Pemilik & Sudo).
• /{BotCommands.UnAuthorizeCommand[0]} atau /{BotCommands.UnAuthorizeCommand[1]}: Membatalkan otorisasi chat atau pengguna untuk menggunakan bot (Hanya Pemilik & Sudo).
• /{BotCommands.AddSudoCommand}: Tambahkan pengguna sudo (Pemilik Saja).
• /{BotCommands.RmSudoCommand}: Hapus pengguna sudo (Pemilik Saja).
• /{BotCommands.AddBlackListCommand[0]} atau /{BotCommands.AddBlackListCommand[1]}: Menambahkan Pengguna di Daftar Hitam, sehingga pengguna tidak dapat menggunakan Bot lagi.
• /{BotCommands.RmBlackListCommand[0]} atau /{BotCommands.RmBlackListCommand[1]}: Menghapus Pengguna yang Masuk Daftar Hitam, sehingga pengguna dapat menggunakan Bot lagi.

<bold>Statistik Bot:</bold>
• /{BotCommands.BroadcastCommand[0]} atau /{BotCommands.BroadcastCommand[1]} [reply_msg]: Disiarkan ke pengguna PM yang telah memulai bot kapan saja.

<bold>Perintah G-Drive:</bold>
• /{BotCommands.GDCleanCommand[0]} atau /{BotCommands.GDCleanCommand[1]} [drive_id]: Hapus semua file dari folder tertentu di Google Drive.

<bold>Batalkan Tugas:</bold>
• /{BotCommands.CancelAllCommand[0]}: Membatalkan semua Tugas & /{BotCommands.CancelAllCommand[1]} untuk Beberapa Bot.

<bold>Pemeliharaan:</bold>
• /{BotCommands.RestartCommand[0]} atau /{BotCommands.RestartCommand[1]}: Mulai ulang dan Perbarui Bot (Hanya Pemilik & Sudo).
• /{BotCommands.RestartCommand[2]}: Mulai ulang dan Perbarui semua Bot (Hanya Pemilik & Sudo).
• /{BotCommands.LogCommand}: Dapatkan file log bot. Berguna untuk mendapatkan laporan kerusakan (Hanya Pemilik & Sudo).

<bold>Ececutors:</bold>
• /{BotCommands.ShellCommand}: Jalankan perintah shell (Hanya Pemilik).
• /{BotCommands.EvalCommand}: Jalankan Baris Kode Python | Garis (Hanya Pemilik).
• /{BotCommands.ExecCommand}: Jalankan Perintah Di Exec (Hanya Pemilik).
• /{BotCommands.ClearLocalsCommand}: Hapus {BotCommands.EvalCommand} atau {BotCommands.ExecCommand} penduduk lokal (Pemilik Saja).
• /exportsession: Menghasilkan User StringSession dari Versi Pyro yang Sama (Hanya Pemilik).

<bold>Umpan RSS:</bold>
• /{BotCommands.RssCommand}: Buka Menu RSS (Sub/Batal Sub/Mulai/Jeda)

<bold>Ekstra:</bold>
• /{BotCommands.AddImageCommand} [url/foto]: Tambahkan Gambar di Bot
• /{BotCommands.ImagesCommand}: Menghasilkan grid Gambar Tersimpan.''',

f'''⌬ <bold><i>Perintah lain-lain!</i></bold>

<bold>Ekstra:</bold>
• /{BotCommands.SpeedCommand[0]} atau /{BotCommands.SpeedCommand[1]}: Periksa Kecepatan di VPS/Server.
• /{BotCommands.MediaInfoCommand[0]} atau /{BotCommands.MediaInfoCommand[1]} [url/media]: Menghasilkan MediaInfo dari Media atau Url DL

<bold>Pencarian Torrent/Drive:</bold>
• /{BotCommands.ListCommand} [kueri]: Telusuri di Google Drive.
• /{BotCommands.SearchCommand} [query]: Mencari torrent dengan API.

<bold>Pencarian Film/Acara TV/Drama:</bold>
• /{BotCommands.IMDBCommand}: Cari di IMDB.
• /{BotCommands.AniListCommand}: Mencari anime di AniList.
• /{BotCommands.AnimeHelpCommand}: Panduan bantuan anime.
• /{BotCommands.MyDramaListCommand}: Cari di MyDramaList.
''']
