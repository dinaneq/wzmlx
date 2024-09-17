#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = 'Original_Rᴇᴘᴏ'
    ST_BN1_URL = 'https://gitlab.com/Jot4349/WZML-X-ADVANCE'
    ST_BN2_NAME = 'Uᴘᴅᴀᴛᴇs'
    ST_BN2_URL = 'https://t.me/NordBotz'
    ST_MSG = '''<blockquote><i>Bot ini dapat melakukan mirror semua tautan, file, dan torrent Anda ke Google Drive atau cloud rclone lainnya, ke Telegram, atau ke server DDL. Ketik {help_command} untuk mendapatkan daftar perintah yang tersedia.</b></blockquote>'''
    ST_BOTPM = '''<i>Sekarang, bot ini akan mengirim semua file dan tautan Anda ke sini. Mulai menggunakan ...</i>'''
    ST_UNAUTH = '''<blockquote><i>Anda bukan pengguna yang diizinkan! Deploy bot WZML-X-ADVANCE Mirror-Leech Anda sendiri.</i></blockquote>'''
    OWN_TOKEN_GENERATE = '''<b>Tᴇᴍᴘᴏʀᴀʀʏ Tᴏᴋᴇɴ ɪs ɴᴏᴛ ʏᴏᴜʀs!</b>\n\n<i>Kɪɴᴅʟʏ ɢᴇɴᴇʀᴀᴛᴇ ʏᴏᴜʀ ᴏᴡɴ.</i>'''
    USED_TOKEN = '''<b>Tᴇᴍᴘᴏʀᴀʀʏ Tᴏᴋᴇɴ ᴀʟʀᴇᴀᴅʏ ᴜsᴇᴅ!</b>\n\n<i>Kɪɴᴅʟʏ ɢᴇɴᴇʀᴀᴛᴇ ᴀ ɴᴇᴡ ᴏɴᴇ.</i>'''
    LOGGED_PASSWORD = '''<b>Bᴏᴛ Aʟʀᴇᴀᴅʏ Lᴏɢɢᴇᴅ Iɴ ᴠɪᴀ Pᴀssᴡᴏʀᴅ</b>\n\n<i>Nᴏ Nᴇᴇᴅ ᴛᴏ Aᴄᴄᴇᴘᴛ Tᴇᴍᴘ Tᴏᴋᴇɴs.</i>'''
    ACTIVATE_BUTTON = 'Aᴄᴛɪᴠᴀᴛᴇ Tᴇᴍᴘᴏʀᴀʀʏ Tᴏᴋᴇɴ'
    TOKEN_MSG = '''<b><u>Gᴇɴᴇʀᴀᴛᴇᴅ Tᴇᴍᴘᴏʀᴀʀʏ Lᴏɢɪɴ Tᴏᴋᴇɴ!</u></b>
<b>Tᴇᴍᴘ Tᴏᴋᴇɴ:</b> <code>{token}</code>
<b>Vᴀʟɪᴅɪᴛʏ:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Aᴄᴛɪᴠᴀᴛᴇᴅ ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Aʟʀᴇᴀᴅʏ Bᴏᴛ Lᴏɢɪɴ Iɴ!</b>'
    INVALID_PASS = '<b>Iɴᴠᴀʟɪᴅ Pᴀssᴡᴏʀᴅ!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bᴏᴛ Pᴇʀᴍᴀɴᴇɴᴛ Lᴏɢɪɴ Sᴜᴄᴄᴇssғᴜʟʟʏ!</b>'
    LOGIN_USED = '<b>Bᴏᴛ Lᴏɢɪɴ Usᴀɢᴇ :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Lihat Log'
    WEB_PASTE_BT = '📨 Wᴇʙ Pᴀsᴛᴇ (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Bᴀsɪᴄ'
    USER_BT = 'Usᴇʀs'
    MICS_BT = 'Mɪᴄs'
    O_S_BT = 'Oᴡɴᴇʀ & Sᴜᴅᴏs'
    CLOSE_BT = 'Close'
    HELP_HEADER = "㊂ <b><i>Hᴇʟᴘ Gᴜɪᴅᴇ Mᴇɴᴜ!</i></b>\n\n<b>Nᴏᴛᴇ: <i>Cʟɪᴄᴋ ᴏɴ ᴀɴʏ CMD ᴛᴏ sᴇᴇ ᴍᴏʀᴇ ᴍɪɴᴏʀ ᴅᴇᴛᴀʟɪs.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''🌀<b><i>Bᴏᴛ Sᴛᴀᴛɪsᴛɪᴄs :</i></b>
• <b>Bᴏᴛ Uᴘᴛɪᴍᴇ :</b> {bot_uptime}

• <b><i>Rᴀᴍ ( MEMORY ) :</i></b>
• {ram_bar} {ram}%
• <b>U :</b> {ram_u} • <b>F :</b> {ram_f} • <b>T :</b> {ram_t}

• <b><i>Sᴡᴀᴘ Mᴇᴍᴏʀʏ :</i></b>
• {swap_bar} {swap}%
• <b>U :</b> {swap_u} • <b>F :</b> {swap_f} • <b>T :</b> {swap_t}

• <b><i>Dɪsᴋ :</i></b>
• {disk_bar} {disk}%
• <b>Tᴏᴛᴀʟ Dɪsᴋ Rᴇᴀᴅ :</b> {disk_read}
• <b>Tᴏᴛᴀʟ Dɪsᴋ Wʀɪᴛᴇ :</b> {disk_write}
• <b>U :</b> {disk_u} • <b>F :</b> {disk_f} • <b>T :</b> {disk_t}
    
    '''
    SYS_STATS = '''🌀 <b><i>Os Sʏsᴛᴇᴍ :</i></b>
• <b>Os Uᴘᴛɪᴍᴇ :</b> {os_uptime}
• <b>Os Vᴇʀsɪᴏɴ :</b> {os_version}
• <b>Os Aʀᴄʜ :</b> {os_arch}

🌀 <b><i>Nᴇᴛᴡᴏʀᴋ Sᴛᴀᴛs :</i></b>
• <b>Uᴘʟᴏᴀᴅ Dᴀᴛᴀ:</b> {up_data}
• <b>Dᴏᴡɴʟᴏᴀᴅ Dᴀᴛᴀ:</b> {dl_data}
• <b>Pᴋᴛs Sᴇɴᴛ:</b> {pkt_sent}k
• <b>Pᴋᴛs Rᴇᴄᴇɪᴠᴇᴅ:</b> {pkt_recv}k
• <b>Tᴏᴛᴀʟ I/O Dᴀᴛᴀ:</b> {tl_data}

• <b>Cᴘᴜ :</b>
• {cpu_bar} {cpu}%
• <b>Cᴘᴜ Fʀᴇǫᴜᴇɴᴄʏ :</b> {cpu_freq}
• <b>Sʏsᴛᴇᴍ Aᴠɢ Lᴏᴀᴅ :</b> {sys_load}
• <b>P-Cᴏʀᴇ(s) :</b> {p_core} • <b>V-Cᴏʀᴇ(s) :</b> {v_core}
• <b>Tᴏᴛᴀʟ Cᴏʀᴇ(s) :</b> {total_core}
• <b>Usᴀʙʟᴇ Cᴘᴜ(s) :</b> {cpu_use}
    '''
    REPO_STATS = '''🌀 <b><i>Rᴇᴘᴏ Sᴛᴀᴛɪsᴛɪᴄs :</i></b>
• <b>Bᴏᴛ Uᴘᴅᴀᴛᴇᴅ        :</b> {last_commit}
• <b>Cᴜʀʀᴇɴᴛ Vᴇʀsɪᴏɴ    :</b> {bot_version}
• <b>Lᴀᴛᴇsᴛ Vᴇʀsɪᴏɴ     :</b> {lat_version}
• <b>Lᴀsᴛ CʜᴀɴɢᴇLᴏɢ     :</b> {commit_details}

🌀 <b>Rᴇᴍᴀʀᴋs :</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = '''🌀 <b><i>Bᴏᴛ Lɪᴍɪᴛᴀᴛɪᴏɴs :</i></b>
<blockquote expandable>• <b>Dɪʀᴇᴄᴛ Lɪᴍɪᴛ :</b> {DL} Gʙ
• <b>Tᴏʀʀᴇɴᴛ Lɪᴍɪᴛ  :</b> {TL} Gʙ
• <b>GDʀɪᴠᴇ Lɪᴍɪᴛ   :</b> {GL} Gʙ
• <b>Yᴛ-Dʟᴘ Lɪᴍɪᴛ   :</b> {YL} Gʙ
• <b>Pʟᴀʏʟɪsᴛ Lɪᴍɪᴛ :</b> {PL}
• <b>Mᴇɢᴀ Lɪᴍɪᴛ     :</b> {ML} Gʙ
• <b>Cʟᴏɴᴇ Lɪᴍɪᴛ    :</b> {CL} Gʙ
• <b>Lᴇᴇᴄʜ Lɪᴍɪᴛ    :</b> {LL} Gʙ

• <b>Tᴏᴋᴇɴ Vᴀʟɪᴅɪᴛʏ         :</b> {TV}
• <b>Usᴇʀ Tɪᴍᴇ Lɪᴍɪᴛ        :</b> {UTI} / Tᴀsᴋ
• <b>Usᴇʀ Pᴀʀᴀʟʟᴇʟ Tᴀsᴋs    :</b> {UT}
• <b>Bᴏᴛ Pᴀʀᴀʟʟᴇʟ Tᴀsᴋs     :</b> {BT}</blockquote>
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Rᴇsᴛᴀʀᴛɪɴɢ...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''🌀 <b><i>Rᴇsᴛᴀʀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ!</i></b>
• <b>Dᴀᴛᴇ         :</b> {date}
• <b>Tɪᴍᴇ         :</b> {time}
• <b>TɪᴍᴇZᴏɴᴇ    :</b> {timz}
• <b>Vᴇʀsɪᴏɴ      :</b> {version}'''
    RESTARTED = '''🌀 <b><i>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Sᴛᴀʀᴛɪɴɢ Pɪɴɢ..</i>'
    PING_VALUE = '<b>Pᴏɴɢ</b>\n<code>{value} ᴍs..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<blockquote><b><i>Tᴀsᴋ Sᴛᴀʀᴛᴇᴅ</i></b>
• <b>Mᴏᴅᴇ:</b> {Mode}
• <b>Bʏ:</b> {Tag}\n\n"""
    LINKS_SOURCE = """➲Sᴏᴜʀᴄᴇ <b>:</b>
• <b>Aᴅᴅᴇᴅ Oɴ:</b> {On}</blockquote>
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
{Source}
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "<blockquote>➲ <b><u>Tᴀsᴋ Sᴛᴀʀᴛᴇᴅ :</u></b>\n\n• <b>Link:</b> <a href='{msg_link}'>Cʟɪᴄᴋ Hᴇʀᴇ</a></blockquote>"
    L_LOG_START =           "<blockquote>➲ <b><u>Lᴇᴇᴄʜ Sᴛᴀʀᴛᴇᴅ :</u></b>\n\n• <b>Usᴇʀ :</b> {mention} ( #ID{uid} )\n• <b>Sᴏᴜʀᴄᴇ :</b> <a href='{msg_link}'>Cʟɪᴄᴋ Hᴇʀᴇ</a></blockquote>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b><i>{Name}</i></b>\n\n'
    SIZE =                  '<blockquote>• <b>Sɪᴢᴇ      : </b>{Size}\n'
    ELAPSE =                '• <b>Eʟᴀᴘsᴇᴅ   : </b>{Time}\n'
    MODE =                  '• <b>Mᴏᴅᴇ      : </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '• <b>Tᴏᴛᴀʟ Fɪʟᴇs       : </b>{Files}\n'
    L_CORRUPTED_FILES =     '• <b>Cᴏʀʀᴜᴘᴛᴇᴅ Fɪʟᴇs   : </b>{Corrupt}\n'
    L_CC =                  '• <b>Bʏ                : </b>{Tag}\n'
    PM_BOT_MSG =            '➲ <b><i>File(s) sudah dikirim</i></b>'
    L_BOT_MSG =             '➲ <b><i>File dikirim ke PM</i></b>'
    L_LL_MSG =              '➲ <b><i>File dikirim ke PM</i></b></blockquote>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '• <b>Tʏᴘᴇ      : </b>{Mimetype}\n'
    M_SUBFOLD =             '• <b>SᴜʙFᴏʟᴅᴇʀs: </b>{Folder}\n'
    TOTAL_FILES =           '• <b>Fɪʟᴇs     : </b>{Files}\n'
    RCPATH =                '• <b>Pᴀᴛʜ      : </b><code>{RCpath}</code>\n'
    M_CC =                  '• <b>Bʏ        : </b>{Tag}\n'
    M_BOT_MSG =             '➲ <b><i>Link download di kirim ke PM dan segera download file anda sebelum ada penghapusan berkala</b></blockquote>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cʟᴏᴜᴅ Lɪɴᴋ'
    SAVE_MSG =        '📨 Sᴀᴠᴇ Mᴇssᴀɢᴇ'
    RCLONE_LINK =     '♻️ RCʟᴏɴᴇ Lɪɴᴋ'
    DDL_LINK =        '📎 {Serv} Lɪɴᴋ'
    SOURCE_URL =      '🔐 Sᴏᴜʀᴄᴇ Lɪɴᴋ'
    INDEX_LINK_F =    '🗂 Iɴᴅᴇx Lɪɴᴋ'
    INDEX_LINK_D =    '⚡ Iɴᴅᴇx Lɪɴᴋ'
    VIEW_LINK =       '🌐 Vɪᴇᴡ Lɪɴᴋ'
    CHECK_PM =        '📥 Vɪᴇᴡ ɪɴ Bᴏᴛ PM'
    CHECK_LL =        '🖇 Vɪᴇᴡ ɪɴ Lɪɴᴋs Lᴏɢ'
    MEDIAINFO_LINK =  '📃 MᴇᴅɪᴀIɴғᴏ'
    SCREENSHOTS =     '🖼 SᴄʀᴇᴇɴSʜᴏᴛs'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '• 📸 : <b><i>{Name}</i></b>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n• 🔥 : {Bar}'
    PROCESSED =         '\n• 💿 : {Processed}'
    SPEED =             '\n• 🚀 : {Speed}'
    STATUS =                                            '• <a href="{Url}">{Status}</a>'
    ETA =                                                '\n• ⏰ : {Eta}'
    ELAPSED =                                     ' • ⏳ : {Elapsed}'
    ENGINE =            '\n• 🚂 : {Engine}'
    STA_MODE =          '\n• ⚒️ : {Mode}'
    SEEDERS =           '\n• 🧲 : {Seeders} • '
    LEECHERS =                                           '👾 : {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n• <b>Sɪᴢᴇ: </b>{Size}'
    SEED_SPEED =     '\n• <b>Sᴘᴇᴇᴅ: </b> {Speed} • '
    UPLOADED =                                     '<b>Uᴘʟᴏᴀᴅᴇᴅ: </b> {Upload}'
    RATIO =          '\n• <b>Rᴀᴛɪᴏ: </b> {Ratio} • '
    TIME =                                         '<b>Tɪᴍᴇ: </b> {Time}'
    SEED_ENGINE =    '\n• <b>Eɴɢɪɴᴇ:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n• <b>Sɪᴢᴇ: </b>{Size}'
    NON_ENGINE =     '\n• <b>Eɴɢɪɴᴇ:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n• 🙎‍♂️ : <code>{User}</code> • '
    ID =                                                        ' (<code>{Id}</code>)'
    BTSEL =          '\n• <b>☑ :</b> {Btsel}'
    CANCEL =         '\n\n⚠️{Cancel} \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n'

    ####------FOOTER--------
    FOOTER = '🌀 <b><i>Bᴏᴛ Sᴛᴀᴛs</i></b>\n'
    TASKS =  '• <b>Tᴀsᴋs:</b> {Tasks}\n'
    BOT_TASKS = '• <b>Tᴀsᴋs:</b> {Tasks}/{Ttask} • <b>Aᴠʟ:</b> {Free}\n'
    Cpu = '• <b>Cᴘᴜ:</b> {cpu}% • '
    FREE =                      '<b>F:</b> {free} [{free_p}%]'
    Ram = '\n• <b>Rᴀᴍ:</b> {ram}% • '
    uptime =                     '<b>UᴘTɪᴍᴇ:</b> {uptime}'
    DL = '\n• <b>🔽 :</b> {DL}/s • '
    UL =                        '<b>🔼 :</b> {UL}/s</blockquote>'

    ###--------BUTTONS-------
    PREVIOUS = '◀️'
    REFRESH = 'Pᴀɢᴇs\n{Page}'
    NEXT = '▶️'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File sudah tersedia di Google Drive.\nSemua disini {content} Hasil nya: '
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Cᴏᴜɴᴛɪɴɢ:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n•\n'
    COUNT_SIZE = '• <b>Sɪᴢᴇ: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '• <b>Tʏᴘᴇ: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '• <b>SᴜʙFᴏʟᴅᴇʀs: </b>{COUNT_SUB}\n'
    COUNT_FILE = '• <b>Fɪʟᴇs: </b>{COUNT_FILE}\n'
    COUNT_CC =   '• <b>Bʏ: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Pencarian untuk  <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Ditemukan {NO} Hasil untuk <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'Tidak di temukan untuk kata kunci <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>Tidak ada tugas yg sedang berjalan 😊</i>
    
<blockquote>🌀 <b><i>Bᴏᴛ Sᴛᴀᴛs</i></b>
• <b>Cᴘᴜ:</b> {cpu}% • <b>F:</b> {free} [{free_p}%]
• <b>Rᴀᴍ:</b> {ram} • <b>UᴘTɪᴍᴇ:</b> {uptime}<b/lockquote>
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>Usᴇʀ Sᴇᴛᴛɪɴɢs :</u></b>
        
•<b> Nᴀᴍᴇ : </b>{NAME} ( <code>{ID}</code> )
•<b> Usᴇʀɴᴀᴍᴇ  :</b> {USERNAME}
•<b> Tᴇʟᴇɢʀᴀᴍ DC :</b> {DC}'''

    UNIVERSAL = '''㊂ <b><u>Uɴɪᴠᴇʀsᴀʟ Sᴇᴛᴛɪɴɢs : {NAME}</u></b>

•<b> YT-DLP Oᴘᴛɪᴏɴs :</b> <b><code>{YT}</code></b>
•<b> Dᴀɪʟʏ Tᴀsᴋs :</b> <code>{DT}</code> ᴘᴇʀ ᴅᴀʏ
•<b> Lᴀsᴛ Bᴏᴛ Usᴇᴅ :</b> <code>{LAST_USED}</code>
•<b> Usᴇʀ Sᴇssɪᴏɴ :</b> <code>{USESS}</code>
•<b> MᴇᴅɪᴀIɴғᴏ Mᴏᴅᴇ :</b> <code>{MEDIAINFO}</code>
•<b> Sᴀᴠᴇ Mᴏᴅᴇ :</b> <code>{SAVE_MODE}</code>
•<b> Usᴇʀ Bᴏᴛ PM :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''㊂ <b><u>Mɪʀʀᴏʀ/Cʟᴏɴᴇ Sᴇᴛᴛɪɴɢs : {NAME}</u></b>

•<b> RCʟᴏɴᴇ Cᴏɴғɪɢ :</b> <i>{RCLONE}</i>
•<b> Mɪʀʀᴏʀ Pʀᴇғɪx :</b> <code>{MPREFIX}</code>
•<b> Mɪʀʀᴏʀ Sᴜғғɪx :</b> <code>{MSUFFIX}</code>
•<b> Mɪʀʀᴏʀ Rᴇᴍɴᴀᴍᴇ :</b> <code>{MREMNAME}</code>
•<b> DDL Sᴇʀᴠᴇʀ(s) :</b> <i>{DDL_SERVER}</i>
•<b> Usᴇʀ TD Mᴏᴅᴇ :</b> <i>{TMODE}</i>
•<b> Tᴏᴛᴀʟ Usᴇʀ TD(s) :</b> <i>{USERTD}</i>
•<b> Dᴀɪʟʏ Mɪʀʀᴏʀ :</b> <code>{DM}</code> ᴘᴇʀ ᴅᴀʏ'''

    LEECH = '''㊂ <b><u>Lᴇᴇᴄʜ Sᴇᴛᴛɪɴɢs ғᴏʀ {NAME}</u></b>

•<b> Dᴀɪʟʏ Lᴇᴇᴄʜ :</b> <code>{DL}</code ᴘᴇʀ ᴅᴀʏ
•<b> Lᴇᴇᴄʜ Tʏᴘᴇ :</b> <i>{LTYPE}</i>
•<b> Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ :</b> <i>{THUMB}</i>
•<b> Lᴇᴇᴄʜ Sᴘʟɪᴛ Sɪᴢᴇ :</b> <code>{SPLIT_SIZE}</code>
•<b> Eǫᴜᴀʟ Sᴘʟɪᴛs :</b> <i>{EQUAL_SPLIT}</i>
•<b> Mᴇᴅɪᴀ Gʀᴏᴜᴘ :</b> <i>{MEDIA_GROUP}</i>
•<b> Lᴇᴇᴄʜ Cᴀᴘᴛɪᴏɴ :</b> <code>{LCAPTION}</code>
•<b> Lᴇᴇᴄʜ Pʀᴇғɪx :</b> <code>{LPREFIX}</code>
•<b> Lᴇᴇᴄʜ Sᴜғғɪx :</b> <code>{LSUFFIX}</code>
•<b> Lᴇᴇᴄʜ Dᴜᴍᴘs :</b> <code>{LDUMP}</code>
•<b> Lᴇᴇᴄʜ Rᴇᴍɴᴀᴍᴇ :</b> <code>{LREMNAME}</code>'''
