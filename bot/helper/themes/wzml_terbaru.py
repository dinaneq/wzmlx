#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = 'Original Repo'
    ST_BN1_URL = 'https://ouo.io/Sjev3s'
    ST_BN2_NAME = 'Repo This bot'
    ST_BN2_URL = 'https://ouo.io/r87GFB'
    ST_MSG = '''Dapat mengunggah file, tautan, torrents, dll. Untuk Telegram, Google Drive, server DDL dan situs yang didukung RCLone!\n\n'''
    ST_BOTPM = '''<b>🕵️ Bot PM berhasil dimulai! \n\nℹ️ Saya akan mengirim semua file dan tautan Anda di sini</b>.'''
    ST_UNAUTH = '''<b>⚠️ Akses ditolak!</b>'''
    LOG_DISPLAY_BT = '📑 Lihat Log'
    WEB_PASTE_BT = '📨 Wᴇʙ Pᴀsᴛᴇ (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Dasar'
    USER_BT = 'Pengguna'
    MICS_BT = 'Lainnya'
    O_S_BT = 'Pemilik & Admin'
    CLOSE_BT = 'Tutup'
    HELP_HEADER = "㊂ <b><i>Petunjuk menggunakan menu bantuan!</i></b>\n\n<b>Nᴏᴛᴇ: <i>Klik pada PERINTAH mana pun untuk melihat detail kecil lainnya.</i></b>"
    # ---------------------

    # async def stats(client, message):
    BOT_STATS = '''<b>🤖 <u>𝘽𝙤𝙩 𝙎𝙩𝙖𝙩𝙞𝙨𝙩𝙞𝙘𝙨</u></b>
    
<b>⏰ Bot Uptime :</b> {bot_uptime}

<b>💽 RAM</b>
➢{ram_bar} » ({ram}%)
➢<b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

<b>👒 SWAP</b>
➢{swap_bar} » ({swap}%)
➢<b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

<b>📦 DISK</b>
➢{disk_bar} » ({disk}%)
➢<b>Total Disk Read :</b> {disk_read}
➢<b>Total Disk Write :</b> {disk_write}
➢<b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}


    
    '''
    SYS_STATS = '''<b>🛠 <u>𝙎𝙮𝙨𝙩𝙚𝙢 𝙎𝙩𝙖𝙩𝙞𝙨𝙩𝙞𝙘𝙨</u></b>
    
<b>⏰ OS Uptime :</b> {os_uptime}
<b>☢️ OS Info :</b> {os_version}
➢<b>🔧 OS Arch :</b> {os_arch}

<b>🖥️ CPU</b>
➢{cpu_bar} » ({cpu}%)
➢<b>Frequency :</b> {cpu_freq}
➢<b>Average Load :</b> {sys_load}
➢<b>P-Cores :</b> {p_core} | <b>V-Cores :</b> {v_core}
➢<b>Total Cores :</b> {total_core}
➢<b>Usable CPUs :</b> {cpu_use}

<b>📶 Network Stats</b>
➢<b>Upload Data:</b> {up_data}
➢<b>Download Data:</b> {dl_data}
➢<b>Pkts Sent:</b> {pkt_sent}k
➢<b>Pkts Received:</b> {pkt_recv}k
➢<b>Total I/O Data:</b> {tl_data}


    '''
    REPO_STATS = '''<b>🧑‍💻 <u>𝙍𝙚𝙥𝙤 𝙎𝙩𝙖𝙩𝙞𝙨𝙩𝙞𝙘𝙨</u></b>
    
<b>♻️ Bot Terupdate :</b> {last_commit}
<b>🆔 Versi Saat ini :</b> {bot_version}
<b>🎈 Versi Terbaru :</b> {lat_version}
<b>📝 Log Perubahan :</b> {commit_details}

<b>💥 REMARKS :</b> <b>{remarks}</b>


    '''
    BOT_LIMITS = '''<b>❗<u>𝘽𝙤𝙩 𝙇𝙞𝙢𝙞𝙩𝙨</u></b>
    
<b>🎯 Direct :</b> <b>{DL} GB</b>
<b>🧲 Torrent :</b> <b>{TL} GB</b>
<b>☁️ GDrive :</b> <b>{GL} GB</b>
<b>📺 YT-DLP :</b> <b>{YL} GB</b>
<b>🎥 Playlist :</b> <b>{PL} Videos</b>
<b>Ⓜ️ Mega :</b> <b>{ML} GB</b>
<b>🎗️ Clone :</b> <b>{CL} GB</b>
<b>📂 Leech :</b> <b>{LL} GB</b>

<b>🔑 Token Validity :</b> {TV}
<b>🐢 Timeout :</b> {UTI}
<b>👤 User Tasks :</b> {UT}
<b>🚧 Total Tasks :</b> {BT}


    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>🔄 Menyalakan Ulang...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''<b>♻️ Bot berhasil di nyalakan! 🎉</b>

<b>📅 Tanggal:</b> {date}
<b>⏰ Waktu:</b> {time}
<b>🌍 ZonaWaktu:</b> {timz}
<b>🆔 Versi:</b> {version}

'''
    RESTARTED = '''<b>🔄 Bot Merestart otomatis!</b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<b>🙄 Starting Ping...</b>'
    PING_VALUE = '<b>Aktive ✅✅✅ \n</b> <b>{value}ms</b>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b>🚧 Tugas Dimulai</b>

<b>💠 Unggah:</b> {Mode}
<b>👤 Pengguna:</b> {Tag}\n\n"""
    LINKS_SOURCE = """<b>💡 Sumber:</b>
<b>⏰ Waktu:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    L_PM_START =            "🏁 <b><u>Leech Dimulai</u> :</b>\n\n<b>💡 sumber :</b> <a href='{msg_link}'>Klik Disini</a>"
    L_LOG_START =           "🏁 <b><u>Leech Dimulai</u> :</b>\n\n➢<b>👤 Pengguna :</b> {mention}\n➢<b>🆔 ID :</b> <b>{uid}</b>\n➢<b>💡 Sumber :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<blockquote><b>{Name}</b></blockquote>\n\n'
    SIZE =                  '<b>💾 Ukuran: </b>{Size}\n'
    ELAPSE =                '<b>⌛ Selesai: </b>{Time}\n'
    MODE =                  '<b>💠 Unggah: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '<b>📂 Total Files: </b>{Files}\n'
    L_CORRUPTED_FILES =     '<b>💀 File Rusak: </b>{Corrupt}\n'
    L_CC =                  '<b>👤 Pengguna: </b>{Tag}\n\n'
    PM_BOT_MSG =            'ℹ️ <b><i>File telah dikirim!</i></b>'
    L_BOT_MSG =             'ℹ️ <b><i>File telah dikirim dalam bot PM!</i></b>'
    L_LL_MSG =              'ℹ️ <b><i>File telah dikirim.Akses melalui tautan!</i></b>'
    
    # ----- MIRROR -------
    M_TYPE =                '<b>📜 Jenis File: </b>{Mimetype}\n'
    M_SUBFOLD =             '<b>🗂️ SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '<b>📂 Files: </b>{Files}\n'
    RCPATH =                '<b>🚩 Path: </b><b>{RCpath}</b>\n'
    M_CC =                  '<b>👤 Pengguna: </b>{Tag}\n\n'
    M_BOT_MSG =             '🏁 <b><i>💥Tautan telah dikirim dalam DM!!</i></b>\n💥Segera amankan file anda, penghapusan/pembersihan drive tidak ada konfirmasi ke pemilik file🙏🙏🙏'
    
    # ----- BUTTONS -------
    CLOUD_LINK =      '♻️ Unduh'
    SAVE_MSG =        '📩 Simpan'
    RCLONE_LINK =     '®️ RClone Link'
    DDL_LINK =        '🚀 {Serv} Link'
    SOURCE_URL =      '💡 Sumber'
    INDEX_LINK_F =    '🚀 Index Link'
    INDEX_LINK_D =    '🚀 Index Link'
    VIEW_LINK =       '🌐 Lihat Tautan'
    CHECK_PM =        '🕵️ Lihat di PM bot'
    CHECK_LL =        '📦 View in Dump'
    MEDIAINFO_LINK =  '📜 MediaInfo'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b>{Name}</b>\n'

    #####---------PROGRESSIVE STATUS-------
    STATUS =            '<blockquote>\n<b>{Status}</b>'
    BAR =               '          {Bar}'
    
    PROCESSED =         '\n<b>🔄 Ukuran       :</b> {Processed}'
    ETA =                '\n<b>⏳ Perkiraan    :</b> {Eta}'
    SPEED =             '\n<b>📶 Kecepatan :</b> {Speed}'
    ELAPSED =          '\n<b>⏰ Berjalan      :</b> {Elapsed}'
    ENGINE =            '\n<b>⚙️ Mesin          :</b> {Engine}'
    STA_MODE =          '\n<b>💠 Unggah      :</b> {Mode}'
    SEEDERS =           '\n<b>🌱S/L               :</b> {Seeders} | '
    LEECHERS =                                           '<b></b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n<b>💾 Size:</b> {Size}'
    SEED_SPEED =     '\n<b>📶 Speed:</b> {Speed} | '
    UPLOADED =                                     '<b>Uploaded:</b> <b>{Upload}</b>'
    RATIO =          '\n<b>🌀 Ratio:</b> <b>{Ratio}</b> | '
    TIME =                                         '<b>Time:</b> <b>{Time}</b>'
    SEED_ENGINE =    '\n<b>⚙️ Engine:</b> <b>{Engine}</b>'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n<b>💾 Ukuran       :</b> <b>{Size}</b>'
    NON_ENGINE =     '\n<b>⚙️ Mesin          :</b> <b>{Engine}</b>'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n<b>👤 Pengguna   :</b> <code>{User}</code>'
    ID =                                                        ' | <b>{Id}</b></blockquote>'
    BTSEL =          '\n<b>✂️ Pilih:</b> {Btsel}'
    CANCEL =         '\n<b>🚫</b> {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '👑 <b><u>Bot Stats</u></b>\n'
    TASKS =  '➢<b>🚧 Tasks:</b> {Tasks}\n'
    BOT_TASKS = '➢<b>🚧 Tasks:</b> <b>{Tasks}/{Ttask}</b> | <b>👷 Available:</b> <b>{Free}</b>\n'
    Cpu = '➢<b>🖥️ CPU:</b> <b>{cpu}%</b> | '
    FREE =                      '<b>📭 Free:</b> <b>{free}</b>'
    Ram = '\n➢<b>💿 RAM:</b> <b>{ram}%</b> '
    uptime = '\n➢<b>⏰ Uptime:</b> <b>{uptime}</b>'
    DL = '\n<b>🚀Unduh:</b> <b>{DL}/s</b> • '
    UL =                        '<b>🚀Unggah:</b> <b>{UL}/s</b>'

    ###--------BUTTONS-------
    PREVIOUS = '⏪'
    REFRESH = '📑 Halaman : {Page}'
    NEXT = '⏭️'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = '<b>🏷️ Nama:</b> <b>{content}</b>\n<b>⚠️ File/folder ini sudah tersedia di drive!</b>\n\n<b>📑 Daftar Hasilnya:</b>'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>🎲 Counting:</b> <b>{LINK}</b>\n\n<b>⏳ Please Wait...</b>'
    COUNT_NAME = '➢<b>🏷️ Name:</b> <b>{COUNT_NAME}</b>\n'
    COUNT_SIZE = '➢<b>💾 Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '➢<b>📜 Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '➢<b>🗂️ SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = '➢<b>📂 Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   '➢<b>👤 User: </b>{COUNT_CC}\n\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>🔍 Mencari :</b> <b>{NAME}</b>'
    LIST_FOUND = '<b>ℹ️ Ditemukan {NO} Hasil untuk </b> <b>{NAME}</b>'
    LIST_NOT_FOUND = '<b>☹️ Tidak di temukan </b> <b>{NAME}</b>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<b>💩 Tidak ada tugas yg sedang berjalan</b>
    
👑 <b><u>Bot Stats</u></b>
➢<b>🖥️ CPU:</b> <b>{cpu}%</b> | <b>💿 RAM:</b> <b>{ram}%</b>
➢<b>📭 Free:</b> <b>{free}</b> | <b>⏰ Uptime:</b> <b>{uptime}</b>
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>Pengaturan Pengguna</u></b>
        
➢<b>👤 Nama :</b> {NAME}
➢<b>🔖 NamaPengguna :</b> {USERNAME}
➢<b>🆔 ID :</b> <b>{ID}</b>
➢<b>🔮 DC :</b> <b>{DC}</b>
➢<b>🗣️ Bahasa :</b> <b>{LANG}</b>

'''

    UNIVERSAL = '''㊂ <b><u>Umum</u></b>

➢<b>📺 YT-DLP Options :</b> <b>{YT}</b>
➢<b>🚧 Tugas Harian :</b> <b>{DT}</b> per hari
➢<b>🟢 Terakhir Digunakan :</b> <b>{LAST_USED}</b>
➢<b>📜 MediaInfo :</b> <b>{MEDIAINFO}</b>
➢<b>🕵️ Bot PM :</b> <b>{BOT_PM}</b>
➢<b>📩 Save Mode :</b> <b>{SAVE_MODE}</b>

'''

    MIRROR = '''㊂ <b><u>Mirror/Clone</u></b>

➢<b>☁️ Mirror Harian:</b> <b>{DM}</b> per hari</i>
➢<b>Ⓟ Prefix :</b> <b>{MPREFIX}</b>
➢<b>Ⓢ Suffix :</b> <b>{MSUFFIX}</b>
➢<b>🌈 Remname :</b> <b>{MREMNAME}</b>
➢<b>🧿 DDL Server(s) :</b> <b>{DDL_SERVER}</b>
➢<b>🎀 RClone :</b> <b>{RCLONE}</b>
➢<b>📮 User TD :</b> <b>{TMODE}</b>
➢<b>📝 TD Info:</b> <b>{USERTD}</b>

'''

    LEECH = '''㊂ <b><u>Leech Settings</u></b>

➢<b>📂 Leech Harian  : </b><b>{DL}</b> per hari
➢<b>⚙️ Leech Type :</b> <b>{LTYPE}</b>
➢<b>🖼️ Thumbnail :</b> <b>Exɪsᴛs</b>
➢<b>♈ Split Size :</b> <b>{SPLIT_SIZE}</b>
➢<b>♐ Equal Splits :</b> <b>{EQUAL_SPLIT}</b>
➢<b>♒ Media Group :</b> <b>{MEDIA_GROUP}</b>
➢<b>📄 Caption :</b> <b>{LCAPTION}</b>
➢<b>Ⓟ Prefix :</b> <b>{LPREFIX}</b>
➢<b>Ⓢ Suffix :</b> <b>{LSUFFIX}</b>
➢<b>📦 Dump :</b> <b>{LDUMP}</b>
➢<b>🌈 Remname :</b> <b>{LREMNAME}</b>

'''
